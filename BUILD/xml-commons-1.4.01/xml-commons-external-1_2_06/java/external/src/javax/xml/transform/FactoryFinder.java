/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 * 
 *      http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package javax.xml.transform;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.io.IOException;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Properties;

/**
 * This class is duplicated for each JAXP subpackage so keep it in sync.
 * It is package private and therefore is not exposed as part of the JAXP
 * API.
 *
 * This code is designed to implement the JAXP 1.1 spec pluggability
 * feature.  The code runs both as part of an unbundled jar file and also
 * when bundled as part of the JDK.  Ideally the code should both compile
 * and run on JDK version 1.1 and later.  However, due to the complexities
 * of invoking Java 2 security methods via reflection, this code will only
 * compile on Java 2 although it will run under JDK 1.1 VMs.  As of 1may02
 * this file is on a "java2-branch".
 *
 * @author Edwin Goei
 */
final class FactoryFinder {
    
    /** Controls debugging output to stderr */
    private static boolean debug;

    /** Cache the contents of the jaxp.properties file, if used. */
    private static Properties jaxpProperties = null;

    /** Cache the timestamp of the jaxp.properties file, if used. */
    private static long lastModified = -1;
    
    /**
     * Default columns per line.
     */
    private static final int DEFAULT_LINE_LENGTH = 80;

    // Define system property "jaxp.debug" to get output
    static {
        try {
            String val =
                SecuritySupport.getInstance().getSystemProperty("jaxp.debug");
            // Allow simply setting the prop to turn on debug
            debug = val != null && (! "false".equals(val));
        } catch (SecurityException se) {
            debug = false;
        }
    }
    
    private FactoryFinder() {}

    /**
     * Main entry point.  Finds and creates a new instance of a concrete
     * factory implementation in the specified order as stated in the JAXP
     * spec.  This code attempts to find a factory implementation in
     * several locations.  If one fails, the next one is tried.  To be
     * more robust, this occurs even if a SecurityException is thrown, but
     * perhaps it may be better to propagate the SecurityException instead,
     * so SecurityException-s are not masked.
     *
     * @return A new instance of the concrete factory class, never null
     *
     * @param factoryId
     *        Name of the factory to find, same as a property name
     *
     * @param fallbackClassName
     *        Implementation class name, if nothing else is found.  Use
     *        null to mean not to use a fallback.
     *
     * @throws FactoryFinder.ConfigurationError
     *         If a factory instance cannot be returned
     *
     * Package private so this code can be shared.
     */
    static Object find(String factoryId, String fallbackClassName)
        throws ConfigurationError
    {
        SecuritySupport ss = SecuritySupport.getInstance();

        // Figure out which ClassLoader to use for loading the provider
        // class.  If there is a Context ClassLoader then use it.
        ClassLoader cl = ss.getContextClassLoader();
        if (cl == null) {
            // Assert: we are on JDK 1.1 or we have no Context ClassLoader
            // so use the current ClassLoader
            cl = FactoryFinder.class.getClassLoader();
        }

        if (debug) dPrint("find factoryId=" + factoryId);

        // Use the system property first
        try {
            String systemProp = ss.getSystemProperty(factoryId);
            if (systemProp != null && systemProp.length() > 0) {
                if (debug) dPrint("found system property, value=" + systemProp);
                return newInstance(systemProp, cl, true);
            }
        } catch (SecurityException se) {
            // Ignore and continue w/ next location
        }

        boolean fExists = false;
        File f = null;
        try {               
            String javah = ss.getSystemProperty("java.home");
            String configFile = javah + File.separator +
                "lib" + File.separator + "jaxp.properties";
            
            f = new File(configFile);
            fExists = ss.getFileExists(f);
            
        } catch (SecurityException se) {
            
            // If there is a security exception, move on to next location.
            lastModified = -1;
            jaxpProperties = null;            
        }    
        
        synchronized (FactoryFinder.class) {    
            
            boolean runBlock = false;
            FileInputStream fis = null;

            try {
                if (lastModified >= 0) {

                    // File has been modified, or didn't previously exist. 
                    // Need to reload properties    
                    if ((fExists) && 
                          (lastModified < (lastModified = ss.getLastModified(f)))) {  
                          runBlock = true;
                    } else {
                        if (!fExists) {
                         // file existed, but it's been deleted.
                         lastModified = -1;
                         jaxpProperties = null;
                        }
                    }        
                } else {
                    if (fExists) { 
                        // File didn't exist, but it does now.
                        runBlock = true;
                        lastModified = ss.getLastModified(f);
                    }    
                }
         
                if (runBlock == true) {
                   // Try to read from $java.home/lib/jaxp.properties
                       jaxpProperties = new Properties();
                   
                       fis = ss.getFileInputStream(f);
                       jaxpProperties.load(fis);
                }       
                
           } catch (Exception x) {
               lastModified = -1;
               jaxpProperties = null;
               // assert(x instanceof FileNotFoundException
               //        || x instanceof SecurityException)
               // In both cases, ignore and continue w/ next location
           }
           finally {
               // try to close the input stream if one was opened.
               if (fis != null) {
                   try {
                       fis.close();
                   }
                   // Ignore the exception.
                   catch (IOException exc) {}
               }
           }
       }
            
       if (jaxpProperties != null) {            
            String factoryClassName = jaxpProperties.getProperty(factoryId);
            if (factoryClassName != null) {
                if (debug) dPrint("found in jaxp.properties, value=" + factoryClassName);
                return newInstance(factoryClassName, cl, true);
            }
        }   

        // Try Jar Service Provider Mechanism
        Object provider = findJarServiceProvider(factoryId);
        if (provider != null) {
            return provider;
        }

        if (fallbackClassName == null) {
            throw new ConfigurationError(
                "Provider for " + factoryId + " cannot be found", null);
        }

        if (debug) dPrint("using fallback, value=" + fallbackClassName);
        return newInstance(fallbackClassName, cl, true);
    }

    private static void dPrint(String msg) {
        if (debug) {
            System.err.println("JAXP: " + msg);
        }
    }

    /**
     * Create an instance of a class using the specified ClassLoader and
     * optionally fall back to the current ClassLoader if not found.
     *
     * @param className Name of the concrete class corresponding to the
     * service provider
     *
     * @param cl ClassLoader to use to load the class, null means to use
     * the bootstrap ClassLoader
     *
     * @param doFallback true if the current ClassLoader should be tried as
     * a fallback if the class is not found using cl
     */
    private static Object newInstance(String className, ClassLoader cl,
                                      boolean doFallback)
        throws ConfigurationError
    {
        // assert(className != null);

        try {
            Class providerClass;
            if (cl == null) {
                // XXX Use the bootstrap ClassLoader.  There is no way to
                // load a class using the bootstrap ClassLoader that works
                // in both JDK 1.1 and Java 2.  However, this should still
                // work b/c the following should be true:
                //
                // (cl == null) iff current ClassLoader == null
                //
                // Thus Class.forName(String) will use the current
                // ClassLoader which will be the bootstrap ClassLoader.
                providerClass = Class.forName(className);
            } else {
                try {
                    providerClass = cl.loadClass(className);
                } catch (ClassNotFoundException x) {
                    if (doFallback) {
                        // Fall back to current classloader
                        cl = FactoryFinder.class.getClassLoader();
                        if(cl != null)
                            providerClass = cl.loadClass(className);
                        else
                            providerClass = Class.forName(className);
                    } else {
                        throw x;
                    }
                }
            }
            Object instance = providerClass.newInstance();
            if (debug) dPrint("created new instance of " + providerClass +
                   " using ClassLoader: " + cl);
            return instance;
        } catch (ClassNotFoundException x) {
            throw new ConfigurationError(
                "Provider " + className + " not found", x);
        } catch (Exception x) {
            throw new ConfigurationError(
                "Provider " + className + " could not be instantiated: " + x,
                x);
        }
    }

    /*
     * Try to find provider using Jar Service Provider Mechanism
     *
     * @return instance of provider class if found or null
     */
    private static Object findJarServiceProvider(String factoryId)
        throws ConfigurationError
    {
        SecuritySupport ss = SecuritySupport.getInstance();
        String serviceId = "META-INF/services/" + factoryId;
        InputStream is = null;

        // First try the Context ClassLoader
        ClassLoader cl = ss.getContextClassLoader();
        if (cl != null) {
            is = ss.getResourceAsStream(cl, serviceId);

            // If no provider found then try the current ClassLoader
            if (is == null) {
                cl = FactoryFinder.class.getClassLoader();
                is = ss.getResourceAsStream(cl, serviceId);
            }
        } else {
            // No Context ClassLoader or JDK 1.1 so try the current
            // ClassLoader
            cl = FactoryFinder.class.getClassLoader();
            is = ss.getResourceAsStream(cl, serviceId);
        }

        if (is == null) {
            // No provider found
            return null;
        }

        if (debug) dPrint("found jar resource=" + serviceId +
               " using ClassLoader: " + cl);

        // Read the service provider name in UTF-8 as specified in
        // the jar spec.  Unfortunately this fails in Microsoft
        // VJ++, which does not implement the UTF-8
        // encoding. Theoretically, we should simply let it fail in
        // that case, since the JVM is obviously broken if it
        // doesn't support such a basic standard.  But since there
        // are still some users attempting to use VJ++ for
        // development, we have dropped in a fallback which makes a
        // second attempt using the platform's default encoding. In
        // VJ++ this is apparently ASCII, which is a subset of
        // UTF-8... and since the strings we'll be reading here are
        // also primarily limited to the 7-bit ASCII range (at
        // least, in English versions), this should work well
        // enough to keep us on the air until we're ready to
        // officially decommit from VJ++. [Edited comment from
        // jkesselm]
        BufferedReader rd;
        try {
            rd = new BufferedReader(new InputStreamReader(is, "UTF-8"), DEFAULT_LINE_LENGTH);
        } catch (java.io.UnsupportedEncodingException e) {
            rd = new BufferedReader(new InputStreamReader(is), DEFAULT_LINE_LENGTH);
        }
        
        String factoryClassName = null;
        try {
            // XXX Does not handle all possible input as specified by the
            // Jar Service Provider specification
            factoryClassName = rd.readLine();
        } catch (IOException x) {
            // No provider found
            return null;
        }
        finally {
            try {
                // try to close the reader.
                rd.close();
            }
            // Ignore the exception.
            catch (IOException exc) {}
        }

        if (factoryClassName != null &&
            ! "".equals(factoryClassName)) {
            if (debug) dPrint("found in resource, value="
                   + factoryClassName);

            // Note: here we do not want to fall back to the current
            // ClassLoader because we want to avoid the case where the
            // resource file was found using one ClassLoader and the
            // provider class was instantiated using a different one.
            return newInstance(factoryClassName, cl, false);
        }

        // No provider found
        return null;
    }

    static class ConfigurationError extends Error {
        private Exception exception;

        /**
         * Construct a new instance with the specified detail string and
         * exception.
         */
        ConfigurationError(String msg, Exception x) {
            super(msg);
            this.exception = x;
        }

        Exception getException() {
            return exception;
        }
    }
}

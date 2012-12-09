#!/bin/sh
# 
# xml-commons-resolver resolver script
# JPackage Project <http://www.jpackage.org/>

# Source functions library
. /usr/share/java-utils/java-functions

# Configuration
MAIN_CLASS=org.apache.xml.resolver.apps.resolver
BASE_JARS="xml-commons-resolver10.jar xml-commons-jaxp-1.1-apis.jar jaxp_parser_impl.jar"
CLASSPATH="$CLASSPATH:__RESOLVERDIR__"

# Set parameters
set_jvm
set_classpath $BASE_JARS
set_flags $BASE_FLAGS
set_options $BASE_OPTIONS

# Let's start
run "$@"

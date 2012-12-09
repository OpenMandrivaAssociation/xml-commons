#!/bin/sh
# 
# xml-commons-resolver xparse script
# JPackage Project <http://www.jpackage.org/>

# Source functions library
. /usr/share/java-utils/java-functions

# Configuration
MAIN_CLASS=org.apache.xml.resolver.apps.xparse
BASE_JARS="xml-commons-resolver11.jar xml-commons-jaxp-1.2-apis.jar jaxp_parser_impl.jar"
CLASSPATH="$CLASSPATH:__RESOLVERDIR__"

# Set parameters
set_jvm
set_classpath $BASE_JARS
set_flags $BASE_FLAGS
set_options $BASE_OPTIONS

# Let's start
run "$@"

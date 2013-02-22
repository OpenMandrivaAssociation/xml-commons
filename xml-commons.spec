%define  _duplicate_files_terminate_build 0

%define section free
%define resolverdir %{_sysconfdir}/java/resolver
%define gcj_support 0

Name:           xml-commons
Version:        1.4.01
Release:        2
Summary:        Common code for XML projects
Epoch:          0
License:        Apache License
URL:            http://xml.apache.org/commons/
# svn export http://svn.apache.org/repos/asf/xerces/xml-commons/tags/xml-commons-1_0_b2/
Source0:        xml-commons-1.0.b2.tar.xz
# svn export http://svn.apache.org/repos/asf/xerces/xml-commons/tags/xml-commons-external-1_2_06/
Source1:        xml-commons-external-1.2.06.tar.xz
# svn export http://svn.apache.org/repos/asf/xerces/xml-commons/tags/xml-commons-external-1_3_05/
Source2:        xml-commons-external-1.3.05.tar.xz
Source30:	xml-commons-resolver-1.1.b1.tar.bz2
# svn export http://svn.apache.org/repos/asf/xml/commons/tags/xml-commons-resolver-1_2/
Source3:        xml-commons-resolver-1.2.tar.xz
# svn export http://svn.apache.org/repos/asf/xerces/xml-commons/tags/xml-commons-external-1_4_01/
Source32:	xml-commons-external-1.4.01.tar.xz
Source4:        xml-commons.which10.script
Source5:        xml-commons.which11.script
Source31:	xml-commons.which12.script
Source6:        xml-commons-resolver10-resolver.1
Source7:        xml-commons-resolver10-resolver.sh
Source8:        xml-commons-resolver10-xparse.1
Source9:        xml-commons-resolver10-xparse.sh
Source10:       xml-commons-resolver10-xread.1
Source11:       xml-commons-resolver10-xread.sh
Source12:       xml-commons-resolver11-resolver.1
Source13:       xml-commons-resolver11-resolver.sh
Source14:       xml-commons-resolver11-xparse.1
Source15:       xml-commons-resolver11-xparse.sh
Source16:       xml-commons-resolver11-xread.1
Source17:       xml-commons-resolver11-xread.sh
Source18:       xml-commons-resolver12-resolver.1
Source19:       xml-commons-resolver12-resolver.sh
Source20:       xml-commons-resolver12-xparse.1
Source21:       xml-commons-resolver12-xparse.sh
Source22:       xml-commons-resolver12-xread.1
Source23:       xml-commons-resolver12-xread.sh
Source24:       %{name}-resolver-CatalogManager.properties


Patch0:         %{name}-external-1.3-build_xml.patch
Patch1:         %{name}-resolver-crosslink.patch

Requires:       jpackage-utils >= 0:1.6
BuildRequires:  ant
BuildRequires:  docbook-style-xsl
BuildRequires:	java-1.6.0-openjdk-devel
# Make sure we don't get 1.7 -- it creates
# jars that are incompatible with 1.6
BuildConflicts:	java-1.7.0-openjdk-devel
BuildRequires:  java-devel >= 0:1.6
BuildRequires:  java-rpmbuild >= 0:1.6
Group:          Development/Java
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif

%description
xml-commons is focused on common code and guidelines for xml projects.
It's first focus will be to organize and have common packaging for the
various externally-defined standards code relating to XML - things like
the DOM, SAX, and JAXP interfaces.
As the xml-commons community forms, we also hope to serve as a holding
area for other common xml-related utilities and code, and to help
promulgate common packaging, testing, documentation, and other
guidelines across all xml.apache.org subprojects.

%package jaxp-1.1-apis
Summary:        JAXP 1.1, DOM2, SAX2, SAX2-ext 1.0 apis
Group:          Development/Java
Provides:       jaxp = 1.1
Provides:       dom = 2
Provides:       sax = 2.0
Provides:       xslt = 1.0
Provides:       xml-commons-apis = %{epoch}:%{version}
Obsoletes:      xml-commons-apis <= 0:1.3.02-2jpp
Requires:       jpackage-utils >= 0:1.6
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description jaxp-1.1-apis
DOM 2 org.w3c.dom and SAX XML 2.0 org.xml.sax processor apis used 
by several pieces of Apache software. XSLT 1.0.
This version includes the JAXP 1.1 APIs -- Java API for XML 
Processing 1.1, i.e. javax.xml{.parsers,.transform}

%package jaxp-1.1-apis-javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}-jaxp-1.1-apis
Provides:       %{name}-apis-javadoc = %{epoch}:%{version}

%description jaxp-1.1-apis-javadoc
%{summary}.

%package jaxp-1.1-apis-manual
Group:          Development/Java
Summary:        Documents for %{name}-jaxp-1.1-apis

%description jaxp-1.1-apis-manual
%{summary}.

%package which10
Summary:        XmlWhich 1.0 utility from %{name}
Group:          Development/Java
Provides:       xml-commons-which = 0:%{version}
Obsoletes:      xml-commons-which < 0:1.3.03
Requires:       jpackage-utils >= 0:1.6
Requires:       java >= 0:1.6
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       ant >= 0:1.6
Requires(preun): update-alternatives
Requires(post): update-alternatives


%description which10
%{name}.

%package which10-javadoc
Summary:        Javadoc for %{name}-which10
Group:          Development/Java

%description which10-javadoc
Javadoc for %{name}-which.

%package resolver10
Summary:        XmlResolver 1.0 utility from %{name}
Group:          Development/Java
Provides:       xml-commons-resolver = 0:%{version}
Obsoletes:      xml-commons-resolver < 0:1.3.03
Requires:       jpackage-utils >= 0:1.6
Requires:       java >= 0:1.6
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description resolver10
%{summary}.

%package resolver10-javadoc
Summary:        Javadoc for %{name}-resolver10
Group:          Development/Java

%description resolver10-javadoc
%{summary}.

%package resolver11
Summary:        XmlResolver 1.1 utility from %{name}
Group:          Development/Java
Provides:       xml-commons-resolver = 0:%{version}
Obsoletes:      xml-commons-resolver < 0:1.3.03
Requires:       jpackage-utils >= 0:1.6
Requires:       java >= 0:1.6
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires(preun): update-alternatives
Requires(post):  update-alternatives

%description resolver11
%{summary}.

%package resolver11-javadoc
Summary:        Javadoc for %{name}-resolver11
Group:          Development/Java

%description resolver11-javadoc
%{summary}.

%package jaxp-1.2-apis
Summary:        JAXP 1.2, DOM 2, SAX 2.0.1, SAX2-ext 1.0 apis
Group:          Development/Java
Provides:       jaxp = 1.2
Provides:       dom = 2
Provides:       sax = 2.0.1
Provides:       xslt = 1.0
Provides:       xml-commons-apis = %{epoch}:%{version}
Obsoletes:      xml-commons-apis <= 0:1.3.02-2jpp
Requires:       jpackage-utils >= 0:1.6
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description jaxp-1.2-apis
DOM 2 org.w3c.dom and SAX XML 2.0 org.xml.sax processor apis used 
by several pieces of Apache software. XSLT 1.0.
This version includes the JAXP 1.2 APIs -- Java API for XML 
Processing 1.2, i.e. javax.xml{.parsers,.transform}

%package jaxp-1.2-apis-javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}-jaxp-1.2-apis
Provides:       %{name}-apis-javadoc = %{epoch}:%{version}

%description jaxp-1.2-apis-javadoc
%{summary}.

%package jaxp-1.2-apis-manual
Group:          Development/Java
Summary:        Documents for %{name}-jaxp-1.2-apis

%description jaxp-1.2-apis-manual
%{summary}.

%package jaxp-1.3-apis
Summary:        JAXP 1.3, DOM 2, SAX 2.0.1, SAX2-ext 1.0 apis
Group:          Development/Java
Provides:       jaxp = 1.3
Provides:       dom = 3
Provides:       sax = 2.0.2
Provides:       xslt = 1.0
Provides:       xml-commons-apis = %{epoch}:%{version}
Obsoletes:      xml-commons-apis <= 0:1.3.02-2jpp
Requires:       jpackage-utils >= 0:1.6
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description jaxp-1.3-apis
DOM 3 org.w3c.dom and SAX XML 2.0.2 (sax2r3) org.xml.sax
processor apis used by several pieces of Apache software.
Thi version includes the JAXP 1.3 APIs --
JSR 206, Java API for XML Processing 1.3, i.e.
javax.xml{.parsers,.transform,.validation,.datatype,.xtype}.

%package jaxp-1.3-apis-javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}-jaxp-1.3-apis
Provides:       %{name}-apis-javadoc = %{epoch}:%{version}

%description jaxp-1.3-apis-javadoc
%{summary}.

%package jaxp-1.3-apis-manual
Group:          Development/Java
Summary:        Documents for %{name}-jaxp-1.3-apis

%description jaxp-1.3-apis-manual
%{summary}.

%package jaxp-1.4-apis
Summary:        JAXP 1.4, DOM 3, SAX 2.0.1, SAX2-ext 1.0 apis
Group:          Development/Java
Provides:       jaxp = 1.4
Provides:       dom = 3
Provides:       sax = 2.0.2
Provides:       xslt = 1.0
Provides:       xml-commons-apis = %{epoch}:%{version}
Obsoletes:      xml-commons-apis <= 0:1.3.02-2jpp
Requires:       jpackage-utils >= 0:1.6
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description jaxp-1.4-apis
DOM 3 org.w3c.dom and SAX XML 2.0.2 (sax2r3) org.xml.sax
processor apis used by several pieces of Apache software.
Thi version includes the JAXP 1.3 APIs --
JSR 206, Java API for XML Processing 1.3, i.e.
javax.xml{.parsers,.transform,.validation,.datatype,.xtype}.

%package jaxp-1.4-apis-javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}-jaxp-1.4-apis
Provides:       %{name}-apis-javadoc = %{epoch}:%{version}

%description jaxp-1.4-apis-javadoc
%{summary}.

%package jaxp-1.4-apis-manual
Group:          Development/Java
Summary:        Documents for %{name}-jaxp-1.4-apis

%description jaxp-1.4-apis-manual
%{summary}.

%package which11
Group:          Development/Java
Summary:        XmlWhich 1.1 from %{name}
Provides:       xml-commons-which = 0:%{version}
Obsoletes:      xml-commons-which < 0:1.3.03
Requires:       jpackage-utils >= 0:1.6
Requires:       java >= 0:1.6
Requires:       ant >= 0:1.6
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description which11
%{summary}.

%package which11-javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}-which11

%description which11-javadoc
%{summary}.

%package which12
Group:          Development/Java
Summary:        XmlWhich 1.2 from %{name}
Provides:       xml-commons-which = 0:%{version}
Obsoletes:      xml-commons-which < 0:1.3.03
Requires:       jpackage-utils >= 0:1.6
Requires:       java >= 0:1.6
Requires:       ant >= 0:1.6
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description which12
%{summary}.

%package which12-javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}-which12

%description which12-javadoc
%{summary}.

%package resolver12
Group:          Development/Java
Summary:        XmlResolver 1.2 from %{name}
Provides:       xml-commons-resolver = 0:%{version}
Obsoletes:      xml-commons-resolver < 0:1.3.03
Requires:       jpackage-utils >= 0:1.6
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       java >= 0:1.6
Requires(preun): update-alternatives
Requires(post): update-alternatives

%description resolver12
%{summary}.

%package resolver12-javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}-resolver12

%description resolver12-javadoc
%{summary}.

%prep
%setup -q -T -c
%{__tar} xf %{SOURCE0}
%{__tar} xf %{SOURCE1}
%{__tar} xf %{SOURCE2}
%{__tar} xf %{SOURCE3}
%{__tar} xf %{SOURCE32}

# remove all binary libs and prebuilt javadocs
rm -rf `find . -name "*.jar" -o -name "*.gz"`
pushd xml-commons-external-1_3_05
tar x --strip-components=1 -f %SOURCE30
cp ../xml-commons-resolver-1_2/java/which.xml java/
%patch0 -p0 -b .p0~
popd
%patch1 -p0 -b .p1~

for i in `egrep -rl 'enum( |\.)' *| egrep '\.java$'`; do
    %{__perl} -pi -e 's/enum([ \.])/enum1\1/g' $i
done

%build
export JAVA_HOME=%_prefix/lib/jvm/java-1.6.0
pushd xml-commons-1_0_b2
pushd java
sed -e 's|call Resolver|call resolver|g' resolver.xml > tempf
sed -e 's|classname="org.apache.xml.resolver.Catalog"|fork="yes" classname="org.apache.xml.resolver.apps.resolver"|g' tempf > resolver.xml
sed -e 's|org.apache.xml.resolver.Catalog|org.apache.xml.resolver.apps.resolver|g' src/manifest.resolver > tempf
cp tempf src/manifest.resolver
rm tempf
popd
# (anssi) Uses 1.5-reserved key "enum"
ant -Dant.build.javac.source=1.4 jars
popd
pushd xml-commons-resolver-1_2
mkdir -p build/site/components/resolver
pushd java
sed -e 's|call Resolver|call resolver|g' resolver.xml > tempf
sed -e 's|classname="org.apache.xml.resolver.Catalog"|fork="yes" classname="org.apache.xml.resolver.apps.resolver"|g' tempf > resolver.xml
sed -e 's|org.apache.xml.resolver.Catalog|org.apache.xml.resolver.apps.resolver|g' src/manifest.resolver > tempf
cp tempf src/manifest.resolver
rm tempf
popd
# (anssi) Uses 1.5-reserved key "enum"
ant -Dant.build.javac.source=1.4 jars javadocs
popd
pushd xml-commons-external-1_2_06
ant -f java/external/build.xml jar javadoc
popd
pushd xml-commons-external-1_3_05
pushd java
sed -e 's|call Resolver|call resolver|g' resolver.xml > tempf
sed -e 's|classname="org.apache.xml.resolver.Catalog"|fork="yes" classname="org.apache.xml.resolver.apps.resolver"|g' tempf > resolver.xml
sed -e 's|org.apache.xml.resolver.Catalog|org.apache.xml.resolver.apps.resolver|g' src/manifest.resolver > tempf
cp tempf src/manifest.resolver
rm tempf
popd
ant jars javadocs
popd
pushd xml-commons-external-1_4_01
ant -f java/external/build.xml jar javadoc
popd

%install
rm -rf $RPM_BUILD_ROOT

# Jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
# JAXP11
install -m 644 xml-commons-1_0_b2/java/external/build/xml-apis.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-jaxp-1.1-apis-%{version}.jar
# resolver10
install -m 644 xml-commons-1_0_b2/java/build/resolver.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-resolver10-%{version}.jar
# which10
install -m 644 xml-commons-1_0_b2/java/build/which.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-which10-%{version}.jar
# resolver11
install -m 644 xml-commons-resolver-1_2/java/build/resolver.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-resolver11-%{version}.jar
# which11
install -m 644 xml-commons-external-1_3_05/java/build/which.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-which11-%{version}.jar
# JAXP12
install -m 644 xml-commons-external-1_2_06/java/external/build/xml-apis.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-jaxp-1.2-apis-%{version}.jar
# JAXP13
install -m 644 xml-commons-external-1_3_05/java/external/build/xml-apis.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-jaxp-1.3-apis-%{version}.jar
install -m 644 xml-commons-external-1_3_05/java/external/build/xml-apis-ext.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-jaxp-1.3-apis-ext-%{version}.jar
# resolver12
install -m 644 xml-commons-resolver-1_2/java/build/resolver.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-resolver12-%{version}.jar
# which12
install -m 644 xml-commons-resolver-1_2/java/build/which.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-which12-%{version}.jar
# JAXP14
install -m 644 xml-commons-external-1_4_01/java/external/build/xml-apis.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-jaxp-1.4-apis-%{version}.jar
install -m 644 xml-commons-external-1_4_01/java/external/build/xml-apis-ext.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-jaxp-1.4-apis-ext-%{version}.jar

pushd $RPM_BUILD_ROOT%{_javadir}
for jar in *-%{version}*; do
ln -sf ${jar} $(echo $jar | sed -e 's|-%{version}\.jar|.jar|');
done
ln -sf %{name}-jaxp-1.1-apis.jar jaxp11.jar
ln -sf %{name}-jaxp-1.2-apis.jar jaxp12.jar
ln -sf %{name}-jaxp-1.3-apis.jar jaxp13.jar
ln -sf %{name}-jaxp-1.3-apis.jar dom3.jar
ln -sf %{name}-jaxp-1.4-apis.jar jaxp14.jar
popd


# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.1-apis-%{version}

# JAXP11
cp -pr xml-commons-1_0_b2/java/external/build/docs/javadoc/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.1-apis-%{version}
ln -s %{name}-jaxp-1.1-apis-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.1-apis
rm -rf xml-commons-1_0_b2/java/external/build/docs/javadoc

# resolver10
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-resolver10-%{version}/org/apache/xml
cp -pr xml-commons-1_0_b2/java/build/docs/javadocs/org/apache/xml/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-resolver10-%{version}/org/apache/xml
ln -s %{name}-resolver10-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-resolver10

# resolver11
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-resolver11-%{version}/
cp -pr xml-commons-resolver-1_2/build/site/components/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-resolver10-%{version}/
ln -s %{name}-resolver11-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-resolver11

# which10
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-which10-%{version}/org/apache/env
cp -pr xml-commons-1_0_b2/java/build/docs/javadocs/org/apache/env/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-which10-%{version}/org/apache/env
ln -s %{name}-which10-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-which10

# JAXP12
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.2-apis-%{version}
cp -pr xml-commons-external-1_2_06/java/external/build/docs/javadoc/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.2-apis-%{version}
ln -s %{name}-jaxp-1.2-apis-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.2-apis
rm -rf xml-commons-external-1_2_06/java/external/build/docs/javadoc

# JAXP13
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.3-apis-%{version}
cp -pr xml-commons-external-1_3_05/java/external/build/docs/javadoc/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.3-apis-%{version}
ln -s %{name}-jaxp-1.3-apis-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.3-apis
rm -rf xml-commons-external-1_3_05/java/external/build/docs/javadoc

# JAXP14
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.4-apis-%{version}
cp -pr xml-commons-external-1_4_01/java/external/build/docs/javadoc/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.4-apis-%{version}
ln -s %{name}-jaxp-1.4-apis-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.4-apis
rm -rf xml-commons-external-1_4_01/java/external/build/docs/javadoc

# resolver12
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-resolver12-%{version}
cp -pr xml-commons-external-1_3_05/java/build/apidocs/resolver/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-resolver12-%{version}
ln -s %{name}-resolver-12-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-resolver12

# which11
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-which11-%{version}
cp -pr xml-commons-external-1_3_05/java/build/apidocs/which/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-which11-%{version}
ln -s %{name}-which11-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-which11

# which12
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-which12-%{version}
cp -pr xml-commons-resolver-1_2/java/build/apidocs/which/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-which12-%{version}
ln -s %{name}-which12-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-which12

# Scripts
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1

cp -p %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/xml-which10
cp -p %{SOURCE5} $RPM_BUILD_ROOT%{_bindir}/xml-which11
cp -p %{SOURCE31} $RPM_BUILD_ROOT%{_bindir}/xml-which12

sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE7} \
  > $RPM_BUILD_ROOT%{_bindir}/xml-resolver10
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE9} \
  > $RPM_BUILD_ROOT%{_bindir}/xml-xread10
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE11} \
  > $RPM_BUILD_ROOT%{_bindir}/xml-xparse10

sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE6} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/xml-resolver10.1
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE8} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/xml-xread10.1
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE10} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/xml-xparse10.1

sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE13} \
  > $RPM_BUILD_ROOT%{_bindir}/xml-resolver11
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE15} \
  > $RPM_BUILD_ROOT%{_bindir}/xml-xread11
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE17} \
  > $RPM_BUILD_ROOT%{_bindir}/xml-xparse11

sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE12} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/xml-resolver11.1
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE14} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/xml-xread11.1
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE16} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/xml-xparse11.1

sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE19} \
  > $RPM_BUILD_ROOT%{_bindir}/xml-resolver12
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE21} \
  > $RPM_BUILD_ROOT%{_bindir}/xml-xread12
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE23} \
  > $RPM_BUILD_ROOT%{_bindir}/xml-xparse12

sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE18} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/xml-resolver12.1
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE20} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/xml-xread12.1
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE22} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/xml-xparse12.1

# Central CatalogManager.properties
install -d -m 755 $RPM_BUILD_ROOT%{resolverdir}
install -m 0644 %{SOURCE24} $RPM_BUILD_ROOT%{resolverdir}/CatalogManager.properties

# docs
# JAXP 1.1
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.1-apis-%{version}
install -m 0644 xml-commons-1_0_b2/java/external/LICENSE* $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.1-apis-%{version}
install -m 0644 xml-commons-1_0_b2/java/external/README* $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.1-apis-%{version}
# JAXP 1.2
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.2-apis-%{version}
install -m 0644 xml-commons-external-1_2_06/java/external/LICENSE* $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.2-apis-%{version}
install -m 0644 xml-commons-external-1_2_06/java/external/README* $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.2-apis-%{version}
# JAXP 1.3
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.3-apis-%{version}
install -m 0644 xml-commons-external-1_3_05/java/external/LICENSE* $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.3-apis-%{version}
install -m 0644 xml-commons-external-1_3_05/java/external/README* $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.3-apis-%{version}
# JAXP 1.4
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.4-apis-%{version}
install -m 0644 xml-commons-external-1_4_01/java/external/LICENSE* $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.4-apis-%{version}
install -m 0644 xml-commons-external-1_4_01/java/external/README* $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.4-apis-%{version}

# manuals
# JAXP 1.1
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-jaxp-1.1-apis-%{version}
cp -pr xml-commons-1_0_b2/java/external/build/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-jaxp-1.1-apis-%{version}
# JAXP 1.2
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-jaxp-1.2-apis-%{version}
cp -pr xml-commons-external-1_2_06/java/external/build/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-jaxp-1.2-apis-%{version}
# JAXP 1.3
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-jaxp-1.3-apis-%{version}
cp -pr xml-commons-external-1_3_05/java/external/build/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-jaxp-1.3-apis-%{version}
# JAXP 1.4
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-jaxp-1.4-apis-%{version}
cp -pr xml-commons-external-1_4_01/java/external/build/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-jaxp-1.4-apis-%{version}



# For Symlinks and alternatives
touch $RPM_BUILD_ROOT%{_javadir}/xml-commons-apis.jar
touch $RPM_BUILD_ROOT%{_javadir}/xml-commons-which.jar
touch $RPM_BUILD_ROOT%{_javadir}/xml-commons-resolver.jar
touch $RPM_BUILD_ROOT%{_javadir}/jaxp.jar
touch $RPM_BUILD_ROOT%{_javadir}/dom3.jar
touch $RPM_BUILD_ROOT%{_javadir}/dom2.jar
touch $RPM_BUILD_ROOT%{_javadir}/dom.jar
touch $RPM_BUILD_ROOT%{_javadir}/sax2.jar
touch $RPM_BUILD_ROOT%{_javadir}/sax.jar
touch $RPM_BUILD_ROOT%{_bindir}/xml-which
touch $RPM_BUILD_ROOT%{_bindir}/xml-resolver
touch $RPM_BUILD_ROOT%{_bindir}/xml-xread
touch $RPM_BUILD_ROOT%{_bindir}/xml-xparse
ln -s %{_sysconfdir}/alternatives/%{name}-apis-javadoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}-apis # ghost symlink
%{__chmod} 755 $RPM_BUILD_ROOT%{_bindir}*

%{__perl} -pi -e 's/\r$//g' README.html KEYS

%{gcj_compile}

# -----------------------------------------------------------------------------

%clean
rm -rf $RPM_BUILD_ROOT

# -----------------------------------------------------------------------------

%files 
%defattr(0644,root,root,0755)
%doc xml-commons-external-1_3_05/*.txt
%config(noreplace) %{resolverdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%endif

%files jaxp-1.1-apis
%defattr(0644,root,root,0755)
%doc %{_datadir}/%{name}-jaxp-1.1-apis-%{version}
%{_javadir}/%{name}-jaxp-1.1-apis*.jar
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-jaxp-1.1-apis*.jar.*
%endif
%ghost %{_javadir}/xml-commons-apis.jar
%ghost %{_javadir}/jaxp11.jar
%ghost %{_javadir}/jaxp.jar
%ghost %{_javadir}/dom2.jar
%ghost %{_javadir}/dom.jar
%ghost %{_javadir}/sax2.jar
%ghost %{_javadir}/sax.jar

%files jaxp-1.1-apis-javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}-jaxp-1.1-apis-%{version}
%ghost %{_javadocdir}/%{name}-jaxp-1.1-apis
%ghost %{_javadocdir}/%{name}-apis

%files jaxp-1.1-apis-manual
%defattr(0644,root,root,0755)
%doc %{_docdir}/%{name}-jaxp-1.1-apis-%{version}

%files which10
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-which10*.jar
%ghost %{_javadir}/xml-commons-which.jar
%attr(0755,root,root) %{_bindir}/xml-which10
%attr(0755,root,root) %ghost %{_bindir}/xml-which

%files which10-javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-which10-%{version}
%ghost %{_javadocdir}/%{name}-which10

%files resolver10
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-resolver10*.jar
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-resolver10*.jar.*
%endif
%ghost %{_javadir}/xml-commons-resolver.jar
%attr(0755,root,root) %{_bindir}/xml-resolver10
%attr(0755,root,root) %{_bindir}/xml-xread10
%attr(0755,root,root) %{_bindir}/xml-xparse10
%{_mandir}/man1/xml-resolver10.1*
%{_mandir}/man1/xml-xread10.1*
%{_mandir}/man1/xml-xparse10.1*
%attr(0755,root,root) %ghost %{_bindir}/xml-resolver
%attr(0755,root,root) %ghost %{_bindir}/xml-xread
%attr(0755,root,root) %ghost %{_bindir}/xml-xparse

%files resolver10-javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-resolver10-%{version}
%ghost %{_javadocdir}/%{name}-resolver10

%files resolver11
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-resolver11*.jar
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-resolver11*.jar.*
%endif
%ghost %{_javadir}/xml-commons-resolver.jar
%attr(0755,root,root) %{_bindir}/xml-resolver11
%attr(0755,root,root) %{_bindir}/xml-xread11
%attr(0755,root,root) %{_bindir}/xml-xparse11
%{_mandir}/man1/xml-resolver11.1*
%{_mandir}/man1/xml-xread11.1*
%{_mandir}/man1/xml-xparse11.1*
%attr(0755,root,root) %ghost %{_bindir}/xml-resolver
%attr(0755,root,root) %ghost %{_bindir}/xml-xread
%attr(0755,root,root) %ghost %{_bindir}/xml-xparse

%files resolver11-javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-resolver11-%{version}
%ghost %{_javadocdir}/%{name}-resolver11

%files jaxp-1.2-apis
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-jaxp-1.2-apis*.jar
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-jaxp-1.2-apis*.jar.*
%endif
%doc %{_datadir}/%{name}-jaxp-1.2-apis-%{version}
%ghost %{_javadir}/xml-commons-apis.jar
%ghost %{_javadir}/jaxp12.jar
%ghost %{_javadir}/jaxp.jar
%ghost %{_javadir}/dom2.jar
%ghost %{_javadir}/dom.jar
%ghost %{_javadir}/sax2.jar
%ghost %{_javadir}/sax.jar

%files jaxp-1.2-apis-javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-jaxp-1.2-apis-%{version}
%ghost %{_javadocdir}/%{name}-jaxp-1.2-apis
%ghost %{_javadocdir}/%{name}-apis

%files jaxp-1.2-apis-manual
%defattr(0644,root,root,0755)
%{_docdir}/%{name}-jaxp-1.2-apis-%{version}

%files jaxp-1.3-apis
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-jaxp-1.3-apis*.jar
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-jaxp-1.3-apis*.jar.*
%endif
%doc %{_datadir}/%{name}-jaxp-1.3-apis-%{version}
%ghost %{_javadir}/xml-commons-apis.jar
%ghost %{_javadir}/jaxp13.jar
%ghost %{_javadir}/jaxp.jar
%ghost %{_javadir}/dom3.jar
%ghost %{_javadir}/dom.jar
%ghost %{_javadir}/sax2.jar
%ghost %{_javadir}/sax.jar

%files jaxp-1.3-apis-javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-jaxp-1.3-apis-%{version}
%ghost %{_javadocdir}/%{name}-jaxp-1.3-apis
%ghost %{_javadocdir}/%{name}-apis

%files jaxp-1.3-apis-manual
%defattr(0644,root,root,0755)
%{_docdir}/%{name}-jaxp-1.3-apis-%{version}

%files jaxp-1.4-apis
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-jaxp-1.4-apis*.jar
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-jaxp-1.4-apis*.jar.*
%endif
%doc %{_datadir}/%{name}-jaxp-1.4-apis-%{version}
%ghost %{_javadir}/xml-commons-apis.jar
%ghost %{_javadir}/jaxp14.jar
%ghost %{_javadir}/jaxp.jar
%ghost %{_javadir}/dom3.jar
%ghost %{_javadir}/dom.jar
%ghost %{_javadir}/sax2.jar
%ghost %{_javadir}/sax.jar

%files jaxp-1.4-apis-javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-jaxp-1.4-apis-%{version}
%ghost %{_javadocdir}/%{name}-jaxp-1.4-apis
%ghost %{_javadocdir}/%{name}-apis

%files jaxp-1.4-apis-manual
%defattr(0644,root,root,0755)
%{_docdir}/%{name}-jaxp-1.4-apis-%{version}

%files which11
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-which11*.jar
%ghost %{_javadir}/xml-commons-which.jar
%attr(0755,root,root) %{_bindir}/xml-which11
%attr(0755,root,root) %ghost %{_bindir}/xml-which

%files which11-javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-which11-%{version}
%ghost %{_javadocdir}/%{name}-which11

%files which12
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-which12*.jar
%ghost %{_javadir}/xml-commons-which.jar
%attr(0755,root,root) %{_bindir}/xml-which12
%attr(0755,root,root) %ghost %{_bindir}/xml-which

%files which12-javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-which12-%{version}
%ghost %{_javadocdir}/%{name}-which12

%files resolver12
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-resolver12*.jar
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-resolver12*.jar.*
%endif
%ghost %{_javadir}/xml-commons-resolver.jar
%attr(0755,root,root) %{_bindir}/xml-resolver12
%attr(0755,root,root) %{_bindir}/xml-xread12
%attr(0755,root,root) %{_bindir}/xml-xparse12
%{_mandir}/man1/xml-resolver12.1*
%{_mandir}/man1/xml-xread12.1*
%{_mandir}/man1/xml-xparse12.1*
%attr(0755,root,root) %ghost %{_bindir}/xml-resolver
%attr(0755,root,root) %ghost %{_bindir}/xml-xread
%attr(0755,root,root) %ghost %{_bindir}/xml-xparse

%files resolver12-javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-resolver12-%{version}
%ghost %{_javadocdir}/%{name}-resolver12

%post jaxp-1.1-apis
#rm -f %{_javadir}/xml-commons-apis.jar
rm -f %{_javadir}/jaxp11.jar
ln -s %{name}-jaxp-1.1-apis.jar %{_javadir}/jaxp11.jar
/usr/sbin/update-alternatives --install %{_javadir}/xml-commons-apis.jar xml-commons-apis %{_javadir}/jaxp11.jar 10100
/usr/sbin/update-alternatives --install %{_javadir}/jaxp.jar jaxp %{_javadir}/jaxp11.jar 10100
/usr/sbin/update-alternatives --install %{_javadir}/dom2.jar dom2 %{_javadir}/jaxp11.jar 10100
/usr/sbin/update-alternatives --install %{_javadir}/dom.jar dom %{_javadir}/jaxp11.jar 10100
/usr/sbin/update-alternatives --install %{_javadir}/sax2.jar sax2 %{_javadir}/jaxp11.jar 10100
/usr/sbin/update-alternatives --install %{_javadir}/sax.jar sax %{_javadir}/jaxp11.jar 10100
/usr/sbin/update-alternatives --install %{_javadir}/xslt.jar xslt %{_javadir}/jaxp11.jar 10100
%if %{gcj_support}
%{update_gcjdb}
%endif

%postun jaxp-1.1-apis
if [ "$1" = "0" ]; then
  /usr/sbin/update-alternatives --remove xml-commons-apis %{_javadir}/jaxp11.jar
  /usr/sbin/update-alternatives --remove jaxp %{_javadir}/jaxp11.jar
  /usr/sbin/update-alternatives --remove dom2 %{_javadir}/jaxp11.jar
  /usr/sbin/update-alternatives --remove dom %{_javadir}/jaxp11.jar
  /usr/sbin/update-alternatives --remove sax2 %{_javadir}/jaxp11.jar
  /usr/sbin/update-alternatives --remove sax %{_javadir}/jaxp11.jar
  /usr/sbin/update-alternatives --remove xslt %{_javadir}/jaxp11.jar
  rm -f %{_javadir}/jaxp11.jar
fi
%if %{gcj_support}
%{clean_gcjdb}
%endif

%post jaxp-1.1-apis-javadoc
rm -f %{_javadocdir}/%{name}-jaxp-1.1-apis
ln -s %{name}-jaxp-1.1-apis-%{version} %{_javadocdir}/%{name}-jaxp-1.1-apis
/usr/sbin/update-alternatives --install %{_javadocdir}/xml-commons-apis xml-commons-apis-javadoc %{_javadocdir}/%{name}-jaxp-1.1-apis/ 10100

%postun jaxp-1.1-apis-javadoc
if [ "$1" = "0" ]; then
  /usr/sbin/update-alternatives --remove xml-commons-apis-javadoc %{_javadocdir}/%{name}-jaxp-1.1-apis/
  rm -f %{_javadocdir}/%{name}-jaxp-1.1-apis
fi

%post which10
/usr/sbin/update-alternatives --install %{_bindir}/xml-which xml-which %{_bindir}/xml-which10 10000
/usr/sbin/update-alternatives --install %{_javadir}/xml-commons-which.jar xml-commons-which %{_javadir}/xml-commons-which10.jar 10000

%postun which10
if [ "$1" = "0" ]; then
  /usr/sbin/update-alternatives --remove xml-which %{_bindir}/xml-which10
  /usr/sbin/update-alternatives --remove xml-commons-which %{_javadir}/xml-commons-which10.jar
fi

%post which10-javadoc
rm -f %{_javadocdir}/%{name}-which10
ln -s %{name}-which10-%{version} %{_javadocdir}/%{name}-which10

%postun which10-javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}-which10
fi

%post resolver10
/usr/sbin/update-alternatives --install %{_bindir}/xml-resolver xml-resolver %{_bindir}/xml-resolver10 10000 \
--slave  %{_javadir}/xml-commons-resolver.jar xml-commons-resolver %{_javadir}/xml-commons-resolver10.jar \
--slave  %{_bindir}/xml-xread xml-xread %{_bindir}/xml-xread10 \
--slave  %{_bindir}/xml-xparse xml-xparse %{_bindir}/xml-xparse10 \
--slave  %{_mandir}/man1/xml-resolver.1.bz2 xml-resolver.1.bz2 %{_mandir}/man1/xml-resolver10.1.bz2 \
--slave  %{_mandir}/man1/xml-xread.1.bz2 xml-xread.1.bz2 %{_mandir}/man1/xml-xread10.1.bz2 \
--slave  %{_mandir}/man1/xml-xparse.1.bz2 xml-xparse.1.bz2 %{_mandir}/man1/xml-xparse10.1.bz2 
%if %{gcj_support}
%{update_gcjdb}
%endif

%postun resolver10
if [ "$1" = "0" ]; then
  /usr/sbin/update-alternatives --remove xml-resolver %{_bindir}/xml-resolver10
fi
%if %{gcj_support}
%{clean_gcjdb}
%endif

%post resolver10-javadoc
rm -f %{_javadocdir}/%{name}-resolver10
ln -s %{name}-resolver10-%{version} %{_javadocdir}/%{name}-resolver10

%postun resolver10-javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}-resolver10
fi

%post resolver11
/usr/sbin/update-alternatives --install %{_bindir}/xml-resolver xml-resolver %{_bindir}/xml-resolver11 10100 \
--slave  %{_javadir}/xml-commons-resolver.jar xml-commons-resolver %{_javadir}/xml-commons-resolver11.jar \
--slave  %{_bindir}/xml-xread xml-xread %{_bindir}/xml-xread11 \
--slave  %{_bindir}/xml-xparse xml-xparse %{_bindir}/xml-xparse11 \
--slave  %{_mandir}/man1/xml-resolver.1.bz2 xml-resolver.1.bz2 %{_mandir}/man1/xml-resolver11.1.bz2 \
--slave  %{_mandir}/man1/xml-xread.1.bz2 xml-xread.1.bz2 %{_mandir}/man1/xml-xread11.1.bz2 \
--slave  %{_mandir}/man1/xml-xparse.1.bz2 xml-xparse.1.bz2 %{_mandir}/man1/xml-xparse11.1.bz2 
%if %{gcj_support}
%{update_gcjdb}
%endif

%postun resolver11
if [ "$1" = "0" ]; then
  /usr/sbin/update-alternatives --remove xml-resolver %{_bindir}/xml-resolver11
fi
%if %{gcj_support}
%{clean_gcjdb}
%endif

%post resolver11-javadoc
rm -f %{_javadocdir}/%{name}-resolver11
ln -s %{name}-resolver11-%{version} %{_javadocdir}/%{name}-resolver11

%postun resolver11-javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}-resolver11
fi

%post jaxp-1.2-apis
rm -f %{_javadir}/xml-commons-apis.jar
rm -f %{_javadir}/jaxp12.jar
ln -s %{name}-jaxp-1.2-apis.jar %{_javadir}/jaxp12.jar
/usr/sbin/update-alternatives --install %{_javadir}/xml-commons-apis.jar xml-commons-apis %{_javadir}/jaxp12.jar 10200
/usr/sbin/update-alternatives --install %{_javadir}/jaxp.jar jaxp %{_javadir}/jaxp12.jar 10200
/usr/sbin/update-alternatives --install %{_javadir}/dom2.jar dom2 %{_javadir}/jaxp12.jar 10200
/usr/sbin/update-alternatives --install %{_javadir}/dom.jar dom %{_javadir}/jaxp12.jar 10200
/usr/sbin/update-alternatives --install %{_javadir}/sax2.jar sax2 %{_javadir}/jaxp12.jar 10200
/usr/sbin/update-alternatives --install %{_javadir}/sax.jar sax %{_javadir}/jaxp12.jar 10200
/usr/sbin/update-alternatives --install %{_javadir}/xslt.jar xslt %{_javadir}/jaxp12.jar 10200
%if %{gcj_support}
%{update_gcjdb}
%endif

%postun jaxp-1.2-apis
if [ "$1" = "0" ]; then
  /usr/sbin/update-alternatives --remove xml-commons-apis %{_javadir}/jaxp12.jar
  /usr/sbin/update-alternatives --remove jaxp %{_javadir}/jaxp12.jar
  /usr/sbin/update-alternatives --remove dom2 %{_javadir}/jaxp12.jar
  /usr/sbin/update-alternatives --remove dom %{_javadir}/jaxp12.jar
  /usr/sbin/update-alternatives --remove sax2 %{_javadir}/jaxp12.jar
  /usr/sbin/update-alternatives --remove sax %{_javadir}/jaxp12.jar
  /usr/sbin/update-alternatives --remove xslt %{_javadir}/jaxp12.jar
  rm -f %{_javadir}/jaxp12.jar
fi
%if %{gcj_support}
%{clean_gcjdb}
%endif

%post jaxp-1.2-apis-javadoc
rm -f %{_javadocdir}/%{name}-jaxp-1.2-apis
ln -s %{name}-jaxp-1.2-apis-%{version} %{_javadocdir}/%{name}-jaxp-1.2-apis
/usr/sbin/update-alternatives --install %{_javadocdir}/xml-commons-apis xml-commons-apis-javadoc %{_javadocdir}/%{name}-jaxp-1.2-apis/ 10200

%postun jaxp-1.2-apis-javadoc
if [ "$1" = "0" ]; then
  /usr/sbin/update-alternatives --remove xml-commons-apis-javadoc %{_javadocdir}/%{name}-jaxp-1.2-apis/
  rm -f %{_javadocdir}/%{name}-jaxp-1.2-apis
fi

%post jaxp-1.3-apis
rm -f %{_javadir}/xml-commons-apis.jar
rm -f %{_javadir}/jaxp13.jar
ln -s %{name}-jaxp-1.3-apis.jar %{_javadir}/jaxp13.jar
/usr/sbin/update-alternatives --install %{_javadir}/xml-commons-apis.jar xml-commons-apis %{_javadir}/jaxp13.jar 10300
/usr/sbin/update-alternatives --install %{_javadir}/jaxp.jar jaxp %{_javadir}/jaxp13.jar 10300
/usr/sbin/update-alternatives --install %{_javadir}/dom.jar dom %{_javadir}/jaxp13.jar 10300
/usr/sbin/update-alternatives --install %{_javadir}/sax2.jar sax2 %{_javadir}/jaxp13.jar 10300
/usr/sbin/update-alternatives --install %{_javadir}/sax.jar sax %{_javadir}/jaxp13.jar 10300
/usr/sbin/update-alternatives --install %{_javadir}/xslt.jar xslt %{_javadir}/jaxp13.jar 10300
%if %{gcj_support}
%{update_gcjdb}
%endif

%postun jaxp-1.3-apis
if [ "$1" = "0" ]; then
  /usr/sbin/update-alternatives --remove xml-commons-apis %{_javadir}/jaxp13.jar
  /usr/sbin/update-alternatives --remove jaxp %{_javadir}/jaxp13.jar
  /usr/sbin/update-alternatives --remove dom %{_javadir}/jaxp13.jar
  /usr/sbin/update-alternatives --remove sax2 %{_javadir}/jaxp13.jar
  /usr/sbin/update-alternatives --remove sax %{_javadir}/jaxp13.jar
  /usr/sbin/update-alternatives --remove xslt %{_javadir}/jaxp13.jar
  rm -f %{_javadir}/jaxp13.jar
fi
%if %{gcj_support}
%{clean_gcjdb}
%endif

%post jaxp-1.3-apis-javadoc
rm -f %{_javadocdir}/%{name}-jaxp-1.3-apis
ln -s %{name}-jaxp-1.3-apis-%{version} %{_javadocdir}/%{name}-jaxp-1.3-apis
/usr/sbin/update-alternatives --install %{_javadocdir}/xml-commons-apis xml-commons-apis-javadoc %{_javadocdir}/%{name}-jaxp-1.3-apis/ 10300

%postun jaxp-1.3-apis-javadoc
if [ "$1" = "0" ]; then
  /usr/sbin/update-alternatives --remove xml-commons-apis-javadoc %{_javadocdir}/%{name}-jaxp-1.3-apis/
  rm -f %{_javadocdir}/%{name}-jaxp-1.3-apis
fi

%post which11
/usr/sbin/update-alternatives --install %{_bindir}/xml-which xml-which %{_bindir}/xml-which11 10100
/usr/sbin/update-alternatives --install %{_javadir}/xml-commons-which.jar xml-commons-which %{_javadir}/xml-commons-which11.jar 10100

%postun which11
if [ "$1" = "0" ]; then
  /usr/sbin/update-alternatives --remove xml-which %{_bindir}/xml-which11
  /usr/sbin/update-alternatives --remove xml-commons-which %{_javadir}/xml-commons-which11.jar
fi

%post which12
/usr/sbin/update-alternatives --install %{_bindir}/xml-which xml-which %{_bindir}/xml-which12 10200
/usr/sbin/update-alternatives --install %{_javadir}/xml-commons-which.jar xml-commons-which %{_javadir}/xml-commons-which12.jar 10200

%postun which12
if [ "$1" = "0" ]; then
  /usr/sbin/update-alternatives --remove xml-which %{_bindir}/xml-which12
  /usr/sbin/update-alternatives --remove xml-commons-which %{_javadir}/xml-commons-which12.jar
fi

%post resolver12
/usr/sbin/update-alternatives --install %{_bindir}/xml-resolver xml-resolver %{_bindir}/xml-resolver12 10200 \
--slave  %{_javadir}/xml-commons-resolver.jar xml-commons-resolver %{_javadir}/xml-commons-resolver12.jar \
--slave  %{_bindir}/xml-xread xml-xread %{_bindir}/xml-xread12 \
--slave  %{_bindir}/xml-xparse xml-xparse %{_bindir}/xml-xparse12 \
--slave  %{_mandir}/man1/xml-resolver.1.lzma xml-resolver.1.lzma %{_mandir}/man1/xml-resolver12.1.lzma \
--slave  %{_mandir}/man1/xml-xread.1.lzma xml-xread.1.lzma %{_mandir}/man1/xml-xread12.1.lzma \
--slave  %{_mandir}/man1/xml-xparse.1.lzma xml-xparse.1.lzma %{_mandir}/man1/xml-xparse12.1.lzma 
%if %{gcj_support}
%{update_gcjdb}
%endif

%postun resolver12
if [ "$1" = "0" ]; then
  /usr/sbin/update-alternatives --remove xml-resolver %{_bindir}/xml-resolver12
fi
%if %{gcj_support}
%{clean_gcjdb}
%endif

# -----------------------------------------------------------------------------


%changelog
* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0:1.3.04-3.0.7mdv2011.0
+ Revision: 608221
- rebuild

* Wed Oct 28 2009 Ahmad Samir <ahmadsamir@mandriva.org> 0:1.3.04-3.0.6mdv2010.1
+ Revision: 459748
- Really fix the alternatives
- Fix update-alternatives (mdv bug #48886)

* Tue Aug 18 2009 Jaroslav Tulach <jtulach@mandriva.org> 0:1.3.04-3.0.5mdv2010.0
+ Revision: 417660
- Simplifying dependencies. Requiring java 1.6 and removing special dependencies on various XML tools as they are part of java 1.6 already

* Sat Jun 20 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0:1.3.04-3.0.4mdv2010.0
+ Revision: 387492
- disable gcj support
- package xml-apis-ext.jar

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0:1.3.04-3.0.3mdv2009.1
+ Revision: 350927
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0:1.3.04-3.0.2mdv2009.0
+ Revision: 266118
- rebuild early 2009.0 package (before pixel changes)

* Tue May 13 2008 Alexander Kurtakov <akurtakov@mandriva.org> 0:1.3.04-0.0.2mdv2009.0
+ Revision: 206557
- use macros for gcj_compile

* Sat Dec 29 2007 David Walluck <walluck@mandriva.org> 0:1.3.04-0.0.1mdv2008.1
+ Revision: 139067
- 1.3.04

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Anssi Hannula <anssi@mandriva.org>
    - buildrequire java-rpmbuild, i.e. build with icedtea on x86(_64)

* Sat Sep 15 2007 Anssi Hannula <anssi@mandriva.org> 5.5mdv2008.0-current
+ Revision: 87278
- rebuild to filter out autorequires of GCJ AOT objects
- remove unnecessary Requires(post) on java-gcj-compat

  + Thierry Vignaud <tv@mandriva.org>
    - kill file require on update-alternatives

* Tue Aug 14 2007 Anssi Hannula <anssi@mandriva.org> 0:1.3.03-5.4mdv2008.0
+ Revision: 63350
- mark xml-commons 1.0 and 1.1 source java source code version as 1.4 as
  they use "enum" which is a reserved word in 1.5 (fixes build)
- remove Requires(post,postun): java-gcj-compat from xml-commons package
  as there is no %%post nor %%postun (Camille B?\195?\169gnis)
- use xml-commons-jaxp-1.1-apis, xml-commons-jaxp-1.2-apis and
  xml-commons-jaxp-1.3-apis explicitely instead of the generic
  xml-commons-apis which is provided by multiple packages (see bug #31473)


* Sat Mar 10 2007 Anssi Hannula <anssi@mandriva.org> 1.3.03-5.3mdv2007.1
+ Revision: 140500
- fix man page alternatives

* Sat Dec 16 2006 David Walluck <walluck@mandriva.org> 0:1.3.03-5.2mdv2007.1
+ Revision: 98105
- rebuild
- Import xml-commons

* Sun Jul 23 2006 David Walluck <walluck@mandriva.org> 0:1.3.03-5.1mdv2007.0
- sync with 0:1.3.03-5jpp

* Thu Jun 22 2006 David Walluck <walluck@mandriva.org> 0:1.3.02-0.b2.7.7.3mdv2007.0
- rebuild

* Fri Jun 02 2006 David Walluck <walluck@mandriva.org> 0:1.3.02-0.b2.7.7.2mdv2007.0
- rebuild for libgcj.so.7

* Mon Apr 10 2006 David Walluck <walluck@mandriva.org> 0:1.3.02-0.b2.7.7.1mdk
- 1.3.02

* Sun May 08 2005 David Walluck <walluck@mandriva.org> 0:1.0-0.b2.7.1mdk
- release


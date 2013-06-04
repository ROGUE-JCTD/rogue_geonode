#!/bin/bash

set -e

DL_ROOT=/var/www/geoserver

# Make sure last job cleaned up
if [ -d ./tmp ]; then
  rm -rf ./tmp
fi

# Checkout exts from server
cp -r ../../geoserver_ext tmp
cp -r debian tmp
pushd tmp

# Replace GeoNode port for production.
#sed -i 's/localhost:8000/127.0.0.1/g' \
#    src/main/java/org/geonode/security/GeoNodeSecurityProvider.java

DEB_VERSION=2.0+$(date +"%Y%m%d%H%M")

mvn clean install

# Build for launchpad
#git-dch --spawn-editor=snapshot --new-version=$DEB_VERSION --git-author --id-length=6 --ignore-branch  --auto --release
#debuild -S
#debuild -uc -us -A
#dput ppa:geonode/snapshots ../geoserver-geonode_${DEB_VERSION}_source.changes
#rm ../geoserver-geonode*

# Re-build local debs
debuild

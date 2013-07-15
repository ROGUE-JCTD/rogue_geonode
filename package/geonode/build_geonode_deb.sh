#!/bin/bash
set -e

# Setup environment variables.
PYENV_HOME=$WORKSPACE/.pyenv/
GIT_REV=$(git log -1 --pretty=format:%h)

# Delete previously built virtualenv
if [ -d $PYENV_HOME ]; then
    rm -rf $PYENV_HOME
fi

# Delete previously built geonode
if [ -d ../geonode ]; then
    rm -rf ../geonode
fi

# Setup the virtualenv
virtualenv --no-site-packages $PYENV_HOME
source $PYENV_HOME/bin/activate
pip install -U Paver

# Setup and Build GeoNode
git clone https://github.com/GeoNode/geonode.git ../geonode

# Build basic Geonode deb
pushd ../geonode
paver setup
popd

# Build ROGUE geonode
paver setup
paver deb -p rogue-jctd/rogue -k ECFC1E52

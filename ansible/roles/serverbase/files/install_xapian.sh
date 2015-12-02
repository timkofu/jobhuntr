#!/usr/bin/env bash
# https://github.com/notanumber/xapian-haystack#installation
# Python 2.7.10
#VERSION=1.2.19
VERSION=1.2.21

# prepare
mkdir /tmp/xapian && cd /tmp/xapian

CORE=xapian-core-$VERSION
BINDINGS=xapian-bindings-$VERSION

# download
echo "Downloading source..."
curl -O http://oligarchy.co.uk/xapian/$VERSION/${CORE}.tar.xz
curl -O http://oligarchy.co.uk/xapian/$VERSION/${BINDINGS}.tar.xz

# extract
echo "Extracting source..."
tar xf ${CORE}.tar.xz
tar xf ${BINDINGS}.tar.xz

# install
echo "Installing Xapian-core..."
cd /tmp/xapian/${CORE}
./configure && make && sudo make install

#PYV=`python -c "import sys;t='{v[0]}'.format(v=list(sys.version_info[:1]));sys.stdout.write(t)";`

#if [ $PYV = "2" ]; then
PYTHON_FLAG=--with-python
#else
#    PYTHON_FLAG=--with-python3
#fi

#if [ $VERSION = "1.3.3" ]; then
#    XAPIAN_CONFIG=$VIRTUAL_ENV/bin/xapian-config-1.3
#else
XAPIAN_CONFIG=
#fi

echo "Installing Xapian-bindings..."
sudo ldconfig
cd /tmp/xapian/${BINDINGS}
./configure $PYTHON_FLAG XAPIAN_CONFIG=$XAPIAN_CONFIG && make && sudo make install

# clean
#rm -rf $VIRTUAL_ENV/packages

# test
python -c "import xapian"

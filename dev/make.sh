#!/bin/sh

# see readme.txt in this directory for information

BASEDIR=$(dirname $0)

VIRTUALENV=`which virtualenv`
APTGET=`which apt-get`

DPKG_LIST=$BASEDIR/dpkg.txt
PYPI_LIST=$BASEDIR/pypi.txt


echo "Bulding environemnt (for Debian/Ubuntu)..."
echo ""
echo "virtualenv: ${VIRTUALENV:=Not found!}"
echo "apt-get: ${APTGET:=Not found!}"
echo "dpkgs: ${DPKG_LIST:=Not found!}"
echo "pypis: ${PYPI_LIST:=Not found!}"
echo ""

# ensure path argument is provided
if [ "$1" != "" ]; then

    # install apt-get packages if any
    if [ -f $DPKG_LIST ]; then
        cat $DPKG_LIST | (while read a; do sudo $APTGET -y install $a; done)
    fi

    # create and activate virtualenv
    if [ ! -f $1/bin/activate ]; then
        $VIRTUALENV --no-site-packages "$1"
    else
        echo "Virtualenv seems to exists: activating."
    fi
    . "$1/bin/activate"

    PIP=`which pip`
    echo "pip: ${PIP:=Not found!}"

    if [ "$VIRTUAL_ENV" != "" ]; then

        # install python packages
        if [ -f $PYPI_LIST ]; then
            $PIP install --upgrade -r $PYPI_LIST
        fi

        cd $1
        DJANGO_PROJ=$1/django_project
        echo "Creating django project at $DJANGO_PROJ ..."
        ./bin/django-admin.py startproject django_project

        echo "Creating app symlinks from $BASEDIR to $DJANGO_PROJ ..."
        ln -vs $BASEDIR/urls.py $BASEDIR/settings $BASEDIR/dreamvault .

        echo "!! You need to set up the database, copy/link settings/local_settings_example.py"
        echo ""  to local_settings.py and run: python manage.py syncdb !!"

    else
        echo "VIRTUAL_ENV not active, skipping installing pypi packages."
    fi

else
    echo "!! Provide path for build environment: sh make.sh /path/to/build"
fi


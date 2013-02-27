#!bash

# Create a virtual environment and ensure all requirements are installed
#
# Provide a path on the command line.
#
# 1. Check dpkg.txt packages are installed (by attempting to install/update them)
# 2. Create virtualenv environment
# 3. Install all the pypi packages from pypi.txt
#
# Note: Assumes pip and virtualenv are already installed

BASEDIR=$(dirname $0)

PIP=`which pip`
VIRTUALENV=`which virtualenv`
APTGET=`which apg-get`

# ensure path argument is provided
if [ "$1" != "" ]; then

    # install apt-get packages if any
    if [ -f dpkg.txt ]; then
        cat dpkg.txt | (while read a; do sudo $APTGET -y install $a; done)
    fi

    # create and activate virtualenv
    $VIRTUALENV "$1"
    . "$1/bin/activate"

    if [ "$VIRTUAL_ENV" != "" ]; then

        # install python packages
        if [ -f pypi.txt ]; then
            $PIP install --upgrade -r pypi.txt
        fi

    else
        echo "VIRTUAL_ENV not active, skipping installing pypi packages."
    fi

else
    echo "Provide path for build environment"
fi


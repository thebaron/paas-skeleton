# .paas-skeleton/python-virtualenv.sh - owned by paas-skeleton.git

# if no VE_PATH has been specified, default it living inside $HOME
if [[ "x${VE_PATH}x" == "xx" ]]; then
    export VE_PATH=${HOME}/.ve
fi
if [ ! -d ${VE_PATH} ]; then
    mkdir -p ${VE_PATH}
fi

# set the actual virtualenv root location
# TODO: set virtualenv root location via OPENSHIFT
# TODO: set virtualenv root location via virtualenvwrapper
if [[ "x${VE_ROOT}x" == "xx" ]]; then
    export VE_ROOT=$VE_PATH/`basename $PWD`
fi

if [ ! -d ${VE_ROOT} ]; then
    echo "Virtual environment root $VE_ROOT missing, creating"
    mkdir -p ${VE_ROOT}
fi

# create the virtual environment only if it does not already exist
make check-paas-skeleton-env $VE_ROOT/bin/activate

# activate the virtual environment
source $VE_ROOT/bin/activate

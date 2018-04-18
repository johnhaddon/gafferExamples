export PYTHONPATH=`pwd`"/python:$PYTHONPATH"
export GAFFER_STARTUP_PATHS=`pwd`/startup:$GAFFER_STARTUP_PATHS

exec gaffer "$@"

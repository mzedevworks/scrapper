#!/bin/bash
ROOT=$(pwd)
echo $ROOT
#create virtual environment
VENV="$ROOT/env"
echo "Creating a virtual environment in directory $VENV"
virtualenv --python=python3.4 $VENV
cd $ROOT
echo "Activating virtual environment"
source $VENV/bin/activate
echo "Done"
echo "Installing packages"
$VENV/bin/pip install --upgrade pip setuptools
$VENV/bin/pip install -e ".[testing]"

#start server
echo "Do you want to run tests first"
echo "1: Yes"
echo "2: No"
read run_tests

if [ $run_tests = 1 ]; then
    $VENV/bin/pytest
fi

echo "Restarting development server"
$VENV/bin/pserve development.ini


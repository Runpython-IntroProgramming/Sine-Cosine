#!/bin/bash
set -e # exit with nonzero exit code if anything fails

# create the tests folder
mkdir tests
cd tests
git init
git pull https://${GH_REPO}
cd ..
# copy ggame
git clone https://github.com/BrythonServer/ggame.git

python tests/test.py ${TESTMODULE}

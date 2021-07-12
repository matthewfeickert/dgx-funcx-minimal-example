#!/bin/bash

pyenv deactivate
pyenv virtualenv 3.8.11 pyhf-funcx
pyenv activate pyhf-funcx
printf "Active pyenv environment: \n"
pyenv version

python -m pip install --upgrade pip setuptools wheel
python -m pip install -r core-requirements.txt
python -m pip list

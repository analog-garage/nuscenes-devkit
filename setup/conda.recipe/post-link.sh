#!/bin/bash

# HACK - install pyquaternion using pip
conda activate ${PREFIX-${CONDA_PREFIX}}
pip install 'pyquaternion>=0.9.5'


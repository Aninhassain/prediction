#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Make sure the build script is executable
chmod +x build.sh

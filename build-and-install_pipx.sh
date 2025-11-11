#!/bin/bash

# check if "gmod-binmod-template" exists in pipx list
if pipx list | grep -q "gmod-binmod-template"; then
    echo "uninstalling existing gmod-binmod-template..."
    pipx uninstall gmod-binmod-template
fi

echo "building gmod-binmod-template..."
pipx install .

# validate installation
if pipx list | grep -q "gmod-binmod-template"; then
    echo "gmod-binmod-template installed successfully!"
else
    echo "gmod-binmod-template installation failed!"
    exit 1
fi
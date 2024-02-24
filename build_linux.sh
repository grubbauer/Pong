#!/bin/bash

# Installing some librarys (python needs to be installed)
pip install pyglet

# Compile
pyinstaller --noconfirm --windowed "Pong.py"

# Making directorys and placeing files
mkdir -p dist/Pong/src/aud
mkdir -p dist/Pong/src/font
mkdir -p dist/Pong/src/img
cp -r src/aud dist/Pong/src/
cp -r src/font dist/Pong/src/
cp -r src/img dist/Pong/src/
cp License dist/Pong/

# Cleanup
rm Pong.spec
rm -rf build
mv dist/Pong ./
rm -rf dist
mv Pong build
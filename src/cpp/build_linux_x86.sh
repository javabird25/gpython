#!/bin/sh

# This script is for compiling C++ part of PyGmod for Linux.
# Main branch of Garry's Mod is still 32-bit.
# Building is performed inside a 32-bit Linux Docker image.
# DLLs will appear in this directory.

set -e

echo 'Building image (this can take a while)...'
image_id=$(docker build --quiet --file build_linux_x86.dockerfile .)
echo 'Creating container...'
container_id=$(docker create $image_id)
echo 'Copying output archive to host...'
docker cp $container_id:/build/out.tar .
echo 'Extracting the archive...'
tar -xf out.tar
echo 'Cleaning up...'
rm out.tar
docker container rm -f $container_id >/dev/null
docker image rm -f $image_id >/dev/null

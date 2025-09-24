#!/bin/bash

# Coping the files from one volume, inside the docker image at build time, causing a git error when trying to trigger the pipeline,
# from the new image (that already has the data), inside the jenkins container.
# The error was: 'not in git directory'.
# After investigation, found out that the last command in this file, fixed the problem. Creating a new image
# from the volume of a container where this command had been executed, seemed to fix the problem.
# Keep this script file, for future reference or similar situation.

container_name=$(docker ps --format '{{.Names}}' | head -n 1)

echo "The name of the container is: $container_name"

docker exec $container_name sh -c "git config --global --add safe.directory '*'"

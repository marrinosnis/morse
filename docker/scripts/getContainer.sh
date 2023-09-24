#!/bin/bash

container_name=$(docker ps --format '{{.Names}}' | head -n 1)

echo "The name of the container is: $container_name"

docker exec $container_name sh -c "git config --global --add safe.directory '*'"

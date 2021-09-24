#!/usr/bin/env bash

# Create Dockerfiles for components
mv .codebuild/nginx.docker .codebuild/relay_nginx.docker

for file in relay_web relay_worker relay_scheduler
do
  cp docker/web/Dockerfile .codebuild/$file.docker
done

# Build Docker images
for file in .codebuild/*.docker
do
  tag=$(basename -- "$file" ".${file##*.}")
  docker build -t $tag -f $file .
done


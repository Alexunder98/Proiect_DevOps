#!/bin/bash

# echo "All arguments:"
# echo "$@"
# echo "Arguments starting from second arg:"
# echo "${@:2}"


# if [ $1='build' ]
# then
#     echo "Da, ii dam cu build"
# fi


case $1 in
  build)
  echo "Building..."
  docker build ${@:2}
  ;;
  push)
  echo "suntem in push"
  ;;
  deploy)
  echo "suntem in deploy"
  ;;
  test)
  echo "suntem in test"
  ;;
  *)
  echo "Try again! Use build, push, deploy, test or stop! :)"
esac
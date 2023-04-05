#!/bin/usr/python3
import sys
# Script

# First arg is used for case
# Second, third, ... args are used as command arguments

# Check first argument
# CASE 1: BUILD

# CASE 2: PUSH

# CASE 3: DEPLOY

# CASE 4: TEST

# Error code if input is invalid.
# print("Try again boomer! Use build, push, deploy, test or stop! :)")


match sys.argv[1]:
    case 'build':
        print(sys.argv[1:])
    case 'push':
        print("Suntem in push")
    case 'deploy':
        print("Suntem in deploy")
    case 'test':
        print("Suntem in test")
    case _:
        print("Try again boomer! Use build, push, deploy, test or stop! :)")
        print(sys.argv[1:])

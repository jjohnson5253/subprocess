#!/usr/bin/env python3

#Jake Johnson Summer 2016

#This program gets the output from a subprocess and prints it

import subprocess

#calls 'fortune' from shell and returns a byte literal stdout
output = subprocess.check_output("fortune")

#this decodes and strips that output to make it readable
strippedOutput = output.decode('utf-8').strip()

print(strippedOutput)
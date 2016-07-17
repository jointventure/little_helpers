#!/usr/bin/env python3
"""shows how to use shell commands in python."""

import os  # operating system

shell = 'ls -l'
cmd = os.popen(shell)

result = cmd.read()
print(result)

cmd.close()

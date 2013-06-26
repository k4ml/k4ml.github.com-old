import os
import commands

run = commands.getstatusoutput

status, output = run('virtualenv .env')
print output

status, output = run('.env/bin/pip install --upgrade pip')
print output

status, output = run('.env/bin/pip install --upgrade "setuptools<0.7"')
print output

status, output = run('.env/bin/pip install --egg --upgrade distribute')
print output

status, output = run('.env/bin/pip install --egg zc.buildout==2.1.0')
print output

status, output = run('.env/bin/buildout bootstrap')
print output

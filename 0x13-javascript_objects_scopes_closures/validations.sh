#!/usr/bin/bash

## Execute permissions.
chmod u+x ./main-files/*.js
chmod u+x *.js

## Clean code.
semistandard ./main-files/*.js
semistandard *.js

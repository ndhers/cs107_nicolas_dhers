#!/bin/bash
find . -maxdepth 1 -type f -exec wc -l {} \; | awk '$2 != "total" { print $2, $1 }'


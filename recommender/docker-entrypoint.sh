#!/bin/bash -e
j2 /docker-templates/sample-template.conf.j2 > /test.txt
exec "$@"
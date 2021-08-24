#!/bin/bash

cd /home/pschlump/go/src/github.com/Univ-Wyo-Education/F21-1010
# rsync -r --delete -a -v -e "ssh -l philip" . philip@192.168.0.197:/Volumes/k100/Linux-wabl001
# rsync --dry-run \
rsync -r -a -v -e "ssh -l philip" \
	--exclude go/pkg/mod \
	. \
	philip@192.168.0.197:/Users/philip/go/src/github.com/Univ-Wyo-Education/F21-1010

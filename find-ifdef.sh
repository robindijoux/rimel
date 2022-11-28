#!/bin/sh

git clone https://github.com/mirror/busybox.git
grep -rn "#ifdef" busybox > ifdef_found.txt
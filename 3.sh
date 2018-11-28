#!/usr/bin/env bash
awk '{print $1}' access.log | sort | uniq -c | sort -r | head -n 10
#!/usr/bin/env bash
# Bundle competition entry files into submission.tar.gz
set -e
tar -czf submission.tar.gz main.py deck.csv
echo "Created submission.tar.gz"

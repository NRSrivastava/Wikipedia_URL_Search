#!/bin/sh
if [[ -z "$1" ]]; then
  echo "Enter search terms"
  read terms
elif [[ -n "$1" ]]; then
  terms="$*"
fi

terms="${terms// /_}"

echo "Finding URL for $terms..."

url="https://en.wikipedia.org/wiki/$terms"

echo "$url"
logdir=bash_Wiki_Search_History.txt
echo "${url}" >> "$logdir"

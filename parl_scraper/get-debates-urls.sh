#!/bin/bash

# Error on undefined variable use, abort on error
set -eu

# Download all table of contents. Uncomment following line or uncompress the
# tables-of-content.tar.xz archive.
# wget http://www.parlament.ch/ab/static/ab/html/f/default.htm -I /ab/toc -r --wait=2

toc_dir="www.parlament.ch/ab/toc"

# Compile a list of table of contents for National Council discussions
file_pattern='f_?_*_*.htm'
file_token='<SPAN id="PageHeaderSNV">Conseil national</SPAN>'
files=($(grep "${file_token}" -l --include="${file_pattern}" -r "${toc_dir}"))

# Extract URLs pointing to the debate texts
url_regex='"/ab/frameset/f/./[0-9]{4}/[0-9]+/f_._[0-9]{4}_[0-9]+_[0-9]+\.htm"'
grep -Eoh "${url_regex}" --include="${file_pattern}" "${files[@]}" > debates-urls.txt

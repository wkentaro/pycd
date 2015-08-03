#!/usr/bin/env sh
#

function pycd ()
{
  local pkg_path
  # check if command installed
  which pypack >/dev/null 2>&1 || {
    echo "please install pycd"
    echo "run \`pip install pycd\`"
    return 1
  }
  if [ "$1" = "" ]; then
    echo "Usage: pycd <package_name>"
  else
    pkg_path=$(pypack find $1 --no-warning)
    if [ "$pkg_path" = "" ]; then
      echo "$1 not found"
    else
      cd $pkg_path
    fi
  fi
}

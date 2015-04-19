#!/usr/bin/env sh
#

function pycd ()
{
  module_path=$(pycd_py find $1 --no-warning)
  if [ "$module_path" != "" ]; then
    cd $module_path
  else
    if [ "$1" = "" ]; then
      echo "Usage: pycd <module_name>"
    else
      echo "$1 not found"
    fi
  fi
}
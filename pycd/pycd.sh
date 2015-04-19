#!/usr/bin/env sh
#

function pycd ()
{
  local module_path
  module_path=`pycd_py find $1 --no-warning`
  if [ "$module_path" != "" ]; then
    cd $module_path
  else
    if [ "$1" = "" ]; then
      echo "Usage: pycd <module_name>"
    else
      echo "not found"
    fi
  fi
}
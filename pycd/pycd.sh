#!/usr/bin/env sh
#

function pycd ()
{
  local module_path
  module_path=`pypkg find $1 --no-warning`
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


# ------------------------------
# Completion
# ------------------------------

# ZSH support
if [[ -n ${ZSH_VERSION-} ]]; then
    autoload -U +X bashcompinit && bashcompinit
fi

_pycd()
{
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts=""

    if [[ ${opts} = "" ]] ; then
        opts=$(pypkg list)
    fi

    if [[ ${cur} = * ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" ${cur}) )
        return 0
    fi
}
complete -F _pycd pycd

# Setup antigen's autocompletion
_pypkg () {
    compadd        \
        find \
        help \
        install_pycd \
        list
}
complete -F _pypkg pypkg

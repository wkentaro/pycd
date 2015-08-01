# ZSH support
if [[ -n ${ZSH_VERSION-} ]]; then
    autoload -U +X bashcompinit && bashcompinit
fi

_pypack () {
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts="find list help"

    COMPREPLY=( $(compgen -W "${opts}" ${cur}) )
    return 0
}
complete -F _pypack pypack

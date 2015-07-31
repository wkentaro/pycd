#!/usr/bin/env python
#
import os
import sys

from clint.textui import colored, puts, indent
from clint.eng import join as eng_join
from clint import Args

from .module import get_module_paths
this_dir = os.path.dirname(__file__)


def display_info():
    puts('pypack: command line tool to handle python packages.\n')
    puts('Usage:')
    with indent():
        puts('pypack <command>')
    puts('Commands:')
    with indent():
        for cmd in cmd_map:
            puts('{0} - {1}'.format(cmd, cmd_info[cmd]))


def main():
    args = Args()
    if args.get(0) in cmd_map:
        arg = args.get(0)
        args.remove(arg)

        try:
            cmd_map.get(arg).__call__(args)
        except KeyboardInterrupt:
            pass
        sys.exit()
    else:
        display_info()


# maybe not needed
# def cmd_install_pycd(args):
#     # path = os.path.join(this_dir, 'pycd.sh')
#     puts('Please add below to your shell config file')
#     shell_cmd = '''if which pypack >/dev/null 2>&1; then
#     source `pypack find pycd`/pycd.sh
# fi'''
#     with indent(4, quote='>'):
#         puts(shell_cmd)
#         # puts('source {0}'.format(path))
#     shell_config = '{home}/.{shell}rc'.format(
#         home=os.environ.get('HOME'),
#         shell=os.path.split(os.environ.get('SHELL'))[-1],
#     )
#     yn = raw_input('add to {0}? [y/N]: '.format(colored.green(shell_config)))
#     if yn.lower() == 'y':
#         with open(shell_config, 'a+') as f:
#             f.write('\n# this line is added by pycd\n')
#             f.write(shell_cmd)
#     sys.exit()


def cmd_find(args):
    module = args.get(0)

    no_warning = False
    if args.contains(('--no-warning')):
        no_warning = True

    if not module:
        if not no_warning:
            print("Please specify a module to find.")
        sys.exit()

    module_paths = get_module_paths()
    if module not in module_paths:
        if not no_warning:
            print("{0} doesn't exist. Use `pypack list`.".format(
                colored.yellow(module)
            ))
        sys.exit(1)

    print(module_paths[module])


def cmd_list(args):
    module_paths = get_module_paths()
    for module in module_paths:
        print(module)


cmd_map = dict(
    find=cmd_find,
    list=cmd_list,
    )

cmd_info = dict(
    find='find package path',
    list='get package list',
    )


if __name__ == '__main__':
    main()

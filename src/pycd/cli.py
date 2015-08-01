#!/usr/bin/env python
#
import os
import sys

from clint.textui import colored, puts, indent
from clint.eng import join as eng_join
from clint import Args

from .package import get_package_paths
this_dir = os.path.dirname(__file__)


def cmd_help(args):
    is_data_only = False
    if args.contains(('--data-only')):
        is_data_only = True

    if is_data_only:
        for cmd in cmd_map:
            puts('{0} - {1}'.format(cmd, cmd_info[cmd]))
    else:
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
    arg = args.get(0)
    if arg in cmd_map:
        args.remove(arg)
        try:
            cmd_map.get(arg).__call__(args)
        except KeyboardInterrupt:
            pass
        sys.exit()
    else:
        cmd_help(args)


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
    pkg = args.get(0)

    no_warning = False
    if args.contains(('--no-warning')):
        no_warning = True

    if not pkg:
        if not no_warning:
            puts("Please specify a package to find.")
        sys.exit()

    pkg_paths = get_package_paths()
    if pkg not in pkg_paths:
        if not no_warning:
            puts("{0} doesn't exist. Use `pypack list`.".format(
                colored.yellow(pkg)
            ))
        sys.exit(1)

    puts(pkg_paths[pkg])


def cmd_list(args):
    pkg_paths = get_package_paths()
    for pkg in pkg_paths:
        puts(pkg)


cmd_map = dict(
    find=cmd_find,
    list=cmd_list,
    help=cmd_help,
    )

cmd_info = dict(
    find='find package path',
    list='get package list',
    help='show help',
    )


if __name__ == '__main__':
    main()

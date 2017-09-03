import os
import sys

from clint import Args
from clint.textui import colored
from clint.textui import indent
from clint.textui import puts

from pycd.package import get_package_paths


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
    env_path = os.getenv('VIRTUAL_ENV')
    if env_path:
        py_version = '{}.{}'.format(sys.version_info.major,
                                    sys.version_info.minor)
        env_lib = os.path.join(env_path,
                               'lib/python{}/site-packages'.format(py_version))
        sys.path.insert(0, env_lib)

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


def cmd_find(args):
    pkg = args.get(0)

    if not pkg:
        puts('Please specify a package to find.', stream=sys.stderr.write)
        sys.exit()

    pkg_paths = get_package_paths()
    if pkg not in pkg_paths:
        puts("{0} doesn't exist. Use `pypack list`.".format(
            colored.yellow(pkg)
        ), stream=sys.stderr.write)
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

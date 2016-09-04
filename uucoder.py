# coding: utf-8

import argparse
import uu
import sys
import os


def createparser():
    parser = argparse.ArgumentParser(description='UUC transcoding program and back again.', prog='Converter',
                                     epilog='Distributed under the MIT license', add_help=True)
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    parser.add_argument('--In', '-i', required=True, action='store', help='The path to the file recoded')
    parser.add_argument('--Out', '-o', required=False, action='store',
                        help='Path where where to save the converted file')
    parser.add_argument('--action', '-a', default='e', required=False, action='store', choices=['e', 'd'],
                        help='e - transformation in UU; d - the transformation of the UU')

    return parser


def coder(flag, path_in, path_out):
    def coder_body(in_p, out_p):
        if flag == 'e':
            uu.encode(in_p, out_p)
        if flag == 'd':
            uu.decode(in_p, out_p)

    if path_in == '*':
        for top, dirs, files in os.walk(os.getcwd()):
            for nm in files:
                path_in = os.path.join(top, nm)
                path_out = path_in + '.uu'
                coder_body(path_in, path_out)

    else:
        if path_out is None:
            path_out = path_in + '.uu'
        coder_body(path_in, path_out)


def main():
    parser = createparser()
    namespace = parser.parse_args(sys.argv[1:])
    in_path = namespace.In
    out_path = namespace.Out
    act = namespace.action

    coder(act, in_path, out_path)
    return 0


main()

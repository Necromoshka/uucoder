# coding: utf-8

import argparse
import uu
import os
import sys


def createparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-R', required=False)
#    parser.add_argument('-m', required=False)
#    parser.add_argument('-f', action='store_true', default=False)
    return parser

def coder(flag,path_in, path_out):
    uu.encode()
    uu.decode()













#parser = createparser()
#namespace = parser.parse_args(sys.argv[1:])

#sr_direktory = namespace.sr
#d_direktory = namespace.data
#tr = Tree()

#for top, dirs, files in os.walk(d_direktory):
#    for nm in files:
#        with open(os.path.join(top, nm), 'rb') as fl:
#            data = fl.read()
#            md5 = hashlib.md5(data).hexdigest()
#            tr.insertrndroot(md5, tr.root, 0)

#for top, dirs, files in os.walk(sr_direktory):
#    for nm in files:

#        with open(os.path.join(top, nm), 'rb') as fl:
#            data = fl.read()
#            md5 = hashlib.md5(data).hexdigest()
#            if namespace.f:
#                if tr.lookup(tr.root, md5, 0):
#                    print os.path.join(top, nm)
#            else:
#                if not tr.lookup(tr.root, md5, 0):
#                    print os.path.join(top, nm)

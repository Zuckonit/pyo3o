#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
#=============================================================================
#     FileName: fetch.py
#         Desc: this is inspired by o3o, just use the yan.json from 
#               https://github.com/turingou/o3o
#               Thanks turning (https://github.com/turingou)
#       Author: Mocker
#        Email: Zuckerwooo@gmail.com
#     HomePage: zuckonit.github.com
#      Version: 0.0.1
#   LastChange: 2013-08-21 07:15:20
#      History:
#=============================================================================
'''

try:
    import json
except ImportError:
    import simplejson as json
import os
import sys

__all__ = ['available', 'fetch']

#face_file = os.path.expanduser('~/.yan.json')
face_file = 'yan.json'  #where is your yan.json

def load_face(jsonfile):
    f = open(jsonfile)
    d = json.load(f)
    f.close()
    return d


def _encode(tag):
    tag = unicode(tag) if isinstance(tag, unicode) else tag.decode('utf-8')
    return tag


def fetch(dface, tag):
    tag = _encode(tag)
    faces = dface['list']
    for face in faces:
        tags = face['tag'].split()
        if tag in tags:
            return [_encode(f) for f in face['yan']]   #return if tag found
    return []


def available():
    dface = load_face(face_file)
    faces = dface['list']
    tags = []
    for face in faces:
        tags.append(face['tag'])
    return [_encode(t) for t in tags]


def usage():
    print >> sys.stdout, """
    %s tag1 tag2...    to get the faces with these tags
    -h|-help|--help    get the usage
    -l|-list|--list    to list all the tags
    """%(os.path.basename(sys.argv[0]))


def opt():
    argc = len(sys.argv)
    if argc == 1 or sys.argv[1] in ['-h','-help', '--help']:
        usage()
        return
    dface = load_face(face_file)
    if sys.argv[1] in ['-l', '-list', '--list']:
        tags = available()
        for tag in tags:
            print tag
        return
    for tag in sys.argv[1:]:  #that's why you can search multi tags at the same time
        print '===== %s ====='%tag
        faces = fetch(dface, tag)
        if faces:
            for f in faces:
                print f
        else:
            print 'no such %s face' % tag


if __name__ == '__main__':
    opt()

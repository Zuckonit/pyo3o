#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
#=============================================================================
#     FileName: fetch.py
#         Desc: this is inspired by o3o, just use the yan.json from 
#               https://github.com/turingou/o3o
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

#face_file = os.path.expanduser('~/.yan.json')
face_file = 'yan.json'

def load_face(jsonfile):
    f = open(jsonfile)
    d = json.load(f)
    f.close()
    return d


def _encode(tag):
    try:
       tag = unicode(tag)
    except UnicodeDecodeError:
       tag = tag.decode('utf8')
    return tag


def fetch(dface, tag):
    tag = _encode(tag)
    faces = dface['list']
    for face in faces:
        tags = face['tag'].split()
        if tag in tags:
            for y in face['yan']:
                print y.encode('utf-8')
            return True
    return False


def get_tags(dface):
    faces = dface['list']
    tags = []
    for face in faces:
        tags.append(face['tag'])
    return tags


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
        tags = get_tags(dface)
        for tag in tags:
            print _encode(tag)
        return
    for tag in sys.argv[1:]:
        print '=====%s====='%tag
        status = fetch(dface, tag)
        if not status:
            print u'no such %s face' % tag


if __name__ == '__main__':
    opt()

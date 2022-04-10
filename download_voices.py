# -*- coding: UTF-8 -*-

import os

CUR_DIR = os.path.dirname(__file__)


def rule(herf):
    return herf[:str.find(herf, ".ogg") + 4]


with open(os.path.join(CUR_DIR, "links")) as reader:
    links = [
        rule(line)
        for line in reader if line
    ]

import wget
from ffmpy3 import FFmpeg


def ogg_to_mp3(src_file, dst_file):
    ff = FFmpeg(
        inputs={src_file: None},
        outputs={dst_file: None},
    )
    print(ff.cmd)
    ff.run()


DST_DIR = os.path.join(CUR_DIR, "klee")
os.makedirs(DST_DIR, exist_ok=True)
for link in links:
    print(link)
    name = os.path.basename(link)
    name = name[len("VO_ZH_klee_"):]
    dst_file = os.path.join(DST_DIR, name)
    if os.path.exists(dst_file):
        pass
    else:
        wget.download(link, dst_file)

    ogg_file, mp3_file = dst_file, dst_file.replace("ogg", "mp3")
    if os.path.exists(ogg_file) and not os.path.exists(mp3_file):
        ogg_to_mp3(ogg_file, mp3_file)

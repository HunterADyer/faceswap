from lib.alignments import Alignments

import sys
import json

folder_name = sys.argv[1] #input folder name with alignmnets.fsa
output_name = sys.argv[2] #filename

aligner = Alignments(folder_name)

align_dict = aligner._load()
output_dict = {}
for image in align_dict:
    x = align_dict[image]['faces'][0]['x']
    y = align_dict[image]['faces'][0]['y']
    w = align_dict[image]['faces'][0]['w']
    h = align_dict[image]['faces'][0]['h']
    output_dict[image] = {}
    output_dict[image]['x'] = x
    output_dict[image]['y'] = y
    output_dict[image]['h'] = h
    output_dict[image]['w'] = w
with open(output_name, 'w') as output_fp:
    output_fp.write(json.dumps(output_dict))

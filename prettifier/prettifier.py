# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 02:12:11 2016

@author: Nguyen Duc Duy

CRAWLED DATA PRETIFIER:
- Remove special characters (\n, \t...)
- Filter those who have more than 3 words only

USAGE: prettifier.py input-file.json output-file.json

"""

# Import libs
from sys import argv;
import json,re;
from textblob import TextBlob;

data = [];
MINIMUM_TAGS_NO = 5; # minimum number of words/number of a document
                    # If a document has less than this number -> Ignore it

# Regular Expression relics
rdict = {
    u"\u2018": '\'',#  LEFT SINGLE QUOTATION MARK
    u"\u2019": '\'',#  RIGHT SINGLE QUOTATION MARK
    u"\u0026":'&',  #  AMPERSAND 
    u"\u2014":'-',  #  EM DASH
    u"\u00ab":'',   #  LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    u"\u00bb":'',   #  RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    u"\u201c":'"',  #  LEFT DOUBLE QUOTATION MARK
    u"\u201d":'"',  #  RIGHT DOUBLE QUOTATION MARK
    u"\u00a0":' ',  #  NO-BREAK SPACE
};

robj = re.compile('|'.join(rdict.keys()));

count = 0;
# Load the JSON file from agument
with open(argv[1]) as input_file:
    for line in input_file:
        count +=1;
        item = json.loads(line);
        content = item['content'].strip();
        content = robj.sub(lambda m: rdict[m.group(0)], content)
        blob = TextBlob(content); #  Run textBlob with the content
        if (len(blob.tags)<MINIMUM_TAGS_NO):
            continue; # Ignore small document
        item['content'] = content;
        data.append(item);
    
print "Input file contains ", count, " lines."    
print "After processing, there are ", len(data) ," refined documented."

# Write to output file
with open(argv[2], 'w') as output_file:
    for jobject in data:
        output_file.write(json.dumps(jobject)+"\n");



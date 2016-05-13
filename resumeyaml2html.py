#!/usr/bin/python
from __future__ import print_function
import re, codecs

htmlfile = 'index.html'
yamlfile = 'rallenresume.yml'

with codecs.open(htmlfile, 'w', 'utf-8') as hf:
	hf.write("<!DOCTYPE HTML><html>")
	hf.write("<head><style>body, p {font-family: sans-serif; font-size: 16px;} </style></head>")
	hf.write("<body>")
#turning our YAML into some very basic html, preserving its existing structure to demonstrate its readability
with codecs.open(yamlfile, 'r', 'utf-8') as lf:
	with codecs.open(htmlfile, 'a', 'utf-8') as hf:
		for line in lf:
			hf.write("<p>")
			if re.search('- ', line):
				for i in range(30):
					hf.write("&nbsp;")
				hf.write(line+"</p>")
			elif re.search(':', line):
				for i in range(20):
					hf.write("&nbsp;")
				hf.write(line+"</p>")
			else:
				for i in range(10):
					hf.write("&nbsp;")
				hf.write(line+"</p>")
		hf.write("</body>")
		hf.write("</html>")
		
		
	
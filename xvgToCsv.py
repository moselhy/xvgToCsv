import os, sys, re

if len(sys.argv) < 2:
	print("No input detected.\nUSAGE: python %s XVGFILEPATH" % sys.argv[0])
	sys.exit(1)

filename = os.path.realpath(sys.argv[1])
fp = open(filename, 'r')
text = fp.readlines()

newtext = []
for l in text:
	if l.startswith(r'#') or l.startswith(r'@'):
		continue
	newline = re.sub(r'  *', ",", l)
	newline = re.sub(r'^,', "", newline)
	newtext.append(newline)

newfilename = os.path.basename(filename).rstrip(r'xvg').rstrip('.')
newfilepath = os.path.join(os.path.dirname(filename), "%s.csv" % newfilename)
newfile = open(newfilepath, 'w')
newfile.writelines(newtext)
newfile.close()

print("Saved file to %s" % newfilepath)

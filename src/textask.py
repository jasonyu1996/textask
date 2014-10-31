import os;
import sys;
import getopt;

class Task:
	def __init__(self, name, path):
		self.name = name;
		self.path = path;

print '\tTeXTask 0.1';
print;

def printUsage():
	print 'Usage: -i <filepath> [-o <outputname>]';

def checkFile(fname):
	if not os.path.exists(fname):
		return -1;
	if os.path.isfile(fname):
		return 0;
	return 1;

if len(sys.argv) == 1:
	printUsage();
	exit();

opts, args = getopt.getopt(sys.argv[1:], 'i:o:');

infile = '';
outname = 'a.tex';

for op, val in opts:
	if op == '-i':
		infile = val;
	elif op == '-o':
		outname = val;

if infile == '':
	print 'Invalid arguments!';
	printUsage();
	exit();

if checkFile(infile) != 0:
	print 'Invalid input file!';
	exit();

title = '';
setter = '';
duration = '';
time = '';
tasks = [];

fin = open(infile, 'r');

os.chdir(os.path.dirname(os.path.abspath(infile)));

for s in fin:
	print s;

fin.close();


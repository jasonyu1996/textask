#coding=utf-8

import os;
import sys;
import getopt;

class Task:
	def __init__(self, name, path):
		self.name = name;
		self.path = path;
		self.title = u'';
		self.testpoint = u'10';
		self.time = '1000MS';
		self.memory = '256MB';
		self.spj = '否';
		self.part = '否';
		self.ty = '传统型';
		self.codelen = '10KB';
		self.isuf = 'in';
		self.osuf = 'out';
		self.add = '否';

	def load(self):
		fname = os.path.join(self.path, self.name + '.cfg');
		if not os.path.isfile(fname) or not os.path.exists(fname):
			return False;
		cin = open(fname, 'r');
		while True:
			__si = cin.readline();
			if not __si:
				break;
			if __si == '':
				continue;
			__p = __si.split(' ');
			if __p[0] == 'title:':
				self.title = ' '.join(__p[1:]).strip('\n');
			elif __p[0] == 'testpoint:':
				self.testpoint = ' '.join(__p[1:]).strip('\n');
			elif __p[0] == 'time:':
				self.time = ' '.join(__p[1:]).strip('\n');
			elif __p[0] == 'memory:':
				self.memory = ' '.join(__p[1:]).strip('\n');
			elif __p[0] == 'spj:':
				self.spj = ' '.join(__p[1:]).strip('\n');
			elif __p[0] == 'part:':
				self.part = ' '.join(__p[1:]).strip('\n');
			elif __p[0] == 'type:':
				self.ty = ' '.join(__p[1:]).strip('\n');
			elif __p[0] == 'codelen:':
				self.codelen = ' '.join(__p[1:]).strip('\n');
			elif __p[0] == 'isuf:':
				self.isuf = ' '.join(__p[1:]).strip('\n');
			elif __p[0] == 'osuf:':
				self.osuf = ' '.join(__p[1:]).strip('\n');
			elif __p[0] == 'add:':
				self.add = ' '.join(__p[1:]).strip('\n');
		cin.close();
		return True;


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

if not os.path.exists(os.path.dirname(os.path.abspath(outname))):
	print 'Invalid output file!';
	exit();

fout = open(outname, 'w');
fout.write('''\\documentclass[a4paper, 11pt]{article}

\\usepackage[BoldFont, SlantFont]{xeCJK}
\\usepackage{amssymb}
\\usepackage{graphicx}
\\usepackage{verbatim}
\\usepackage[margin=2.5cm]{geometry}

\\setCJKmainfont{SimSun}
''');

title = '';
setter = '';
duration = '';
time = '';
tasks = [];


def addTask(task):
	if not task.load():
		return False;
	tasks.append(task);
	return True;
	

fin = open(infile, 'r');


os.chdir(os.path.dirname(os.path.abspath(infile)));

while True:
	s = fin.readline();
	if not s:
		break;
	if s == '':
		continue;
	contents = s.split(' ');
	if contents[0] == 'title:':
		title = ' '.join(contents[1:]).strip('\n');
	elif contents[0] == 'setter:':
		setter = ' '.join(contents[1:]).strip('\n');
	elif contents[0] == 'time:':
		time = ' '.join(contents[1:]).strip('\n');
	elif contents[0].strip('\n') == 'problem:':
		name = fin.readline().strip('\n');
		pos = fin.readline().strip('\n');
		if addTask(Task(name, pos)):
			print 'Problem %s added' % (name);
		else:
			print 'Problem %s not found' % (name);

fin.close();

fout.close();


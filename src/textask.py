#coding=gbk

import os;
import sys;
import getopt;
import codecs;
import time;

class Task:
	def __init__(self, name, path):
		self.name = name;
		self.path = path;
		self.title = '';
		self.testpoint = '10';
		self.time = '1000MS';
		self.memory = '256MB';
		self.spj = 'No';
		self.part = 'No';
		self.ty = 'Conventional';
		self.codelen = '10KB';
		self.isuf = 'in';
		self.osuf = 'out';
		self.add = 'No';

	def load(self):
		fname = os.path.join(self.path, self.name + '.cfg');
		if checkFile(fname) != 0:
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
	print 'Usage: -i <input_path> [-o <output_path>]';

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

fout = codecs.open(outname, 'w', 'utf-8');

def printHead(he):
	fout.write(('		\\hline \\textbf{%s} ' % (he)).decode('gbk'));

def printItem(it):
	fout.write(('& %s ' % (it)).decode('gbk'));

def printNewLine():
	fout.write('\\\\ \n');

def printNewPage():
	fout.write('	\\newpage\n');

def printLeading(con):
	fout.write(('	\subsection*{%s}\n' % (con)).decode('gbk'));

def printSubleading(con):
	fout.write(('	\subsubsection*{%s}\n' % (con)).decode('gbk'));

def printContent(ta, leading, suf):
	fname = os.path.join(ta.path, ta.name + '.' + suf);
	if checkFile(fname) == 0:
		printLeading(leading);
		printFile(fname);

def printFile(fname):
	of = open(fname, 'r');
	fout.write(of.read().decode('gbk'));
	of.close();

def printSample(ta):
	i = 0;
	while(True):
		fname1 = os.path.join(ta.path, '%s.%d.%s' % (ta.name, i, ta.isuf));
		fname2 = os.path.join(ta.path, '%s.%d.%s' % (ta.name, i, ta.osuf));
		if checkFile(fname1) == 0 and checkFile(fname2) == 0:
			if i == 0:
				printLeading('Sample');
			printSubleading('Input');
			fout.write('	{\\ttfamily\\begin{verbatim}\n');
			printFile(fname1);
			fout.write('	\\end{verbatim}}\n\\rmfamily\n');
			printSubleading('Output');
			fout.write('	{\\ttfamily\\begin{verbatim}\n');
			printFile(fname2);
			fout.write('	\\end{verbatim}}\n\\rmfamily\n');
		else:
			break;
		i += 1;

fout.write('''%% This file was generated using TeXTask
%% %s

''' % (time.strftime('%Y/%m/%d',time.localtime(time.time()))));

fout.write('''\\documentclass[a4paper, 11pt]{article}

\\usepackage[BoldFont, SlantFont]{xeCJK}
\\usepackage{amssymb}
\\usepackage{graphicx}
\\usepackage{verbatim}
\\usepackage[margin=2.5cm]{geometry}

\\usepackage{array}
\\newcommand{\\PreserveBackslash}[1]{\\let\\temp=\\\\#1\let\\\\=\\temp}
\\newcolumntype{C}[1]{>{\\PreserveBackslash\\centering}p{#1}}
\\newcolumntype{R}[1]{>{\\PreserveBackslash\\raggedleft}p{#1}}
\\newcolumntype{L}[1]{>{\\PreserveBackslash\\raggedright}p{#1}}

\\setCJKmainfont{SimSun}

''');




title = '';
setter = '';
duration = '5h';
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
	elif contents[0].strip('\n') == 'problem:':
		name = fin.readline().strip('\n');
		pos = fin.readline().strip('\n');
		if addTask(Task(name, pos)):
			print 'Problem %s added' % (name);
		else:
			print 'Problem %s not found' % (name);

fin.close();

fout.write(('''
\\setlength{\\parskip}{8pt}

\\title{%s}
\\author{}
\\date{}
''' % (title)).decode('gbk'));

fout.write('''\\begin{document}
	\\rmfamily
	\\vspace{3cm}
	\\maketitle
	''');

if setter != '':
	fout.write(('''
	\\begin{center}
		\\large
		\\textbf{Problem setter:} %s\\\\
		\\normalsize
	\\end{center}
''' % (setter)).decode('gbk'));

if duration != '':
	fout.write(('''
	\\begin{center}
		\\large
		\\textbf{Duration:} %s
		\\normalsize
	\\end{center}
''' % (duration)).decode('gbk'));

fout.write('	\\vspace{3cm} \\Large \\begin{center}\\textbf{Problem List}\\end{center} \\normalsize \\vspace{0.3cm}\n');

fout.write('''
	\\begin{table}[htbp]
		\\centering\\begin{tabular}{|L{3cm}||''');

for i in range(0, len(tasks)):
	fout.write('C{4cm}|');

fout.write('}\n');

printHead('Name');
for t in tasks:
	printItem(t.name);
printNewLine();

printHead('Title');
for t in tasks:
	printItem(t.title);
printNewLine();

printHead('Input');
for t in tasks:
	printItem(t.name + '.' + t.isuf);
printNewLine();

printHead('Output');
for t in tasks:
	printItem(t.name + '.' + t.osuf);
printNewLine();

printHead('Time limit');
for t in tasks:
	printItem(t.time);
printNewLine();

printHead('Memory limit');
for t in tasks:
	printItem(t.memory);
printNewLine();

printHead('Test point');
for t in tasks:
	printItem(t.testpoint);
printNewLine();

printHead('Type');
for t in tasks:
	printItem(t.ty);
printNewLine();

printHead('Partial score');
for t in tasks:
	printItem(t.part);
printNewLine();

printHead('SpecialJudge');
for t in tasks:
	printItem(t.spj);
printNewLine();

printHead('Attachment');
for t in tasks:
	printItem(t.add);
printNewLine();

printHead('Code len. limit');
for t in tasks:
	printItem(t.codelen);
printNewLine();

fout.write('''		\hline \\end{tabular}
	\\end{table}
''');

printNewPage();

for t in tasks:
	fout.write(('''	\\begin{center}\section*{%s}\\end{center}\n''' % (t.title)).decode('gbk'));
	printContent(t, 'Background', 'bg');
	printContent(t, 'Description', 'desc');
	printContent(t, 'Input', 'input');
	printContent(t, 'Output', 'output');
	printSample(t);
	printContent(t, 'Constraints', 'cst');
	printContent(t, 'Judging Rules', 'rule');
	printContent(t, 'Hint', 'hint');
	printContent(t, 'Notes', 'notes');
	printNewPage();

fout.write('\\end{document}\n');


fout.close();


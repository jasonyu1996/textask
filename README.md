# Introduction
TeXTask is a Python script used to generate tex source files for Olympiad in Informatics problem set.

# Usage
	python textask.py -i <input_path> [-o <output_path>]

## Problem set information file

First you should input the general information about the problem set in a single file. In such a file each line is simply like this:
	<argument_name>: <argument_value>

The following is a list of such arguments supported:
* *title* title of the problem set
* *setter* problem setter
* *duration* how long the exam will last

The problem list should also be given in this file. The description for each problem follows the following format.
	problem:
	<problem_name>
	<directory_of_the_problem>

Here `<problem_name>` is actually an ID of the problem, which will be used as the prefix of the file name for both input and output. Besides, the files describing the whole problem will all be named with this prefix.

The `<directory_of_the_problem>` gives the directory where you prepare the complete information of the problem.

## Problem information file

For a problem listed in the file above, you should put all the information files of that problem directly under `<directory_of_the_problem>`.

Note that among those files one file cannot be missing, or the script will warn that it can not find the problem. This file should be named `<problem_name>.cfg`, and it provides the basic information about the problem. The format is similar to the one introduced above. The list of arguments:

* *title* title of the problem
* *testpoint*number of test points
* *time* time limit for the problem
* *memory* memory limit for the problem
* *spj* special judge
* *part* partial score
* *type* type of the problem
* *codelen* code length limit for the problem
* *isuf* input file name suffix
* *osuf* output file name suffix
* *add* with attachment or not

Then following files can be used to provide more information. All of them are named `<problem_name>.<suffix>`, and the available file name suffixes are listed below.

* *bg* problem background
* *desc* description
* *input* input description
* *output* output description
* *cst* constraints
* *hint* hint
* *rule* judging rules
* *notes* notes

All of those files can be given in tex format, and they will be directly embedded into the output file.

Besides sample tests may be provided. The file names are `<problem_name>.<d>.in` and `<problem_name>.<d>.out`, where `<d>` stands for the sample numbe (starting from 0).

----------------------------------------
Author: Jason Yu



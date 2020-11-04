CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Installation
 * Using Pysassquatch


INTRODUCTION
------------

PySASSQuatch is a package for creating dynamic qss files using a similar ideology as SASS.

Currently pysassquatch only updates variables.

INSTALLATION
------------

Clone the repo. Then, run `python setup.py install`


USING PYSASSQUATCH
------------------
The easiest way to use pysassqautch is by

`pysassquatch-convert -i <input_file> -o <output_file>`

Arguments:
* Input File: --input-file (-i) [Required]
 > This is the input file name. The input file needs to be a .sqss file.

* Output File: --output-file (-o) [Optional]
 > This is the output file name. The output file needs to be a .qss file.

If there is not an output file provided (e.g. `pysassquatch-convert -i <input_file>`) then the program will default to
<input_file>.qss

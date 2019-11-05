# Deduplicator

===
Copyright 2019, University of Illinois at Chicago and Oregon Health & Science University
 
 
This file is part of the deduplicator project.
 
 
Licensed under the Apache License, Version 2.0 (the "License");
 
you may not use this file except in compliance with the License.
 
You may obtain a copy of the License at
 
 
    http://www.apache.org/licenses/LICENSE-2.0
 
 
Unless required by applicable law or agreed to in writing, software
 
distributed under the License is distributed on an "AS IS" BASIS,
 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 
See the License for the specific language governing permissions and
 
limitations under the License.
 
===
 
# Software requirements

1. Python3 
Download Python 3.7.4
Anaconda distribution can also be used.
Use pip to install the python packages. If using Anaconda distribution, use conda to install the python packages. 


2. Python packages needed
unidecode (https://pypi.org/project/Unidecode/). 
fuzzywuzzy (https://pypi.org/project/fuzzywuzzy/)
python-Levenshtein (https://pypi.org/project/python-Levenshtein/)


3.Bibutils
Download the system compatible (Mac or Windows, whichever is applicable) binaries from http://bibutils.refbase.org
Unzip and place them in the system's executable path.

4. Other notes
The match_dictionaries module of the code uses a text file, 'J_Medline.txt' (ftp://ftp.ncbi.nih.gov/pubmed/J_Medline.txt), to match journal abbreviations with journal full names. The file contains full name and abbreviations of all the journals cited in PubMed.  In future, this file will need to be replaced with the more updated version.


# Limitations
The code may not work if the input files have characters from non-Latin languages like Chinese, Japanese, Korean or Persian.




# Usage of the code on the command line

The code needs the following REQUIRED arguments:
1. -input_file <names of the .ris files to be compared and/or xml pubmed file; give it any number of files to be compared>
2. -output_file <name of the file which will have the output from the PYTHON3_DEDUPLICATOR>
 

The code will produce two .ris files - one with unique records and the other file with the duplicate records that were removed. 

*** EXAMPLE ***
(base) MDYA257:deduplicator dasp$ python main_code.py -input_file ../../../EXAMPLES/ca/184_pubmed.xml ../../../EXAMPLES/ca/1423_ccrct.ris -output_file ../../../EXAMPLES/ca/OUTPUT/output_ca
 
**** Output from the PYTHON_DEDUPLICATOR ***
 
Found 1 input .ris files ['../../../EXAMPLES/ca/1423_ccrct.ris']
../../../EXAMPLES/ca/1423_ccrct.ris has 1423 records
 
Found 1 input .xml files ['../../../EXAMPLES/ca/184_pubmed.xml']
This/These will be converted to .ris file(s).
Converting the .xml file(s) to .ris file(s)...
Note: This may take some time!!
Converted ../../../EXAMPLES/ca/184_pubmed.xml to ../../../EXAMPLES/ca/184_pubmed.ris
Done!
 
../../../EXAMPLES/ca/184_pubmed.xml had 184 records
../../../EXAMPLES/ca/184_pubmed.ris has 184 records
 
Total number of records to be deduplicated is 1607.
 
Starting deduplication...
Deduplication Done!!
 
Number of unique records is 1473.
Number of duplicate records is 134.
 
Unique records have been written out to ../../../EXAMPLES/ca/OUTPUT/output_ca.unique_records.ris (1473 records)
Duplicate records have been written out to ../../../EXAMPLES/ca/OUTPUT/output_ca.duplicate_records.ris (134 records)
*** *** ***

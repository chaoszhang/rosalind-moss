# Rosalind Plagiarism Checker

Simple script to export code from Rosalind and run it through the Moss plagiarism checker

## Getting Started

This project requires Python 2, Node, and Perl.

### Prerequisites

You need to have a Moss account. The information provided from them should be put into a file called `moss` in this directory. Alternatively you can use the file `moss_template`, change it to `moss` and put your Moss user_id into the place where it says `$userid=<YOUR USER_ID HERE>;`.

You also need credentials for Rosalind. Your Rosalind credentials should go into a file called `config.py` in this directory. See `config_template.py` for an example of how it should look.

## Usage

From the command line the whole code can simply be run with:
```
python main.py '<ROSALIND_URL>' <ASSIGNMENT_NUMBER>
```
Where `<ROSALIND_URL>` is the url corresponding to the grade sheet for the particular section, and `<ASSIGNMENT_NUMBER>` corresponds to which assignment to check for plagiarism. `<ASSIGNMENT_NUMBER>` can also be a list of values like
`0,1,2,3,4` for all desired assignments.

eg,
```
python main.py 'http://rosalind.info/classes/257/students/' 0
```
or
```
python main.py 'http://rosalind.info/classes/257/students/' 0,1,2,3,4
```
or
```
python main.py 'http://rosalind.info/classes/257/students/' 0,1,2,3,4 > output.txt
```

## output
This will generate a Moss report for each language detected in the output from Rosalind. Each report is separated by a few lines. To save this information
please pipe it to a file as seen above.

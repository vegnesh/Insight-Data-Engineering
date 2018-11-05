# Table of Contents
1. [Introduction](README.md#introduction)
2. [Key Assumptions](README.md#key-assumptions)
3. [Running Instructions](README.md#running-instructions)
4. [Code Description](README.md#code-description)



# Introduction

This repository contains the submission for the Insight Data Engineering Challenge. The problem statement, relevant data and the instructions for the solution can be found in [this site](https://github.com/InsightDataScience/h1b_statistics)

The submission given here follows the suggested layout provided in the instructions. Kindly note that the input folder contains a sample input file only. The actual input file needs to be loaded.

# Key Assumptions

The following assumptions are assumed for the program to work without errors:

1.  The input file should be named `h1b_input.csv` and must be present in the input folder
2.  The input files contains a header line containing the column names/titles of the data. 
3.  All the data and the header is assumed to be separated by `;`
4.  It is assumed that there is atleast one column header with the words __`SOC`__ and __`CODE`__ within the column name
5.  It is assumed that there is atleast one column header with the words __`SOC`__ and __`NAME`__ within the column name
6.  It is assumed that there is atleast one column header with the word __`STATUS`__ within the column name
7.  It is assumed that there is atleast one column header with the words __`WORK`__ and __`STATE`__ within the column name
8.  The program requires Python3. `run.sh` executues the code with a call to Python3

# Running Instructions

If the assumptions stated in the previous sections are satisfied, you can execute the `run.sh` file using a linux terminal. On code completetion, check the `output` folder for results.

# Code Description

The code loads the data present in the CSV file considering each data line as a dictionary. The key is given by the column name and the value is corresponding row value. It create a list of dictionaries to store data.

Following this, the key names are analyzed to ensure one can obtain the names used in CSV file for the state of work, SOC code, SOC name and the status of the application.

Using the column names obtained in the previous step, the data on state of work, SOC code and SOC name are stored only for certified applications and stored as a list

Unique data values are obtained by converting the set to a list. Using this unique data the statistics information is collected.

Finally, the data is sorted based on the suggested scheme in the instructions and finally stored in the output files.

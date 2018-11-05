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


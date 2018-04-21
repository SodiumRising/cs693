# cs693

When you run the program it will ask you to input the file names you would like to measure the metrics of. 
If you would like to put in more than one file separate each file name with a space.
Example: (SampleIncludingAll1.py test.py)

Lines of Code will prompt you asking if you would like to exclude comments, blank lines, and imports.
You can choose by inputting y for yes or n for no.

Next will be LCOM. 
WIP

Next will be CBO.
WIP

DIT will prompt you asking if you would like to include the object in the calculation. You may input y for yes and n for no.
If you input y, when the program finds a class extending object, it will include it in the DIT count.

NOC will then print automatically without any user input.

Finally the Weight Methods per Class will prompt you if you would like to include the constructor in the calculation.
Once again you may enter y for yes or n for no. The constructor in Python will be the Def __init__.

After all entries are inputted, the code will print out the results for all the metrics for the current file. 
If two files are given the next file will now load, and prompt the user with the same questions.

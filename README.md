# cs693

This project is used to find various metrics of a given python code.

After hitting run, the program will prompt the user to input the name of the file or files they would like to have the metrics ran against
In order to put more than one file in, please separate each python file by a space.
EX: SampleIncludingAll1.py test.py

After the files are inputted, the program will prompt the user if they would like to exclude comments, blank lines, and imports.
The user can choose Yes or No via y or n in the terminal 

After total lines of code are printed out, LCOM, CBO, and Number of Children will automatically print afterwards.

When the DIT function is started it will ask the user if they would like to include the object. All functions in python are 
inherited by the object. Therefore, the selection of off will show the true inherited classes, while a yes will show 
the object connections as well.

The next input the user will need to give is whether or not to include the constructor in the calculation for the 
Weight Methods per Class Calculation. Once again the user can select yes or no via y or n.
The constructor in python is "__init__"

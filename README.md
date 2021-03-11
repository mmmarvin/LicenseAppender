#License Appender
=================

A simple python script to help append license information to source code files

#Usage
=================
To run license appender, run:<br>
python3 lappend.py [flags] [location of files to append license to]<br>
   -l name of license to use<br>
   -e extensions to append license to<br>
   -n name of license holder<br>
   -y year to add on the license<br>
   -p program name to add to license<br>

#Example Usage
=================
python3 lappend.py -l gpl3 -e .c.h -n My\ Name -y 2020-2021 -p My\ Program


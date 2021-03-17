#License Appender
=================

A simple python script to help append license information to source code files

#Usage
=================
To run license appender, run:<br>
```bash
python3 lappend.py [flags] [location of files to append license to]
```

   &emsp;&emsp;-l name of license to use<br>
   &emsp;&emsp;-e extensions to append license to<br>
   &emsp;&emsp;-n name of license holder<br>
   &emsp;&emsp;-y year to add on the license<br>
   &emsp;&emsp;-p program name to add to license<br>

#Example Usage
=================
```bash
python3 lappend.py -l gpl3 -e .c.h -n My\ Name -y 2020-2021 -p My\ Program
```


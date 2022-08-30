First edit the MarkingConfig file.

You can edit the MarkingConfig script as needed. 
The program will replace (studentName) with the provided name each run. 

(opt1) will be replaced with the chosen option in the 'OPTION 1:' section.
(opt2) will be replaced with the chosen option in the 'OPTION 2:' section. 
etc

There may be as many OPTION sections as needed.
Each OPTION section may have as many options as needed.
Each OPTION section will be asked, but if there is not an equivalent '(opt_)' in the script it won't be in the result.
You may write something next to the OPTIONs to give context during the program's run, if desired. (See OPTION 3 in the example.)

A 'YOUR_RESULTS.txt' file will be created if there is not one in the folder.
This means you can take out that file or rename it as needed to organise your results, 
and a new one will be created on the next run.


There must be a 'MarkingConfig.txt' in the same folder as the Python program.
The 'MarkingConfig.txt' should be formatted similar to the example below.


Nowhere in the script or options should you put a second capitalised 'SCRIPT', nor a capitalised 'OPTION' anywhere other than the start of an OPTIONs section.



ENSURE THERE ARE EMPTY LINES BETWEEN EACH SECTION.

EXAMPLE:

SCRIPT:
Hi (studentName). You should (opt1) the (opt2). Pretty sure (opt3). (opt4).

OPTION 1:
crush
smash
eat
peel

OPTION 2:
banana man
apple man
human man
yellow cat
black cat
blue cat
green cat

OPTION 3: (What will he think about it?)
he won't like it
he will love it
he won't mind

OPTION 4:
Anyway, bye

~
Hope the program is useful for you!
Zedekai Thorpe
z@zedekai.com
~

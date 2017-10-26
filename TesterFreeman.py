#Tester
global ChordURL
table = str.maketrans(dict.fromkeys('[\'\"]'))
fh = open("TestURLsFreeman.txt", "r")
if fh.mode == 'r':  # check to make sure that the file was opened
    for line in fh.readlines():
        ChordURL = str(line.translate(table).strip())
        exec(open('FunctionReformatter-Experimental.py').read())
    fh.close()  # close the file

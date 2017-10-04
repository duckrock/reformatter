#Define Function song list of lists or songlol
def songlol(songfile,songlist):  # Open the file back up and read the contents into a list of lists
    fh = open(songfile, "r")
    if fh.mode == 'r':  # check to make sure that the file was opened
         for line in fh.readlines():
            y = [line.strip('\n')]
            songlist.append(y)   #Load the file contents into a list of lists
            #songlist.append(line)  # Load the file contents into a list of lists
         fh.close() #close the file
songlist = [] # Instantiate variable songlist as a list
#----------------------------------------------------
songlol('SongFile.txt', songlist) #call the function to put the file into a list of lists
#Remove blank lines
songlist = [x for x in songlist if x != ['']]
print(songlist)

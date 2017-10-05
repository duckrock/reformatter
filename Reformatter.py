exec(open('HTMLtoTXTFileFreeman.py').read())
exec(open('FileToListOfLists.py').read())
#----------------------------------------------------
table = str.maketrans(dict.fromkeys('[\'\"]')) #Create a translate table to remove extraneous list characters like [,],'
#########################################################
SongStart = 0 #Hardcoded start of the chords line, usually the Lyrics are one line later
SpecialLine = ['Intro','Verse','VERSE','Chorus','CHORUS','Refrain','REFRAIN','Instrumental','INSTRUMENTAL','Solo','Verse 1','Verse 2','Verse 3','Outro'] #used to check for special song lines
TitleLine = [' - ', 'Capo'] #usually this is when there is an embedded title, just print it
SomeChords = ['A  ','[A]','F#m ','G  ','A  ','F  ','E  ','Am7  ','C  ','D7  '] #used to check for a succession of chords
#######################################################
def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)
#######################################################
print(songlist)
WrkStr5 = str(songlist[SongStart]).translate(table) #Get the first line of the song
file=open("ReformattedSong.txt","w") # Open a file
while SongStart+1<len(songlist):  # go to the end of the list of list elements
    WrkStr1 = str(songlist[SongStart]).translate(table) #first line of text, should be chords above lyrics
    WrkStr2 = str(songlist[SongStart+1]).translate(table) #second line of text, should be lyrics
    #print(WrkStr1,'raw1')
    #print(WrkStr2,'raw2')
    ChordLineLen = len(WrkStr1.rstrip()) #total length of line with the chord, need this to back from
    LyricLineLen = len(WrkStr2.rstrip()) #need this in the case the lyric line is shorter than the chordline
    if ChordLineLen>LyricLineLen:
        WrkStr2 = WrkStr2.ljust(ChordLineLen) #force the lyric line to be as long as the chordline
    if ChordLineLen > 0 : #this must be a nonblank row of text
        # Check the first string and see if it is special
        if any([st in WrkStr1 for st in TitleLine]):#are you looking like a title?  with a hyphen?
            #print(WrkStr1.strip())
            file.write(WrkStr1.strip() + '\n')  # If there is a title, add it to the file first.
            SongStart = SongStart + 1  # advance the line checker
        elif any([st in WrkStr1 for st in SpecialLine]): # are you a chorus, verse, etc?
            #print('['+WrkStr1.strip()+']')
            file.write('\n')  # If there is a special section, skip a line in the file
            SongStart = SongStart + 1  # advance the line checker
        elif any([st in WrkStr1 for st in SomeChords]) and any([st in WrkStr2 for st in SpecialLine]):
            #print('['+WrkStr1.strip()+']')
            file.write('['+WrkStr1.strip()+']\n')  # If there is a title, add it to the file first.
            SongStart = SongStart + 1  # advance the line checker
        else:
            #####################################################################
            y=80 ###This is the last position
            PartialChord=""
            if any([st in WrkStr2 for st in SomeChords]):
            #this checks for multiple lines of chords,
                #print('[' + WrkStr1 + ']')
                #print('[' + WrkStr2 + ']')
                file.write('[' + WrkStr1 + ']\n')
                file.write('[' + WrkStr2 + ']\n')
                SongStart = SongStart + 2
            elif (any([st in WrkStr1 for st in SomeChords]) and WrkStr2.rstrip() == ""):
                #print('[' + WrkStr1 + ']')
                file.write('[' + WrkStr1 + ']\n')
                SongStart = SongStart + 2
            else: #we do NOT have an instrumental or solo
                while y > 1: #keep going until you get to the leftmost position of the line
                    for x in range(0,ChordLineLen): #x is 0 to 30
                        y = (ChordLineLen - x) #y is starting at the right side
                        z = str(WrkStr1[(y-1):y]) # z is the rightmost chord character, position 29:30
                        if not z.isspace(): #if the rightmost character is not blank, build the chord
                            PartialChord = (z + PartialChord) #add the characters together
                        elif PartialChord != "": #now we have hit whitespace,
                            # check if we have a partial chord or if we hit the beginning of the line (pos 1)
                            FullChord = PartialChord #Finalize rightmost full chord such as B7 or Bsus4
                            PartialChord = "" #blank out partial chord for next time
                            WrkStr3 = WrkStr2[:y-1].lstrip()
                            WrkStr4 = WrkStr2[y-1:]
                            WrkStr5= (WrkStr3+"["+FullChord+"]"+WrkStr4)
                            break
                        if PartialChord != ""  and y == 1:
                            FullChord = PartialChord  # Finalize rightmost full chord such as B7 or Bsus4
                            PartialChord = ""  # blank out partial chord for next time
                            WrkStr3 = WrkStr2[:y - 1].lstrip()
                            WrkStr4 = WrkStr2[y - 1:]
                            WrkStr5 = (WrkStr3 + "[" + FullChord + "]" + WrkStr4)
                            break
                    WrkStr1 = WrkStr1[:y]# new chord string w/o the rightmost chord, stopping just there
                    WrkStr2 = WrkStr5 #new lyric string with the rightmost chord(s) now embedded
                #print (WrkStr5)
                file.write(WrkStr5+ '\n')
                SongStart=SongStart+2
    else:
        SongStart=SongStart+1
file.close()
WebSongTitle = WebSongTitle[:-22].title()+'\n'+ChordURL
line_prepender('ReformattedSong.txt',WebSongTitle)

print("I created a file called ReformattedSong.txt")
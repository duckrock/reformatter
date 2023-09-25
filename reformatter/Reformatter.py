exec(open('HTMLtoTXTFileFreeman.py').read())
exec(open('FileToListOfLists.py').read())
#----------------------------------------------------
table = str.maketrans(dict.fromkeys('[\'\"]')) #Create a translate table to remove extraneous list characters like [,],'
#########################################################
SongStart = 0 #Hardcoded start of the chords line, usually the Lyrics are one line later
SpecialLine = ['Intro','Verse','Chorus','Refrain','Instrumental','Solo','Verse 1','Verse 2','Verse 3','Outro','Bridge'] #used to check for special song lines
TitleLine = ['Capo ']
SomeChords = ['A  ','[A] ','F#m ','G  ','F  ','E  ','Am7  ','C  ','D7  ','E/','A/','G/','Am/','G ','C ','Em','Am ','Bm','C ','D ','G ','E ','B7 '] #used to check for a succession of chords
SingleChordLine = ['A','B','C','D','E','F','G','Am']
#######################################################
def line_prepender(filename, line): #used later to prepend the song's title and URL, after processing is over
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)
#######################################################
print(songlist) #debug
CapoTitle = "No Capo"
WrkStr5 = str(songlist[SongStart]).translate(table) #Get the first line of the song
NewFileName = '_'+WebSongTitle[:20]+".txt" #use first 10 chars of song title for filename.
file=open(NewFileName,"w") # Open a file for output called the truncated name of the song
while SongStart+1<len(songlist):  # start at the first in the list, then move forward
    WrkStr1 = str(songlist[SongStart]).translate(table) #first line of text, should be chords above lyrics
    WrkStr2 = str(songlist[SongStart+1]).translate(table) #second line of text, should be lyrics
    #print(WrkStr1,'raw1')
    #print(WrkStr2,'raw2')
    ChordLineLen = len(WrkStr1.rstrip()) #total length of line with the chord, need this to back from
    LyricLineLen = len(WrkStr2.rstrip()) #need this in the case the lyric line is shorter than the chordline
    if ChordLineLen>LyricLineLen:
        WrkStr2 = WrkStr2.ljust(ChordLineLen) #force the lyric line to be as long as the chordline
    if ChordLineLen > 0 : #must be a nonblank row of text, otherwise go to the next line
        # Check the first string and see if it is special
        if any([st in WrkStr1.title() for st in TitleLine]): # is capo in the first line?
            CapoTitle = WrkStr1.title()
            SongStart = SongStart + 1
        elif any([st in WrkStr2.title() for st in TitleLine]): # is capo in the second line?
            CapoTitle = WrkStr2.title()
            SongStart = SongStart + 2
        elif any([st in WrkStr1.title() for st in SpecialLine]):# or not any([st in WrkStr1 for st in SomeChords]):
            # are you a chorus, verse, etc? OR are you no chords at all? then just write/print you with brackets
            file.write('['+WrkStr1.strip()+']'+'\n')
            SongStart = SongStart + 1  # advance the line checker
        elif any([st in WrkStr1 for st in SomeChords]) and any([st in WrkStr2 for st in SomeChords]):
            #are you chords on top  more chords?
            file.write('[' + WrkStr1.strip() + ']')
            file.write('[' + WrkStr2.strip() + ']\n')
            SongStart = SongStart + 1
        elif any([st in WrkStr1 for st in SomeChords]) and any([st in WrkStr2.title() for st in SpecialLine]):
            #are you chords on top of a special line ?
            file.write('[' + WrkStr1.strip() + ']\n')
            file.write('[' + WrkStr2.strip() + ']\n')
            SongStart = SongStart + 2
        elif any([st in WrkStr1.title() for st in SpecialLine]) or any([st in WrkStr2.title() for st in SpecialLine]) or any([st in WrkStr2 for st in SomeChords]):
            #print('#you are a special line on line 1 or 2 or you are a chord line on line 2?')#you are NOT a special line on line one nor chord on line one or line 2?
            #print(WrkStr1.strip())
            file.write(WrkStr1.strip() + '\n')  # If there is a title, add it to the file first.
            SongStart = SongStart + 1  # advance the line checker
            #print('in elif6')
        else:
            #####################################################################
            y=80 ###This is the last position of a line
            PartialChord=""
            if any([st in WrkStr2 for st in SomeChords]) and any([st in WrkStr1 for st in SomeChords]): #this checks for multiple lines of chords,
                #print('[' + WrkStr1 + ']')
                #print('[' + WrkStr2 + ']')
                file.write('[' + WrkStr1 + ']\n')
                file.write('[' + WrkStr2 + ']\n')
                SongStart = SongStart + 2
            elif (any([st in WrkStr1 for st in SomeChords]) and WrkStr2.rstrip() == ""): #chords at the bottom of the page?
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

WebSongTitle = WebSongTitle[:-22].title()+" - "+CapoTitle+'\n'+ChordURL
line_prepender(NewFileName,WebSongTitle)

print("I created a file called "+NewFileName)
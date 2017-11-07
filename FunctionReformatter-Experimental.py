#John Freeman
#Get the URL from the user and parse that HTML into usable text file before we begin the editing
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os ###for filepath name
UltimateGuitar = 'https://tabs.ultimate-guitar.com'
CowboyLyrics = 'https://www.cowboylyrics.com'
CountryTabs = 'http://www.countrytabs.com'
############################################################

def main():
    GetChordURL() # Comment this out for testing and run TesterFreeman for full regression test.
    #if ChordURL[:4] == CowboyLyrics[:4]: #Input is a URL, not text, so convert it to text
    HTMLGetWebSongTitle(ChordURL)
    HTMLToTextFunc(ChordURL)
    #else:
    #    GetTextInput()
    #    WebSongTitle = 'Text Input'
    FileToLOL('UnformattedSong.txt')  # call the function to put the file into a list of lists
    ReformatterFunc(SongList, WebSongTitle, ChordURL)
    LinePrepender(os.path.join(os.path.expanduser('~'), 'Documents\\GitHub\\reformatter\\Songs', NewFileName), WebSongTitle)
    print("I created a file called " + NewFileName)
#######################################################
def GetChordURL():#Ask for Chord URL or hardcode for testing
    global ChordURL
    ChordURL = str(input("Hello! What URL or Text has the song you want to reformat? (put space after and click enter)\n"))
########################################################
def GetTextInput():#Not used yet, used to accept text instead of a URL
    #pass
    f = open("UnformattedSong.txt", "w+")
    # write the song into the file
    f.write(ChordURL)
    f.close()
    print("I created a file called UnformattedSong.txt")
#######################################################
def HTMLGetWebSongTitle(ChordURL):#From ChordURL, Get the Song Title
    global WebSongTitle
    page = urlopen(ChordURL)  # query the website and return the html to the variable ‘page’
    # parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, "html.parser")
    WebSongTitle = soup.title.string
    WebSongTitle = WebSongTitle.title()
#######################################################
def HTMLToTextFunc(ChordURL):#From ChordURL, get text from chord sites and load to TXT file
    page = urlopen(ChordURL)  # query the website and return the html to the variable ‘page’
    # parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, "html.parser")
    print(ChordURL)
    #print(WebSongTitle)
    print("Thanks, let me see what I can do")
    #print(ChordPage[:32])
    #if any([st in ChordURL for st in UltimateGuitar]):
    if ChordURL[:32] == UltimateGuitar:
        print ("Calling BeautifulSoup on Ultimate site")
        SongToReformat = soup.find("textarea", class_="js-tab-textarea ug-no-height").get_text()
        #SongToReformat = soup.textarea.string
    elif ChordURL[:28] == CowboyLyrics:
        SongToReformat = soup.pre.string
        print("Calling BeautifulSoup on Cowboy site")
    else:
        SongToReformat = "There has been an error or unsupported website, nothing written"
    #print(SongToReformat)
    # Open a file for writing and create it if it doesn't exist
    f = open("UnformattedSong.txt", "w+")
    # write the song into the file
    f.write(str(SongToReformat))
    f.close()
    print ("I created a file called UnformattedSong.txt")
#######################################################
def FileToLOL(songfile): # Creates the song list of lists from file
    global SongList
    # Open the file back up and read the contents into a list of lists
    SongList = []  # Instantiate variable SongList as a list
    fh = open(songfile, "r")
    if fh.mode == 'r':  # check to make sure that the file was opened
        for line in fh.readlines():
            y = [line.strip('\n')]
            SongList.append(y)  # Load the file contents into a list of lists
            # SongList.append(line)  # Load the file contents into a list of lists
        fh.close()  # close the file

    SongList = [x for x in SongList if x != ['']]
#######################################################
def ReformatterFunc(SongList,WebSongTitle,ChordURL):
    global NewFileName
    #----------------------------------------------------
    table = str.maketrans(dict.fromkeys('[\'\"]')) #Create a translate table to remove extraneous list characters like [,],'
    #########################################################
    SongStart = 0 #Hardcoded start of the chords line, usually the Lyrics are one line later
    SpecialLine = ['Intro','Verse','Chorus','Refrain','Instrumental','Solo','Verse 1','Verse 2','Verse 3','Outro','Bridge','Fade Finish','Pause...'] #used to check for special song lines
    TitleLine = ['Capo ']
    SomeChords = ['A  ','[A] ','F#m ','G  ','F  ','E  ','Am7  ','C  ','D7  ','E/','A/','G/',
                  'Am/','G ','C ','Em','Am ','Bm','C ','D ','G ','E ','B7 ','F5','E5','F#5','G5','Bb5','C5'] #used to check for a succession of chords
    SingleChordLine = ['A','B','C','D','E','F','G','Am']
    ThrowawayLine = ['---','|-',]
    CapoTitle = "No Capo"
    print(SongList) #debug
    NewFileName = '_' + WebSongTitle[:20] + ".txt"  # use first 10 chars of song title for filename.
    #WrkStr5 = str(SongList[SongStart]).translate(table) #Get the first line of the song
    #os.path.join(os.path.expanduser('~'), 'Songs', NewFileName)
    file=open(os.path.join(os.path.expanduser('~'), 'Documents\\GitHub\\reformatter\\Songs', NewFileName),"w") # Open a file for output called the truncated name of the song
    while SongStart+1<len(SongList):  # start at the first in the list, then move forward
        WrkStr1 = str(SongList[SongStart]).translate(table) #first line of text, should be chords above lyrics
        WrkStr2 = str(SongList[SongStart+1]).translate(table) #second line of text, should be lyrics
        #print(WrkStr1,'raw1')
        #print(WrkStr2,'raw2')
        ChordLineLen = len(WrkStr1.rstrip()) #total length of line with the chord, need this to back from
        LyricLineLen = len(WrkStr2.rstrip()) #need this in the case the lyric line is shorter than the chordline
        if ChordLineLen>LyricLineLen:
            WrkStr2 = WrkStr2.ljust(ChordLineLen) #force the lyric line to be as long as the chordline
        if ChordLineLen > 0 : #must be a nonblank row of text, otherwise go to the next line
            # Check the first string and see if it is special
            if any([st in WrkStr1.title() for st in TitleLine]): # is capo or Capo (title) in the first line?
                CapoTitle = WrkStr1.title()
                SongStart +=1
            elif any([st in WrkStr1.strip() for st in ThrowawayLine]):
                SongStart +=1
            elif any([st in WrkStr2.strip() for st in ThrowawayLine]):
                SongStart +=2
            elif any([st in WrkStr2.title() for st in TitleLine]): # is capo in the second line?
                CapoTitle = WrkStr2.title()
                SongStart +=2
            elif any([st in WrkStr1.title() for st in SpecialLine]) or WrkStr1.title()==SingleChordLine:# are you a chorus, verse, etc? or single chord? then just print with brackets
                file.write('['+WrkStr1.strip()+']'+'\n')
                SongStart +=1  # advance the line checker
            elif (any([st in WrkStr1 for st in SomeChords]) or  WrkStr1.title()==SingleChordLine) and (any([st in WrkStr2 for st in SomeChords]) or WrkStr2.title()==SingleChordLine): #are you chord(s) on top  more chords? you may be a solo!
                file.write('[' + WrkStr1.strip() + ']')
                file.write('[' + WrkStr2.strip() + ']\n')
                SongStart +=2
            elif any([st in WrkStr1 for st in SomeChords]) and any([st in WrkStr2.title() for st in SpecialLine]):
                #print('#are you chords on top of a special line ?')
                file.write('[' + WrkStr1.strip() + ']\n')
                file.write('[' + WrkStr2.strip() + ']\n')
                #file.write('#are you chords on top of a special line ?')
                SongStart +=2
            elif any([st in WrkStr1.title() for st in SpecialLine]):#you are a special line on line 1, just print
                file.write(WrkStr1.strip() + '\n')  # If there is a title, add it to the file first.
                #file.write(WrkStr2.strip() + '\n')
                SongStart +=1  # advance the line checker
                #print('in elif6')
            elif any([st in WrkStr2.title() for st in SpecialLine]):
                file.write('[' + WrkStr2.title().strip() + ']\n')  # If there is a special line in stream2
                SongStart +=2  # advance the line checker
            elif any([st in WrkStr2 for st in SomeChords]):# If there is chords in stream2
                file.write('[' + WrkStr2.strip() + ']\n')
                SongStart +=2  # advance the line checker
            #elif (any([st in WrkStr1 for st in SomeChords]) and WrkStr2.rstrip() == ""): #chords at the bottom of the page?
             #   file.write('[' + WrkStr1 + ']\n')
              #  SongStart +=2
            else:############################################################################
                y=80 ###This is the last position of a line
                PartialChord=""
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
                SongStart+=2
        else:
            SongStart+=1
    file.close()
    WebSongTitle = WebSongTitle[:-22].title() + " - " + CapoTitle + '\n' + ChordURL
#######################################################
def LinePrepender(filename, line): #used later to prepend the song's title and URL to file contents, after processing is over
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)
    return
#######################################################
if __name__ == "__main__": main()

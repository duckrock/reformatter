#John Freeman
#Get the URL from the user and parse that HTML into usable text file before we begin the editing
from bs4 import BeautifulSoup
from urllib.request import urlopen
UltimateGuitar = 'https://tabs.ultimate-guitar.com'
CowboyLyrics = 'https://www.cowboylyrics.com'
CountryTabs = 'http://www.countrytabs.com'
###################################################################################################################

def main():
    HTMLGetWebSongTitle(GetChordURL())
    HTMLToTextFunc(ChordURL)
    FileToLOL('UnformattedSong.txt')  # call the function to put the file into a list of lists
    # Remove blank lines
    ReformatterFunc(SongList, WebSongTitle, ChordURL)
    LinePrepender(NewFileName, WebSongTitle)
    print("I created a file called " + NewFileName)
#######################################################
def GetChordURL():#Ask for Chord URL or hardcode for testing
    global ChordURL
    ChordURL = str(input("Hello! What URL has the song you want to reformat? (put space after and click enter)\n"))
    # specify the url
    # dev hardcode------------------------------------------------------------------------
    # ChordURL = "https://tabs.ultimate-guitar.com/w/willie_nelson/all_of_me_crd.htm"
    # ChordURL = "https://tabs.ultimate-guitar.com/s/sturgill_simpson/turtles_all_the_way_down_crd.htm"
    # ChordURL = "https://www.cowboylyrics.com/tabs/simpson-sturgill/keep-it-between-the-lines-31497.html"
    ChordURL = "https://tabs.ultimate-guitar.com/c/creedence_clearwater_revival/have_you_ever_seen_the_rain_crd.htm"
    # ChordURL = 'https://tabs.ultimate-guitar.com/c/conor_oberst/till_st_dymphna_kicks_us_out_crd.htm'
    # ChordURL =
    # dev hardcode--------------------------------------------------------------------------
    return ChordURL
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
    SpecialLine = ['Intro','Verse','Chorus','Refrain','Instrumental','Solo','Verse 1','Verse 2','Verse 3','Outro','Bridge'] #used to check for special song lines
    TitleLine = ['Capo ']
    SomeChords = ['A  ','[A] ','F#m ','G  ','F  ','E  ','Am7  ','C  ','D7  ','E/','A/','G/','Am/','G ','C ','Em','Am ','Bm','C ','D ','G ','E ','B7 '] #used to check for a succession of chords
    SingleChordLine = ['A','B','C','D','E','F','G','Am']
    CapoTitle = "No Capo"
    print(SongList) #debug
    NewFileName = '_' + WebSongTitle[:20] + ".txt"  # use first 10 chars of song title for filename.
    WrkStr5 = str(SongList[SongStart]).translate(table) #Get the first line of the song
    file=open(NewFileName,"w") # Open a file for output called the truncated name of the song
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

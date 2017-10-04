#John Freeman
#Get the URL from the user and parse that HTML into usable text file before we begin the editing
from bs4 import BeautifulSoup
from urllib.request import urlopen
#chord_page = input("Hello! What URL has the song you want to reformat?\n")
ChordPage = str(input("Hello! What URL has the song you want to reformat? (put space after and click enter)\n"))
# specify the url
#dev hardcode------------------------------------------------------------------------
#ChordPage = "https://tabs.ultimate-guitar.com/w/willie_nelson/all_of_me_crd.htm"
#ChordPage = "https://tabs.ultimate-guitar.com/s/sturgill_simpson/turtles_all_the_way_down_crd.htm"
#ChordPage = "https://www.cowboylyrics.com/tabs/simpson-sturgill/keep-it-between-the-lines-31497.html"
#dev hardcode--------------------------------------------------------------------------
UltimateGuitar = 'https://tabs.ultimate-guitar.com'
CowboyLyrics = 'https://www.cowboylyrics.com'
print (ChordPage)
#OK, back to normal
print ("Thanks, let me see what I can do")
# query the website and return the html to the variable ‘page’
page = urlopen(ChordPage)
# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, "html.parser")
#print(ChordPage[:32])
if ChordPage[:32] == UltimateGuitar:
    SongToReformat = (soup.textarea.string)
elif ChordPage[:28] == CowboyLyrics:
    SongToReformat = (soup.pre.string)
#print(SongToReformat)
# Open a file for writing and create it if it doesn't exist
f = open("SongFile.txt", "w+")
# write the song into the file
f.write(SongToReformat)
f.close()
print ("I created a file called SongFile.txt")


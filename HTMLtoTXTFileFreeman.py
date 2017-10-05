#John Freeman
#Get the URL from the user and parse that HTML into usable text file before we begin the editing
from bs4 import BeautifulSoup
from urllib.request import urlopen
ChordURL = str(input("Hello! What URL has the song you want to reformat? (put space after and click enter)\n"))
# specify the url
#dev hardcode------------------------------------------------------------------------
#ChordURL = "https://tabs.ultimate-guitar.com/w/willie_nelson/all_of_me_crd.htm"
#ChordURL = "https://tabs.ultimate-guitar.com/s/sturgill_simpson/turtles_all_the_way_down_crd.htm"
#ChordURL = "https://www.cowboylyrics.com/tabs/simpson-sturgill/keep-it-between-the-lines-31497.html"
ChordURL = "https://tabs.ultimate-guitar.com/c/creedence_clearwater_revival/have_you_ever_seen_the_rain_crd.htm"
#dev hardcode--------------------------------------------------------------------------
UltimateGuitar = 'https://tabs.ultimate-guitar.com'
CowboyLyrics = 'https://www.cowboylyrics.com'
print (ChordURL)
print ("Thanks, let me see what I can do")
page = urlopen(ChordURL) # query the website and return the html to the variable ‘page’
# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page,"html.parser")
WebSongTitle=soup.title.string
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


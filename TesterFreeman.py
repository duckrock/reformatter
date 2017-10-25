#Tester
global ChordURL
table = str.maketrans(dict.fromkeys('[\'\"]'))
fh = open("TestURLsFreeman.txt", "r")
if fh.mode == 'r':  # check to make sure that the file was opened
    for line in fh.readlines():
        ChordURL = str(line.translate(table).strip())
        exec(open('FunctionReformatter-Experimental.py').read())
    fh.close()  # close the file

# ChordURLSet = ["https://tabs.ultimate-guitar.com/w/willie_nelson/all_of_me_crd.htm",
#                "https://tabs.ultimate-guitar.com/s/sturgill_simpson/turtles_all_the_way_down_crd.htm",
#                "https://www.cowboylyrics.com/tabs/simpson-sturgill/keep-it-between-the-lines-31497.html",
#                "https://tabs.ultimate-guitar.com/c/creedence_clearwater_revival/have_you_ever_seen_the_rain_crd.htm",
#                "https://tabs.ultimate-guitar.com/c/conor_oberst/till_st_dymphna_kicks_us_out_crd.htm"]
# x=1
# while x<5:
#     print(ChordURLSet[x])
#     ChordURL=ChordURLSet[x]
#     exec(open('FunctionReformatter-Experimental.py').read())
#     x+=1
#

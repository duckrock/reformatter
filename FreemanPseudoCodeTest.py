# Chord Music Reformatting Project - John Freeman - Sept 2017
# I play guitar and sing and would like songs reformatted from the standard to my format that is easily
# read on one page on an iPad or 10" tablet without scrolling.
####################################################################
# Use RPA to Get the song I want from the internet (future)
# https://tabs.ultimate-guitar.com/w/willie_nelson/all_of_me_crd.htm is a good example
# Use RPA to Get it into a temporary text file with predictable character positions (future)  Do I want to view source?
# and then look at that first? (future)
# Parse out the text file of the song itself, removing all extraneous junk, signatures, ad copy (future)
# Line by line (see example below), get the chord line, right side first so as to not upset the line up
# After the chord line, insert the chord with a bracket ahead and behind [ ].
# if close, put it at the start of the appropriate lyric word.  If in middle (usually on the syllable)
# then use exact spacing.
# if a multicharacter chord, be prepared such as D, Dsus, Dmsus, D3msus, etc.
# Remove the chord line

# will look like this: Happy Birthday - by Fred Jones
# Original:
#      C           G#           Dsus4
#Happy Birthday to you, Happy Birthday to you
#Reformatted
#Happy [C]Birthday to [G#]you, Happy Birth[Dsus4]day to you
#
# and so on.  This makes font changes and other customer edits much easier after the fact.

# afterwards, make the typeface Arial 14 pt. and remove
# any multi-line blank line breaks, only one line should ever be blank at most between lines. (future)
# Manually I will still have normalize the repeat chorus if it is repeated unneccesarily
# and other tweeks (future)

#Use RPA to get a potential song into a text file with predictable constructs
# Open the text file representing the "before" and go thru it


            

#Find the position of the last letter (the "Dsus4" in the example)
#GetPositionRightMost(Line 1 of that Dsus4) = J
#Put the last string into memory X=last grouping (Duss4)
#Go to that position (J) in Line 2
#Insert a "[", then the X, then the "]"
#Repeat for the next rightmost string of characters
    

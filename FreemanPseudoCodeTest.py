# Chord Music Reformatting Project - John Freeman - Sept 2017
# I play guitar and sing and would like songs reformatted from the standard to my format that is easily
# read on one page on an iPad or 10" tablet without scrolling.
####################################################################
# Use method (beautifulsoup) to Get the song I want from the internet
# https://tabs.ultimate-guitar.com/w/willie_nelson/all_of_me_crd.htm is a good example
# Use method to get it into a temporary text file with predictable character positions
# Parse out the text file of the song itself, removing all extraneous junk, signatures, ad copy
# Line by line (see example below), get the chord line, right side first so as to not upset the line up
# After the chord line, insert the chord with a bracket ahead and behind [ ].
# if a multicharacter chord, be prepared such as D, Dsus, Dmsus, D3msus, etc.
# Remove the old dedicated chord line since the chord is now embedded in the lyrics

# will look like this: Happy Birthday - by Fred Jones
# Original:
#      C           G#           Dsus4
#Happy Birthday to you, Happy Birthday to you
#Reformatted
#Happy [C]Birthday to [G#]you, Happy Birth[Dsus4]day to you
#
# and so on.  This makes font changes and other customer edits much easier after the fact.
# afterwards, make the typeface Arial 14 pt. and remove.
# if user chooses a tablet type, try to get it optimized for one-page viewing on that tablet type
# any multi-line blank line breaks, only one line should ever be blank at most between lines.
# Manually I will still have normalize the repeat chorus if it is repeated unnecessarily
# and other tweeks (future)

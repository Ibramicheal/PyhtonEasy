#A prog for my favourite song
"""
printing the details of my favourite song, hope you enjoy the song.
This is my gift to you.
"""

Artist = "Mbosso "
Title = "Hodari"
Genre = "Bongo flavour"#a type of tanzanian music
DurationInSeconds = "4mins 02secs"
fileType = "mp4"
#Cost in pounds
cost = 2.50
yearOfRelease = 2018
monthOfRelease = "september"
dayOfRelease = 24
viewsOnYouTube = 31071275

#function to print out who the artist is.
def whoISTheArtist():
    print(Artist)
#function to print out tittle of song
def whatIsTheTittle():
    print(Title)

#function to print out cost of track in pounds
def whatIsTheCost():
    print(cost)

#function with boolean expersion in it
def expersionCheckMonth(month):
    if month == "september":
        return True
    else:
        return False

whoISTheArtist()
whatIsTheTittle()
whatIsTheCost()
expersionCheckMonth("september")
expersionCheckMonth("november")

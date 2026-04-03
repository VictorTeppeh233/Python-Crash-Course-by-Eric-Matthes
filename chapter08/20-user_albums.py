# assignment 8.8
# user albums

"""
Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
Be sure to include a quit value in the while loop.
"""

def make_ablbum(artist_name, album_title):
    """Function takes details of the album then puts it in a dictionary."""
    album = {'Artist name' : artist_name.title(), 'Album Title': album_title.title()}

    # returning the value of the function
    return album
#message for user
print("(Enter 'q' to end the game.)")

#while loop
while True:
    #receiving input    
    artist = input('Enter the name of the artist. ')
    if artist == "q":
        break
    title = input('Enter the name of the title of the album. ')
    if title == "q":
        break
    
    #calling the function and printing it
    details = make_ablbum(artist, title)
    print(details)

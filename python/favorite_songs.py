my_music = ["The House of the Rising Sun",
            "I Disappear",
            "Ain't No Sunshine",
            "Landing in London"]

print("These are my favorite songs:")

for song in my_music:
    print(song)


user_playlist = []
new_song = ""

while new_song != "end":
    new_song = input ("What are yours? Type 'end' to finish adding songs: ") 
    user_playlist.append(new_song)

    if new_song == "end":
        user_playlist.remove("end")
        for user_song in user_playlist:
            print (user_song)
             
    

    



    

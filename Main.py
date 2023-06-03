import os

from Playlist import Playlist
from Song import Song

ActivePlaylist = Playlist("Empty", "N/A")

def Menu():
  os.system('cls')
  print("""

        Options
      1. Add Song
      2. Remove Song
      3. Load Playlist
      4. Save Playlist
      5. Shuffle
      6. Quit

  """)
  while True:
    print("""
        Playlist
    Currently Playing:
    """)
    
    for SongObj in ActivePlaylist.Songs:
        print(SongObj.Title + " - " + str(SongObj.Duration) + " secs")
    
    UserInput = str(input("> "))
    
    if UserInput == "1":
        Title = ""
        Artist = ""
        Duration = 0

        while True:
            Title = str(input("Title of Song: "))
            if len(Title) > 0:
                break

        while True:
            Artist = str(input("Artist: "))
            if len(Artist) > 0:
                break
        while True:
            try:
                Duration = int(input("Duration: "))
                if Duration > 0:
                    break
            except:
                print("input a Number!")

        ActivePlaylist.Enqueue(Song(Title, Artist, Duration))

    elif UserInput == "2":
        SongToRemove = str(input("Song Name: "))
        
        for EnqueuedSong in ActivePlaylist.Songs:
            if EnqueuedSong.Title == SongToRemove:
                ActivePlaylist.Remove(EnqueuedSong)

    elif UserInput == "3":
        FileDirectory = str(input("File: "))
        ActivePlaylist.Load(FileDirectory)
    elif UserInput == "4":
        ActivePlaylist.Save(False)
    elif UserInput == "5":
        ActivePlaylist.Shuffle()
    elif UserInput == "6":
        return False

while True:
  Menu()
  break

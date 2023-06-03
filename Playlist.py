from Song import Song
import random

class Playlist:
  def __init__(self, title, filename):
    self.Title = title
    self.Filename = filename
    self.Songs = []
  
  def Load(self, filename):
    self.Songs = []
    
    print("Opening Playlist")

    try:
        File = open(filename + ".txt", "r")
    except:
        print("File not found!")
        
    for line in File:
      Fields = line.split(";")
      SongObj = Song(Fields[0], Fields[1], int(Fields[2]))
      self.Enqueue(SongObj)

  def Save(self, removeWhenSaved):
    print("Saving")
    File = ""

    if self.Filename == "N/A":
        while True:
            newFile = str(input("Create a File: "))
            if len(newFile) > 0:
                open(newFile + ".txt", 'x')
                self.Filename = newFile + ".txt"
            break

    File = open(self.Filename, "w")

    for SongObj in self.Songs:
      File.write(SongObj.Title + ";" + SongObj.Artist + ";" + str(SongObj.Duration) + ";" + "\n")
      
      if removeWhenSaved:
        self.Remove(SongObj)

    File.close()

  def Enqueue(self, SongObj):
    self.Songs.append(SongObj)

  def Remove(self, SongObj):
    self.Songs.remove(SongObj)

  def Shuffle(self):
    random.shuffle(self.Songs)

  def Reset(self):
    self.Songs = []
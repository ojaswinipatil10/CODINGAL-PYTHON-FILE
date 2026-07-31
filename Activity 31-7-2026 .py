class Playlist :
     def __init__(self , name, genre):
          self.name = name
          self.genre = genre
          self.songs = []
          print("----- __________-----")
          print(f"Playlist '[self.name] ' ([self.genre]) is ready !")
     def add_song(self , song):
          self.songs.append(song)
          print(f"'[song] ' add to [self.name].")
     def remove_song(self , song):
          if song in self.songs:
               self.songs.remove(song)
               print(f"'[song]' not found in the playlist !!!")
     def display(self):
          print(f"/n----[self.name] ([self.genre])---")
          if self.songs:
               for i, song in enumerate(self.songs , 1):
                    print(f" [i]. [song]")
          else:
               print("NO SONGS YET , ADD SOME !!!!")
     def __del__(self):
          print("----- __________-----")
          print(f"Playlist '[self.name]' has been deleted . GOOD BYEE!!!")
my_playlist = Playlist("RoAd TrIp MiX" , "POP")
while True:
     print("/n1. Add song 2. Remove song 3. View the Playlist  4. Delete & Quit")
     choice = input("Enter choice : __________ ")

     if choice == "1":
          song = input("Enter the song name : _______")
          my_playlist.add_song(song)
     elif choice == "2":
           song = input("Enter the song name to remove : _______")
           my_playlist.remove_song(song)
     elif choice == "3":
           my_playlist.display()
     elif choice == "4":
         del my_playlist 
         break
     else:
          print("INVALID CHOICE , Enter 1 , 2 , 3 , or 4.")
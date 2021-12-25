albums = [("SonTungMTP", "NhacTre", 2018, [
          (1, "Con mua ngang qua."), (2, "Chung ta khong thuoc ve nhau"), (3, "Noi nay co anh")]),
          ("Ho Quang Hieu", "Nhac Vui", 2019, [(1, "Khong cam xuc"), (2, "Noi ay con tim ve"), (3, "Tim em")])]

for artist, album, year, songs in albums:
    print("Artist: {}, Album: {}, Year: {}, Song: {}".format(
        artist, album, year, songs))

print("=========" * 4)
album = albums[1]
print("\nAlbums", album)
songs = album[3]
print("\nSongs: ", songs)
song = songs[1]
print("\nsong: ", song)

mayhem = albums[1][3][1]
print("\nmayhem: ", mayhem)

print(albums[1])
print(albums[1][3][0])
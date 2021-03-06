from nested_data import albums

SONG_LIST_INDEX = 3
SONG_TITLE_INDEX = 1 # (1, "Không cảm xúc"). Nó sẽ lấy "Không cảm xúc" ra ngoài.

while True:
    print("Please choose your album (invalid choice exits): ")
    for index, (artis, album, year, songs) in enumerate(albums):
        print("{}: {}"
              .format(index + 1, album))

    choice = int(input())
    if 1 <= choice <= len(albums):
        song_list = albums[choice - 1][SONG_LIST_INDEX]
    else:
        break

    print("Please choose your song: ")
    for index, (track_number, song) in enumerate(song_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(song_list):
        title = song_list[song_choice - 1][SONG_TITLE_INDEX]
    else:
        break

    print("Playing {}".format(title))
    print("=" * 40)

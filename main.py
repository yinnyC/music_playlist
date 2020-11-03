from linked_list import LinkedList

# Create a music playlist
music_playlist = LinkedList()
# Append 3 songs
music_playlist.append("Fast Car")
music_playlist.append("Sweet Disposition")
music_playlist.append("Underwater")
print("----- Browse Music Playlist ----")
music_playlist.print_songs()
# Prepend 2 songs
music_playlist.prepend('Some Nights')
music_playlist.prepend('Thursday')
print("----- Browse Music Playlist ----")
music_playlist.print_songs()
# Delete the first and the last song
music_playlist.delete_from_head()
music_playlist.delete_from_tail()
print("----- Browse Music Playlist ----")
music_playlist.print_songs()
# Find songs

print('\nFind song <Thursday> :', music_playlist.find('Thursday'))
print('Find song <Fast Car> :', music_playlist.find('Fast Car'))

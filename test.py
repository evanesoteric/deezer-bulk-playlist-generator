import deezer

album_tracklist = []

client = deezer.Client(app_id='123456', app_secret='0000000000000000')

client = deezer.Client(headers={'Accept-Language': 'en-US'})

album = client.get_album('000000000')

for track in album.get_tracks():
    album_tracklist.append(str(track.id))
    print(track.id)

# create playlist

manage_library

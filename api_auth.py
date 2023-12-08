

app_id = 123456
redirect_uri = ''

# get access token
r = requests.post(
	'https://connect.deezer.com/oauth/auth',
	app_id=app_id,
	redirect_uri=redirect_uri)



http://api.deezer.com/playlist/<playlist_id>/tracks?access_token=<access_token>&request_method=post&songs=<track_id>


title = 'Alpha Omega'





import requests


DEEZER_APP_ID = '123456'
DEEZER_REDIRECT_URI = 'http://localhost:8080/oauth/return'
perms = 'manage_library'

r = requests.get(f'https://connect.deezer.com/oauth/auth.php?app_id={DEEZER_APP_ID}'
           f'&redirect_uri={DEEZER_REDIRECT_URI}&perms={perms}')


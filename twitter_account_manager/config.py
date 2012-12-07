class Config:
	DEBUG = False
	CSRF_ENABLED = True

	TWITTER_BASE_URL='https://api.twitter.com/1/'
	TWITTER_REQUEST_TOKEN_URL='https://api.twitter.com/oauth/request_token'
	TWITTER_ACCESS_TOKEN_URL='https://api.twitter.com/oauth/access_token'
	TWITTER_AUTHOTIZE_URL='https://api.twitter.com/oauth/authenticate'
import json

from rauth import OAuth1Service, OAuth2Service
from flask import current_app, url_for, redirect, request, session

class OAuthSignIn(object):
    providers = None

    def __init__(self, name):
        self.name = name
        credentials = current_app.config['OAUTH_CREDENTIALS'][name]
        self.id = credentials['id']
        self.secret = credentials['secret']

    def authorize(self):
        pass

    def callback(self):
        pass

    def get_callback_url(self):
        return url_for('oauth.callback', provider=self.name, _external=True)

    @classmethod
    def get_provider(self, provider_name):
        if self.providers is None:
            self.providers = {}
            for provider_class in self.__subclasses__():
                provider = provider_class()
                self.providers[provider.name] = provider

        return self.providers[provider_name]

class FacebookSignIn(OAuthSignIn):
    def __init__(self):
        super(FacebookSignIn, self).__init__('facebook')

        self.service = OAuth2Service(
            name='facebook',
            client_id=self.id,
            client_secret=self.secret,
            authorize_url='https://graph.facebook.com/oauth/authorize',
            access_token_url='https://graph.facebook.com/oauth/access_token',
            base_url='https://graph.facebook.com/'
        )

    def authorize(self):
        return redirect(self.service.get_authorize_url(
            scope='public_profile,email',
            response_type='code',
            redirect_uri=self.get_callback_url()
        ))

    def callback(self):
        if 'code' not in request.args:
            return None, None, None

        oauth_session = self.service.get_auth_session(
            data={
                'code': request.args['code'],
                'grant_type': 'authorization_code',
                'redirect_uri': self.get_callback_url()
            }
        )

        me = oauth_session.get('me?fields=name,id,email,picture').json()
        return ('facebook$' + str(me['id']), me['name'], me['email'], me['picture']['data']['url'])

class TwitterSignIn(OAuthSignIn):
    def __init__(self):
        super(TwitterSignIn, self).__init__('twitter')

        self.service = OAuth1Service(
            name='twitter',
            consumer_key=self.id,
            consumer_secret=self.secret,
            request_token_url='https://api.twitter.com/oauth/request_token',
            authorize_url='https://api.twitter.com/oauth/authorize',
            access_token_url='https://api.twitter.com/oauth/access_token',
            base_url='https://api.twitter.com/1.1/'
        )

    def authorize(self):
        request_token = self.service.get_request_token(
            params={'oauth_callback': self.get_callback_url()}
        )
        session['request_token'] = request_token
        return redirect(self.service.get_authorize_url(request_token[0]))

    def callback(self):
        request_token = session.pop('request_token')

        if 'oauth_verifier' not in request.args:
            return None, None, None

        oauth_session = self.service.get_auth_session(
            request_token[0],
            request_token[1],
            data={
                'oauth_verifier': request.args['oauth_verifier']
            }
        )

        me = oauth_session.get('account/verify_credentials.json').json()
        return ('twitter$' + str(me['id']), me['name'], me['screen_name'], me['profile_image_url'])

class GooglePlusSignIn(OAuthSignIn):
    def __init__(self):
        super(GooglePlusSignIn, self).__init__('google')

        self.service = OAuth2Service(
            name='google',
            client_id=self.id,
            client_secret=self.secret,
            authorize_url='https://accounts.google.com/o/oauth2/v2/auth',
            access_token_url='https://www.googleapis.com/oauth2/v4/token',
            base_url='https://www.googleapis.com/oauth2/v3/userinfo'
        )

    def authorize(self):
        return redirect(self.service.get_authorize_url(
            scope='profile email',
            response_type='code',
            redirect_uri=self.get_callback_url()
        ))

    def callback(self):
        if 'code' not in request.args:
            return None, None, None

        oauth_session = self.service.get_auth_session(
            data={
                'code': request.args['code'],
                'grant_type': 'authorization_code',
                'redirect_uri': self.get_callback_url()
            },
            decoder=json.loads
        )

        me = oauth_session.get('').json()
        return ('google$' + me['sub'], me['name'], me['email'], me['picture'])

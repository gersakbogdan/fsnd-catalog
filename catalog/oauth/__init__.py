from rauth import OAuth2Service
from flask import current_app, url_for, redirect, request

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

        me = oauth_session.get('me?fields=name,id,email').json()
        return ('facebook$' + me['id'], me.get('name'), me.get('email'))

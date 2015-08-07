import datetime
from authomatic import core
from authomatic.providers.oauth2 import OAuth2, PROVIDER_ID_MAP


class Instagram(OAuth2):
    """
    Instagram |oauth2| provider.

    """
    user_authorization_url = 'https://instagram.com/oauth/authorize'
    access_token_url = 'https://instagram.com/oauth/access_token'
    user_info_url = 'https://api.instagram.com/v1/users/self'
    same_origin = False

    supported_user_attributes = core.SupportedUserAttributes(
        id=True,
        name=True,
        picture=True,
        nickname=True,
    )

    def __init__(self, *args, **kwargs):
        super(Instagram, self).__init__(*args, **kwargs)

        if self.popup:
            self.user_authorization_url += '?display=popup'


    @staticmethod
    def _x_user_parser(user, data):
        if "data" in data:
            data = data['data']
        user.picture = data.get("profile_picture")
        user.nickname = data.get("username")
        user.id = data.get("id")
        user.name = data.get('full_name')
        return user


    @staticmethod
    def _x_refresh_credentials_if(credentials):
        return True

    def _x_scope_parser(self, scope):
        return ' '.join(scope) if scope else ''


PROVIDER_ID_MAP += [Instagram, ]
from authomatic.providers import oauth2, oauth1
import providers

CONFIG = {

    'tw': {
        'class_': oauth1.Twitter,
        'consumer_key': 'DEcOUhlz3xKFmrP42BUHlsf0Q',
        'consumer_secret': 'vYkk2fM5YlByAxizCxxymcYndCRJZItbjXTOoa7t9smGDRcclJ',
    },

    'fb': {
        'class_': oauth2.Facebook,
        'consumer_key': '1483307331966597',
        'consumer_secret': '2d64be58c66714dc89df32cc8e289018',
        'scope': ['public_profile', 'email', 'user_friends'],
    },

    'linkedin': {
        'class_': oauth2.LinkedIn,
        'consumer_key': '771ffgzstsv4kh',
        'consumer_secret': 'D0gKcvqZK1RXW4XV',
        'scope': ['r_basicprofile',],
    },

    'instagram': {
        'class_': providers.Instagram,
        'consumer_key': '47226506dde246b1acefd1d3bcc6937f',
        'consumer_secret': '0b5810c090c0450ea2578a7624ff0b0c',
        'scope': ['basic', 'relationships'],
    },
}
from main import mongo


def find_mutual_friends(provider, user_id):
    url = get_access_url(provider, user_id)
    response = provider.access(url)
    if response.status == 200:
        return search_mutual_friends(provider, response.data)
    return []


def get_access_url(provider, user_id):
    return {
        'fb': _find_fb_friends_url,
        'tw': _find_tw_friends_url,
        'instagram': _find_insta_friends_url,
        'linkedin': _find_link_friends_url,
    }.get(provider.name, lambda x: "")(user_id)


def search_mutual_friends(provider, data):
    friends_ids = {
        'fb': _search_fb_friends,
        'tw': _search_tw_friends,
        'instagram': _search_insta_friends,
    }.get(provider.name, lambda x: "")(data)
    if provider.name == 'fb':
        return friends_ids
    else:
        return list(mongo.db.social_users.find(
            {"id": {"$in": friends_ids}, "provider": provider.name}).distinct("id"))


def _search_fb_friends(response_data):
    friends = []
    for friend_info in response_data['data']:
        friends += [friend_info['id']]
    return friends


def _search_tw_friends(response_data):
    return response_data['ids']


def _search_insta_friends(response_data):
    friends = []
    for friend_info in response_data['data']:
        friends += [friend_info['id']]
    return friends


def _find_fb_friends_url(user_id):
    return "https://graph.facebook.com/me/friends"


def _find_tw_friends_url(user_id):
    return "https://api.twitter.com/1.1/followers/ids.json?user_id={}&count=5".format(user_id)


def _find_link_friends_url(user_id):
    # WORKS IF HAVE "r_network" scope permission
    return "https://api.linkedin.com/v1/people/id={}/connections".format(user_id)


def _find_insta_friends_url(user_id):
    return "https://api.instagram.com/v1/users/{}/follows".format(user_id)
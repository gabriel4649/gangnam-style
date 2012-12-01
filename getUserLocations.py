#!/usr/bin/python

import twitter, codecs, sys, pickle

sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

try:
    # read python dict back from the file
    pkl_file = open('tweet_user_data.pkl', 'rb')
    users = pickle.load(pkl_file)
    pkl_file.close()

except:
    users = {}    

usernames = sys.stdin.readlines()
api = twitter.Api()

for idx, username in enumerate(usernames):
    if username in users:
        continue

    try:
        user = api.GetUser(username[:-1])
    except:
        print "Quouta is finished at user# " + str(idx)
        break

    attributes = {}
    attributes['name'] = user.name
    attributes['id'] = user.id
    attributes['location'] = user.location
    attributes['description'] = user.description
    attributes['profile_image_url'] = user.profile_image_url
    attributes['profile_background_tile'] = user.profile_background_tile
    attributes['profile_background_image_url'] = user.profile_background_image_url
    attributes['profile_sidebar_fill_color'] = user.profile_sidebar_fill_color
    attributes['profile_background_color'] = user.profile_background_color
    attributes['profile_link_color'] = user.profile_link_color
    attributes['profile_text_color'] = user.profile_text_color
    attributes['protected'] = user.protected
    attributes['utc_offset'] = user.utc_offset
    attributes['time_zone'] = user.time_zone
    attributes['url'] = user.url
    attributes['status'] = user.status
    attributes['statuses_count'] = user.statuses_count
    attributes['followers_count'] = user.followers_count
    attributes['friends_count'] = user.friends_count
    attributes['favourites_count'] = user.favourites_count
    users[username] = attributes

# write python dict to a file
output = open('tweet_user_data.pkl', 'wb')
pickle.dump(users, output)
output.close()

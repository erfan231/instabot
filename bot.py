import json
from instapy import InstaPy
import random


tags = ["cybersecurity", "coding", "hacking", "pythonprogramming", "kali_linux","linux", "hacker", "hackingnews", "growthhackking", "programming", "computerscience"]
rand_tag = random.shuffle(tags)

with open("./credentials.json") as file:
    config = json.load(file)

session = InstaPy(username=config.get("username"), password=config.get("password"), headless_browser=False)
# headless browser = true implies that it will work in background without opening browser

session.login()


session.set_quota_supervisor(enabled=True, sleep_after=["likes_d", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                            peak_likes_hourly=57,
                            peak_likes_daily=585,
                            peak_comments_hourly=31,
                            peak_comments_daily=182,
                            peak_follows_hourly=48,
                            peak_follows_daily=166,
                            peak_unfollows_hourly=35,
                            peak_unfollows_daily=402,
                            peak_server_calls_hourly=None,
                            peak_server_calls_daily=4700)

session.set_dont_like(["naked", "sex"])
#will unfollow 12 of your not fllowing back
session.set_do_like(enabled=True, percentage=100)

# comment on specefic media types (photos/vids)
session.set_comments(["great post!", "nice content"])

# comment section
session.set_do_comment(enabled=True, percentage=100)
session.set_do_follow(enabled=True, percentage=100, times=2)

session.set_skip_users(skip_private=True,
                       skip_business=True,
                       business_percentage=100)

session.unfollow_users(amount=112, nonFollowers=True, style="RANDOM", unfollow_after=None, sleep_delay=30)

# like section (Chnage tags here)
session.like_by_tags(tags, amount=9)

session.end()

"""
Follow someone else's followers

#Follows the followers of each given user
# The usernames can be either a list or a string
# The amount is for each account, in this case 30 users will be followed
# If randomize is false it will pick in a top-down fashion

session.follow_user_followers(['friend1', 'friend2', 'friend3'], amount=10, randomize=False)

# default sleep_delay=600 (10min) for every 10 user following, in this case
# sleep for 60 seconds

session.follow_user_followers(['friend1', 'friend2', 'friend3'], amount=10, randomize=False, sleep_delay=60)
"""

"""
Follow the likers of photos of users#
This will follow the people those liked photos of given list of users#

session.follow_likers(['user1' , 'user2'], photos_grab_amount = 2, follow_likers_per_photo = 3, randomize=True, sleep_delay=600, interact=False)
"""




# more cool codes
# https://instapy.org/actions/
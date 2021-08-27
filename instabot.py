from instapy import InstaPy

session = InstaPy(username = "USERNAME", password = "PASSWORD")
session.login()

session.set_relationship_bounds(enabled = False, max_followers = 900) #True

session.set_do_follow(False, percentage=100) #True
session.like_by_tags(["gamergirl", "girlgamer", "like4likes", "follow4likes", "feminism", "girlpower", "follow4follow"], amount = 6)
#session.set_dont_like(["nsfw"])

#session.unfollow_users(amount=6, allFollowing=True, sleep_delay=60)

session.end

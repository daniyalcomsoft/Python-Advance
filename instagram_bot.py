from instabot import Bot

bot=Bot()
bot.login(username="", password="")

# if you want to follow someone 
bot.follow('seavycloudinc')

# if we want to upload a photo
bot.upload_photo("", caption="I love Python")

# if you want to unfollow a person 
bot.unfollow("seavycloudinc")

# if you want to send multiple messages
bot.send_message("everyone love python", ["daniyalakhtar22", "cloudseavyinc"])

# if you want to check followers or follorwing 
followers=bot.get_user_followers("seavycloudinc")
for f in followers:
    print(bot.get_user_info(f))
following=bot.get_user_following("seavycloudinc")
for f in following:
    print(bot.get_user_info(f))


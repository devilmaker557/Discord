# REDDIT
from discord.ext import commands
from src.commands.Reddit.post_from_subreddit import RedditBot


class RedditCog(commands.Cog):
    """
    Cog for reddit class, searches for certain results on reddit using the praw library
    """

    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def rsearch(self, ctx):
        """
        Top post from reddit search
        Prohibits nsfw posts from appearing in non-nsfw channels
        :param ctx: the full discord message from the user as a Context class from Discord.py
        :return:None
        """
        message = ctx.message
        topic = " ".join(ctx.message.content.split()[1:])
        is_nsfw, url = RedditBot().search_first_topic(topic)
        if message.channel.is_nsfw():
            try:
                await message.channel.send(url)
            except Exception:
                await message.channel.send("Not found")
        else:
            if not is_nsfw:
                await message.channel.send(url)
            else:
                await message.add_reaction(self.client.get_emoji(521430118502236160))

    @commands.command()
    async def rrand(self, ctx):
        """
        Random search result from a subreddit
        :param ctx: the full discord message from the user as a Context class from Discord.py
        :return: None
        """
        message = ctx.message

        subreddit = ctx.message.content.split()[1]
        is_nsfw, url = RedditBot().random_post_sub(subreddit)
        if message.channel.is_nsfw():
            try:
                await message.channel.send(url)
            except Exception:
                await message.channel.send("Not found")
        else:
            if not is_nsfw:
                await message.channel.send(url)
            else:
                await message.add_reaction(self.client.get_emoji(521430118502236160))

    @commands.command()
    async def rtop(self, ctx):
        """
        Top post from hot of subreddit
        :param ctx: the full discord message from the user as a Context class from Discord.py
        :return: None
        """
        message = ctx.message
        subreddit = ctx.message.content.split()[1]
        is_nsfw, url = RedditBot().top_post_subreddit(subreddit)
        if message.channel.is_nsfw():
            try:
                await message.channel.send(url)
            except Exception:
                await message.channel.send("Not found")
        else:
            if not is_nsfw:
                await message.channel.send(url)
            else:
                await message.add_reaction(self.client.get_emoji(521430118502236160))
                await message.add_reaction(self.client.get_emoji(521430137724731392))

    @commands.command()
    async def rrsearch(self, ctx):
        """
        Random post from search results
        :param ctx: the full discord message from the user as a Context class from Discord.py
        :return: None
        """
        message = ctx.message

        topic = " ".join(ctx.message.content.split()[1:])
        is_nsfw, url = RedditBot().search_topic_random(topic)
        if message.channel.is_nsfw():
            try:
                await message.channel.send(url)
            except Exception:
                await message.channel.send("Not found")
        else:
            if not is_nsfw:
                await message.channel.send(url)
            else:
                await message.add_reaction(self.client.get_emoji(521430118502236160))

    @commands.command()
    async def rbon(self, ctx):
        """
        Best Of N from a subreddit
        :param ctx: the full discord message from the user as a Context class from Discord.py
        :return: None
        """
        message = ctx.message
        subreddit = ctx.message.content.split()[1]
        try:
            number = int(ctx.message.content.split()[2])
        except IndexError:
            number = 3
        is_nsfw, urls = RedditBot().top_x_posts(subreddit, number)
        if urls == -1:
            await message.channel.send("Max limit is 5!")
            return
        if message.channel.is_nsfw():
            try:
                await message.channel.send(urls)
            except Exception:
                await message.channel.send("Not found")
        else:
            if not is_nsfw:
                await message.channel.send(urls)
            else:
                await message.add_reaction(self.client.get_emoji(521430118502236160))
                await message.add_reaction(self.client.get_emoji(521430137724731392))


def setup(bot):
    bot.add_cog(RedditCog(bot))

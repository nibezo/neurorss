from telegram.ext import *
import Constants as keys

print("Start..")


def make_msg(article_name, description, article_link, rss_from, msg):
    """Make message design."""
    msg = article_name + "\n" + "\n" + description + "\n" + "\n" + rss_from + "\n" + article_link
    return msg


def post_msg():
    """

    Post one message on the channel.

    """
    updater = Updater(keys.API_KEY, use_context=True)
    updater.bot.send_message('@neurorss',
                             make_msg(keys.article_name, keys.description, keys.article_link, keys.rss_from,
                                      keys.msg), disable_notification=True, parse_mode="Markdown")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    post_msg()  # Post one message on the channel

    updater.start_polling()
    updater.idle()


main()

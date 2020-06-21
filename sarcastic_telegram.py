import logging
from uuid import uuid4

from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.utils.helpers import escape_markdown


def start(update, context):
    update.message.reply_text('Hi! Welcome to Sarcastic bot!')


def help_command(update, context):
    update.message.reply_text('Help!')


def sarcastic_text(msg):
    result = ''
    for i in range(len(msg)):
        if i % 2 == 0:
            result = result + msg[i].lower()
        else:
            result = result + msg[i].upper()

    return result


def sarcastic_text_reversed(msg):
    result = ''
    for i in range(len(msg)):
        if i % 2 == 0:
            result = result + msg[i].upper()
        else:
            result = result + msg[i].lower()

    return result


def inlinequery(update, context):
    query = update.inline_query.query
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title="Caps",
            input_message_content=InputTextMessageContent(
                query.upper())),

        InlineQueryResultArticle(
            id=uuid4(),
            title="Bold",
            input_message_content=InputTextMessageContent(
                "*{}*".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN)),

        InlineQueryResultArticle(
            id=uuid4(),
            title="Italic",
            input_message_content=InputTextMessageContent(
                "_{}_".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN)),

        InlineQueryResultArticle(
            id=uuid4(),
            title="Sarcasm",
            input_message_content=InputTextMessageContent(
                "{}".format(sarcastic_text(query)),
                parse_mode=ParseMode.MARKDOWN)),

        InlineQueryResultArticle(
            id=uuid4(),
            title="Sarcasm Reversed",
            input_message_content=InputTextMessageContent(
                "{}".format(sarcastic_text_reversed(query)),
                parse_mode=ParseMode.MARKDOWN)),

    ]

    update.inline_query.answer(results)


def main():
    updater = Updater("1255069464:AAEQy1ubd-zYVErItgnWkIJqCT14NYMXFCY", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(InlineQueryHandler(inlinequery))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

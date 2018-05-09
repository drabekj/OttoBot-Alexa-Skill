REQUEST_LAUNCH_MSG = "Hello, I'm Otto Investment bot, I' here to inform you about your investments. Do you want me to tell you a report on your portfolio? Or maybe information about specific stock? "
REQUEST_LAUNCH_REPROMPT = "Go on, tell me what can I do for you."

REQUEST_END_MSG = "Bye bye. "

# General
INTENT_GENERAL_OK = "Ok then."
INTENT_GENERAL_REPROMPT = "Is there something else I can help you with?"

# Price
INTENT_STOCK_PRICE_MSG = "The price of {0} is ${1}."
INTENT_STOCK_PRICE_MSG_FAIL = "Sorry, there was a problem getting data for {}"

# Watchlist
INTENT_WATCHLIST_REPORT_MSG_INTRO = "Here is your watchlist:"
INTENT_WATCHLIST_REPORT_MSG_BODY = " Stock {} is {} {:.2f}%. "
INTENT_WATCHLIST_EMPTY_MSG = "Your watchlist is empty. "

INTENT_ADD_TO_WATCHLIST_ASK_CONFIRMATION = "Should I add stock {}? "
INTENT_ADD_TO_WATCHLIST_DENIED = "Ok, not adding it. "
INTENT_ADD_TO_WATCHLIST_CONFIRMED = "Ok, adding {} to watchlist. "
INTENT_ADDED_TO_WATCHLIST = "Stock {} was added to watchlist. "
INTENT_ADDED_TO_WATCHLIST_EXISTS = "Stock {} is already in your watchlist. "
INTENT_ADDED_TO_WATCHLIST_FAIL = "Couldn't add stock to watchlist. "

INTENT_REMOVE_FROM_WATCHLIST_ASK_CONFIRMATION = "Should I remove {}? "
INTENT_REMOVE_FROM_WATCHLIST_DENIED = "Ok, not removing it. "
INTENT_REMOVE_FROM_WATCHLIST_CONFIRMED = "Ok, removing {} from watchlist. "
INTENT_REMOVE_FROM_WATCHLIST_NOT_THERE = "There is no stock {} in your watchlist. "
INTENT_REMOVE_FROM_WATCHLIST_FAIL = "Couldn't remove stock from watchlist. "

# Education
INTENT_EDU_IN_CONSTRUCTION = "Can't explain {} right now."

# News
INTENT_NEWS_ABOUT_COMPANY_INTRO = "Here are some articles mentioning {}: "
INTENT_NEWS_ABOUT_COMPANY_ASK_MORE_INFO = "Should I send you a link to one of the articles? "
INTENT_NEWS_ABOUT_COMPANY_ASK_ARTICLE_NO = "Which one? "
INTENT_NEWS_ABOUT_COMPANY_FAIL_ARTICLE_NOT_FOUND = "Sorry, couldn't find this article. "
INTENT_NEWS_ABOUT_COMPANY_ARTICLE_SENT = "Article was sent to your device. "
INTENT_NEWS_ABOUT_COMPANY_ARTICLE_CARD_TITLE = "Article about {}"
INTENT_NEWS_ABOUT_COMPANY_ARTICLE_CARD_CONTENT = "{}"

# Error states
ERROR_NOT_AUTHENTICATED = "First you need to authenticate in the Alexa App."
ERROR_NOT_AUTHENTICATED_REPROMPT = "Please go to the Alexa App and link your Facebook account to use this feature."
ERROR_CANT_ADD_TO_WATCHLIST = "Sorry, I wasn't able to add stock {} to watchlist."

REQUEST_LAUNCH_MSG = "Hey, I'm Otto Investment bot, I' here to inform you about your investments. Do you want me to tell you a report on your portfolio? Or maybe information about specific stock? "
REQUEST_LAUNCH_REPROMPT = "Go on, tell me what can I do for you."

REQUEST_END_MSG = "Bye bye. "

INTENT_STOCK_PRICE_MSG = "The price of {0} is ${1}."
INTENT_STOCK_PRICE_MSG_FAIL = "Sorry, there was a problem getting data for {}"

# Watchlist
INTENT_WATCHLIST_REPORT_MSG_INTRO = "Here is your watchlist:"
INTENT_WATCHLIST_REPORT_MSG_BODY = " stock {} is valued at ${}"
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

INTENT_GENERAL_REPROMPT = "Is there something else I can help you with?"

# Error states
ERROR_NOT_AUTHENTICATED = "First you need to authenticate in the Alexa App."
ERROR_NOT_AUTHENTICATED_REPROMPT = "Please go to the Alexa App and link your Facebook account to use this feature."

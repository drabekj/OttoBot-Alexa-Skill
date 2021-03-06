REQUEST_LAUNCH_MSG = "Hello, I'm Otto Investment bot, I' here to inform you about your investments. Do you want me to tell you a report on your portfolio? Or maybe information about specific stock? "
REQUEST_LAUNCH_REPROMPT = "Go on, tell me what can I do for you."

REQUEST_END_MSG = "Bye bye. "

# General
INTENT_GENERAL_OK = "Ok then."
INTENT_GENERAL_REPROMPT = "Is there something else I can help you with?"

# Help
INTENT_HELP = "Looks like you are confused. You can ask about a stock price, market cap of a company, add and remove stocks from virtual portfolio. Get a performance report on your portfolio. You can also get an investing term explained or a investing strategy. You can even ask bout the news regarding a traded company. What would like to do?"

# Price
INTENT_STOCK_PRICE_MSG = "The price of {0} is ${1}."
INTENT_STOCK_PRICE_MSG_FAIL = "Sorry, there was a problem getting data for {}"

# Market Cap
INTENT_MARKET_CAP_MSG = "The Market Cap of {0} is ${1}."
INTENT_MARKET_CAP_MSG_FAIL = "Sorry, there was a problem getting market capitalization for {}"

# Investing Strategy
INTENT_INVEST_STRAT_MSG = "Here is a example of investing strategy, this one is called {}. {}"

# Watchlist
INTENT_WATCHLIST_REPORT_TOP_STOCK = "The best performing stock is {} which is {} {:.2f}%. "
INTENT_WATCHLIST_REPORT_WORST_STOCK = "The worst performing stock is {} which is {} {:.2f}%. "
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

# Analytics recommendation
INTENT_RCMD_NO_RCMD = "There is no analyst recommendation for this stock."
INTENT_RCMD_STRONG_BUY = "The analysts are strongly suggesting to buy this stock."
INTENT_RCMD_BUY = "The analysts are suggesting to consider buying this stock."
INTENT_RCMD_OPT_HOLD = "The analysts are somewhat optimistic, they are torn between holding or even buying this stock."
INTENT_RCMD_HOLD = "The analysts suggest not making any decisions just yet, you should hold to this stock."
INTENT_RCMD_PES_HOLD = "The analysts are worried about this one, they suggest holding, whit some intentions to selling."
INTENT_RCMD_SELL = "The stock has been underperforming, analysts suggest considering selling."
INTENT_RCMD_STRONG_SELL = "The analysts strongly suggest selling this stock."

# Error states
ERROR_NOT_AUTHENTICATED = "First you need to authenticate in the Alexa App."
ERROR_NOT_AUTHENTICATED_REPROMPT = "Please go to the Alexa App and link your Facebook account to use this feature."
ERROR_CANT_ADD_TO_WATCHLIST = "Sorry, I wasn't able to add stock {} to watchlist."
ERROR_NEWS_BAD_TICKER = "Sorry it is not possible to get news for this company."
ERROR_NEWS_NO_NEWS = "Sorry, there are now news for company {}"
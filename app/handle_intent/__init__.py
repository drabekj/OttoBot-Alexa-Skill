import app.intent_stock_price as intent_stock
from app import intent_watchlist
from app.utils.MyError import UnknownIntentError


def handle_intent(request):
    intent_name = request.intent_name()

    if intent_name == 'WhatsTheStockPriceIntent':
        return intent_stock.handle_get_stock_price_intent(request)
    elif intent_name == 'ReportStockWatchlistIntent':
        return intent_watchlist.handle_report_stock_watchlist(request)
    elif intent_name == 'AddStockToWatchlistIntent':
        return intent_watchlist.handle_add_to_watchlist(request)
    else:
        raise UnknownIntentError('Cant handle this type of intent: ' + intent_name)

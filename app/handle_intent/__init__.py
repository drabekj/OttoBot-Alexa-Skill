import app.intent_stock_price as intent_stock
from app import intent_watchlist


def handle_intent(request):
    intent_name = request.intent_name()
    print("LOG-i: WhatsTheStockPriceIntent")

    if intent_name == 'WhatsTheStockPriceIntent':
        return intent_stock.handle_get_stock_price_intent(request)
    elif intent_name == 'ReportStockWatchlistIntent':
        return intent_watchlist.handle_report_stock_watchlist(request)
    else:
        raise KeyError('Cant handle this type of intent: ' + intent_name)

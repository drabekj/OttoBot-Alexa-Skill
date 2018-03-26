import app.intent_stock_price as intent_stock
from app import handle_end
from app.intent_education import handle_education
from app.intent_news import handle_news
from app.intent_watchlist.add import handle_add_to_watchlist
from app.intent_watchlist.remove import handle_remove_from_watchlist
from app.intent_watchlist.report import handle_report_stock_watchlist
from app.utils.MyError import UnknownIntentError


def handle_intent(request):
    intent_name = request.intent_name()

    if intent_name == 'WhatsTheStockPriceIntent':
        return intent_stock.handle_get_stock_price_intent(request)
    elif intent_name == 'ReportStockWatchlistIntent':
        return handle_report_stock_watchlist(request)
    elif intent_name == 'AddStockToWatchlistIntent':
        return handle_add_to_watchlist(request)
    elif intent_name == 'RemoveStockFromWatchlistIntent':
        return handle_remove_from_watchlist(request)
    elif intent_name == 'EducateIntent':
        return handle_education(request)
    elif intent_name == 'NewsAboutCompanyIntent':
        return handle_news(request)
    elif intent_name == 'AMAZON.StopIntent':
        return handle_end(request)
    else:
        raise UnknownIntentError('Cant handle this type of intent: ' + intent_name)

from app.intent_stock_price import handle_get_stock_price_intent


def handle_intent(request):
    intent_name = request.intent_name()
    print("i-LOG: WhatsTheStockPriceIntent")

    try:
        return {
            'WhatsTheStockPriceIntent': handle_get_stock_price_intent(request),
        }[intent_name]
    except KeyError as error:
        raise

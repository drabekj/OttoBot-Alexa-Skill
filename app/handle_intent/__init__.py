import app.intent_stock_price as intent_stock


def handle_intent(request):
    intent_name = request.intent_name()
    print("LOG-i: WhatsTheStockPriceIntent")

    try:
        return {
            'WhatsTheStockPriceIntent':
                intent_stock.handle_get_stock_price_intent(request),
        }[intent_name]
    except KeyError as error:
        raise

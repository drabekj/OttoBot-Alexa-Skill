from datetime import date

from static.strings import *

# Test data values
test_stock_1_ticker = "TSLA"
test_stock_1_date = date(2018, 1, 1)
test_stock_1_close = 333.33

test_stock_2_ticker = "IBM"
test_stock_2_date = date(2018, 1, 1)
test_stock_2_close = 159.22

test_user_id = 2003646219648973
test_user_name = "John"

test_add_stock = "AMZN"


def launch_request():
    return {
        'session': {
            'new': True,
            'sessionId': 'SessionId.3bff8921-b907-4dc7-964e-04a67fc2c1e3',
            'application': {
                'applicationId': 'amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96'
            },
            'attributes': {},
            'user': {
                'accessToken': 'EAAdvSgyprPcBAGWGAKsr03UddHlyX6JiqV9v7aAvGxfNBRNAKCAfrJ6uDD4ixxkX6TAWxZC9F6kTKS2edxg3cZBW9CZBQ1zuM8HKhPc45bIrC3OADEPGIKGm2i0o5eH3sa9p5c6QXrN1jdzYAW0vCAVBGZA1wDk3s7IrZAjVwXgZDZD',
                'userId': 'amzn1.ask.account.AE7YEGFRUCUT2J24CYPQUWILRXKBRID4L7ZDK2GRZD6DOHYLKE4X6TFZMNYHYSVOU546M7OS6PQWYX6APXGBKIF4WMRB4YACKZZMB63XNAKOQ35VS7SUPME33JJ7V3EJDZLDARVNRUTVOGMSIDWJHKRYSXT2XDUYVPRD6URE3OOGSFM4MWSFMOPTELRTGBB6E6PKWRCBI3PGDGY'
            }
        },
        'request': {
            'type': 'LaunchRequest',
            'requestId': 'EdwRequestId.2fae8fcb-e14f-4bdf-a1c1-0f85354ccaad',
            'locale': 'en-US',
            'timestamp': '2017-10-10T11:10:25Z'
        },
        'context': {
            'AudioPlayer': {
                'playerActivity': 'IDLE'
            },
            'System': {
                'application': {
                    'applicationId': 'amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96'
                },
                'user': {
                    'userId': 'amzn1.ask.account.AE7YEGFRUCUT2J24CYPQUWILRXKBRID4L7ZDK2GRZD6DOHYLKE4X6TFZMNYHYSVOU546M7OS6PQWYX6APXGBKIF4WMRB4YACKZZMB63XNAKOQ35VS7SUPME33JJ7V3EJDZLDARVNRUTVOGMSIDWJHKRYSXT2XDUYVPRD6URE3OOGSFM4MWSFMOPTELRTGBB6E6PKWRCBI3PGDGY'
                },
                'device': {
                    'supportedInterfaces': {}
                }
            }
        },
        'version': '1.0'
    }


def intent_request_get_stock_price():
    return {
        "session": {
            "new": True,
            "sessionId": "SessionId.3bff8921-b907-4dc7-964e-04a67fc2c1e3",
            "application": {
                "applicationId": "amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96"
            },
            "attributes": {
                "userName": "John"
            },
            "user": {
                "accessToken": "EAAdvSgyprPcBAGWGAKsr03UddHlyX6JiqV9v7aAvGxfNBRNAKCAfrJ6uDD4ixxkX6TAWxZC9F6kTKS2edxg3cZBW9CZBQ1zuM8HKhPc45bIrC3OADEPGIKGm2i0o5eH3sa9p5c6QXrN1jdzYAW0vCAVBGZA1wDk3s7IrZAjVwXgZDZD",
                "userId": "amzn1.ask.account.AE7YEGFRUCUT2J24CYPQUWILRXKBRID4L7ZDK2GRZD6DOHYLKE4X6TFZMNYHYSVOU546M7OS6PQWYX6APXGBKIF4WMRB4YACKZZMB63XNAKOQ35VS7SUPME33JJ7V3EJDZLDARVNRUTVOGMSIDWJHKRYSXT2XDUYVPRD6URE3OOGSFM4MWSFMOPTELRTGBB6E6PKWRCBI3PGDGY"
            }
        },
        "request": {
            "type": "IntentRequest",
            "requestId": "EdwRequestId.9b507a59-af84-4f5e-b1e3-54eb7d317fa9",
            "intent": {
                "name": "WhatsTheStockPriceIntent",
                "slots": {
                    "stockTicker": {
                        "name": "stockTicker",
                        "value": "tsla"
                    }
                }
            },
            "locale": "en-US",
            "timestamp": "2017-09-21T12:28:08Z"
        },
        "context": {
            "AudioPlayer": {
                "playerActivity": "IDLE"
            },
            "System": {
                "application": {
                    "applicationId": "amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96"
                },
                "user": {
                    "userId": "amzn1.ask.account.AE7YEGFRUCUT2J24CYPQUWILRXKBRID4L7ZDK2GRZD6DOHYLKE4X6TFZMNYHYSVOU546M7OS6PQWYX6APXGBKIF4WMRB4YACKZZMB63XNAKOQ35VS7SUPME33JJ7V3EJDZLDARVNRUTVOGMSIDWJHKRYSXT2XDUYVPRD6URE3OOGSFM4MWSFMOPTELRTGBB6E6PKWRCBI3PGDGY"
                },
                "device": {
                    "supportedInterfaces": {}
                }
            }
        },
        "version": "1.0"
    }


RESPONSE_intent_request_get_stock_price = INTENT_STOCK_PRICE_MSG \
    .format(test_stock_1_ticker, test_stock_1_close)


def intent_report_watchlist():
    return {
        "session": {
            "new": False,
            "sessionId": "SessionId.3bff8921-b907-4dc7-964e-04a67fc2c1e3",
            "application": {
                "applicationId": "amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96"
            },
            "attributes": {
                "userName": test_user_name,
                "userId": test_user_id
            },
            "user": {
                "accessToken": "EAAdvSgyprPcBAGWGAKsr03UddHlyX6JiqV9v7aAvGxfNBRNAKCAfrJ6uDD4ixxkX6TAWxZC9F6kTKS2edxg3cZBW9CZBQ1zuM8HKhPc45bIrC3OADEPGIKGm2i0o5eH3sa9p5c6QXrN1jdzYAW0vCAVBGZA1wDk3s7IrZAjVwXgZDZD",
                "userId": "amzn1.ask.account.AE7YEGFRUCUT2J24CYPQUWILRXKBRID4L7ZDK2GRZD6DOHYLKE4X6TFZMNYHYSVOU546M7OS6PQWYX6APXGBKIF4WMRB4YACKZZMB63XNAKOQ35VS7SUPME33JJ7V3EJDZLDARVNRUTVOGMSIDWJHKRYSXT2XDUYVPRD6URE3OOGSFM4MWSFMOPTELRTGBB6E6PKWRCBI3PGDGY"
            }
        },
        "request": {
            "type": "IntentRequest",
            "requestId": "EdwRequestId.14d6a81a-28b1-4e19-9505-ac16e540ea5e",
            "intent": {
                "name": "ReportStockWatchlistIntent",
                "slots": {}
            },
            "locale": "en-US",
            "timestamp": "2017-11-09T13:22:55Z"
        },
        "context": {
            "AudioPlayer": {
                "playerActivity": "IDLE"
            },
            "System": {
                "application": {
                    "applicationId": "amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96"
                },
                "user": {
                    "userId": "amzn1.ask.account.AE7YEGFRUCUT2J24CYPQUWILRXKBRID4L7ZDK2GRZD6DOHYLKE4X6TFZMNYHYSVOU546M7OS6PQWYX6APXGBKIF4WMRB4YACKZZMB63XNAKOQ35VS7SUPME33JJ7V3EJDZLDARVNRUTVOGMSIDWJHKRYSXT2XDUYVPRD6URE3OOGSFM4MWSFMOPTELRTGBB6E6PKWRCBI3PGDGY"
                },
                "device": {
                    "supportedInterfaces": {}
                }
            }
        },
        "version": "1.0"
    }


RESPONSE_intent_report_watchlist = INTENT_WATCHLIST_REPORT_MSG_INTRO \
                                   + INTENT_WATCHLIST_REPORT_MSG_BODY.format(
    test_stock_1_ticker, test_stock_1_close) \
                                   + INTENT_WATCHLIST_REPORT_MSG_BODY.format(
    test_stock_2_ticker, test_stock_2_close)

RESPONSE_intent_report_empty_watchlist = INTENT_WATCHLIST_EMPTY_MSG


def intent_report_watchlist_not_authenticated():
    return {
        "session": {
            "new": False,
            "sessionId": "SessionId.3bff8921-b907-4dc7-964e-04a67fc2c1e3",
            "application": {
                "applicationId": "amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96"
            },
            "attributes": {
                "userName": "John",
                "stockTicker": "IBM"
            },
            "user": {
                "userId": "amzn1.ask.account.AE7YEGFRUCUT2J24CYPQUWILRXKBRID4L7ZDK2GRZD6DOHYLKE4X6TFZMNYHYSVOU546M7OS6PQWYX6APXGBKIF4WMRB4YACKZZMB63XNAKOQ35VS7SUPME33JJ7V3EJDZLDARVNRUTVOGMSIDWJHKRYSXT2XDUYVPRD6URE3OOGSFM4MWSFMOPTELRTGBB6E6PKWRCBI3PGDGY"
            }
        },
        "request": {
            "type": "IntentRequest",
            "requestId": "EdwRequestId.14d6a81a-28b1-4e19-9505-ac16e540ea5e",
            "intent": {
                "name": "ReportStockWatchlistIntent",
                "slots": {}
            },
            "locale": "en-US",
            "timestamp": "2017-11-09T13:22:55Z"
        },
        "context": {
            "AudioPlayer": {
                "playerActivity": "IDLE"
            },
            "System": {
                "application": {
                    "applicationId": "amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96"
                },
                "user": {
                    "userId": "amzn1.ask.account.AE7YEGFRUCUT2J24CYPQUWILRXKBRID4L7ZDK2GRZD6DOHYLKE4X6TFZMNYHYSVOU546M7OS6PQWYX6APXGBKIF4WMRB4YACKZZMB63XNAKOQ35VS7SUPME33JJ7V3EJDZLDARVNRUTVOGMSIDWJHKRYSXT2XDUYVPRD6URE3OOGSFM4MWSFMOPTELRTGBB6E6PKWRCBI3PGDGY"
                },
                "device": {
                    "supportedInterfaces": {}
                }
            }
        },
        "version": "1.0"
    }


RESPONSE_intent_report_watchlist_not_authenticated = ERROR_NOT_AUTHENTICATED


def intent_add_to_watchlist():
    return {
        "session": {
            "new": False,
            "sessionId": "SessionId.3bff8921-b907-4dc7-964e-04a67fc2c1e3",
            "application": {
                "applicationId": "amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96"
            },
            "attributes": {
                "userName": test_user_name,
                "userId": test_user_id,
                "stockTicker": test_add_stock
            },
            "user": {
                'accessToken': 'EAAdvSgyprPcBAGWGAKsr03UddHlyX6JiqV9v7aAvGxfNBRNAKCAfrJ6uDD4ixxkX6TAWxZC9F6kTKS2edxg3cZBW9CZBQ1zuM8HKhPc45bIrC3OADEPGIKGm2i0o5eH3sa9p5c6QXrN1jdzYAW0vCAVBGZA1wDk3s7IrZAjVwXgZDZD',
                "userId": "amzn1.ask.account.AE7YEGFRUCUT2J24CYPQUWILRXKBRID4L7ZDK2GRZD6DOHYLKE4X6TFZMNYHYSVOU546M7OS6PQWYX6APXGBKIF4WMRB4YACKZZMB63XNAKOQ35VS7SUPME33JJ7V3EJDZLDARVNRUTVOGMSIDWJHKRYSXT2XDUYVPRD6URE3OOGSFM4MWSFMOPTELRTGBB6E6PKWRCBI3PGDGY"
            }
        },
        "request": {
            "type": "IntentRequest",
            "requestId": "EdwRequestId.14d6a81a-28b1-4e19-9505-ac16e540ea5e",
            "intent": {
                "name": "AddStockToWatchlistIntent",
                "slots": {
                    "stockTicker": {
                        "name": "stockTicker",
                        "value": test_add_stock
                    }
                }
            },
            "locale": "en-US",
            "timestamp": "2017-11-09T13:22:55Z"
        },
        "context": {
            "AudioPlayer": {
                "playerActivity": "IDLE"
            },
            "System": {
                "application": {
                    "applicationId": "amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96"
                },
                "user": {
                    "userId": "amzn1.ask.account.AE7YEGFRUCUT2J24CYPQUWILRXKBRID4L7ZDK2GRZD6DOHYLKE4X6TFZMNYHYSVOU546M7OS6PQWYX6APXGBKIF4WMRB4YACKZZMB63XNAKOQ35VS7SUPME33JJ7V3EJDZLDARVNRUTVOGMSIDWJHKRYSXT2XDUYVPRD6URE3OOGSFM4MWSFMOPTELRTGBB6E6PKWRCBI3PGDGY"
                },
                "device": {
                    "supportedInterfaces": {}
                }
            }
        },
        "version": "1.0"
    }


RESPONSE_intent_add_to_watchlist = INTENT_ADDED_TO_WATCHLIST \
    .format(test_add_stock)

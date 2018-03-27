from datetime import date

from static.strings import *

# Test data values
from static.strings_edu import TERM_EQUITY

test_stock_1_ticker = "TSLA"
test_stock_1_name = "Tesla"
test_stock_1_date_1 = date(2018, 1, 1)
test_stock_1_date = date(2018, 1, 2)
test_stock_1_close_1 = 333.33
test_stock_1_close = 344.44
test_stock_1_price_change = 3.23

test_stock_2_ticker = "IBM"
test_stock_2_name = "International Business Machines"
test_stock_2_date_1 = date(2018, 1, 1)
test_stock_2_date = date(2018, 1, 2)
test_stock_2_close_1 = 153.22
test_stock_2_close = 150.00
test_stock_2_price_change = 2.15

test_user_id = 2003646219648973
test_user_name = "John"
access_token = "EAAdvSgyprPcBAGWGAKsr03UddHlyX6JiqV9v7aAvGxfNBRNAKCAfrJ6uDD4ixxkX6TAWxZC9F6kTKS2edxg3cZBW9CZBQ1zuM8HKhPc45bIrC3OADEPGIKGm2i0o5eH3sa9p5c6QXrN1jdzYAW0vCAVBGZA1wDk3s7IrZAjVwXgZDZD"

test_add_stock = "AMZN"
test_add_company = "Amazon"


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
            "locale": "en-US",
            "timestamp": "2017-09-21T12:28:08Z",
            "intent": {
                "name": "WhatsTheStockPriceIntent",
                "confirmationStatus": "NONE",
                "slots": {
                    "stockTicker": {
                        "name": "stockTicker",
                        "value": "TSLA",
                        "resolutions": {
                            "resolutionsPerAuthority": [
                                {
                                    "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96.LIST_OF_TICKERS",
                                    "status": {
                                        "code": "ER_SUCCESS_MATCH"
                                    },
                                    "values": [
                                        {
                                            "value": {
                                                "name": "TSLA",
                                                "id": "ec367bc4f92cd97cec81bf7b43cffaf7"
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        "confirmationStatus": "NONE"
                    }
                }
            },
            "dialogState": "STARTED"
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
    test_stock_1_name, "up", test_stock_1_price_change) \
                                   + INTENT_WATCHLIST_REPORT_MSG_BODY.format(
    test_stock_2_name, "down", test_stock_2_price_change)

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
                "stockTicker": test_add_stock
            },
            "user": {
                "accessToken": access_token,
                "userId": "amzn1.ask.account.AE7YEGFRUCUT2J24CYPQUWILRXKBRID4L7ZDK2GRZD6DOHYLKE4X6TFZMNYHYSVOU546M7OS6PQWYX6APXGBKIF4WMRB4YACKZZMB63XNAKOQ35VS7SUPME33JJ7V3EJDZLDARVNRUTVOGMSIDWJHKRYSXT2XDUYVPRD6URE3OOGSFM4MWSFMOPTELRTGBB6E6PKWRCBI3PGDGY"
            }
        },
        "request": {
            "type": "IntentRequest",
            "requestId": "EdwRequestId.14d6a81a-28b1-4e19-9505-ac16e540ea5e",
            "locale": "en-US",
            "timestamp": "2017-11-09T13:22:55Z",
            "intent": {
                "name": "AddStockToWatchlistIntent",
                "confirmationStatus": "NONE",
                "slots": {
                    "stockTicker": {
                        "name": "stockTicker",
                        "confirmationStatus": "NONE"
                    }
                }
            },
            "dialogState": "STARTED"
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


RESPONSE_intent_add_to_watchlist_ask_confirmation = \
    INTENT_ADD_TO_WATCHLIST_ASK_CONFIRMATION.format(test_add_stock)


def intent_add_to_watchlist_deny():
    return {
        "version": "1.0",
        "session": {
            "new": False,
            "sessionId": "amzn1.echo-api.session.dd553fd1-97d1-4a04-8f45-6c3634c9dbd6",
            "application": {
                "applicationId": "amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96"
            },
            "attributes": {
                "stockTicker": test_add_stock,
                "userName": test_user_name,
                "userId": test_user_id
            },
            "user": {
                "userId": "amzn1.ask.account.AF64Z7P3TBODT4C6VB4SUJG67LSDJXMRPB4ZCN72Z5VSCFIS6COGQPHPPZCTUFCKYVNG37E56FUQHEHZQEMDEZHDP6EJ4ML6CZHBOKETG3TF44YRKRRIHUF4TMFMDKXSSPXBKW62LQVB4JNZ4NPGW5YMTRZZHNBFEYU7J4XF6MZPZRYA4KRS3ZKJHPHSKRB6ZOAHNXQ56T2HP7A",
                "accessToken": "EAAdvSgyprPcBAIKigdddcnZACP9WfbhiIPxTW1UHvW3sWu24S9AXNrbuzPWLoEIxxo8rQaqPZAZBCaHkr0gsTegIpTHIJNHQvQd59ABekEMNMB0xUgZBGJkZByydtZCT6yOwE4rMOg33t3TzO2j1SJFvqymbP1qEIfg5lGu1byUQZDZD"
            }
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
                    "userId": "amzn1.ask.account.AF64Z7P3TBODT4C6VB4SUJG67LSDJXMRPB4ZCN72Z5VSCFIS6COGQPHPPZCTUFCKYVNG37E56FUQHEHZQEMDEZHDP6EJ4ML6CZHBOKETG3TF44YRKRRIHUF4TMFMDKXSSPXBKW62LQVB4JNZ4NPGW5YMTRZZHNBFEYU7J4XF6MZPZRYA4KRS3ZKJHPHSKRB6ZOAHNXQ56T2HP7A",
                    "accessToken": access_token
                },
                "device": {
                    "deviceId": "amzn1.ask.device.AHDOK5CWXV4NE5TF26TG5TYEADGQ4A47BCE6FXG32QREQSAS66YFK2U6RAIUP3HOVVZSIRA3TV2DRQSYB7PX2HU37EXVILXGXKXVJBZENKWJJ2DBOFPASRBXWEWLTSJPB7FWFYDCV2S7KDLPTNSIYRAQG6UA",
                    "supportedInterfaces": {
                        "AudioPlayer": {}
                    }
                },
                "apiEndpoint": "https://api.amazonalexa.com",
                "apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLmRiYTEzNDZlLTVmNGEtNGY5ZS05ZDE0LWRjNjFkZDA4NGY5NiIsImV4cCI6MTUyMTU3MDgyNSwiaWF0IjoxNTIxNTY3MjI1LCJuYmYiOjE1MjE1NjcyMjUsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUhET0s1Q1dYVjRORTVURjI2VEc1VFlFQURHUTRBNDdCQ0U2RlhHMzJRUkVRU0FTNjZZRksyVTZSQUlVUDNIT1ZWWlNJUkEzVFYyRFJRU1lCN1BYMkhVMzdFWFZJTFhHWEtYVkpCWkVOS1dKSjJEQk9GUEFTUkJYV0VXTFRTSlBCN0ZXRllEQ1YyUzdLRExQVE5TSVlSQVFHNlVBIiwidXNlcklkIjoiYW16bjEuYXNrLmFjY291bnQuQUY2NFo3UDNUQk9EVDRDNlZCNFNVSkc2N0xTREpYTVJQQjRaQ043Mlo1VlNDRklTNkNPR1FQSFBQWkNUVUZDS1lWTkczN0U1NkZVUUhFSFpRRU1ERVpIRFA2RUo0TUw2Q1pIQk9LRVRHM1RGNDRZUktSUklIVUY0VE1GTURLWFNTUFhCS1c2MkxRVkI0Sk5aNE5QR1c1WU1UUlpaSE5CRkVZVTdKNFhGNk1aUFpSWUE0S1JTM1pLSkhQSFNLUkI2Wk9BSE5YUTU2VDJIUDdBIn19.ckoUTAg_lM6Gwz4Q4WakmZ0MvSc3Zt_pQCCNhBW1X1nY8LWqwkDtAeDL5OcgvwKLeDAkjk2_ct6m0kyHLI45wvfe9iOEgbIuqJjkMz9Y1cSnvLc_RRCzVi1POm5fYBX2jhjcruUXkMXae6-6XoU4NIs7I1xl-IUTAdTI8XKXscuDhNjs30uJb1gQ_Mxoj34woYOS7NgCFXuHKiGtoid5ro61c8HKar7mfhD5-SZ8Ki-8H2vpgiDKNAkh0Ys2Unsk2LNwY604zhkyzG17Be0wT7cbgJ8-vVdrbsDoqIvfJmnCF6M8WTDKbAvMzkCY87ATCzIZjTDr_hDRlqmBuMVNMw"
            }
        },
        "request": {
            "type": "IntentRequest",
            "requestId": "amzn1.echo-api.request.905dc8f4-c230-49ee-b3c1-e751edd7ec58",
            "timestamp": "2018-03-20T17:33:45Z",
            "locale": "en-US",
            "intent": {
                "name": "AddStockToWatchlistIntent",
                "confirmationStatus": "DENIED",
                "slots": {
                    "stockTicker": {
                        "name": "stockTicker",
                        "confirmationStatus": "NONE"
                    }
                }
            },
            "dialogState": "IN_PROGRESS"
        }
    }


RESPONSE_intent_add_to_watchlist_denied = INTENT_ADD_TO_WATCHLIST_DENIED


def intent_add_to_watchlist_confirm():
    return {
        "version": "1.0",
        "session": {
            "new": False,
            "sessionId": "amzn1.echo-api.session.37d0c2cf-c631-490c-9cd0-dfeeeb62cabb",
            "application": {
                "applicationId": "amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96"
            },
            "attributes": {
                "stockTicker": "RAVN",
                "userName": test_user_name,
                "userId": test_user_id
            },
            "user": {
                "userId": "amzn1.ask.account.AF64Z7P3TBODT4C6VB4SUJG67LSDJXMRPB4ZCN72Z5VSCFIS6COGQPHPPZCTUFCKYVNG37E56FUQHEHZQEMDEZHDP6EJ4ML6CZHBOKETG3TF44YRKRRIHUF4TMFMDKXSSPXBKW62LQVB4JNZ4NPGW5YMTRZZHNBFEYU7J4XF6MZPZRYA4KRS3ZKJHPHSKRB6ZOAHNXQ56T2HP7A",
                "accessToken": access_token
            }
        },
        "context": {
            "AudioPlayer": {
                "playerActivity": "IDLE"
            },
            "Display": {
                "token": ""
            },
            "System": {
                "application": {
                    "applicationId": "amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96"
                },
                "user": {
                    "userId": "amzn1.ask.account.AF64Z7P3TBODT4C6VB4SUJG67LSDJXMRPB4ZCN72Z5VSCFIS6COGQPHPPZCTUFCKYVNG37E56FUQHEHZQEMDEZHDP6EJ4ML6CZHBOKETG3TF44YRKRRIHUF4TMFMDKXSSPXBKW62LQVB4JNZ4NPGW5YMTRZZHNBFEYU7J4XF6MZPZRYA4KRS3ZKJHPHSKRB6ZOAHNXQ56T2HP7A",
                    "accessToken": access_token
                },
                "device": {
                    "deviceId": "amzn1.ask.device.AHDOK5CWXV4NE5TF26TG5TYEADGTBNUFFTERBPCFLHQUZPXYL35SLWECEFYCJZNJHSJ633PNN3BFHCDUCKSMY2FCRWFEX2UIW3IHCLM7EIR2XTYSFM3C3ZVHRDMUCIOPGP5DZWU53Y4OVMPEFV23ZW3WIOLQ",
                    "supportedInterfaces": {
                        "AudioPlayer": {},
                        "Display": {
                            "templateVersion": "1.0",
                            "markupVersion": "1.0"
                        }
                    }
                },
                "apiEndpoint": "https://api.amazonalexa.com",
                "apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLmRiYTEzNDZlLTVmNGEtNGY5ZS05ZDE0LWRjNjFkZDA4NGY5NiIsImV4cCI6MTUyMTY1NzA1NywiaWF0IjoxNTIxNjUzNDU3LCJuYmYiOjE1MjE2NTM0NTcsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUhET0s1Q1dYVjRORTVURjI2VEc1VFlFQURHVEJOVUZGVEVSQlBDRkxIUVVaUFhZTDM1U0xXRUNFRllDSlpOSkhTSjYzM1BOTjNCRkhDRFVDS1NNWTJGQ1JXRkVYMlVJVzNJSENMTTdFSVIyWFRZU0ZNM0MzWlZIUkRNVUNJT1BHUDVEWldVNTNZNE9WTVBFRlYyM1pXM1dJT0xRIiwidXNlcklkIjoiYW16bjEuYXNrLmFjY291bnQuQUY2NFo3UDNUQk9EVDRDNlZCNFNVSkc2N0xTREpYTVJQQjRaQ043Mlo1VlNDRklTNkNPR1FQSFBQWkNUVUZDS1lWTkczN0U1NkZVUUhFSFpRRU1ERVpIRFA2RUo0TUw2Q1pIQk9LRVRHM1RGNDRZUktSUklIVUY0VE1GTURLWFNTUFhCS1c2MkxRVkI0Sk5aNE5QR1c1WU1UUlpaSE5CRkVZVTdKNFhGNk1aUFpSWUE0S1JTM1pLSkhQSFNLUkI2Wk9BSE5YUTU2VDJIUDdBIn19.Hocqg0bseUant_mh6X_0mMU2s3BJ0iBZrvSKNYiPHrWXYkWa0P4-s8b9SaNt5PWTtu2ZiUzZ8O5QFROyWtyp0qY9Erm8Iqb8S0xT4xvXaf2Jvrw2kfOFfBUQPwYaIvo_F6wH6gUg6-NPVJhcpzqnZc16l8aXDHCDrPQG2lTjyWwfPZ1soyLK9xuWl5VDNo3nLrZTRofFHOhbyRjzrzHtmIjAAzrTP23PsJL4eDo_Cr84eOsqTxtAGNHxofmMIebc26bu3HkMF2pgEh1x5AH2i9_TdyaX7RJ3a6vwRzqHY3kEHZZyq2jM-W8hCo--K1PXTPUvV7DYkpNrQIeOdVUm8g"
            }
        },
        "request": {
            "type": "IntentRequest",
            "requestId": "amzn1.echo-api.request.e39b32a6-1ad5-41d7-819e-4a8d595a77b1",
            "timestamp": "2018-03-21T17:30:57Z",
            "locale": "en-GB",
            "intent": {
                "name": "AddStockToWatchlistIntent",
                "confirmationStatus": "CONFIRMED",
                "slots": {
                    "stockTicker": {
                        "name": "stockTicker",
                        "value": "Amazon",
                        "resolutions": {
                            "resolutionsPerAuthority": [
                                {
                                    "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96.LIST_OF_TICKERS",
                                    "status": {
                                        "code": "ER_SUCCESS_MATCH"
                                    },
                                    "values": [
                                        {
                                            "value": {
                                                "name": test_add_stock,
                                                "id": "e15ce71ff533c9125f11a46c09e2412b"
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        "confirmationStatus": "NONE"
                    }
                }
            },
            "dialogState": "IN_PROGRESS"
        }
    }


RESPONSE_intent_add_to_watchlist_confirmed = INTENT_ADD_TO_WATCHLIST_CONFIRMED \
    .format(test_add_stock)


def intent_remove_from_watchlist(ticker):
    return {
        "version": "1.0",
        "session": {
            "new": False,
            "sessionId": "amzn1.echo-api.session.7069db3a-1c85-4c18-90ae-7e95dd36efaa",
            "application": {
                "applicationId": "amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96"
            },
            "attributes": {
                "stockTicker": "MSFT"
            },
            "user": {
                "userId": "amzn1.ask.account.AF64Z7P3TBODT4C6VB4SUJG67LSDJXMRPB4ZCN72Z5VSCFIS6COGQPHPPZCTUFCKYVNG37E56FUQHEHZQEMDEZHDP6EJ4ML6CZHBOKETG3TF44YRKRRIHUF4TMFMDKXSSPXBKW62LQVB4JNZ4NPGW5YMTRZZHNBFEYU7J4XF6MZPZRYA4KRS3ZKJHPHSKRB6ZOAHNXQ56T2HP7A",
                "accessToken": access_token
            }
        },
        "context": {
            "AudioPlayer": {
                "playerActivity": "IDLE"
            },
            "Display": {
                "token": ""
            },
            "System": {
                "application": {
                    "applicationId": "amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96"
                },
                "user": {
                    "userId": "amzn1.ask.account.AF64Z7P3TBODT4C6VB4SUJG67LSDJXMRPB4ZCN72Z5VSCFIS6COGQPHPPZCTUFCKYVNG37E56FUQHEHZQEMDEZHDP6EJ4ML6CZHBOKETG3TF44YRKRRIHUF4TMFMDKXSSPXBKW62LQVB4JNZ4NPGW5YMTRZZHNBFEYU7J4XF6MZPZRYA4KRS3ZKJHPHSKRB6ZOAHNXQ56T2HP7A",
                    "accessToken": access_token
                },
                "device": {
                    "deviceId": "amzn1.ask.device.AHDOK5CWXV4NE5TF26TG5TYEADGTBNUFFTERBPCFLHQUZPXYL35SLWECEFYCJZNJHSJ633PNN3BFHCDUCKSMY2FCRWFEX2UIW3IHCLM7EIR2XTYSFM3C3ZVHRDMUCIOPGP5DZWU53Y4OVMPEFV23ZW3WIOLQ",
                    "supportedInterfaces": {
                        "AudioPlayer": {},
                        "Display": {
                            "templateVersion": "1.0",
                            "markupVersion": "1.0"
                        }
                    }
                },
                "apiEndpoint": "https://api.amazonalexa.com",
                "apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLmRiYTEzNDZlLTVmNGEtNGY5ZS05ZDE0LWRjNjFkZDA4NGY5NiIsImV4cCI6MTUyMTcxNzgzMiwiaWF0IjoxNTIxNzE0MjMyLCJuYmYiOjE1MjE3MTQyMzIsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUhET0s1Q1dYVjRORTVURjI2VEc1VFlFQURHVEJOVUZGVEVSQlBDRkxIUVVaUFhZTDM1U0xXRUNFRllDSlpOSkhTSjYzM1BOTjNCRkhDRFVDS1NNWTJGQ1JXRkVYMlVJVzNJSENMTTdFSVIyWFRZU0ZNM0MzWlZIUkRNVUNJT1BHUDVEWldVNTNZNE9WTVBFRlYyM1pXM1dJT0xRIiwidXNlcklkIjoiYW16bjEuYXNrLmFjY291bnQuQUY2NFo3UDNUQk9EVDRDNlZCNFNVSkc2N0xTREpYTVJQQjRaQ043Mlo1VlNDRklTNkNPR1FQSFBQWkNUVUZDS1lWTkczN0U1NkZVUUhFSFpRRU1ERVpIRFA2RUo0TUw2Q1pIQk9LRVRHM1RGNDRZUktSUklIVUY0VE1GTURLWFNTUFhCS1c2MkxRVkI0Sk5aNE5QR1c1WU1UUlpaSE5CRkVZVTdKNFhGNk1aUFpSWUE0S1JTM1pLSkhQSFNLUkI2Wk9BSE5YUTU2VDJIUDdBIn19.OkXlUEjCd6Iglrsyvlae9gRgPjfdj1qG5YJnwQdhdzybyeGXhEfZmWqgwOunT4I8GFWx5dOwxNWVc9c5niIWW5oglqw_oXYAPk5o3BluqHZ9XswAg9NG7yGD5rfhfhqnnNIAcZLIbfCK0-gnmMmXUEFsPKwSlCNrRafY8RwG9d889G5oWVIdq4eEyO3Y8JpyvSbUTgbzOEAHUI556AJhSRCCNruV6jzVjHpzGkxo290Gtwd53sdMZpB6IdhZAp6Yg9R0CUz92v5WL5mCiXR-TcjuP0qszcN3TaVDXsjkCySR20fSzaeRhHJ6UVielyAJHVVi86eStHO-w0FjzvH_Vg"
            }
        },
        "request": {
            "type": "IntentRequest",
            "requestId": "amzn1.echo-api.request.760441d3-3935-497f-807d-5ec71010649b",
            "timestamp": "2018-03-22T10:23:52Z",
            "locale": "en-GB",
            "intent": {
                "name": "RemoveStockFromWatchlistIntent",
                "confirmationStatus": "NONE",
                "slots": {
                    "stockTicker": {
                        "name": "stockTicker",
                        "value": "Amazon",
                        "resolutions": {
                            "resolutionsPerAuthority": [
                                {
                                    "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96.LIST_OF_TICKERS",
                                    "status": {
                                        "code": "ER_SUCCESS_MATCH"
                                    },
                                    "values": [
                                        {
                                            "value": {
                                                "name": ticker,
                                                "id": "ec367bc4f92cd97cec81bf7b43cffaf7"
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        "confirmationStatus": "NONE"
                    }
                }
            },
            "dialogState": "STARTED"
        }
    }


RESPONSE_intent_remove_from_watchlist_ask_confirmation = \
    INTENT_REMOVE_FROM_WATCHLIST_ASK_CONFIRMATION.format(test_add_stock)


def intent_remove_from_watchlist_deny():
    return {
        "version": "1.0",
        "session": {
            "new": False,
            "sessionId": "amzn1.echo-api.session.8d26efa2-ddce-4849-a30e-10861bba8a1b",
            "application": {
                "applicationId": "amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96"
            },
            "attributes": {
                "userName": test_user_name,
                "userId": test_user_id
            },
            "user": {
                "userId": "amzn1.ask.account.AF64Z7P3TBODT4C6VB4SUJG67LSDJXMRPB4ZCN72Z5VSCFIS6COGQPHPPZCTUFCKYVNG37E56FUQHEHZQEMDEZHDP6EJ4ML6CZHBOKETG3TF44YRKRRIHUF4TMFMDKXSSPXBKW62LQVB4JNZ4NPGW5YMTRZZHNBFEYU7J4XF6MZPZRYA4KRS3ZKJHPHSKRB6ZOAHNXQ56T2HP7A",
                "accessToken": access_token
            }
        },
        "context": {
            "AudioPlayer": {
                "playerActivity": "IDLE"
            },
            "Display": {
                "token": ""
            },
            "System": {
                "application": {
                    "applicationId": "amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96"
                },
                "user": {
                    "userId": "amzn1.ask.account.AF64Z7P3TBODT4C6VB4SUJG67LSDJXMRPB4ZCN72Z5VSCFIS6COGQPHPPZCTUFCKYVNG37E56FUQHEHZQEMDEZHDP6EJ4ML6CZHBOKETG3TF44YRKRRIHUF4TMFMDKXSSPXBKW62LQVB4JNZ4NPGW5YMTRZZHNBFEYU7J4XF6MZPZRYA4KRS3ZKJHPHSKRB6ZOAHNXQ56T2HP7A",
                    "accessToken": "EAAdvSgyprPcBAIKigdddcnZACP9WfbhiIPxTW1UHvW3sWu24S9AXNrbuzPWLoEIxxo8rQaqPZAZBCaHkr0gsTegIpTHIJNHQvQd59ABekEMNMB0xUgZBGJkZByydtZCT6yOwE4rMOg33t3TzO2j1SJFvqymbP1qEIfg5lGu1byUQZDZD"
                },
                "device": {
                    "deviceId": "amzn1.ask.device.AHDOK5CWXV4NE5TF26TG5TYEADGTBNUFFTERBPCFLHQUZPXYL35SLWECEFYCJZNJHSJ633PNN3BFHCDUCKSMY2FCRWFEX2UIW3IHCLM7EIR2XTYSFM3C3ZVHRDMUCIOPGP5DZWU53Y4OVMPEFV23ZW3WIOLQ",
                    "supportedInterfaces": {
                        "AudioPlayer": {},
                        "Display": {
                            "templateVersion": "1.0",
                            "markupVersion": "1.0"
                        }
                    }
                },
                "apiEndpoint": "https://api.amazonalexa.com",
                "apiAccessToken": access_token
            }
        },
        "request": {
            "type": "IntentRequest",
            "requestId": "amzn1.echo-api.request.146ab20c-e925-4371-b8b6-2774bdaca9ae",
            "timestamp": "2018-03-22T11:01:14Z",
            "locale": "en-GB",
            "intent": {
                "name": "RemoveStockFromWatchlistIntent",
                "confirmationStatus": "DENIED",
                "slots": {
                    "stockTicker": {
                        "name": "stockTicker",
                        "value": "Amazon",
                        "resolutions": {
                            "resolutionsPerAuthority": [
                                {
                                    "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96.LIST_OF_TICKERS",
                                    "status": {
                                        "code": "ER_SUCCESS_MATCH"
                                    },
                                    "values": [
                                        {
                                            "value": {
                                                "name": test_add_stock,
                                                "id": "ec367bc4f92cd97cec81bf7b43cffaf7"
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        "confirmationStatus": "NONE"
                    }
                }
            },
            "dialogState": "IN_PROGRESS"
        }
    }


RESPONSE_intent_remove_from_watchlist_denied = \
    INTENT_REMOVE_FROM_WATCHLIST_DENIED


def intent_remove_from_watchlist_confirm():
    return {
        "version": "1.0",
        "session": {
            "new": False,
            "sessionId": "amzn1.echo-api.session.8d26efa2-ddce-4849-a30e-10861bba8a1b",
            "application": {
                "applicationId": "amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96"
            },
            "attributes": {
                "userName": test_user_name,
                "userId": test_user_id
            },
            "user": {
                "userId": "amzn1.ask.account.AF64Z7P3TBODT4C6VB4SUJG67LSDJXMRPB4ZCN72Z5VSCFIS6COGQPHPPZCTUFCKYVNG37E56FUQHEHZQEMDEZHDP6EJ4ML6CZHBOKETG3TF44YRKRRIHUF4TMFMDKXSSPXBKW62LQVB4JNZ4NPGW5YMTRZZHNBFEYU7J4XF6MZPZRYA4KRS3ZKJHPHSKRB6ZOAHNXQ56T2HP7A",
                "accessToken": "EAAdvSgyprPcBAIKigdddcnZACP9WfbhiIPxTW1UHvW3sWu24S9AXNrbuzPWLoEIxxo8rQaqPZAZBCaHkr0gsTegIpTHIJNHQvQd59ABekEMNMB0xUgZBGJkZByydtZCT6yOwE4rMOg33t3TzO2j1SJFvqymbP1qEIfg5lGu1byUQZDZD"
            }
        },
        "context": {
            "AudioPlayer": {
                "playerActivity": "IDLE"
            },
            "Display": {
                "token": ""
            },
            "System": {
                "application": {
                    "applicationId": "amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96"
                },
                "user": {
                    "userId": "amzn1.ask.account.AF64Z7P3TBODT4C6VB4SUJG67LSDJXMRPB4ZCN72Z5VSCFIS6COGQPHPPZCTUFCKYVNG37E56FUQHEHZQEMDEZHDP6EJ4ML6CZHBOKETG3TF44YRKRRIHUF4TMFMDKXSSPXBKW62LQVB4JNZ4NPGW5YMTRZZHNBFEYU7J4XF6MZPZRYA4KRS3ZKJHPHSKRB6ZOAHNXQ56T2HP7A",
                    "accessToken": "EAAdvSgyprPcBAIKigdddcnZACP9WfbhiIPxTW1UHvW3sWu24S9AXNrbuzPWLoEIxxo8rQaqPZAZBCaHkr0gsTegIpTHIJNHQvQd59ABekEMNMB0xUgZBGJkZByydtZCT6yOwE4rMOg33t3TzO2j1SJFvqymbP1qEIfg5lGu1byUQZDZD"
                },
                "device": {
                    "deviceId": "amzn1.ask.device.AHDOK5CWXV4NE5TF26TG5TYEADGTBNUFFTERBPCFLHQUZPXYL35SLWECEFYCJZNJHSJ633PNN3BFHCDUCKSMY2FCRWFEX2UIW3IHCLM7EIR2XTYSFM3C3ZVHRDMUCIOPGP5DZWU53Y4OVMPEFV23ZW3WIOLQ",
                    "supportedInterfaces": {
                        "AudioPlayer": {},
                        "Display": {
                            "templateVersion": "1.0",
                            "markupVersion": "1.0"
                        }
                    }
                },
                "apiEndpoint": "https://api.amazonalexa.com",
                "apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLmRiYTEzNDZlLTVmNGEtNGY5ZS05ZDE0LWRjNjFkZDA4NGY5NiIsImV4cCI6MTUyMTcyMDA3NCwiaWF0IjoxNTIxNzE2NDc0LCJuYmYiOjE1MjE3MTY0NzQsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUhET0s1Q1dYVjRORTVURjI2VEc1VFlFQURHVEJOVUZGVEVSQlBDRkxIUVVaUFhZTDM1U0xXRUNFRllDSlpOSkhTSjYzM1BOTjNCRkhDRFVDS1NNWTJGQ1JXRkVYMlVJVzNJSENMTTdFSVIyWFRZU0ZNM0MzWlZIUkRNVUNJT1BHUDVEWldVNTNZNE9WTVBFRlYyM1pXM1dJT0xRIiwidXNlcklkIjoiYW16bjEuYXNrLmFjY291bnQuQUY2NFo3UDNUQk9EVDRDNlZCNFNVSkc2N0xTREpYTVJQQjRaQ043Mlo1VlNDRklTNkNPR1FQSFBQWkNUVUZDS1lWTkczN0U1NkZVUUhFSFpRRU1ERVpIRFA2RUo0TUw2Q1pIQk9LRVRHM1RGNDRZUktSUklIVUY0VE1GTURLWFNTUFhCS1c2MkxRVkI0Sk5aNE5QR1c1WU1UUlpaSE5CRkVZVTdKNFhGNk1aUFpSWUE0S1JTM1pLSkhQSFNLUkI2Wk9BSE5YUTU2VDJIUDdBIn19.dt4vFs8v7rZyVq_pbauE8rJb5txqsbMg1x-2l1xy99dQnwppoRkXudAur2OxVgWSclEUHmT5U3i4eMaCkkSlODBuoTO06sV3NFmQollsqfWmXpy2VUAK87zWe5MWBHke9hKQVUnqv6pwatcutDYqiAJ7j_psaTSwVHul1wRtBwG0IbTUgZjw4igNBpF69W9aSoZnHqANAsu8ZRTYQBAYLF4x_PUiviFHTHUSnraA6PGdj76f8rlEUBT6216KuRzCcgdhewI29ODzDzieDf3IivmN6Mp07JVJovDvIlu0LptmxwdNALhfktlz8X2A0_J8_EBlu_PgrOqC1WDh-f8YNw"
            }
        },
        "request": {
            "type": "IntentRequest",
            "requestId": "amzn1.echo-api.request.146ab20c-e925-4371-b8b6-2774bdaca9ae",
            "timestamp": "2018-03-22T11:01:14Z",
            "locale": "en-GB",
            "intent": {
                "name": "RemoveStockFromWatchlistIntent",
                "confirmationStatus": "CONFIRMED",
                "slots": {
                    "stockTicker": {
                        "name": "stockTicker",
                        "value": "Amazon",
                        "resolutions": {
                            "resolutionsPerAuthority": [
                                {
                                    "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96.LIST_OF_TICKERS",
                                    "status": {
                                        "code": "ER_SUCCESS_MATCH"
                                    },
                                    "values": [
                                        {
                                            "value": {
                                                "name": test_add_stock,
                                                "id": "ec367bc4f92cd97cec81bf7b43cffaf7"
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        "confirmationStatus": "NONE"
                    }
                }
            },
            "dialogState": "IN_PROGRESS"
        }
    }


RESPONSE_intent_remove_from_watchlist_confirmed = \
    INTENT_REMOVE_FROM_WATCHLIST_CONFIRMED
RESPONSE_intent_remove_from_watchlist_not_there = \
    INTENT_REMOVE_FROM_WATCHLIST_NOT_THERE.format(test_stock_1_ticker)


def intent_education_equity():
    return {
        'version': '1.0',
        'session': {
            'new': False,
            'sessionId': 'amzn1.echo-api.session.9793a0a7-619c-4f11-832c-255f5b5ded0a',
            'application': {
                'applicationId': 'amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96'
            },
            'user': {
                'userId': 'amzn1.ask.account.AF64Z7P3TBODT4C6VB4SUJG67LSDJXMRPB4ZCN72Z5VSCFIS6COGQPHPPZCTUFCKYVNG37E56FUQHEHZQEMDEZHDP6EJ4ML6CZHBOKETG3TF44YRKRRIHUF4TMFMDKXSSPXBKW62LQVB4JNZ4NPGW5YMTRZZHNBFEYU7J4XF6MZPZRYA4KRS3ZKJHPHSKRB6ZOAHNXQ56T2HP7A',
                'accessToken': access_token
            }
        },
        'context': {
            'AudioPlayer': {
                'playerActivity': 'STOPPED'
            },
            'System': {
                'application': {
                    'applicationId': 'amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96'
                },
                'user': {
                    'userId': 'amzn1.ask.account.AF64Z7P3TBODT4C6VB4SUJG67LSDJXMRPB4ZCN72Z5VSCFIS6COGQPHPPZCTUFCKYVNG37E56FUQHEHZQEMDEZHDP6EJ4ML6CZHBOKETG3TF44YRKRRIHUF4TMFMDKXSSPXBKW62LQVB4JNZ4NPGW5YMTRZZHNBFEYU7J4XF6MZPZRYA4KRS3ZKJHPHSKRB6ZOAHNXQ56T2HP7A',
                    'accessToken': access_token
                },
                'device': {
                    'deviceId': 'amzn1.ask.device.AHDOK5CWXV4NE5TF26TG5TYEADGUXG2VGOZVSI26DKPB2SHOPZIK7IP6PB242QH4JSHRVNBXXOCKROBQ3MGYAB5AKBFX36SE6TKYW6C7AYLYQFNOLG2MNZDZ2IONXJCOZDUWQURABRQSRHZNB3N3OCHVCK7TCGTCPZJTNX76ARBSTZSREG2JG',
                    'supportedInterfaces': {
                        'AudioPlayer': {}
                    }
                },
                'apiEndpoint': 'https://api.amazonalexa.com',
                'apiAccessToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLmRiYTEzNDZlLTVmNGEtNGY5ZS05ZDE0LWRjNjFkZDA4NGY5NiIsImV4cCI6MTUyMjAxNjcxOSwiaWF0IjoxNTIyMDEzMTE5LCJuYmYiOjE1MjIwMTMxMTksInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUhET0s1Q1dYVjRORTVURjI2VEc1VFlFQURHVVhHMlZHT1pWU0kyNkRLUEIyU0hPUFpJSzdJUDZQQjI0MlFINEpTSFJWTkJYWE9DS1JPQlEzTUdZQUI1QUtCRlgzNlNFNlRLWVc2QzdBWUxZUUZOT0xHMk1OWkRaMklPTlhKQ09aRFVXUVVSQUJSUVNSSFpOQjNOM09DSFZDSzdUQ0dUQ1BaSlROWDc2QVJCU1RaU1JFRzJKRyIsInVzZXJJZCI6ImFtem4xLmFzay5hY2NvdW50LkFGNjRaN1AzVEJPRFQ0QzZWQjRTVUpHNjdMU0RKWE1SUEI0WkNONzJaNVZTQ0ZJUzZDT0dRUEhQUFpDVFVGQ0tZVk5HMzdFNTZGVVFIRUhaUUVNREVaSERQNkVKNE1MNkNaSEJPS0VURzNURjQ0WVJLUlJJSFVGNFRNRk1ES1hTU1BYQktXNjJMUVZCNEpOWjROUEdXNVlNVFJaWkhOQkZFWVU3SjRYRjZNWlBaUllBNEtSUzNaS0pIUEhTS1JCNlpPQUhOWFE1NlQySFA3QSJ9fQ.h9QzcQtrZj1YfdJgAPIuVSo2N3goUhJhc1p-fzoNfH3Z-goQkvXCfn5Pzh1_lINU15Wne3qXXLI7bUGcakWaQU9ZZRjeNQjtXgk9BuiQfjpgUpYX05ddZOB5FK1QF0FepHYq1m-HsxOzSig2PepXSAMekhF6Ebwtvfmq3Pb_AzEwWPe2MpkeYan2nGJlD22G6diByV8tarDHh4kB6zS-yzQmDfxOZASZg5p9PmZ4W6LXF-mmdLL0MObMPhJgjZzBN5kARb2ov4Wq7MgxYKSrSxanlRYOnvK6op85AFHVF6y4lmnUFMZO611Fc5NaUCGyVgwJWEHA9xRX1Tk-6lUmRQ'
            }
        },
        'request': {
            'type': 'IntentRequest',
            'requestId': 'amzn1.echo-api.request.4c98b9a2-dfe2-47ce-8838-b211695c733d',
            'timestamp': '2018-03-25T21:25:19Z',
            'locale': 'en-US',
            'intent': {
                'name': 'EducateIntent',
                'confirmationStatus': 'NONE',
                'slots': {
                    'term': {
                        'name': 'term',
                        'value': 'equity',
                        'resolutions': {
                            'resolutionsPerAuthority': [{
                                'authority': 'amzn1.er-authority.echo-sdk.amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96.LIST_OF_TERMS',
                                'status': {
                                    'code': 'ER_SUCCESS_MATCH'
                                },
                                'values': [{
                                    'value': {
                                        'name': 'Equity',
                                        'id': 'd9df825203724a2f3412de3fc7a7a2be'
                                    }
                                }]
                            }]
                        },
                        'confirmationStatus': 'NONE'
                    }
                }
            },
            'dialogState': 'STARTED'
        }
    }


RESPONSE_intent_education_equity = TERM_EQUITY


def intent_news_about_company():
    return {
        'version': '1.0',
        'session': {
            'new': False,
            'sessionId': 'amzn1.echo-api.session.729a6db6-0611-4fac-aa35-a91f0db5c024',
            'application': {
                'applicationId': 'amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96'
            },
            'user': {
                'userId': 'amzn1.ask.account.AF64Z7P3TBODT4C6VB4SUJG67LSDJXMRPB4ZCN72Z5VSCFIS6COGQPHPPZCTUFCKYVNG37E56FUQHEHZQEMDEZHDP6EJ4ML6CZHBOKETG3TF44YRKRRIHUF4TMFMDKXSSPXBKW62LQVB4JNZ4NPGW5YMTRZZHNBFEYU7J4XF6MZPZRYA4KRS3ZKJHPHSKRB6ZOAHNXQ56T2HP7A',
                'accessToken': 'EAAdvSgyprPcBAIKigdddcnZACP9WfbhiIPxTW1UHvW3sWu24S9AXNrbuzPWLoEIxxo8rQaqPZAZBCaHkr0gsTegIpTHIJNHQvQd59ABekEMNMB0xUgZBGJkZByydtZCT6yOwE4rMOg33t3TzO2j1SJFvqymbP1qEIfg5lGu1byUQZDZD'
            }
        },
        'context': {
            'System': {
                'application': {
                    'applicationId': 'amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96'
                },
                'user': {
                    'userId': 'amzn1.ask.account.AF64Z7P3TBODT4C6VB4SUJG67LSDJXMRPB4ZCN72Z5VSCFIS6COGQPHPPZCTUFCKYVNG37E56FUQHEHZQEMDEZHDP6EJ4ML6CZHBOKETG3TF44YRKRRIHUF4TMFMDKXSSPXBKW62LQVB4JNZ4NPGW5YMTRZZHNBFEYU7J4XF6MZPZRYA4KRS3ZKJHPHSKRB6ZOAHNXQ56T2HP7A',
                    'accessToken': 'EAAdvSgyprPcBAIKigdddcnZACP9WfbhiIPxTW1UHvW3sWu24S9AXNrbuzPWLoEIxxo8rQaqPZAZBCaHkr0gsTegIpTHIJNHQvQd59ABekEMNMB0xUgZBGJkZByydtZCT6yOwE4rMOg33t3TzO2j1SJFvqymbP1qEIfg5lGu1byUQZDZD'
                },
                'device': {
                    'deviceId': 'amzn1.ask.device.AHDOK5CWXV4NE5TF26TG5TYEADGUXG2VGOZVSI26DKPB2SHOPZIK7IP6PB242QH4JSHRVNBXXOCKROBQ3MGYAB5AKBFX36SE6TKYW6C7AYLYQFNOLG2MNZDZ2IONXJCOZDUWQURABRQSRHZNB3N3OCHVCK7TCGTCPZJTNX76ARBSTZSREG2JG',
                    'supportedInterfaces': {
                        'AudioPlayer': {}
                    }
                },
                'apiEndpoint': 'https://api.amazonalexa.com',
                'apiAccessToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLmRiYTEzNDZlLTVmNGEtNGY5ZS05ZDE0LWRjNjFkZDA4NGY5NiIsImV4cCI6MTUyMjA3Njk0NSwiaWF0IjoxNTIyMDczMzQ1LCJuYmYiOjE1MjIwNzMzNDUsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUhET0s1Q1dYVjRORTVURjI2VEc1VFlFQURHVVhHMlZHT1pWU0kyNkRLUEIyU0hPUFpJSzdJUDZQQjI0MlFINEpTSFJWTkJYWE9DS1JPQlEzTUdZQUI1QUtCRlgzNlNFNlRLWVc2QzdBWUxZUUZOT0xHMk1OWkRaMklPTlhKQ09aRFVXUVVSQUJSUVNSSFpOQjNOM09DSFZDSzdUQ0dUQ1BaSlROWDc2QVJCU1RaU1JFRzJKRyIsInVzZXJJZCI6ImFtem4xLmFzay5hY2NvdW50LkFGNjRaN1AzVEJPRFQ0QzZWQjRTVUpHNjdMU0RKWE1SUEI0WkNONzJaNVZTQ0ZJUzZDT0dRUEhQUFpDVFVGQ0tZVk5HMzdFNTZGVVFIRUhaUUVNREVaSERQNkVKNE1MNkNaSEJPS0VURzNURjQ0WVJLUlJJSFVGNFRNRk1ES1hTU1BYQktXNjJMUVZCNEpOWjROUEdXNVlNVFJaWkhOQkZFWVU3SjRYRjZNWlBaUllBNEtSUzNaS0pIUEhTS1JCNlpPQUhOWFE1NlQySFA3QSJ9fQ.blpu80Ylk7TpYqc5oaQ_OSA20xvbsdhVlH9DcJ8P-qHqiyZ9O4LDD3EkNISfjk1hFBMTypbMp1J4MeGbqMl8f7OczvHOFqriIhYWrko9uVXEX0TaXui08XTDzw1ElbdE3oYvZhYT3ITNm50Ln5ycgqTPB9ASqoqToZyy7VsCOGoTRTel1f9KbR7qdM7te0E4FQuxqG2LjpPu0LvQJddPyoly1TPINCH-2ogZSlaxQoZYH0fsxCKYLbyGZMCklfPUxVA8PJ72E5NlNIxep4LMcruWuFwPyaIUQeA_It6Be9KQ8NaL0Ie5OD3GpOl76PlgR8hZWZq_2cpHKCIEsAlDDg'
            }
        },
        'request': {
            'type': 'IntentRequest',
            'requestId': 'amzn1.echo-api.request.dae00bae-6a6f-446b-be73-d7070107f045',
            'timestamp': '2018-03-26T14:09:05Z',
            'locale': 'en-US',
            'intent': {
                'name': 'NewsAboutCompanyIntent',
                'confirmationStatus': 'NONE',
                'slots': {
                    'stockTicker': {
                        'name': 'stockTicker',
                        'value': test_stock_1_name,
                        'resolutions': {
                            'resolutionsPerAuthority': [{
                                'authority': 'amzn1.er-authority.echo-sdk.amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96.LIST_OF_TICKERS',
                                'status': {
                                    'code': 'ER_SUCCESS_MATCH'
                                },
                                'values': [{
                                    'value': {
                                        'name': test_stock_1_ticker,
                                        'id': 'b004b3ecde24c85e32c1923f10d3fb62'
                                    }
                                }]
                            }]
                        },
                        'confirmationStatus': 'NONE'
                    }
                }
            },
            'dialogState': 'STARTED'
        }
    }


RESPONSE_intent_news_about_company = INTENT_NEWS_ABOUT_COMPANY_INTRO \
    .format(test_stock_1_name) + "<break time=\\\'700ms\\\'/>"


def intent_news_send_link():
    return {
        'version': '1.0',
        'session': {
            'new': False,
            'sessionId': 'amzn1.echo-api.session.a9f8c241-740c-4831-bd3c-aba7a976499d',
            'application': {
                'applicationId': 'amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96'
            },
            'user': {
                'userId': 'amzn1.ask.account.AF64Z7P3TBODT4C6VB4SUJG67LSDJXMRPB4ZCN72Z5VSCFIS6COGQPHPPZCTUFCKYVNG37E56FUQHEHZQEMDEZHDP6EJ4ML6CZHBOKETG3TF44YRKRRIHUF4TMFMDKXSSPXBKW62LQVB4JNZ4NPGW5YMTRZZHNBFEYU7J4XF6MZPZRYA4KRS3ZKJHPHSKRB6ZOAHNXQ56T2HP7A',
                'accessToken': access_token
            }
        },
        'context': {
            'AudioPlayer': {
                'playerActivity': 'STOPPED'
            },
            'System': {
                'application': {
                    'applicationId': 'amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96'
                },
                'user': {
                    'userId': 'amzn1.ask.account.AF64Z7P3TBODT4C6VB4SUJG67LSDJXMRPB4ZCN72Z5VSCFIS6COGQPHPPZCTUFCKYVNG37E56FUQHEHZQEMDEZHDP6EJ4ML6CZHBOKETG3TF44YRKRRIHUF4TMFMDKXSSPXBKW62LQVB4JNZ4NPGW5YMTRZZHNBFEYU7J4XF6MZPZRYA4KRS3ZKJHPHSKRB6ZOAHNXQ56T2HP7A',
                    'accessToken': access_token
                },
                'device': {
                    'deviceId': 'amzn1.ask.device.AHDOK5CWXV4NE5TF26TG5TYEADGUXG2VGOZVSI26DKPB2SHOPZIK7IP6PB242QH4JSHRVNBXXOCKROBQ3MGYAB5AKBFX36SE6TKYW6C7AYLYQFNOLG2MNZDZ2IONXJCOZDUWQURABRQSRHZNB3N3OCHVCK7TCGTCPZJTNX76ARBSTZSREG2JG',
                    'supportedInterfaces': {
                        'AudioPlayer': {}
                    }
                },
                'apiEndpoint': 'https://api.amazonalexa.com',
                'apiAccessToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLmRiYTEzNDZlLTVmNGEtNGY5ZS05ZDE0LWRjNjFkZDA4NGY5NiIsImV4cCI6MTUyMjE1MjY1NCwiaWF0IjoxNTIyMTQ5MDU0LCJuYmYiOjE1MjIxNDkwNTQsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUhET0s1Q1dYVjRORTVURjI2VEc1VFlFQURHVVhHMlZHT1pWU0kyNkRLUEIyU0hPUFpJSzdJUDZQQjI0MlFINEpTSFJWTkJYWE9DS1JPQlEzTUdZQUI1QUtCRlgzNlNFNlRLWVc2QzdBWUxZUUZOT0xHMk1OWkRaMklPTlhKQ09aRFVXUVVSQUJSUVNSSFpOQjNOM09DSFZDSzdUQ0dUQ1BaSlROWDc2QVJCU1RaU1JFRzJKRyIsInVzZXJJZCI6ImFtem4xLmFzay5hY2NvdW50LkFGNjRaN1AzVEJPRFQ0QzZWQjRTVUpHNjdMU0RKWE1SUEI0WkNONzJaNVZTQ0ZJUzZDT0dRUEhQUFpDVFVGQ0tZVk5HMzdFNTZGVVFIRUhaUUVNREVaSERQNkVKNE1MNkNaSEJPS0VURzNURjQ0WVJLUlJJSFVGNFRNRk1ES1hTU1BYQktXNjJMUVZCNEpOWjROUEdXNVlNVFJaWkhOQkZFWVU3SjRYRjZNWlBaUllBNEtSUzNaS0pIUEhTS1JCNlpPQUhOWFE1NlQySFA3QSJ9fQ.IKkIGLaHj4kngyHzhBogIN57HU4-iLKHrP_Hzn3zD2wW9bxjX1evYwLZIOinUwUJxj6uBuM6_XxyK1d0DjttjH4yLDrLIGEQRzKVx9UDpDonLA_ZjqSKbSJiBHgKKzAEYLXtlf_tuz4NtuTMjN88jSfzEeX6LvRlod1lOmYGWbgu8IWNEopAgAPCMjZbWNwkm5p0AVpZr3QSvjfNmGTbRQnVG6sxqxpgmNic1A_JmoYTnPr-pvjX_61Sg-NrlelKRlU6LKifM_KF7xA4Br_3VnT7RXepu0osJ5ZseK8MvLa4fEZtDUuPYwcGH3zsp1i5eJQtq-PQiQjGheKwGtTIKA'
            }
        },
        'request': {
            'type': 'IntentRequest',
            'requestId': 'amzn1.echo-api.request.2febd657-9e04-432c-8bf9-c1ec46aee2d0',
            'timestamp': '2018-03-27T11:10:54Z',
            'locale': 'en-US',
            'intent': {
                'name': 'NewsAboutCompanyIntent',
                'confirmationStatus': 'CONFIRMED',
                'slots': {
                    'stockTicker': {
                        'name': 'stockTicker',
                        'value': test_stock_1_name,
                        'resolutions': {
                            'resolutionsPerAuthority': [{
                                'authority': 'amzn1.er-authority.echo-sdk.amzn1.ask.skill.dba1346e-5f4a-4f9e-9d14-dc61dd084f96.LIST_OF_TICKERS',
                                'status': {
                                    'code': 'ER_SUCCESS_MATCH'
                                },
                                'values': [{
                                    'value': {
                                        'name': test_stock_1_ticker,
                                        'id': '261fd26b0151a81370d097e4ed4c6505'
                                    }
                                }]
                            }]
                        },
                        'confirmationStatus': 'NONE'
                    },
                    'articleNo': {
                        'name': 'articleNo',
                        'value': '1',
                        'confirmationStatus': 'NONE'
                    }
                }
            },
            'dialogState': 'IN_PROGRESS'
        }
    }


RESPONSE_intent_news_send_link = INTENT_NEWS_ABOUT_COMPANY_LINK_CARD_CONTENT \
    .format("http")

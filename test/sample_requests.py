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
access_token = "EAAdvSgyprPcBAGWGAKsr03UddHlyX6JiqV9v7aAvGxfNBRNAKCAfrJ6uDD4ixxkX6TAWxZC9F6kTKS2edxg3cZBW9CZBQ1zuM8HKhPc45bIrC3OADEPGIKGm2i0o5eH3sa9p5c6QXrN1jdzYAW0vCAVBGZA1wDk3s7IrZAjVwXgZDZD"

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

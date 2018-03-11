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

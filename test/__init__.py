import random

import requests
import json

from app.models import Stock
from static import strings_edu


strategies = strings_edu.STRATEGIES['data']

pick = random.randint(0, len(strategies) - 1)

strategy_name = strategies[pick]['name']
strategy_content = strategies[pick]['content']

print(strategy_name)
print(strategy_content)

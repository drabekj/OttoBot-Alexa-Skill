import random

import requests
import json

from app.models import Stock
from app.utils.Sentiment import Analyst
from static import strings_edu


tslaAnalyst = Analyst("TSLA")
tslaAnalyst.recommendation()

print("Finish")

import requests
from sqlalchemy.exc import OperationalError

from app import db, logger
from app.utils.MyError import EntryExistsError


class Stock(db.Model):
    """This class represents the stock table."""

    __tablename__ = 'Stock'

    stockId = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(255))
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
    open = db.Column(db.Float())
    high = db.Column(db.Float())
    low = db.Column(db.Float())
    close = db.Column(db.Float())
    volume = db.Column(db.Float())
    ex_dividend = db.Column(db.Float())
    split_ratio = db.Column(db.Float())
    adj_open = db.Column(db.Float())

    def __init__(self, ticker, date, open=0, high=0, low=0, close=0, volume=0,
                 ex_dividend=0, split_ratio=0, adj_open=0):
        """initialize with name."""
        self.ticker = ticker
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.ex_dividend = ex_dividend
        self.SplitRatio = split_ratio
        self.AdjOpen = adj_open

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_last(ticker):
        param = {
            'symbols': ticker,
            'types': 'quote',
        }
        try:
            r = requests.get("https://api.iextrading.com/1.0/stock/market/batch", params=param)
            r.raise_for_status()

            data = r.json()
        except requests.exceptions.HTTPError as err:
            print("HTTPError: " + str(err))
            return None
        except requests.exceptions.Timeout as err:
            print("Timeout: " + str(err))
            return None
        except requests.exceptions.TooManyRedirects as err:
            print("TooManyRedirects: " + str(err))
            return None
        except requests.exceptions.RequestException as err:
            print("RequestException: " + str(err))
            return None

        price = data[ticker]['quote']['latestPrice']

        # return Stock.query.filter_by(ticker=ticker) \
        #     .order_by(Stock.date.desc()).first()
        return {
            'ticker': ticker,
            'price': price,
        }

    @staticmethod
    def get_stats(ticker):
        try:
            r = requests.get("https://api.iextrading.com/1.0/stock/{}/stats".format(ticker))
            r.raise_for_status()

            data = r.json()
        except requests.exceptions.HTTPError as err:
            print("HTTPError: " + str(err))
            return None
        except requests.exceptions.Timeout as err:
            print("Timeout: " + str(err))
            return None
        except requests.exceptions.TooManyRedirects as err:
            print("TooManyRedirects: " + str(err))
            return None
        except requests.exceptions.RequestException as err:
            print("RequestException: " + str(err))
            return None

        return data

    # @staticmethod
    # def get_nth_latest(ticker, n=0):
    #     """ Get the n-th latest entry for ticker, where n=0 is the most recent one."""
    #     return Stock.query.filter_by(ticker=ticker) \
    #         .order_by(Stock.date.desc()).limit(n).all()

    @staticmethod
    def get_change_batch(ticker_list):
        """
        :param ticker_list:
        :return: List of 24 hour changes
        """
        changes = []
        param = {
            'symbols': ",".join(ticker_list),
            'types': 'quote',
        }
        try:
            r = requests.get(
                "https://api.iextrading.com/1.0/stock/market/batch",
                params=param)
            r.raise_for_status()

            data = r.json()
        except requests.exceptions.HTTPError as err:
            print("HTTPError: " + str(err))
            return None
        except requests.exceptions.Timeout as err:
            print("Timeout: " + str(err))
            return None
        except requests.exceptions.TooManyRedirects as err:
            print("TooManyRedirects: " + str(err))
            return None
        except requests.exceptions.RequestException as err:
            print("RequestException: " + str(err))
            return None

        for stock in data:
            change = data[stock]['quote']['changePercent'] * 100
            changes.append(change)

        return changes

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Stock: {} {} {}>".format(self.date, self.ticker, self.close)


class User(db.Model):
    """This class represents the users table."""

    __tablename__ = 'users'

    userId = db.Column(db.String(255), nullable=False, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    watchlist = db.relationship('Watchlist', backref='watchlist',
                                lazy='dynamic')

    def __init__(self, user_id, name):
        self.userId = user_id
        self.name = name

    def save(self):
        try:
            db.session.merge(self)
            db.session.commit()
        except OperationalError as e:
            logger.exception("Can't connect to MySQL server ottobotdb.clccaawfuuph.eu-central-1.rds.amazonaws.com")


    @staticmethod
    def get_user(user_id):
        return User.query.filter_by(userId=user_id).first()

    def __repr__(self):
        return "<User: {} {}>".format(self.name, self.userId)


class Watchlist(db.Model):
    """This class represents the watchlists table."""

    __tablename__ = 'watchlists'

    id = db.Column(db.Integer, primary_key=True)
    stock_ticker = db.Column(db.String(255))
    userId = db.Column(db.String(255), db.ForeignKey('users.userId'))

    def __init__(self, stock_ticker, user_id):
        self.stock_ticker = stock_ticker
        self.userId = user_id

    def save(self):
        if Watchlist.ticker_in_watchlist_exists(self.userId, self.stock_ticker):
            raise EntryExistsError(
                message="There is already entry for userId:{0} of stock:{1}"
                    .format(self.userId, self.stock_ticker))

        db.session.add(self)
        db.session.commit()

    def delete(self):
        try:
            result = Watchlist.query\
                .filter_by(userId=self.userId, stock_ticker=self.stock_ticker)\
                .first()
            db.session.delete(result)
            db.session.commit()
            logger.info(f"Deleted users:{self.userId} stock:{self.stock_ticker} from DB")
        except:
            logger.exception(f"Couldn't delete {self.stock_ticker} for user {self.userId} from DB")

    @staticmethod
    def get_users_tickers(user_id):
        """
        :return: List[str] of tickers for given user in his watchlist
        """
        results = []
        """:type results list[Watchlist]"""

        try:
            results = Watchlist.query.filter_by(userId=user_id).all()
        except OperationalError:
            logger.exception("Can't connect to MySQL server ottobotdb.clccaawfuuph.eu-central-1.rds.amazonaws.com")
        ticker_list = [item.stock_ticker for item in results]

        return ticker_list

    @staticmethod
    def ticker_in_watchlist_exists(user_id, ticker):
        ticker_list = Watchlist.get_users_tickers(user_id)

        for item in ticker_list:
            if item == ticker:
                return True
        return False

    @staticmethod
    def delete_all():
        Watchlist.query.delete()
        db.session.commit()

    def __repr__(self):
        return "<Watchlist item: {} {}>".format(self.userId, self.stock_ticker)

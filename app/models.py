from app import db


class Stock(db.Model):
    """This class represents the stock table."""

    __tablename__ = 'Stock'

    Ticker = db.Column(db.String(255), primary_key=True)
    Date = db.Column(db.DateTime, default=db.func.current_timestamp())
    Open = db.Column(db.Float())
    High = db.Column(db.Float())
    Low = db.Column(db.Float())
    Close = db.Column(db.Float())
    Volume = db.Column(db.Float())
    ExDividend = db.Column(db.Float())
    SplitRatio = db.Column(db.Float())
    AdjOpen = db.Column(db.Float())

    def __init__(self, Ticker, Date, Open=0, High=0, Low=0, Close=0, Volume=0,
                 ExDividend=0, SplitRatio=0, AdjOpen=0):
        """initialize with name."""
        self.Ticker = Ticker
        self.Date = Date
        self.Open = Open
        self.High = High
        self.Low = Low
        self.Close = Close
        self.Volume = Volume
        self.ExDividend = ExDividend
        self.SplitRatio = SplitRatio
        self.AdjOpen = AdjOpen

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_last(ticker):
        return Stock.query.filter_by(Ticker=ticker) \
            .order_by(Stock.Date.desc()).first()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Stock: {} {} {}>".format(self.Date, self.Ticker, self.Close)


class User(db.Model):
    """This class represents the users table."""

    __tablename__ = 'users'

    userId = db.Column(db.String(255), nullable=False, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    watchlist = db.relationship('Watchlist', backref='watchlist', lazy='dynamic')

    def __init__(self, user_id, name):
        self.userId = user_id
        self.name = name

    def save(self):
        db.session.merge(self)
        db.session.commit()

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
        db.session.merge(self)
        db.session.commit()

    @staticmethod
    def get_users_tickers(user_id):
        """
        :return: List[str] of tickers for given user in his watchlist
        """

        results = Watchlist.query.filter_by(userId=user_id).all()
        """:type results list[Watchlist]"""
        ticker_list = [item.stock_ticker for item in results]

        return ticker_list

    @staticmethod
    def delete_all():
        Watchlist.query.delete()
        db.session.commit()

    def __repr__(self):
        return "<Watchlist item: {} {}>".format(self.userId, self.stock_ticker)

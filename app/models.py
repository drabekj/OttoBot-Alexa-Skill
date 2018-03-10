from app import db


class Stock(db.Model):
    """This class represents the stock table."""

    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.DateTime, default=db.func.current_timestamp())
    Ticker = db.Column(db.String(255))
    Open = db.Column(db.Float())
    High = db.Column(db.Float())
    Low = db.Column(db.Float())
    Close = db.Column(db.Float())
    Volume = db.Column(db.Float())
    ExDividend = db.Column(db.Float())
    SplitRatio = db.Column(db.Float())
    AdjOpen = db.Column(db.Float())


    def __init__(self, date, ticker, close, open):
        """initialize with name."""
        self.date = date
        self.ticker = ticker
        self.close = close
        self.open = open

    @staticmethod
    def get_last(ticker):
        return Stock.query.filter_by(Ticker=ticker).order_by(Stock.Date.desc())\
            .first()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Stock: {} {} {}>".format(self.date, self.ticker, self.close)

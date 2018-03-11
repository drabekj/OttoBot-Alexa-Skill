from app import db


class Stock(db.Model):
    """This class represents the stock table."""

    __tablename__ = 'Stock'

    # id = db.Column(db.Integer, primary_key=True)
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
        return Stock.query.filter_by(Ticker=ticker).order_by(Stock.Date.desc())\
            .first()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Stock: {} {} {}>".format(self.date, self.ticker, self.close)

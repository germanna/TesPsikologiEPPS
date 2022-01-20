from app import db

class Percentile(db.Model):
    id_percentile = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    score = db.Column(db.Integer)
    ach = db.Column(db.Integer)
    DEF = db.Column(db.Integer)
    ord = db.Column(db.Integer)
    exh = db.Column(db.Integer)
    aut = db.Column(db.Integer)
    aff = db.Column(db.Integer)
    int = db.Column(db.Integer)
    suc = db.Column(db.Integer)
    dom = db.Column(db.Integer)
    aba = db.Column(db.Integer)
    nur = db.Column(db.Integer)
    chg = db.Column(db.Integer)
    end = db.Column(db.Integer)
    het = db.Column(db.Integer)
    agg = db.Column(db.Integer)

    def __repr__(self):
        return '{}'.format(self.score, self.ach, self.DEF, self.ord, self.exh, self.aut, self.aff, self.int, self.suc, self.dom, self.aba, self.nur, self.chg, self.end, self.het, self.agg)
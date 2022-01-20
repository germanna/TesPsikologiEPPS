from app import db

class Soal(db.Model):
    id_soal = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    pernyataan_a = db.Column(db.String(1000))
    pernyataan_b = db.Column(db.String(1000))

    def __repr__(self):
        return '{}'.format(self.id_soal, self.pernyataan_a, self.pernyataan_b)
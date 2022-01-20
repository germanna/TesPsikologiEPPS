from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    username = db.Column(db.String(100), index=True, unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    umur = db.Column(db.Integer, nullable = False)
    jeniskelamin = db.Column(db.String(50), nullable = False)
    image_file = db.Column(db.String(100), nullable=False, default="undraw_profile.svg")
    hasiltes = db.relationship('HasilTes', backref='identitas',lazy=True)
    roles = db.Column(db.String(10), nullable=False, default="User")

    def __repr__(self):
        return '{}'.format(self.id, self.fullname, self.email, self.jeniskelamin, self.password, self.umur, self.username, self.created_at, self.roles)

class HasilTes(db.Model):
    id_hasil = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nilai_ach = db.Column(db.Integer, nullable=False)
    nilai_def = db.Column(db.Integer, nullable=False)
    nilai_ord = db.Column(db.Integer, nullable=False)
    nilai_exh = db.Column(db.Integer, nullable=False)
    nilai_aut = db.Column(db.Integer, nullable=False)
    nilai_aff = db.Column(db.Integer, nullable=False)
    nilai_int  = db.Column(db.Integer, nullable=False)
    nilai_suc = db.Column(db.Integer, nullable=False)
    nilai_dom = db.Column(db.Integer, nullable=False)
    nilai_aba = db.Column(db.Integer, nullable=False)
    nilai_nur = db.Column(db.Integer, nullable=False)
    nilai_chg = db.Column(db.Integer, nullable=False)
    nilai_end = db.Column(db.Integer, nullable=False)
    nilai_het = db.Column(db.Integer, nullable=False)
    nilai_agg = db.Column(db.Integer, nullable=False)
    hasil_pekerjaan_ach = db.Column(db.String(250), nullable=False)
    hasil_pekerjaan_def = db.Column(db.String(250), nullable=False)
    hasil_pekerjaan_ord = db.Column(db.String(250), nullable=False)
    hasil_pekerjaan_exh = db.Column(db.String(250), nullable=False)
    hasil_pekerjaan_aut = db.Column(db.String(250), nullable=False)
    hasil_pekerjaan_aff = db.Column(db.String(250), nullable=False)
    hasil_pekerjaan_int = db.Column(db.String(250), nullable=False)
    hasil_pekerjaan_suc = db.Column(db.String(250), nullable=False)
    hasil_pekerjaan_dom = db.Column(db.String(250), nullable=False)
    hasil_pekerjaan_aba = db.Column(db.String(250), nullable=False)
    hasil_pekerjaan_nur = db.Column(db.String(250), nullable=False)
    hasil_pekerjaan_chg = db.Column(db.String(250), nullable=False)
    hasil_pekerjaan_end = db.Column(db.String(250), nullable=False)
    hasil_pekerjaan_het = db.Column(db.String(250), nullable=False)
    hasil_pekerjaan_agg = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '{}'.format(self.id_hasil, self.nilai_ach, self.nilai_def, self.nilai_ord, self.nilai_exh, self.nilai_aut, self.nilai_aff, self.nilai_int, self.nilai_suc, self.nilai_dom, self.nilai_aba, self.nilai_nur, self.nilai_chg, self.nilai_end, self.nilai_het, self.nilai_agg, self.hasil_pekerjaan_ach, self.hasil_pekerjaan_def, self.hasil_pekerjaan_ord, self.hasil_pekerjaan_exh, self.hasil_pekerjaan_aut, self.hasil_pekerjaan_aff, self.hasil_pekerjaan_int, self.hasil_pekerjaan_suc, self.hasil_pekerjaan_dom, self.hasil_pekerjaan_aba, self.hasil_pekerjaan_nur, self.hasil_pekerjaan_chg, self.hasil_pekerjaan_end, self.hasil_pekerjaan_het, self.hasil_pekerjaan_agg)

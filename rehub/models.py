from rehub import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Report(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    kind = db.Column(db.Integer)
    title = db.Column(db.String(300))

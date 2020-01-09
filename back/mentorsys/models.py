from sqlalchemy.ext.declarative import declarative_base
from mentorsys import db, ma
""" 
Base = db.make_declarative_base(db.Model)


# Base Schema - adds Schema to Model for JSON serialization (using Marshmallow)
def add_schema(cls):
    class Schema(ma.ModelSchema):
        class Meta:
            model = cls
    cls.Schema = Schema
    return cls
 """

# @add_schema
class Mentee(db.Model):
    # __tablename__ = "mentee"
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    telnum = db.Column(db.String(20), nullable=True)
    contract = db.Column(db.String(10))
    mentor_id = db.Column(db.Integer, db.ForeignKey('mentor.id'), nullable=True)

    def __init__(self, fname, lname, email, telnum, contract):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.telnum = telnum
        self.contract = contract
        # self.mentor_id = 1

    def __repr__(self):
        return f"Mentee{self.id} - {self.fname} {self.lname}\n{self.email}\n" \
               f"{self.telnum}\n{self.contract}\n{self.mentor_id}"

# Mentor Model
# @add_schema
class Mentor(db.Model):
    # __tablename__ = "mentor"
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120))
    telnum = db.Column(db.String(20))
    contract = db.Column(db.String(15)) # status of mentor contract eg.(APPROVED, PENDING)
    current = db.Column(db.Integer, default=0)  # current number of mentees assigned
    met_max = db.Column(db.Integer, default=1)  # maximum number of mentees that can be assigned
    mentees = db.relationship('Mentee', backref='mentor')   # mentees assigned

    def __init__(self, fname, lname, email, telnum, contract, current, met_max):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.telnum = telnum
        self.contract = contract
        self.current = current
        self.met_max = met_max

    def __repr__(self):
        return f"Mentor{self.id} - {self.fname} {self.lname}\n" \
               f"{self.email}\n{self.telnum}\n{self.contract}\n" \
               f"{self.current}\n{self.met_max}\n{self.mentees}"



class MenteeSchema(ma.ModelSchema):
    class Meta:
        model = Mentee
        fiels = ('id', 'fname', 'lname', 'email', 'telnum', 'contract', 'mentor_id')


class MentorSchema(ma.ModelSchema):
    class Meta:
        model = Mentor
        fiels = ('id', 'fname', 'lname', 'email', 'telnum', 'contract', 'current', 'met_max')


mentee_schema = MenteeSchema()
mentees_schema = MenteeSchema(many=True)
mentor_schema = MentorSchema()
mentors_schema = MentorSchema(many=True)

# DB DESTROY AND CREATE
db.drop_all()
db.create_all()

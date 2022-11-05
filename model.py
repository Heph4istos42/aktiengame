from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class Company_Value(db.Model):    
    companyId = db.Column(db.Integer, db.ForeignKey('company.companyId'), primary_key=True, nullable=False)
    time = db.Column(db.String(50), primary_key=True, nullable=False)
    value = db.Column(db.Integer, nullable=False)
    
    def __init__(self, companyId, time, value):
        self.companyId = companyId
        self.time = time
        self.value = value

class Company(db.Model):    
    companyId = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
            
    def __init__(self, companyId, name):
        self.companyId = companyId
        self.name = name        

class Nutzer(db.Model):    
    username = db.Column(db.String(100), primary_key=True, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    hashedPassword = db.Column(db.String(450))
    authCookie = db.Column(db.String(100))
    
    def __init__(self, username, weight, height, hashedPassword):
        self.username = username
        self.weight = weight
        self.height  = height 
        self.hashedPassword = hashedPassword

class NutzerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Nutzer
        
class CompanySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Company

class Company_ValueSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Company_Value

companySchema = CompanySchema()
companysSchema = CompanySchema(many=True) 

nutzerSchema = NutzerSchema()
nutzersSchema = NutzerSchema(many=True)

company_ValueSchema = Company_ValueSchema()
company_ValuesSchema = Company_ValueSchema(many=True)
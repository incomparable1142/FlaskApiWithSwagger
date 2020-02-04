from .. import db


class WOFieldsModel(db.Model):
    __tablename__ = 'is_WOFields'
    Active = db.Column(db.INT)
    BooleanVal = db.Column(db.INT)
    CreatedBy = db.Column(db.String(45))
    Currency = db.Column(db.String(45))
    IntVal = db.Column(db.INT)
    LastModifiedBy = db.Column(db.String(45))
    Name = db.Column(db.TEXT)
    Product = db.Column(db.String(45))
    RecordType = db.Column(db.String(45))
    ServiceFlowStep = db.Column(db.String(45))
    StringVal = db.Column(db.TEXT)
    Type = db.Column(db.String(45))
    WOCheckListId = db.Column(db.Integer, db.ForeignKey('is_WOChecklist.id'))
    Id = db.Column(db.Integer, primary_key=True)


    def __init__(self,
                    Active,
                    BooleanVal,
                    CreatedBy,
                    Currency,
                    IntVal,
                    LastModifiedBy,
                    Name,
                    Product,
                    RecordType,
                    ServiceFlowStep,
                    StringVal,
                    Type,
                    WOCheckListId
                 ):
        self.Active = Active
        self.BooleanVal = BooleanVal
        self.CreatedBy = CreatedBy
        self.Currency = Currency
        self.IntVal = IntVal
        self.LastModifiedBy = LastModifiedBy
        self.Name = Name
        self.Product = Product
        self.RecordType = RecordType
        self.ServiceFlowStep = ServiceFlowStep
        self.StringVal = StringVal
        self.Type = Type
        self.WOCheckListId = WOCheckListId

    # To convert the data from list to json
    def json(self):
        return {
                'Active':self.Active,
                'BooleanVal':self.BooleanVal,
                'CreatedBy':self.CreatedBy,
                'Currency':self.Currency,
                'IntVal':self.IntVal,
                'LastModifiedBy':self.LastModifiedBy,
                'Name': self.Name,
                'Product':self.Product,
                'RecordType':self.RecordType,
                'ServiceFlowStep':self.ServiceFlowStep,
                'StringVal':self.StringVal,
                'Type':self.Type,
                'WOCheckListId':self.WOCheckListId
                }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(WOCheckListId=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return WOFieldsModel.query.order_by(WOFieldsModel.WOCheckListId).all()

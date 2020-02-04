from .. import db


class FieldGroupModel(db.Model):
    __tablename__ = 'is_FieldGroups'
    Id = db.Column(db.String(45), primary_key=True)
    Name = db.Column(db.String(45))
    Active = db.Column(db.INT)
    CreatedBy = db.Column(db.String(45))
    ModifiedBy = db.Column(db.String(45))
    CreatedDate = db.Column(db.DATETIME)
    ModifiedDate =db.Column(db.DATETIME)
    ModNum   = db.Column(db.INT)
    ChklistId = db.Column(db.Integer, db.ForeignKey('is_checklist.Id'))

    def __init__(self,
                 Id,
                 Name,
                 Active,
                 CreatedBy,
                 ModifiedBy,
                 CreatedDate,
                 ModifiedDate,
                 ModNum,
                 ChklistId,
                 ):
        self.Id = Id
        self.Name = Name
        self.Active = Active
        self.CreatedBy = CreatedBy
        self.ModifiedBy = ModifiedBy
        self.CreatedDate = CreatedDate
        self.ModifiedDate = ModifiedDate
        self.ModNum = ModNum
        self.ChklistId = ChklistId
    # To convert the data from list to json

    def json(self):
        return {
            'Id':self.Id,
            'Name':self.Name,
            'Active':self.Active,
            'CreatedBy':self.CreatedBy,
            'ModifiedBy':self.ModifiedBy,
            'CreatedDate':str(self.CreatedDate),
            'ModifiedDate':str(self.ModifiedDate),
            'ModNum':self.ModNum,
            'ChklistId':self.ChklistId
                }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(Id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return FieldGroupModel.query.order_by(FieldGroupModel.Id).all()

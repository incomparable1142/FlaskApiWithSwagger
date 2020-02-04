from .. import db


class FieldModel(db.Model):
    __tablename__ = 'is_Fields'
    Id = db.Column(db.String(45), primary_key=True)
    Name = db.Column(db.String(45))
    Active = db.Column(db.INT)
    CreatedBy = db.Column(db.String(45))
    ModifiedBy = db.Column(db.String(45))
    CreatedDate = db.Column(db.DATETIME)
    ModifiedDate =db.Column(db.DATETIME)
    ModNum   = db.Column(db.INT)
    DataType = db.Column(db.String(45))
    Group = db.Column(db.INT)
    GroupSeq =  db.Column(db.INT)
    FieldGroupId = db.Column(db.Integer, db.ForeignKey('is_FieldGroup.id'))

    #FieldGroups = db.relationship('is_FieldGroup', lazy='dynamic')
    def __init__(self,
                 Id,
                 Name,
                 Active,
                 CreatedBy,
                 ModifiedBy,
                 CreatedDate,
                 ModifiedDate,
                 ModNum,
                 DataType,
                 Group,
                 GroupSeq,
                 FieldGroupId,
                 ):
        self.Id = Id
        self.Name = Name
        self.Active = Active
        self.CreatedBy = CreatedBy
        self.ModifiedBy = ModifiedBy
        self.CreatedDate = CreatedDate
        self.ModifiedDate = ModifiedDate
        self.ModNum = ModNum
        self.DataType = DataType
        self.Group = Group
        self.GroupSeq = GroupSeq
        self.FieldGroupId = FieldGroupId

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
            'DataType':self.DataType,
            'Group':self.Group,
            'GroupSeq':self.GroupSeq,
            'FieldGroupId':self.FieldGroupId,
            #'FieldGroups': [is_FieldGroup.json() for is_FieldGroup in self.is_FieldGroup.all()]
                }

    @classmethod
    def find_by_id(cls, Id):
        return cls.query.filter_by(Id=Id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return FieldModel.query.order_by(FieldModel.Id).all()
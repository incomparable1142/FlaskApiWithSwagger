from .. import db


class ChecklistModel(db.Model):
    __tablename__ = 'is_checklist'
    Id = db.Column(db.String(45), primary_key=True)
    Name = db.Column(db.String(45))
    Description = db.Column(db.String(255))
    Active = db.Column(db.INT)
    CreatedBy = db.Column(db.String(45))
    ModifiedBy = db.Column(db.String(45))
    CreatedDate = db.Column(db.DATETIME)
    ModifiedDate =db.Column(db.DATETIME)
    ModNum   = db.Column(db.INT)


    def __init__(self,
                 Id,
                 Name,
                 Description,
                 Active,
                 CreatedBy,
                 ModifiedBy,
                 CreatedDate,
                 ModifiedDate,
                 ModNum,
                 ):
        self.Id = Id
        self.Name = Name
        self.Description = Description
        self.Active = Active
        self.CreatedBy = CreatedBy
        self.ModifiedBy = ModifiedBy
        self.CreatedDate = CreatedDate
        self.ModifiedDate = ModifiedDate
        self.ModNum = ModNum
    # To convert the data from list to json
    def json(self):
        return {
            'Id':self.Id,
            'Name':self.Name,
            'Description':self.Description,
            'Active':self.Active,
            'CreatedBy':self.CreatedBy,
            'ModifiedBy':self.ModifiedBy,
            'CreatedDate':str(self.CreatedDate),
            'ModifiedDate':str(self.ModifiedDate),
            'ModNum':self.ModNum
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
        return ChecklistModel.query.order_by(ChecklistModel.Id).all()
from .. import db


class WOChecklistModel(db.Model):
    __tablename__ = 'is_WOCheckList'
    Active = db.Column(db.INT)
    ClonedFrom = db.Column(db.TEXT)
    CreatedBy = db.Column(db.String(45))
    Currency = db.Column(db.String(45))
    Description = db.Column(db.TEXT)
    Include = db.Column(db.INT)
    LastModifiedBy = db.Column(db.String(45))
    Owner = db.Column(db.String(45))
    Product = db.Column(db.String(45))
    RecordType = db.Column(db.String(45))
    Status = db.Column(db.String(45))
    StepName = db.Column(db.String(80))
    WorkOrderId = db.Column(db.String(80), db.ForeignKey('is_WorkOrder.id'))
    Id = db.Column(db.Integer, primary_key=True)


    def __init__(self,
                    Active,
                    ClonedFrom,
                    CreatedBy,
                    Currency,
                    Description,
                    Include,
                    LastModifiedBy,
                    Owner,
                    Product,
                    RecordType,
                    Status,
                    StepName,
                    WorkOrderId,
                    Id,
                 ):
        self.Active = Active
        self.ClonedFrom = ClonedFrom
        self.CreatedBy = CreatedBy
        self.Currency = Currency
        self.Description = Description
        self.Include = Include
        self.LastModifiedBy = LastModifiedBy
        self.Owner = Owner
        self.Product = Product
        self.RecordType = RecordType
        self.Status = Status
        self.StepName = StepName
        self.WorkOrderId = WorkOrderId
        self.Id = Id

    # To convert the data from list to json
    def json(self):
        return {
            'Active': self.Active,
            'ClonedFrom': self.ClonedFrom,
            'CreatedBy': self.CreatedBy,
            'Currency': self.Currency,
            'Description': self.Description,
            'Include': self.Include,
            'LastModifiedBy': self.LastModifiedBy,
            'Owner': self.Owner,
            'Product': self.Product,
            'RecordType': self.RecordType,
            'Status': self.Status,
            'StepName': self.StepName,
            'WorkOrderId': self.WorkOrderId,
            'Id': self.Id
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
        return WOChecklistModel.query.order_by(WOChecklistModel.Id).all()

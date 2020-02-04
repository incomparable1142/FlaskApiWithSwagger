from .. import db
from sqlalchemy.exc import SQLAlchemyError


class WorkOrderModel(db.Model):
    __tablename__ = 'is_WorkOrder'
    Id = db.Column(db.String(45), primary_key=True)
    Account = db.Column(db.String(45))
    Asset = db.Column(db.String(45))
    BusinessHours = db.Column(db.String(45))
    Contact = db.Column(db.String(45))
    CreatedBy = db.Column(db.String(45))
    CreatedDate =db.Column(db.DATETIME)
    Description = db.Column(db.TEXT)
    Discount = db.Column(db.String(45))
    Duration = db.Column(db.INTEGER)
    DurationType = db.Column(db.String(45))
    GrandTotal = db.Column(db.String(45))
    LastModifiedBy = db.Column(db.String(45))
    LastModifiedByDate =db.Column(db.DATETIME)
    LineItemCount = db.Column(db.String(45))
    Owner = db.Column(db.String(45))
    PriceBook = db.Column(db.String(45))
    Product = db.Column(db.String(45))
    ServiceRequest = db.Column(db.String(45))
    Status = db.Column(db.String(45))
    Subject = db.Column(db.String(80))
    TotalPrice = db.Column(db.String(45))
    #workOrders = db.relationship('WorkOrderModel', lazy='dynamic')


    def __init__(self,
                 Id,
                 Account,
                 Asset,
                 BusinessHours,
                 Contact,
                 CreatedBy,
                 CreatedDate,
                 Description,
                 Discount,
                 Duration,
                 DurationType,
                 GrandTotal,
                 LastModifiedBy,
                 LastModifiedByDate,
                 LineItemCount,
                 Owner,
                 PriceBook,
                 Product,
                 ServiceRequest,
                 Status,
                 Subject,
                 TotalPrice,
                 ):
        self.Account = Account
        self.Asset = Asset
        self.BusinessHours = BusinessHours
        self.Contact = Contact
        self.CreatedBy = CreatedBy
        self.CreatedDate = CreatedDate
        self.Description = Description
        self.Discount = Discount
        self.Duration = Duration
        self.DurationType = DurationType
        self.GrandTotal = GrandTotal
        self.LastModifiedBy = LastModifiedBy
        self.LastModifiedByDate = LastModifiedByDate
        self.LineItemCount = LineItemCount
        self.Owner = Owner
        self.PriceBook = PriceBook
        self.Product = Product
        self.ServiceRequest = ServiceRequest
        self.Status = Status
        self.Subject = Subject
        self.TotalPrice = TotalPrice
        self.Id = Id

    # To convert the data from list to json
    def json(self):
        return {'Id': self.Id,
                'Account': self.Account,
                'Asset': self.Asset,
                'BusinessHours': self.BusinessHours,
                'Contact': self.Contact,
                'CreatedBy': self.CreatedBy,
                'CreatedDate': str(self.CreatedDate),
                'Description': self.Description,
                'Discount': self.Discount,
                'Duration': self.Duration,
                'DurationType': self.DurationType,
                'GrandTotal': self.GrandTotal,
                'LastModifiedBy': self.LastModifiedBy,
                'LastModifiedByDate': str(self.LastModifiedByDate),
                'LineItemCount': self.LineItemCount,
                'Owner': self.Owner,
                'PriceBook': self.PriceBook,
                'Product': self.Product,
                'ServiceRequest': self.ServiceRequest,
                'Status': self.Status,
                'Subject': self.Subject,
                'TotalPrice': self.TotalPrice
                }

    @classmethod
    def find_by_id(cls, Id):
        return cls.query.filter_by(Id=Id).first()

    def save_to_db(self):
        db.session.add(self)
        try:
            db.session.commit()
        except SQLAlchemyError as e:
            print(str(e))
            db.session.rollback()
            raise

    def delete_from_db(self):
        db.session.delete(self)
        try:
            db.session.commit()
        except SQLAlchemyError as e:
            print(str(e))
            db.session.rollback()
            raise

    @classmethod
    def get_all(cls):
        return WorkOrderModel.query.order_by(WorkOrderModel.Id).all()
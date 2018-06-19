# from datetime import datetime
# from app import db
# class Qqnums(db.Model):
#     __tablename__="qqnums"
#     id=db.Column(db.Integer,primary_key=True)
#     qqnum=db.Column(db.String(11),unique=True)
#     add_date=db.Column(db.DateTime,index=True,default=datetime.now)
    
#     def __init__(self, qqnum, add_date=None):
#         self.qqnum=qqnum
#         self.add_date=add_date
        

#     def __repr__(self):
#         return '<Qqnums %r>' % self.title


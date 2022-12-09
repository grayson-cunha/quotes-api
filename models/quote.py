import datetime
import mongoengine as mongo

from models import Users

class Quotes(mongo.Document):
  text = mongo.StringField()
  user = mongo.ReferenceField(Users, required=True)
  created_at = mongo.DateField(default=datetime.datetime.now)
  
  
  def to_dict(self):
    return {
      "id": str(self.pk),
      "text": self.text,
      "user": self.user,
      "created_at": self.created_at
    }

import mongoengine as mongo
import datetime

class User(mongo.Document):
  name = mongo.StringField()
  email = mongo.StringField()
  hash_password = mongo.StringField()
  created_at = mongo.DateField(default=datetime.datetime.now)
  
  
  def to_dict(self):
    return {
      "id": str(self.pk),
      "name": self.name,
      "email": self.email,
      "created_at": self.created_at
    }

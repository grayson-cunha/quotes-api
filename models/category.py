import mongoengine as mongo

class Categories(mongo.Document):
  name = mongo.StringField()
  color = mongo.StringField()

  def to_dict(self):
    return {
      "id": str(self.pk),
      "name": self.name,
      "color": self.color
    }

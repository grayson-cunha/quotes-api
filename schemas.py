from marshmallow import Schema, fields

class CategorySchema(Schema):
  id = fields.Str(dump_only=True)
  name = fields.Str(required=True)
  color = fields.Str(required=True)

class CategoryUpdateSchema(Schema):
  name = fields.Str()
  color = fields.Str()

class UserSchema(Schema):
  id = fields.Str(dump_only=True)
  name = fields.Str(required=True)
  email = fields.Str(required=True)
  
class UserUpdateSchema(Schema):
  name = fields.Str()
  email = fields.Str()

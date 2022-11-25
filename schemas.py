from marshmallow import Schema, fields

class CategorySchema(Schema):
  id = fields.Str(dump_only=True)
  name = fields.Str(required=True)
  color = fields.Str(required=True)

class CategoryUpdateSchema(Schema):
  name = fields.Str()
  color = fields.Str()

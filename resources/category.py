from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import CategorySchema, CategoryUpdateSchema
from models import Categories

blp = Blueprint("Categories", __name__, url_prefix="/categories", description="Operations on categories")

@blp.route("/")
class CategoriesResource(MethodView):
  @blp.response(200, CategorySchema(many=True))
  def get(self):
    categories = Categories.objects()
    return categories
  
  @blp.arguments(CategorySchema)
  @blp.response(201, CategorySchema)
  def post(self, new_categorie):
    category = Categories(**new_categorie).save()
    
    return category.to_dict()

@blp.route("/<string:category_id>")
class CategoriesByIdResource(MethodView):
  @blp.arguments(CategoryUpdateSchema)
  @blp.response(200, CategorySchema)
  def put(self, category_data, category_id):
    category = Categories.objects(id=category_id).first()
    
    if not category:
      abort(404, "Category not found")
  
    category.update(**category_data)
    category.reload()
    return category.to_dict()
  
  @blp.response(200, CategorySchema)
  def delete(self, category_id):
    category = Categories.objects(id=category_id).first()
    
    if not category:
      abort(404, "Category not found")
      
    category.delete()
    return category.to_dict()

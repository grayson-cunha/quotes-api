from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import UserSchema, UserUpdateSchema
from models import User

blp = Blueprint("Users", __name__, url_prefix="/users", description="Operations on users")

@blp.route("/")
class CategoriesResource(MethodView):
  @blp.arguments(UserSchema)
  @blp.response(201, UserSchema)
  def post(self, new_user):
    user = User(**new_user).save()
    
    return user.to_dict()


@blp.route("/<string:user_id>")
class CategoriesResource(MethodView):
  @blp.arguments(UserUpdateSchema)
  @blp.response(200, UserSchema)
  def put(self, user_data, user_id):
    user = User.objects(id=user_id).first()
    
    if not user:
      abort(404, "User not found")
  
    user.update(**user_data)
    user.reload()
    return user.to_dict()

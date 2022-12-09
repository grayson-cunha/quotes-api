from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import QuoteSchema, UpdateQuoteSchema
from models import Quotes

blp = Blueprint("Quotes", __name__, url_prefix="/quotes", description="Operations on quotes")

class QuotesResource(MethodView):
  
  @blp.arguments(QuoteSchema)
  @blp.response(201, QuoteSchema)
  def post(self, new_quote):
    quote = Quotes(**new_quote).save()
    
    return quote
  
class QuotesByUserResource:
  pass

@blp.route("<string:quote_id>")
class QuotesByIdResource(MethodView):
  @blp.arguments(UpdateQuoteSchema)
  @blp.response(200, QuoteSchema)
  def put(self, quote_id, quote_data):
    quote = Quotes.objects(id=quote_id).first()
    
    if not quote:
      abort(404, "Quote not found")
  
    quote.update(**quote_data)
    quote.reload()
    return quote.to_dict()

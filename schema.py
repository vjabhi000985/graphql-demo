import strawberry
from model import predict_price

@strawberry.type
class PredictResult:
  sqft: float
  predict_price: float

@strawberry.type
class Query:
  hello: str = "GraphQL ML API is running!"

@strawberry.type 
class Mutation:
  @strawberry.mutation
  def predict(sqft:float) -> PredictResult:
    price = predict_price(sqft)
    return PredictResult(sqft=sqft, predict_price=price)

schema = strawberry.Schema(query=Query, mutation=Mutation)

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from schema import schema

graphql_app = GraphQLRouter(schema=schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def root():
  return {"info": "Visit /graphql for ML GraphQL Playground"}
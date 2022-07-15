import os
import uvicorn
from fastapi import FastAPI
from app.db.database import engine
from app.db import models
from app.api import crud

description = """
This API will let you perform CRUD operations inside a Postgres DB that saves data about the busiest air routes.

Route ID will be "ORG-DST" as for Origin and Destiny.
"""

tags_metadata = [
    {
        "name": "CRUD",
        "description": "Database CRUD operations.",
    }
]

app = FastAPI(
    title="Busiest Air Routes",
    description=description,
    docs_url="/",
    version="latest",
    contact={
        "name": "Github",
        "url": "https://github.com/LucasLivrone/busiest-air-routes"
    },
    openapi_tags=tags_metadata,
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,  # Used to hide Schemas at Docs site
        "showExtensions": False
    }
)

models.Routes.metadata.create_all(bind=engine)


@app.get("/GET/{route}", tags=["CRUD"])
async def read_number_of_flights_for_a_specific_route(route: str):
    return crud.get_route(route)


@app.get("/GET/all/routes", tags=["CRUD"])
async def read_number_of_flights_for_all_routes():
    return crud.get_all_routes()


@app.put("/POST/{route}", tags=["CRUD"])
async def create_a_specific_route_flight_record(route: str):
    return crud.create_route(route)


@app.put("/PUT/{route}", tags=["CRUD"])
async def update_a_specific_route_flight_record(route: str):
    return crud.update_route(route)


# @app.delete("/DELETE/{route}", tags=["CRUD"])
# async def delete_a_specific_route(route):
#     return True


# if __name__ == "__main__":  # pragma: no cover
#     port = int(os.environ.get("PORT", default=80))
#     uvicorn.run("main:app", host="0.0.0.0", port=port)
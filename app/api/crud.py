from app.db.database import db
from app.db import models
from fastapi import HTTPException


def get_route(route):
    existing_route = db.query(models.Routes).filter(models.Routes.route == route).first()
    if not existing_route:
        raise HTTPException(status_code=404, detail=f"The route {route} is not found.")
    else:
        return existing_route


def get_all_routes():
    return db.query(models.Routes).all()


def create_route(route):
    existing_route = db.query(models.Routes).filter(models.Routes.route == route).first()
    if not existing_route:
        new_route = models.Routes(route=route, flights=1)
        db.add(new_route)
        db.commit()
        db.refresh(new_route)
        return f"The route {route} has been added to the database."
    else:
        raise HTTPException(status_code=400, detail=f"The route {route} already exists.")


def update_route(route):
    existing_route = db.query(models.Routes).get(route)
    if existing_route:
        new_flights = existing_route.flights + 1
        existing_route.flights = new_flights
        db.commit()
        return f"The route {route} has been updated."
    else:
        raise HTTPException(status_code=404, detail=f"The route {route} is not found.")


def delete_route(route):
    existing_route = db.query(models.Routes).get(route)
    if existing_route:
        db.delete(existing_route)
        db.commit()
        return f"The route {route} has been deleted."
    else:
        raise HTTPException(status_code=404, detail=f"The route {route} is not found.")
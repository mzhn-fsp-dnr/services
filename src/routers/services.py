from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.helpers.services_helpers import (
    create_service,
    get_service,
    delete_service,
    get_services,
    update_service,
)
from src.schemas.service import ServiceSchema, ServiceCreate
from .. import database


router = APIRouter(
    prefix="/services", tags=["services"], responses={404: {"description": "Not Found"}}
)


@router.post("/", response_model=ServiceSchema)
def create_new_service(
    service_create: ServiceCreate, db: Session = Depends(database.get_db)
):
    return create_service(db, service_create)


# Get a single service by ID
@router.get("/{service_id}", response_model=ServiceSchema)
def read_service(service_id: UUID, db: Session = Depends(database.get_db)):
    return get_service(db, service_id)


# Get all services (optionally filter by parent_id)
@router.get("/", response_model=List[ServiceSchema])
def read_services(
    parent_id: Optional[UUID] = None, db: Session = Depends(database.get_db)
):
    return get_services(db, parent_id)


# Update a service by ID
@router.put("/{service_id}", response_model=ServiceSchema)
def update_existing_service(
    service_id: UUID,
    service_data: ServiceCreate,
    db: Session = Depends(database.get_db),
):
    return update_service(db, service_id, service_data)


# Delete a service by ID
@router.delete("/{service_id}")
def delete_existing_service(service_id: UUID, db: Session = Depends(database.get_db)):
    delete_service(db, service_id)
    return {"msg": "Service deleted successfully"}

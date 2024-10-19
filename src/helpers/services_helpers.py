from typing import List, Optional
from uuid import UUID
from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.models.service import Service
from src.schemas.service import ServiceCreate, ServiceSchema


def create_service(db: Session, service_create: ServiceCreate) -> ServiceSchema:
    new_service = Service(name=service_create.name, parent_id=service_create.parent_id)
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return ServiceSchema.from_orm(new_service)


def get_service(db: Session, service_id: UUID) -> ServiceSchema:
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return ServiceSchema.from_orm(service)


def get_services(db: Session, parent_id: Optional[UUID] = None) -> List[ServiceSchema]:
    query = db.query(Service)
    if parent_id:
        query = query.filter(Service.parent_id == parent_id)
    else:
        query = query.filter(Service.parent_id == None)

    services = query.all()
    return [ServiceSchema.from_orm(service) for service in services]


def update_service(
    db: Session, service_id: UUID, service_data: ServiceCreate
) -> ServiceSchema:
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    service.name = service_data.name
    service.parent_id = service_data.parent_id

    db.commit()
    db.refresh(service)
    return ServiceSchema.from_orm(service)


def delete_service(db: Session, service_id: UUID) -> None:
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    db.delete(service)
    db.commit()

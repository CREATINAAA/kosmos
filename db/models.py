from sqlalchemy import Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.types import JSON
from typing import Any


Base = DeclarativeBase

class Model(Base):
    type_annotation_map = {
        dict[str, Any]: JSON
    }


class SkorozvonOrm(Model):
    __tablename__ = "skorozvon"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[str]

    lead_id: Mapped[int] 
    lead_name: Mapped[str] 
    lead_comment: Mapped[str] 
    lead_post: Mapped[str] 
    lead_city: Mapped[str] 
    lead_business: Mapped[str] 
    lead_homepage: Mapped[str] 
    lead_emails: Mapped[str]  
    lead_inn: Mapped[str] 
    lead_kpp: Mapped[str] 
    lead_created_at: Mapped[str] 
    lead_updated_at: Mapped[str] 
    lead_deleted_at: Mapped[str] 
    lead_parent_lead_id: Mapped[str] 
    lead_tags: Mapped[list[str]] = mapped_column(ARRAY(String)) 
    lead_phones: Mapped[str] 

    contact_id: Mapped[str]
    contact_name: Mapped[str]
    contact_comment: Mapped[str]
    contact_post: Mapped[str]
    contact_city: Mapped[str]
    contact_business: Mapped[str]
    contact_homepage: Mapped[str]
    contact_emails: Mapped[str]
    contact_inn: Mapped[str]
    contact_kpp: Mapped[str]
    contact_created_at: Mapped[str]
    contact_updated_at: Mapped[str]
    contact_deleted_at: Mapped[str]
    contact_parent_lead_id: Mapped[str]
    contact_tags: Mapped[str]
    contact_address: Mapped[str]
    contact_phones: Mapped[str]

    call_id: Mapped[int]
    call_phone: Mapped[str]
    call_source: Mapped[str]
    call_direction: Mapped[str]
    call_params: Mapped[dict[str, Any]]
    call_lead_id: Mapped[int]
    call_organization_id: Mapped[int]
    call_user_id: Mapped[int]
    call_started_at: Mapped[str]
    call_connected_at: Mapped[str]
    call_ended_at: Mapped[str]
    call_reason: Mapped[str]
    call_duration: Mapped[int]
    call_scenario_id: Mapped[int]
    call_result_id: Mapped[int]
    call_incoming_phone: Mapped[str]
    call_recording_url: Mapped[str]
    call_call_type: Mapped[str]
    call_region: Mapped[str]
    call_local_time: Mapped[str]
    call_call_project_id: Mapped[int]
    call_call_project_title: Mapped[str]
    call_scenario_result_group_id: Mapped[int]
    call_scenario_result_group_title: Mapped[str]

    call_result_result_id: Mapped[int]
    call_result_result_name: Mapped[str]
    call_result_comment: Mapped[str]

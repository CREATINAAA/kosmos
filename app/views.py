import json
import logging

from ..service.exceptions import FieldsAreEmpty, InvalidLeadId

from ..db.repositories import SkorozvonRepository
from ..facades.leadvertex import leadvertex_api


def logic(request):
    try:
        leadvertex_api.send_lead(request)
    except (FieldsAreEmpty, InvalidLeadId) as e:
        return (f"Warning! {e}")
    SkorozvonRepository.add_one(request)
    return {"message": "Webhook processed"}
        
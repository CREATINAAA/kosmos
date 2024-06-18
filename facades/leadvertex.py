from ..service.exceptions import FieldsAreEmpty
from ..app import conf
import requests
from .skorozvon import skorozvon_api
from ..service.logger import log_response, log_request
from urllib.parse import urlencode


class LeadvertexAPI():
    def __init__(self) -> None:
        self.token = conf.LEADVERTEX_TOKEN
        self.webmaster_id = conf.LEADVERTEX_ID
        self.url = "https://basedlt.leadvertex.ru/api/webmaster/v2/addOrder.html?webmasterID=2&token=4RFV-5Tgb"
        self.sk_id_leadvert_id = {
            "134548": 72247,
            "152316": 77147,
            "163243": 81685,
            "123997": 87526,
            "125190": 70907,
            "123630": 70802,
            "162422": 80979,
            "135040": 70805,
            "162721": 84652,
            "160214": 84654,
            "169348": 86874,
            "161656": 84656,
            "163276": 81951,
            "153714": 77494,
            "135485": 77403,
            "166685": 84663,
            "167177": 82932,
            "169960": 83871,
            "169962": 83873,
            "162958": 72478,
            "161176": 80959,
            "138309": 77497,
            "125190": 72178,
            "159459": 80380,
            "175438": 85774,
            "175575": 85799,
            "182414": 87753,
            "182965": 87940,
            "186001": 90716,
            "181825": 83869,
            "186477": 88813,
            "189963": 90070,
            "189964": 90071,
            "190780": 90440,
            "191136": 90588,
            "185581": 89833,
            "191913": 90835,
            "192089": 90961,
            "192779": 91110,
            "192474": 91044,
            "192753": 91173,
            "198256": 93036,
            "200662": 93833,
            "203587": 94714,
            "206240": 95419,
            "205939": 86874,
            "207069": 95732,
            "208647": 93658,
            "207793": 96399,
            "211164": 97019,
            "211167": 97023,
            "208094": 96065,
            "210715": 96831,
        }
    
    def send_lead(self, request):
        skorozvon_leads = skorozvon_api.get_request(f"leads/{request.lead_id}/")
        print(skorozvon_leads)
        if request.lead_name is None:
            raise FieldsAreEmpty("Field lead_name is empty!")
        elif skorozvon_leads.get('phones') is None:
            raise FieldsAreEmpty("Field phone is empty!")
        elif request.call_user_id is None:
            raise FieldsAreEmpty("Field call_user_id is empty!")
        
        encoded_data = urlencode({
            "fio": request.lead_name,
            "phone": skorozvon_leads.get('phones'),
            "comment": request.lead_comment,
            "operatorID": self.sk_id_leadvert_id[f"{request.call_user_id}"],
        })
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        log_request(dict(request), request)
        response = requests.post(url=self.url, headers=headers, data=encoded_data)
        log_response(response.status_code, response.json())
        return response.json()
    
    
leadvertex_api = LeadvertexAPI()

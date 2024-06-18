from pathlib import Path
import os
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.environ.get("DATABASE_URL")

LEADVERTEX_TOKEN = os.environ.get("LEADVERTEX_TOKEN")
LEADVERTEX_ID = os.environ.get("LEADVERTEX_ID")

SKOROZVON_USERNAME = os.environ.get("SKOROZVON_USERNAME")
SKOROZVON_API_KEY = os.environ.get("SKOROZVON_API_KEY")
SKOROZVON_CLIENT_ID = os.environ.get("SKOROZVON_CLIENT_ID")
SKOROZVON_CLIENT_SECRET = os.environ.get("SKOROZVON_CLIENT_SECRET")

DOLPHILOL_API_KEY = os.environ.get("DOLPHILOL_API_KEY")
DOLPHILOL_NAME = os.environ.get("DOLPHILOL_NAME")

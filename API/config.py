import os
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()


SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-if-missing")
DEBUG = os.getenv("DEBUG", "False") == "True"
# Puedes añadir más configuraciones aquí si lo necesitas

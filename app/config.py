from dotenv import load_dotenv
import os


load_dotenv('C:/Users/Pom4ek/Projects/Archi-Backend/app/.env')


# database
DATABASE_USERNAME = os.environ.get("DATABASE_USERNAME")
DATABASE_PASS = os.environ.get("DATABASE_PASS")
DATABASE_HOST = os.environ.get("DATABASE_HOST")
DATABASE_PORT = os.environ.get("DATABASE_PORT")
DATABASE_URL = f'postgresql://{DATABASE_USERNAME}:{DATABASE_PASS}@{DATABASE_HOST}:{DATABASE_PORT}'

# tokens
SECRET = str(os.environ.get("TOKEN")) # looks like: b17c9c662c64c82fa50ecd8cade20720e427dd1b9938ff40844f90e6a3e63d7e
SECRET_ALGORITHM = str(os.environ.get("SECRET_ALGORITHM"))
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.environ.get("REFRESH_TOKEN_EXPIRE_DAYS"))
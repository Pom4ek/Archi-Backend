from dotenv import load_dotenv
import os


load_dotenv()


DATABASE_USERNAME = os.environ.get("DATABASE_USERNAME")
DATABASE_PASS = os.environ.get("DATABASE_PASS")
DATABASE_HOST = os.environ.get("DATABASE_HOST")
DATABASE_PORT = os.environ.get("DATABASE_PORT")
DATABASE_URL = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASS}@{DATABASE_HOST}:{DATABASE_PORT}"

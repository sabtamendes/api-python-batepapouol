from dotenv import load_dotenv

load_dotenv()

from os import getenv

ENV = getenv("ENV")
IS_TEST_ENV = ENV and ENV in ("test") # test é o valor da variável de ambiente no .env
db_hostname = getenv("DATABASE_HOST")
db_port = getenv("DATABASE_PORT")
db_password = getenv("DATABASE_PASSWORD")
db_name = getenv("DATABASE_NAME")
db_user = getenv("DATABASE_USERNAME")

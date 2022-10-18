HOSTNAME="database-1-instance-1.cyreumlnhmm6.eu-west-1.rds.amazonaws.com/warehouse"
PORT=5432
USERNAME="postgres"
PASSWORD="jacaranda"
dbschema= 'dw,public'
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOSTNAME}"

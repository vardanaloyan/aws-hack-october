from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

from config import *

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'options': '-csearch_path={}'.format(dbschema)}
)
# from sqlalchemy import inspect
# inspector = inspect(engine)
# schemas = inspector.get_schema_names()
#
# for schema in schemas:
#     print("schema: %s" % schema)
#     for table_name in inspector.get_table_names(schema=schema):
#         for column in inspector.get_columns(table_name, schema=schema):
#             print("Column: %s" % column)



Base = automap_base()
Base.prepare(engine, reflect=True)

Facility = Base.classes.facility
session = Session(engine)

res = session.query(Facility).first()
print(res.facility_name)

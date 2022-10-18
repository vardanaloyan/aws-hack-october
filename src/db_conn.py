from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import Table
from sqlalchemy import MetaData, Column, Integer
from config import *
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import Executable, ClauseElement

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



metadata = MetaData(engine)
v = Table('mum_digital_record', metadata, autoload=True)

Session = sessionmaker(bind=engine)
session = Session()
recs = session.query(v).filter_by(mum_key=38936893).all()

# for r in engine.execute(v.select().fetch(10)):
#     print (r)

# Base = automap_base()
# Base.prepare(engine, reflect=True)
#
# Facility = Base.classes.mum_digital_record
# session = Session(engine)
#
# res = session.query(Facility).first()
# print(res.facility_name)

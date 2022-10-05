from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql://root@127.0.0.1/fastapistruktur")
meta = MetaData()
conn = engine.connect()

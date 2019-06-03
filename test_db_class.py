from libraries.db_lib import db_handler
from static.db_schema import tables

handler = db_handler()
handler.connect()
handler.create_db('Test')
handler.use_db('Test')
handler.drop_table('Cities')
handler.create_table(tables)
handler.write_in_table("Cities (city) values ('Roma')")
print(handler.select_all('Cities'))
handler.close_conn()
from peewee import *

database = SqliteDatabase('captchadb.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class RunBruteForce(BaseModel):
    id = TextField(primary_key=True)
    number_of_tried = IntegerField()

    class Meta:
        table_name = 'RUN_BRUTE_FORCE'


if __name__=="__main__":
    records = RunBruteForce.select().where(RunBruteForce.id==1).dicts().execute()
    if records is None:
        print(len(records))
    for record in records:
        print(record)
    print(records[0])

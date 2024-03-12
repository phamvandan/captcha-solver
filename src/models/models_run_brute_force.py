from pydantic import BaseModel
# import sqlite3
import models.orm_models as orm_models

class RunBruteForce(BaseModel):
    id: str
    number_of_tried: int

# insert 
def insert_run_brute_force(data: RunBruteForce):
    orm_models.RunBruteForce.replace(**data.dict()).execute()

# get record by id
def get_run_brute_force_by_id(id: str):
    records = orm_models.RunBruteForce.select().where(orm_models.RunBruteForce.id==id).dicts().execute()
    return records

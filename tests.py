import peewee
from Peewee import Peewee

# create the database
database = Peewee().create_database("Database.db")

# create the class Example with fields id and level
class Example(peewee.Model):
  id,level=Peewee().fields()["autofield"](),Peewee().fields()["int"]()
  class Meta:
    database = database

# initiate the table
Peewee().create_table(Example)

# create some examples
Example(level=100).save()

Example(level=120).save()

Example(level=200).save()

# select the objects created
print(list(Example.select()))

# select the objects created where the level is over 110
print(list(Example.select().where(Example.level > 110)))

# drop the table
Peewee().drop_table(Example)

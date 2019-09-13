import peewee

class Peewee:
  create_database=lambda self,name: peewee.SqliteDatabase(name)
  create_table=lambda self,x: x.create_table()
  drop_table=lambda self,x: x.drop_table()
  fields=lambda self: {"foreignkey":peewee.ForeignKeyField,"manytomany":peewee.ManyToManyField,"primarykey":peewee.PrimaryKeyField,"autofield":peewee.AutoField,"char":peewee.CharField,"int":peewee.IntegerField,"float":peewee.FloatField,"bigint":peewee.BigIntegerField,"datetime":peewee.DateTimeField,"blob":peewee.BlobField,}

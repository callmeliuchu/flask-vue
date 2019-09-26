from playhouse.db_url import connect
from playhouse.signals import Model
import peewee
from datetime import datetime

local = 'mysql://root:root@localhost:3306/moments?charset=utf8'

db = connect(local)


class Moment(Model):
    pid = peewee.CharField(max_length=36,primary_key=True)
    orgId = peewee.CharField(max_length=36)
    title = peewee.CharField(max_length=200)
    createTime = peewee.DateTimeField(
        formats='%Y-%m-%d %H:%M:%S',
        default=datetime.now
    )

    class Meta:
        database = db
        db_table = 'core_moment'

class MomentTag(Model):
    pid = peewee.CharField(max_length=36,primary_key=True)
    orgId = peewee.CharField(max_length=36)
    title = peewee.CharField(max_length=200)


    class Meta:
        database = db
        db_table = 'core_moment_tag'




# for v in Moment.select().dicts():
#     print(v)

# r = MomentTag.select().where(MomentTag.title % '%{}%'.format('朋友圈'))
# for v in r:
#     print(v.title)

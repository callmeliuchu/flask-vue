import peewee
from peewee import Model          # peewee提供的基础类，一个Model就对应一个数据库
from peewee import SqliteDatabase      # 我使用sqlite做展示，peewee支持常见的MySQL、PostgreSQL等等多种数据库
from datetime import datetime
from playhouse.shortcuts import model_to_dict



db = SqliteDatabase('/home/liuchu/flask-vue-crud/flaskbb.sqlite')


class Posts(Model):
    id = peewee.IntegerField()
    topic_id = peewee.IntegerField()
    user_id = peewee.IntegerField()
    type = peewee.IntegerField()
    username = peewee.CharField(max_length=200)
    content = peewee.TextField()
    belong_to_post_id = peewee.IntegerField()
    date_created = peewee.DateTimeField(
        formats='%Y-%m-%d %H:%M:%S',
        default=datetime.now
    )

    class Meta:
        database = db
        db_table = 'posts'


class Categories(Model):
    id = peewee.IntegerField()
    title = peewee.CharField(max_length=255)


    class Meta:
        database = db
        db_table = 'categories'



class Topic(Model):
    id = peewee.IntegerField()
    forum_id = peewee.IntegerField()
    title = peewee.CharField(max_length=200)
    description = peewee.TextField()


    class Meta:
        database = db
        db_table = 'topics'



class Forum(Model):
    id = peewee.IntegerField()
    category_id = peewee.IntegerField()
    title = peewee.CharField(max_length=200)


    class Meta:
        database = db
        db_table = 'forums'


def create_table(table):
    u"""
    如果table不存在，新建table
    """
    if not table.table_exists():
        table.create_table()

def drop_table(table):
    u"""
    table 存在，就删除
    """
    if table.table_exists():
        table.drop_table()




def get_topic_posts(topic_id):
    data = {}
    v = Topic.select().where(Topic.id == topic_id).first()
    data['topic'] = model_to_dict(v)
    r = Posts.select().where(Posts.topic_id == topic_id).group_by(Posts.belong_to_post_id)
    ids = [v.belong_to_post_id for v in r]
    data['posts'] = []
    for b_id in ids:
        v = Posts.select().where(Posts.type.in_([6,1])).where(Posts.belong_to_post_id == b_id).order_by(Posts.id.desc()).first()
        data['posts'].append(model_to_dict(v))
    return data




from collections import defaultdict



def get_topic_tree():
    dict1 = defaultdict(list)
    for topic in Topic.select():
        topic_dict = model_to_dict(topic)
        topic_dict['name'] = topic.title
        dict1[topic.forum_id].append(topic_dict)


    dict2 = defaultdict(list)
    for forum in Forum.select():
        forum_dict = model_to_dict(forum)
        forum_dict['name'] = forum.title
        forum_dict['children'] = dict1[forum.id]
        dict2[forum.category_id].append(forum_dict)


    final_list = []
    for category in Categories.select():
        category_dict = model_to_dict(category)
        category_dict['name'] = category.title
        category_dict['children'] = dict2[category.id]
        final_list.append(category_dict)


    return final_list








# r = Categories.select().order_by(Categories.id)
#
#
# for v in r:
#     print(v.id,v.title)
#     forums = Forum.select().where(Forum.category_id == v.id)
#     for forum in forums:
#         print('  ',forum.id,forum.category_id,forum.title)


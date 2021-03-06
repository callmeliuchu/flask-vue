import peewee
from peewee import Model          # peewee提供的基础类，一个Model就对应一个数据库
from peewee import SqliteDatabase      # 我使用sqlite做展示，peewee支持常见的MySQL、PostgreSQL等等多种数据库
from datetime import datetime
from playhouse.shortcuts import model_to_dict



db = SqliteDatabase('../../flask-forum/flaskbb.sqlite')


class Posts(Model):
    id = peewee.IntegerField()
    topic_id = peewee.IntegerField()
    user_id = peewee.IntegerField()
    type = peewee.IntegerField()
    username = peewee.CharField(max_length=200)
    content = peewee.TextField()
    belong_to_post_id = peewee.IntegerField()
    parent_post_id = peewee.IntegerField()
    title = peewee.CharField(max_length=255)
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


# create table topics
# (
#   hidden        BOOLEAN,
#   hidden_at     DATETIME,
#   id            INTEGER      not null
#     constraint pk_topics
#     primary key,
#   forum_id      INTEGER      not null
#     constraint fk_topics_forum_id_forums
#     references forums
#       on delete cascade,
#   title         VARCHAR(255) not null,
#   description   TEXT         not null,
#   user_id       INTEGER
#     constraint fk_topics_user_id_users
#     references users,
#   username      VARCHAR(200) not null,
#   date_created  DATETIME     not null,
#   last_updated  DATETIME     not null,
#   locked        BOOLEAN      not null,
#   important     BOOLEAN      not null,
#   views         INTEGER      not null,
#   post_count    INTEGER      not null,
#   first_post_id INTEGER
#     constraint fk_topics_first_post_id_posts
#     references posts
#       on delete cascade,
#   last_post_id  INTEGER
#     constraint fk_topics_last_post_id_posts
#     references posts,
#   hidden_by_id  INTEGER
#     constraint fk_Topic_hidden_by
#     references users,
#   check (hidden IN (0, 1)),
#   check (important IN (0, 1)),
#   check (locked IN (0, 1))
# );
class Topic(Model):
    id = peewee.IntegerField()
    forum_id = peewee.IntegerField()
    title = peewee.CharField(max_length=200)
    description = peewee.TextField()
    hidden = peewee.BooleanField(default=False)
    hidden_at = peewee.DateTimeField(default=datetime.now())
    user_id = peewee.IntegerField()
    username = peewee.CharField(max_length=200)
    date_created = peewee.DateTimeField(default=datetime.now())
    last_updated = peewee.DateTimeField(default=datetime.now())
    locked = peewee.BooleanField(default=False)
    important = peewee.BooleanField(default=False)
    views = peewee.IntegerField(default=0)
    post_count = peewee.IntegerField(default=0)
    first_post_id = peewee.IntegerField(default=-1)
    last_post_id = peewee.IntegerField(default=-1)
    hidden_by_id = peewee.IntegerField(default=-1)
    is_deleted = peewee.IntegerField(default=0)




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



class PostTypeCategory(Model):
    id = peewee.IntegerField()
    category = peewee.IntegerField()
    type = peewee.IntegerField()
    desc = peewee.CharField(max_length=200)


    class Meta:
        database = db
        db_table = 'post_type_category'



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
    for topic in Topic.select().where(Topic.is_deleted == 0):
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




def get_posts_struct(post_id):
    r = PostTypeCategory.select()
    type2category = {}
    for v in r:
        type2category[v.type] = v.category



    r = Posts.select().where(Posts.belong_to_post_id == post_id).order_by(Posts.id)

    parent_children = defaultdict(list)
    posts = {}

    for v in r:
        post_dict = model_to_dict(v)
        parent_children[v.parent_post_id].append(post_dict)
        posts[v.id] = post_dict

    arr = []
    while True:

        children = parent_children[post_id]
        post_info = defaultdict(list)
        main_post = posts[post_id]
        post_info['post_main'].append(main_post)
        has_next_parent = False
        for child in children:
            if child['type'] == 6:
                post_id = child['id']
                has_next_parent = True
            else:
                category = type2category[child['type']]
                key = 'post_{}'.format(category)
                post_info[key].append(child)
        arr.append(post_info)
        if not has_next_parent:
            break

    return arr




def delete_topic(topic_id):
    v = Topic.select().where(Topic.id == topic_id).first()
    if v:
        v.is_deleted = 1
        v.save()
    return {'is_deleted': True}




# v = Topic(
#     forum_id = 1,
#     title = 'hahahha',
#     description = 'aaaaaaaa',
#     username='哈哈哈',
#     user_id=1
# )
# v.save()










# res = get_posts_struct()
# print(res)






# r = Categories.select().order_by(Categories.id)
#
#
# for v in r:
#     print(v.id,v.title)
#     forums = Forum.select().where(Forum.category_id == v.id)
#     for forum in forums:
#         print('  ',forum.id,forum.category_id,forum.title)


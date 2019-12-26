import peewee
from peewee import Model          # peewee提供的基础类，一个Model就对应一个数据库
from peewee import SqliteDatabase      # 我使用sqlite做展示，peewee支持常见的MySQL、PostgreSQL等等多种数据库
from datetime import datetime
from playhouse.shortcuts import model_to_dict



db = SqliteDatabase('/home/liuchu/flask-forum/flask_forum.sqlite')


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


class Question(Model):
    id = peewee.IntegerField()
    topic_id = peewee.IntegerField()
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
        db_table = 'questions'



class Forum(Model):
    id = peewee.IntegerField()
    category_id = peewee.IntegerField()
    title = peewee.CharField(max_length=200)


    class Meta:
        database = db
        db_table = 'forums'


class Topics(Model):
    id = peewee.IntegerField()
    parent_id = peewee.IntegerField()
    name = peewee.CharField(max_length=200)

    class Meta:
        database = db
        db_table = 'topics'


class PostTypeCategory(Model):
    id = peewee.IntegerField()
    category = peewee.IntegerField()
    type = peewee.IntegerField()
    desc = peewee.CharField(max_length=200)


    class Meta:
        database = db
        db_table = 'post_type_category'


class Team(Model):
    name = peewee.CharField(max_length=200)
    parent_id = peewee.IntegerField()


    class Meta:
        database = db
        db_table = 'team'


class TeamMembers(Model):
    team_id = peewee.IntegerField()
    user_id = peewee.IntegerField()

    class Meta:
        database = db
        db_table = 'team_members'


class Users(Model):
    username = peewee.CharField(max_length=200)

    class Meta:
        database = db
        db_table = 'users'



class TeamTopics(Model):
    team_id = peewee.IntegerField()
    topic_id = peewee.IntegerField()

    class Meta:
        database = db
        db_table = 'team_topics'




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


from collections import defaultdict
def get_team_organization():
    r = Team.select()
    map = defaultdict(list)
    roots = []
    team_info = {}
    for v in r:
        if v.parent_id == -1:
            roots.append(v.id)
        else:
            map[v.parent_id].append(v.id)


        info = model_to_dict(v)
        info['children'] = []
        team_info[v.id] = info



    data = [team_info[root] for root in roots]

    queue = data[:]
    while queue:
        info = queue.pop(0)
        _id = info['id']
        for child_id in map[_id]:
            child_info = team_info[child_id]
            info['children'].append(child_info)
            queue.append(child_info)



    return data



def get_team_topic_question_tree(team_id):
    r = TeamTopics.select().where(TeamTopics.team_id == team_id)
    topic_ids = []
    for v in r:
        topic_ids.append(v.topic_id)


    map = defaultdict(list)


    r1 = Topics.select()

    map = defaultdict(list)
    topic_info = {}
    for v in r1:
        if v.parent_id == -1:
            pass
        else:
            map[v.parent_id].append(v.id)

        info = model_to_dict(v)
        info['children'] = []

        topic_info[v.id] = info


    data = [topic_info[_id] for _id in topic_ids]

    queue = data[:]


    while queue:
        info = queue.pop(0)
        _id = info['id']

        if _id in map:
            for child_id in map[_id]:
                child_info = topic_info[child_id]
                info['children'].append(child_info)
                queue.append(child_info)
        else:
            r2 = Question.select().where(Question.topic_id == _id)

            for v2 in r2:
                question_info = model_to_dict(v2)
                question_info['children'] = []
                question_info['name'] = question_info['title']
                info['children'].append(question_info)




    print(data)
    return data



# get_team_topic_question_tree(1)



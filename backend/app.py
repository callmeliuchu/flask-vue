from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
from backend.models.model import *
from backend.models.moment_model import Moment,MomentTag
from backend.publish.redis_pub import fetch_hot_tags
from backend.models.new_forum_model import get_team_organization,get_team_topic_question_tree,get_question_posts



DEBUG = True


app = Flask(__name__)
app.config.from_object(__name__)
app.config['JSON_AS_ASCII'] = False

def register_blueprints(app):
    """ Register Blueprints. """
    from backend.authapi.auth import auth_bp

    app.register_blueprint(
        auth_bp,
        url_prefix='{prefix}'.format(
            prefix='/api'
        )
    )
    return None




register_blueprints(app)



CORS(app)


BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]


@app.route('/books',methods=['GET','POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        book_id = post_data.get('id')
        BOOKS.append(
            {
               'id': book_id if book_id else uuid.uuid4().hex,
               'title':post_data.get('title'),
               'author': post_data.get('author'),
               'read': post_data.get('read')
            }
        )
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)



def remove(book_id):
    idx = -1
    for i in range(len(BOOKS)):
        if BOOKS[i]['id'] == book_id:
            idx = i
            break
    if idx >= 0 :
        del BOOKS[idx]
        return True
    return False

@app.route('/books/<book_id>',methods=['PUT','DELETE'])
def sing_book(book_id):
    response_obj = {'status':'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        book = {
               'id': book_id,
               'title':post_data.get('title'),
               'author': post_data.get('author'),
               'read': post_data.get('read')
            }
        for i in range(len(BOOKS)):
            if BOOKS[i]['id'] == book_id:
                BOOKS[i] = book
        response_obj['book'] = book
        return jsonify(response_obj)
    if request.method == 'DELETE':
        remove(book_id)
        return jsonify(response_obj)


@app.route('/ping',methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/posts',methods=['GET'])
def posts():
    # data = {
    #     'columns': ['id', 'content', 'date_created'],
    #     'posts': [{'id': 1, 'content': '我们是共产主义接班人', 'created_at': '1994-09-14 10:50:55'},
    #             {'id': 1, 'content': '我们是共产主义接班人', 'created_at': '1994-09-14 10:50:55'}],
    # }
    columns = ['id', 'content', 'date_created','down_vote']
    posts = [v for v in Posts.select().dicts()]
    data = {}
    data['columns'] = columns
    data['posts'] = posts

    return jsonify(data)


@app.route('/moments',methods=['GET'])
def moment():
    # data = {
    #     'columns': ['id', 'content', 'date_created'],
    #     'posts': [{'id': 1, 'content': '我们是共产主义接班人', 'created_at': '1994-09-14 10:50:55'},
    #             {'id': 1, 'content': '我们是共产主义接班人', 'created_at': '1994-09-14 10:50:55'}],
    # }
    columns = ['pid', 'title', 'createTime']
    moments = [v for v in Moment.select().limit(10).dicts()]
    data = {}
    data['columns'] = columns
    data['moments'] = moments

    return jsonify(data)


@app.route('/orgtag/<org_id>',methods=['GET'])
def org_tag(org_id):
    data = {}
    data['tags'] = fetch_hot_tags(org_id)
    return jsonify(data)


@app.route('/orgtag/<org_id>/<tag>',methods=['GET'])
def org_tag_search(org_id,tag):
    r = MomentTag.select().where(MomentTag.orgId == org_id).where(MomentTag.title % '%{}%'.format(tag)).dicts()
    moments = [v for v in r]
    data = {}
    data['moments'] = moments
    columns = ['pid','orgId','title']
    data['columns'] = columns
    return jsonify(data)


@app.route('/topic/<int:topic_id>',methods=['GET'])
def topic_posts(topic_id):
    return jsonify(get_topic_posts(topic_id))



@app.route('/topictree',methods=['GET'])
def topic_tree():
    tree = get_topic_tree()
    return jsonify(tree)



@app.route('/poststruct/<int:post_id>')
def posts_struct(post_id):
    arr = get_posts_struct(post_id)
    data = {

    }
    data['posts_struct'] = arr
    return jsonify(data)


@app.route('/topic/new',methods=['POST'])
def topic_new():
    print('aaaaaa')
    post_data = request.get_json()
    v = Topic(
        forum_id = post_data['forum_id'],
        title = post_data['title'],
        description = post_data['content'],
        username='哈哈哈',
        user_id=1
    )
    v.save()
    data = {}
    data['status'] = 'success'
    return jsonify(data)


@app.route('/topic/<int:topic_id>/delete',methods=['GET'])
def topic_delete(topic_id):
    data = delete_topic(topic_id)
    return jsonify(data)

@app.route('/team/organization',methods=['GET'])
def team_organization():
    data = get_team_organization()
    return jsonify(data)


@app.route('/main_page',methods=['GET'])
def main_page():
    res = {}
    res['team_organization'] = get_team_organization()
    res['topic_tree'] = get_topic_tree()
    return jsonify(res)

@app.route('/team/<int:team_id>/topic_tree',methods=['GET'])
def get_topic_tree_by_team_id(team_id):
    topic_tree = get_team_topic_question_tree(team_id)
    return jsonify(topic_tree)



if __name__ == '__main__':
    app.run()
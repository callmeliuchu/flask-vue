from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid




DEBUG = True


app = Flask(__name__)
app.config.from_object(__name__)



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


if __name__ == '__main__':
    app.run()
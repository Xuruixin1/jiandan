#coding: utf-8
from flask import Flask, request
from flask.ext.restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

POSTS = [
    {},
    {'title': 'first post', 'content': 'first post'},
    {'title': 'last post', 'content': 'last post'},
    {'title': 'how to learn interface test',
     'content': 'how to learn interface test'}
]

def abort_if_post_doesnt_exist(post_id):
    try:
        POSTS[post_id]
    except IndexError:
        abort(404, message="POSTS doesn't exist")

parser = reqparse.RequestParser()
parser.add_argument('post', type=int)

class Post(Resource):
    # /posts/1 GET
    def get(self, post_id):
        post_id = int(post_id)
        abort_if_post_doesnt_exist(post_id)
        return POSTS[post_id]

    # /posts/1 DELETE
    def delete(self, post_id):
        post_id = int(post_id)
        abort_if_post_doesnt_exist(post_id)
        del POSTS[post_id]
        return '', 204

    # /posts/1 PUT
    def put(self, post_id):
        json_data = request.get_json(force=True)
        post_id = int(post_id)
        post = {'title': json_data['title'], 'content': json_data['content']}
        POSTS[post_id] = post
        return post, 201

class PostList(Resource):
    # /posts GET
    def get(self):
        posts = []
        for post in POSTS:
            if post:
                new_post = {}
                new_post['url'] = '/posts/' + str(POSTS.index(post))
                new_post['title'] = post['title']
                posts.append(new_post)
        return posts


    # /posts POST
    def post(self):
        json_data = request.get_json(force=True)
        post_id = len(POSTS)
        POSTS.append({'title': json_data['title'], 'content': json_data['content']})
        return POSTS[post_id], 201

api.add_resource(PostList, '/posts')
#api.add_resource(Post, '/posts/<post_id>')


if __name__ == '__main__':
    app.run(debug=True)
from app import create_app

app = create_app()


if __name__ == "__app__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)

# from flask import Flask, jsonify, request, redirect
# from flask_cors import CORS, cross_origin
# from flask_pymongo import PyMongo
# import json
# from bson.objectid import ObjectId
# from bson.json_util import dumps
#
# app = Flask(__name__)
# CORS(app)
# app.config['MONGO_DBNAME'] = 'myDatabase'
# app.config["MONGO_URI"] = "mongodb://mongo/myDatabase"
# mongo = PyMongo(app)
#
# #Set the photos collection variable
# photos = mongo.db.photos
#
# #API Root route
# @app.route("/")
# def hello():
#     return "Welcome to the Photo Counter API"
#
# #Get all photos
# @app.route('/api/photo/allphotos', methods=['GET'])
# def get_all_photos():
#     try:
#         if photos.count_documents({}) != 0:
#             all_photos = list(photos.find({}))
#             return dumps(all_photos)
#         else:
#             return jsonify([])
#     except:
#         return "Error fetching the photos collection", 500
#
# #Get a single photo obj by ID
# @app.route('/api/photo/<photo_id>', methods=['GET'])
# def get_photo(photo_id):
#     try:
#         photo = photos.find_one({ '_id': ObjectId(photo_id)})
#         photo_obj = dumps(photo)
#         return photo_obj
#     except:
#         return "Error fetching requested photo object", 500
#
# #Get photo file by file name
# @app.route('/api/file/<filename>', methods=['GET'])
# def file(filename):
#     try:
#         return mongo.send_file(filename)
#     except:
#         return "Error fetching requested file", 500
#
# #Upload a new photo file
# @app.route("/api/upload", methods=["POST"])
# def save_file():
#     try:
#         if 'new_file' in request.files:
#             new_file = request.files['new_file']
#             mongo.save_file(new_file.filename, new_file)
#             data = {'name' : new_file.filename, 'score': 0}
#             photos.insert_one(data)
#         return dumps(data)
#     except:
#         return "Error uploading file", 500
#
# #Upvote a photo score by ID
# @app.route('/api/upvote/<photo_id>', methods=['POST'])
# def add_vote(photo_id):
#     try:
#         updated_photo = photos.find_one_and_update({ '_id': ObjectId(photo_id)}, {'$inc': {'score': 1 }}, new=True)
#         return dumps(updated_photo)
#     except:
#         return "Error upvoting photo", 500
#
# #Downvote a photo score by ID
# @app.route('/api/downvote/<photo_id>', methods=['POST'])
# def subtract_vote(photo_id):
#     try:
#         updated_photo = photos.find_one_and_update({ '_id': ObjectId(photo_id)}, {'$inc': {'score': -1 }}, new=True)
#         return dumps(updated_photo)
#     except:
#         return "Error downvoting photo", 500
#
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port = 5000, debug=True)
#

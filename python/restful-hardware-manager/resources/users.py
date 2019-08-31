from flask_restful import Resource

USERS = [
    {"name": "foo"},
    {"name": "bar"},
]

class Users(Resource):
    def get(self):
        return USERS


class User(Resource):
    def get(self, name):
        for user in USERS:
            if user.get('name') == name:
                return user
        return 'does not exist', 404

    def delete(self, name):
        for user in USERS:
            if user.get('name') == name:
                USERS.remove(user)
                return "removed", 200
        return "user was not present", 200

    def post(self, name):
        for user in USERS:
            if user.get('name') == name:
                return "user already exists", 204
        USERS.append({"name": name})
        return "user created", 201

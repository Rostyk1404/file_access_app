# 1. створити файл
# 2. прочитати
# 3. змінити
# 4. видалити
from flask import Flask, request
import datetime
import os
import json

app = Flask(__name__)


@app.route('/file/task', methods=['GET', 'POST', 'PUT', 'DELETE'])
def file_tasks():
    if request.method == 'GET':
        """get info from file"""
        path = "/created_file.txt"
        with open(path, "r") as file:
            return file.read()

    elif request.method == 'POST':
        """create file"""
        dater = json.loads(request.data)
        data = f"{dater}\n"
        with open('created_file.txt', "w") as new_file:
            new_file.write(data)
        return "201"
    elif request.method == "PUT":
        "modify/update file"
        dateti = json.loads(request.data)
        data = f"{dateti}\n"
        with open('created_file.txt', "a") as new_file:
            new_file.write(data)
        return "204"
    elif request.method == 'DELETE':
        """delete file"""
        os.remove("created_file.txt")
        return "204"
    else:
        return '405'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

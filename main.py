import os.path as op

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.fileadmin import FileAdmin

app = Flask(__name__)
app.config['DEBUG'] = True

admin = Admin(app)
path = op.join(op.dirname(__file__), 'static')
admin.add_view(FileAdmin(path, '/static/', name='Static Files'))

if __name__ == "__main__":
    app.run()

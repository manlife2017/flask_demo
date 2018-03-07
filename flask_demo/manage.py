# -*- coding:utf-8 -*-
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from exts import db
from views import app

manage = Manager(app)
migrate = Migrate(app, db)
manage.add_command('db', MigrateCommand)


@manage.option('-h', '--host', help='server host')
@manage.option('-p', '--port', help='server port')
def runserver(host=None, port=None):
    if host is not None and port is not None:
        app.run(host=host, port=int(port))
    else:
        app.run()

if __name__ == '__main__':
    manage.run()
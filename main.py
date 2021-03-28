from app import create_app, db
from flask_migrate import Migrate
from app.models import Contact, User


app = create_app('development')

Migrate(app, db)

@app.shell_context_processor
def shell_context():
    return dict(
        app = app,
        db = db,
        User = User,
        Contact = Contact
    )

if __name__ == '__main__':
    app.run()
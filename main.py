from app import create_app, db


app = create_app('development')


@app.shell_context_processor
def shell_context():
    return dict(
        app = app,
        db = db
    )
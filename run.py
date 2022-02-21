from app import app, db
from app.models import Post

@app.shell_context_processor
def make_context():
    return{
        'Post': Post,
        'db': db
    }
from app import app
count = 1


@app.route('/')
def index():
    global count
    count+=1
    return f"Hello, World!{count}"
from flask import Flask,redirect,url_for

app =Flask(__name__)

def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
    return update_wrapper(no_cache, view)
    
@app.route("/")

def home():
    return "Hello! this is the main page<h1>HELLO<h1>"

@app.route("/<name>")

def user(name):

    return(f"Hello, {name}! How can I help?")


@app.route("/admin")
def admin():

    return redirect(url_for("home"))


if __name__=="__main__":
    app.run()
    

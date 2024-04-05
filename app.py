from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

def fill_login_context(context: dict) -> None:
    context['title'] = "Це сторінка авторизації"

@app.post("/login")
def post_login():
    context = {
        'name': request.form.get('name'),
        'surname': request.form.get('surname'),
        'email': request.form.get('email'),
        'password': request.form.get('password')
    }
    fill_login_context(context)
    return f'Запит методом POST, передане значення: {context}'

@app.get("/login")
def get_login():
    context = {}
    fill_login_context(context)
    return render_template("login.html", **context)

if __name__ == "__main__":
    app.run(debug=True)
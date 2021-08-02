from flask import Flask
from flask import render_template
from flask import request
import forms

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    comment_form = forms.ClaseFormulario(request.form)
    if request.method == 'POST' and comment_form.validate():
        print(comment_form.name.data)
        print(comment_form.email.data)
        print(comment_form.telephone.data)
    
    title = 'Formulario'
    return render_template('index.html', title = title, form = comment_form)


if __name__ == '__main__':
    app.run(debug =True)

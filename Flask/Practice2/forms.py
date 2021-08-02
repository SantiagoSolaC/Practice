from wtforms import Form, StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class ClaseFormulario(Form):
    name = StringField ('Nombre', [validators.Required(message = 'Este campo es obligatorio'), 
    validators.length(min = 4, max = 16, message = 'Este campo debe contener de 4 a 16 caracteres')])
    email = EmailField ('Email', [validators.Required(message = 'Este campo es obligatorio'),
    validators.length(min = 7, max = 50, message = 'Este campo debe contener de 7 a 50 caracteres')])
    telephone = TextField ('Telefono', [validators.Required(message = 'Este campo es obligatorio'), 
    validators.length(min = 4, max = 16, message = 'Este campo debe contener de 4 a 16 caracteres')])
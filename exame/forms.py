from django  import forms

class ContactoForm(forms.Form):
    nome = forms.CharField(label='Nome',max_length=100)
    email = forms.EmailField(label='Email', max_length=150)
    assunto = forms.CharField(label='Assunto',max_length=200)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())



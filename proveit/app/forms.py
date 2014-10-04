from django.forms import ModelForm

from app.models import Proof

class ProofForm(ModelForm):
    class Meta:
        model = Proof
        fields = ['proof']

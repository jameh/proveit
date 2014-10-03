from django.db import models
from django.forms.extras import widgets

class Proposition(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=10000)
    def __unicode__(self):
        return self.title

class Proof(models.Model):
    proof_title = models.CharField(max_length=200)
    proof_abstract = models.CharField(max_length=500)
    proof = models.TextField(max_length=10000)
    terms = models.ManyToManyField('Definition', related_name='references')
    proved = models.ManyToManyField('Proposition', related_name='proof_proved')
    assumed = models.ManyToManyField('Proposition', related_name='proof_assumed')
    def __unicode__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=20)
    following = models.ManyToManyField('User', related_name='followed_by')
    star_proofs = models.ManyToManyField('Proof', related_name='starred_by')
    def __unicode__(self):
        return self.name

class Definition(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=10000)

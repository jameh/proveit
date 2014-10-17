from django.db import models
from django.forms.extras import widgets

class Proposition(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=10000)
    def __unicode__(self):
        return self.title

class Proof(models.Model):
    # content
    proof_markdown = models.TextField(max_length=10000)
    
    # we derive these fields from proof_markdown
    proof_title = models.CharField(max_length=200)
    proof_abstract = models.CharField(max_length=500)
    terms = models.ManyToManyField('Definition', related_name='references')
    proved = models.ManyToManyField('Proposition', related_name='proof_proved')
    assumed = models.ManyToManyField('Proposition', related_name='proof_assumed')
    
    # metadata
    author = models.ForeignKey('User')
    proof_id = models.CharField(max_length=7)
    published = models.BooleanField(default=False)
    date_published = models.DateField()
    revision = models.IntegerField()
    def __unicode__(self):
        return self.proof_title

class Definition(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=10000)

class User(models.Model):
    name = models.CharField(max_length=20)
    following = models.ManyToManyField('User', related_name='followed_by')
    star_proofs = models.ManyToManyField('Proof', related_name='starred_by')
    def __unicode__(self):
        return self.name

class Comment(models.Model):
    proof = models.ForeignKey(Proof)
    element_number = models.IntegerField()

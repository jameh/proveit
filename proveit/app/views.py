from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.db import models

from models import Proof

from app.util.proof_processor import mdProcessor


"""Get the user context, adding it to the dictionary"""
def _get_user_context(request, context={}):
    if request.user.is_authenticated():
        context["username"] = request.user.username
    return context

def index(request):
    context = _get_user_context(request)
    context["proof_list"] = [{"get_absolute_url": "lala", "title": "lala"}]
    return render(request, 'proveit/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("proveit/index.html")
    else:
        form = UserCreationForm()
    return render(request, "proveit/register.html", {
        'form': form,
    })

"""Presentation page for proof
edit button for owner

"""
def proof(request):
    pass

class ProofForm(ModelForm):
    class Meta:
        model = Proof
        fields = ['proof']

"""Create new proof, edit interface
url is /new
autosaves to user's drafts
"""
def new(request):
    context = _get_user_context(request)
    if request.method == 'POST':
        form = ProofForm(request.POST)
        if form.is_valid():
            print("VALID FORM")
            print(form.cleaned_data['proof'])
            if 'preview' in request.POST:
                # here, we've requested simply a markdown preview
                context['proof_markdown'] = mdProcessor.convert(form.cleaned_data['proof'])
                # context['markdown_preview'] = md(form.proof)
        else:
            print("INVALID FORM")
        # check that form is valid, from 'publish' button
        # get most recent proof from db
        # increment the id, make new proof entry in db
        # pass that id to edit.html
        pass
    else:
        # GET
        initial_markdown = \
"""# Proof title
## Abstract
"""
        form = ProofForm(initial={'proof': initial_markdown})
        context['proof_markdown'] = mdProcessor.convert(initial_markdown)
    context["form"] = form

    return render(request, "proveit/edit.html", context)

"""Edit existing proof (which you own)
url is /h4sH/edit
autosaves to user's drafts, on first GET, check
for uncommited changes, ask if user would like
to continue editing them.
"""
def edit(request, id):
    context = _get_user_context(request)
    if request.method == 'POST':
        # two cases: explicit save, implicit save
        # on explicit save, redirect to proof page
        #   create form
        #   check form is valid
        #   return redirect to final 'proof' page
        # on implicit save, no redirect (ajax?..)
        #   create form,
        #   check form is valid
        #   submit database save or sumfing
        #   return
        pass
    else:
        # get unique id based on url
        # get database entry
        # return create_proof.html with that info
        return render(request, "proveit/edit.html", context)
        # raise 404 if does not exist

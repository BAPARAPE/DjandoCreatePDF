from django.shortcuts import render, redirect
from django.http import response
from django.http.response import HttpResponse
from .models import Profile
import pdfkit
from django.template.loader import get_template
import io

from CV.models import Profile


def index(request):
    return render(request, 'CV/resume.html')

def formulaire(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        Competence = request.POST.get("Competence")
        langue = request.POST.get("langue")
        internet = request.POST.get("internet")
        objectif = request.POST.get("objectif")
        experience = request.POST.get("experience")
        education = request.POST.get("education")
        Projet = request.POST.get("Projet")
        donnees = Profile(name=name, email=email, phone=phone, address=address, Competence=Competence, langue=langue, experience=experience, objectif=objectif, internet=internet, Projet=Projet, education=education)
        donnees.save()
        return redirect("verification")
    return render(request, 'CV/form.html')

def verification(request):
    profiles = Profile.objects.all()[:1]
    for profile in profiles:
        name = profile.name
        email = profile.email
        phone = profile.phone
        address = profile.address
        Competence = profile.Competence
        langue = profile.langue
        internet = profile.internet
        objectif = profile.objectif
        experience = profile.experience.split
        education = profile.education
        Projet = profile.Projet
    return render(request, 'CV/verification.html', {'address':address, 'name':name, 'email':email, 'phone':phone, 'Competence':Competence, 'internet':internet, 'langue':langue, 'experience':experience, 'objectif':objectif, 'education': education, 'Project':Projet })

def generer(request, id):
    profile = Profile.objects.get(pk=id)
    name=profile.name
    phone=profile.phone
    email =profile.email
    address =profile.address
    com = profile.competance
    langue = profile.langue
    interet = profile.interet
    exp = profile.experience
    objectif = profile.objectif 
    education = profile.education 
    project = profile.Projet

    template = get_template('pdf/generator.html')
    context = {'address':address, 'name':name, 'email':email, 'phone':phone, 'com':com, 'interet':interet, 'langue':langue, 'experience':exp, 'objectif':objectif, 'education': education, 'project':project }
    html = template.render(context)
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    pdf = pdfkit.from_string(html, False, options)

    reponse = HttpResponse(pdf, content_type='application/pdf')
    reponse['Content-Disposition']="attachement"
    return reponse

def download(request):
    profile = Profile.objects.all()
    return render(request, 'pdf/download.html', {'profile':profile}) 
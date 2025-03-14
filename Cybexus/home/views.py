from django.shortcuts import render
from .models import Formation

def home(request):
    formations = Formation.objects.all() 
    return render(request, 'home/index.html', {'formations': formations})

def formation(request):
    formations = Formation.objects.all()
    
    # Organiser les formations par catégories (exemple avec des titres)
    categories = {
        "Cybersécurité": [],
        "Design": [],
        "Réseau": [],
        "Développement mobile": [],
        "Développement web": []
    }

    for formation in formations:
        if "cybersécurité" in formation.titre.lower():
            categories["Cybersécurité"].append(formation)
        elif "design" in formation.titre.lower():
            categories["Design"].append(formation)
        elif "réseau" in formation.titre.lower():
            categories["Réseau"].append(formation)
        elif "mobile" in formation.titre.lower():
            categories["Développement mobile"].append(formation)
        elif "web" in formation.titre.lower():
            categories["Développement web"].append(formation)
    
    return render(request, 'formation/formation.html', {'formation': categories})

def contact(request):
    # Informations de contact en dur (car pas de modèle pour contact)
    contacts = {
        "email": "contact@cybexus.com",
        "telephone": "+33 1 23 45 67 89",
        "adresse": "123 Avenue de la Cybersécurité, Paris, France",
        "reseaux": {
            "Facebook": "https://facebook.com/cybexus",
            "Twitter": "https://twitter.com/cybexus",
            "LinkedIn": "https://linkedin.com/company/cybexus"
        }
    }
    
    return render(request, 'contact/contact.html', {'contacts': contacts})

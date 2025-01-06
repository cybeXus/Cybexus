from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import CustomUser  # Assuming you have a custom user model

def sign_in(request):
    if request.method == 'POST':
        frst_name = request.POST['frst_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        User = get_user_model()  # utilise le modele personnaliser

        # Vérification des champs obligatoires
        if not frst_name or not last_name or not username or not email or not phone or not password or not confirm_password:
            messages.error(request, 'Tous les champs sont obligatoires.')
            return redirect('sign_in')

        # Validation pour vérifier que le champ contient uniquement des chiffres
        if not phone.isdigit():
            messages.error(request, "Le numéro de téléphone doit contenir uniquement des chiffres.")
            return render(request, 'authentification/sign_in.html')  # Retourne le formulaire avec un message d'erreur
        
        # Vérification si les mots de passe correspondent
        if password != confirm_password:
            messages.error(request, 'Les mots de passe ne correspondent pas.')
            return redirect('sign_in')

        # Vérification si l'utilisateur existe déjà
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Le nom d’utilisateur est déjà utilisé.')
            return redirect('sign_in')

        if User.objects.filter(phone=phone).exists():
            messages.error(request, 'Le numéro de téléphone est déjà utilisé.')
            return redirect('sign_in')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'L’email est déjà utilisé.')
            return redirect('sign_in')

        # Création de l'utilisateur
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = frst_name
        user.last_name = last_name
        user.phone = phone  
        user.save()

        messages.success(request, 'Compte créé avec succès. Vous pouvez maintenant vous connecter.')
        return redirect('login')  # Redirige vers la page de connexion après l'inscription

    return render(request, 'authentification/sign_in.html')

def user_login(request):  # Renamed the function to avoid conflict with the login method
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Renamed the login method import to auth_login
            return redirect('Home')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect')
    return render(request, 'authentification/login.html')

from django.shortcuts import render
from django.contrib.auth import authenticate, login as login_request, logout
from django.shortcuts import render , redirect 
import json
from django.http import JsonResponse
from django.contrib.auth.models import User 

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    return redirect('dashboard')
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    else:
        datas = {

        }
        return render(request, 'pages/guest-login.html', datas)

def signup(request):
    if request.user.is_authenticated:
        try:
            if hasattr(request.user, 'student_user'):
                return redirect('index_student')
            elif hasattr(request.user, 'instructor'):
                return redirect('dashboard')
        except:
            return redirect("/admin/")
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            # Vérification des données
            if not username or not email or not password:
                datas = {'error': "Tous les champs sont obligatoires."}
                return render(request, 'pages/guest-signup.html', datas)

            # Création de l'utilisateur
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')  # Redirige vers la page de connexion après inscription
            except Exception as e:
                datas = {'error': f"Erreur lors de la création de l'utilisateur : {str(e)}"}
                return render(request, 'pages/guest-signup.html', datas)

        # Pour les requêtes GET
        datas = {}
        return render(request, 'pages/guest-signup.html', datas)
 

def forgot_password(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    return redirect('dashboard')
        except:
            print("3")
            return redirect("/admin/")
    else:
        datas = {

        }
        return render(request, 'pages/guest-forgot-password.html', datas)



from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as login_request
from django.contrib.auth.models import User

@csrf_exempt
def islogin(request):
    if request.method == "POST":
        try:
            # Vérifie si les données sont envoyées au format JSON
            if request.content_type == "application/json":
                postdata = json.loads(request.body.decode('utf-8'))
                username = postdata.get('username')
                password = postdata.get('password')
            else:
                # Sinon, utilise les données du formulaire POST classique
                username = request.POST.get('username')
                password = request.POST.get('password')

            # Initialisation
            isSuccess = False
            u_type = ''
            redirect_url = ''

            # Authentification
            if '@' in username:
                user = authenticate(email=username, password=password)
            else:
                user = authenticate(username=username, password=password)

            if user is not None and user.is_active:
                login_request(request, user)  # Connecte l'utilisateur

                # Vérification du type d'utilisateur
                if hasattr(user, 'student_user'):
                    u_type = "student"
                    redirect_url = "index_student"  # URL name de la page étudiant
                elif hasattr(user, 'instructor'):
                    u_type = "instructor"
                    redirect_url = "dashboard"  # URL name de la page instructeur
                else:
                    u_type = "admin"
                    redirect_url = "/admin/"  # URL de l'admin

                # Redirection après connexion
                return redirect(redirect_url)

            # Si les identifiants sont incorrects
            return JsonResponse({
                'success': False,
                'message': 'Vos identifiants ne sont pas corrects.',
            }, safe=False)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f"Une erreur s'est produite : {str(e)}",
            }, safe=False)
    else:
        return JsonResponse({
            'success': False,
            'message': "Méthode non autorisée.",
        }, safe=False)

    
def deconnexion(request):
    logout(request)
    return redirect('login')

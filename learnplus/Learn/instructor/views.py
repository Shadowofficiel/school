from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from school import models as school_models
from quiz import models as quiz_models
from forum import models as forum_models
from chat import models as chat_models
from . import models
from django.utils.safestring import mark_safe
import json
from django.http import JsonResponse 
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render, redirect
from forum.models import Reponse
from forum.models import Sujet
from chat.models import Salon
from instructor import models as instructor_models 
from instructor.models import AffectationMatiere
from quiz.models import Quiz, Question
from quiz.models import QuizResult
from school.models import Classe
from chat.models import Salon, Message
# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    if request.user.is_authenticated:
        try:
            if hasattr(request.user, 'student_user'):
                return redirect('index_student')
            
            if hasattr(request.user, 'instructor'):
                # Récupérer les matières affectées à l'instructeur connecté
                matieres = models.AffectationMatiere.objects.filter(instructor=request.user.instructor).select_related('matiere')
                datas = {
                    'matiere': [affectation.matiere for affectation in matieres],
                }
                return render(request, 'pages/instructor-dashboard.html', datas)

        except Exception as e:
            print(e)
            return redirect('/admin/')

 


@login_required(login_url = 'login')
def account_edit(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                return render(request,'pages/instructor-account-edit.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    



# @login_required(login_url = 'login')
# def browse_courses(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                 return render(request,'pages/instructor-browse-courses.html',datas)
#         except Exception as e:
# print(e)
#             print("3")
#             return redirect("/admin/")
    



# @login_required(login_url = 'login')
# def carts(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                 return render(request,'pages/instructor-cart.html',datas)
#         except Exception as e:
# print(e)
#             print("3")
#             return redirect("/admin/")
   



@login_required(login_url='login')
def course_add(request):
    if request.user.is_authenticated:
        try:
            if hasattr(request.user, 'student_user'):
                return redirect('index_student')

            if hasattr(request.user, 'instructor'):
                # Filtrer les matières assignées à cet instructeur uniquement
                matieres_assignees = models.AffectationMatiere.objects.filter(
                    instructor=request.user.instructor
                ).select_related('matiere')

                # Récupérer uniquement les objets Matiere
                matiere = [affectation.matiere for affectation in matieres_assignees]

                datas = {
                    'matiere': matiere,
                }
                return render(request, 'pages/instructor-course-add.html', datas)
        except Exception as e:
            print(e)
            return redirect('/admin/')




@login_required(login_url='login')
def course_edit(request, slug):
    if request.user.is_authenticated:
        try:
            if hasattr(request.user, 'student_user'):
                return redirect('index_student')

            if hasattr(request.user, 'instructor'):
                # Filtrer les matières assignées à cet instructeur uniquement
                matieres_assignees = models.AffectationMatiere.objects.filter(
                    instructor=request.user.instructor
                ).select_related('matiere')

                # Récupérer uniquement les objets Matiere
                matiere = [affectation.matiere for affectation in matieres_assignees]

                # Récupérer le chapitre à partir du slug
                chapitre = school_models.Chapitre.objects.get(slug=slug)

                # Vérifier que le chapitre appartient à une matière assignée
                if chapitre.matiere not in matiere:
                    return redirect('/admin/')  # Redirection si non autorisé

                datas = {
                    'matiere': matiere,
                    'chapitre': chapitre,
                }
                return render(request, 'pages/instructor-course-edit.html', datas)
        except Exception as e:
            print(e)
            return redirect('/admin/')



@login_required(login_url='login')
def courses(request):
    if hasattr(request.user, 'student_user'):
        return redirect('index_student')

    if hasattr(request.user, 'instructor'):
        try:
            # Récupérer les matières assignées à cet instructeur
            matieres_assignees = models.AffectationMatiere.objects.filter(
                instructor=request.user.instructor
            ).select_related('matiere')

            # Vérifier si l'instructeur a des matières assignées
            if not matieres_assignees.exists():
                message = "Vous n'avez pas encore été assigné à une matière. Veuillez contacter l'administration."
                show_add_button = False
                chapitres = None
            else:
                # Récupérer les chapitres liés aux matières assignées
                chapitres = school_models.Chapitre.objects.filter(
                    matiere__in=[affectation.matiere for affectation in matieres_assignees],
                    status=True
                )

                # Vérifier si des chapitres existent
                if not chapitres.exists():
                    message = "Ajouter un cours pour ajouter des chapitres."
                    show_add_button = False
                else:
                    message = None
                    show_add_button = True  # Le bouton est cliquable uniquement si des chapitres existent

            datas = {
                'Chapitre': chapitres,
                'message': message,
                'show_add_button': show_add_button,
            }
            return render(request, 'pages/instructor-courses.html', datas)

        except Exception as e:
            print(f"Erreur: {e}")
            return redirect("/admin/")

    return redirect('/login/')


@login_required(login_url = 'login')
def matiere(request, slug):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    Chapitre = school_models.Chapitre.objects.filter(Q(status=True) & Q(classe=request.user.instructor.classe) & Q(matiere__slug=slug))
                    datas = {
                            'Chapitre' : Chapitre ,
                           }
                    return render(request,'pages/instructor-cours-chap.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")



@login_required(login_url = 'login')
def earnings(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                    return render(request,'pages/instructor-account-edit.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")





# @login_required(login_url = 'login')
# def edit_invoice(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
#                 print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-edit-invoice.html',datas)
#         except Exception as e:
#             print(e)
#             print("3")
#             return redirect("/admin/")





@login_required(login_url = 'login')
def forum(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    forum_general = forum_models.Sujet.objects.filter(cours=None)
                    forum = forum_models.Sujet.objects.filter(cours__chapitre__classe=request.user.instructor.classe)
                    datas = {
                        'forum_general': forum_general,
                        'forum': forum,
                    }
                    return render(request,'pages/instructor-forum.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    



@login_required(login_url='login')
def forum_ask(request):
    try:
        # Vérification si l'utilisateur est un étudiant
        if hasattr(request.user, 'student_user'):
            return redirect('index_student')

        # Vérification si l'utilisateur est un instructeur
        if hasattr(request.user, 'instructor'):
            # Récupérer les matières assignées à l'instructeur
            affectations = instructor_models.AffectationMatiere.objects.filter(
                instructor=request.user.instructor
            )

            if not affectations.exists():
                message = "Vous n'avez pas encore été assigné à une matière. Veuillez contacter l'administration."
                return render(request, 'pages/instructor-forum-ask.html', {'message': message})

            # Récupérer les matières assignées
            matieres = [affectation.matiere for affectation in affectations]

            # Récupérer les cours liés à ces matières via les chapitres
            cours_list = school_models.Cours.objects.filter(
                chapitre__matiere__in=matieres,
                status=True  # Cours actifs uniquement
            ).distinct()

            if not cours_list.exists():
                message = "Aucun cours n'est disponible pour vos matières assignées. Vous pouvez poser des questions générales uniquement."
                return render(request, 'pages/instructor-forum-ask.html', {'message': message})

            # Passer les cours à la vue
            datas = {
                'cours_list': cours_list,
                'message': None,  # Aucun message d'erreur
            }
            return render(request, 'pages/instructor-forum-ask.html', datas)

    except Exception as e:
        # Gérer les erreurs et rediriger vers l'admin en cas de problème
        print(f"Erreur: {e}")
        return redirect("/admin/")




@login_required(login_url='login')
def forum_thread(request, slug):
    forum = get_object_or_404(forum_models.Sujet, slug=slug)
    responses = forum.sujet_reponse.all()
    context = {
        "forum": forum,
        "responses": responses,
    }
    return render(request, 'forum/forum_detail.html', context)


@login_required(login_url='login') 
def delete_forum(request, slug):
    try:
        forum = get_object_or_404(Sujet, slug=slug)
        if request.user == forum.user:
            if request.method == 'POST':
                forum.delete()
                print("Forum supprimé avec succès.")
                return redirect('instructor-forum')  # Rediriger après suppression
            else:
                print("La requête n'est pas POST.")
        else:
            print("Utilisateur non autorisé.")
            return redirect('instructor-forum-thread', slug=slug)  # Rediriger si non autorisé
    except Exception as e:
        print(f"Erreur lors de la suppression du forum : {e}")
        return redirect('instructor-forum')

@login_required(login_url='login')
def delete_response(request, id):
    try:
        reponse = get_object_or_404(Reponse, id=id)
        if request.method == 'POST' and request.user == reponse.user:
            sujet_slug = reponse.sujet.slug
            reponse.delete()
            # Mettez ici le nom correct de l'URL
            return redirect('instructor-forum-thread', slug=sujet_slug)
        return redirect('instructor-forum-thread', slug=reponse.sujet.slug)
    except Exception as e:
        print(e)
        return redirect('/admin/')

@login_required(login_url='login')
def post_reply(request, slug):
    if request.method == 'POST':
        # Récupérer le texte de la réponse
        reponse_text = request.POST.get('reponse')
        if not reponse_text:
            return JsonResponse({
                'success': False,
                'message': 'La réponse ne peut pas être vide.'
            })

        # Récupérer le sujet à partir du slug
        sujet = get_object_or_404(Sujet, slug=slug)

        # Créer et enregistrer la réponse
        try:
            reponse = Reponse.objects.create(
                user=request.user,
                sujet=sujet,
                reponse=reponse_text
            )
            reponse.save()
            return redirect('forum_thread', slug=sujet.slug)
        except Exception as e:
            print(e)  # Pour déboguer l'erreur
            return JsonResponse({
                'success': False,
                'message': 'Une erreur est survenue lors de l\'ajout de la réponse.'
            })
    else:
        return JsonResponse({
            'success': False,
            'message': 'Méthode non autorisée.'
        })


# @login_required(login_url = 'login')
# def invoice(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
#                 print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-invoice.html',datas)
#         except Exception as e:
#             print(e)
#             print("3")
#             return redirect("/admin/")
    





# @login_required(login_url = 'login')
# def invoice_settings(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-invoice-settings.html',datas)
#         except Exception as e:
# print(e)
#             print("3")
#             return redirect("/admin/")
    





@login_required(login_url = 'login')
def lesson_add(request, slug):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    chapitre = school_models.Chapitre.objects.get(slug=slug)
                    datas = {
                        'chapitre': chapitre,
                           }
                    return render(request,'pages/instructor-lesson-add.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")



@login_required(login_url = 'login')
def lesson_edit(request, slug, id):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    chapitre = school_models.Chapitre.objects.get(id=id)
                    cours = school_models.Cours.objects.get(slug=slug)

                    datas = {
                        'chapitre': chapitre,
                        'cours': cours,
                    }
                    return render(request,'pages/instructor-lesson-edit.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")




@login_required(login_url='login')
def messages(request, classe):
    """
    Vue pour afficher les messages d'une classe spécifique.
    """
    try:
        # Vérifiez si l'utilisateur est un instructeur
        if hasattr(request.user, 'instructor'):
            try:
                # Extraire les informations de la classe
                niveau_nom, numero_classe = classe.split()
                classe_instance = get_object_or_404(
                    Classe, 
                    niveau__nom=niveau_nom, 
                    numeroClasse=int(numero_classe)
                )

                # Récupérer le salon correspondant
                salon = get_object_or_404(Salon, classe=classe_instance)

                # Récupérer les messages associés
                messages = Message.objects.filter(salon=salon).order_by('date_add')

                # Préparer les données pour le contexte
                context = {
                    'info_classe': classe_instance,
                    'classe': salon,
                    'messages': messages,
                    'classe_json': mark_safe(json.dumps(salon.id)),
                    'username': mark_safe(json.dumps(request.user.username)),
                }
                return render(request, 'pages/instructor-messages.html', context)
            except ValueError:
                # Gestion du format incorrect de `classe`
                print("Erreur : format de la classe invalide.")
                return redirect('dashboard')
        else:
            return redirect('login')
    except Exception as e:
        print(f"Erreur : {e}")
        return redirect('dashboard')
    
    
# @login_required(login_url = 'login')
# def messages_2(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
#                 print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-messages-2.html',datas)
#         except Exception as e:
#             print(e)
#             print("3")
#             return redirect("/admin/")






# @login_required(login_url = 'login')
# def my_courses(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-my-courses.html',datas)
#         except Exception as e:
# print(e)
#             print("3")
  





@login_required(login_url='login')
def profile(request):
    try:
        # Vérifier si l'utilisateur est un étudiant
        if hasattr(request.user, 'student_user'):
            return redirect('index_student')

        # Vérifier si l'utilisateur est un instructeur
        if hasattr(request.user, 'instructor'):
            # Récupérer les informations de l'instructeur
            instructor = request.user.instructor
            context = {
                'instructor': instructor,  # Passer les données de l'instructeur au template
            }
            return render(request, 'pages/instructor-profile.html', context)

    except Exception as e:
        # Afficher une erreur dans la console pour le débogage
        print(f"Erreur dans la vue profile: {e}")
        return redirect('/admin/')



@login_required(login_url='login')
def quiz_edit(request, slug):
    if not hasattr(request.user, 'instructor'):
        return redirect('dashboard')  # Redirect if the user is not an instructor

    try:
        quiz = quiz_models.Quiz.objects.get(slug=slug)

        if request.method == 'POST':
            # Handle quiz editing logic here
            titre = request.POST.get('quiz_title')
            temps = request.POST.get('quiz_time')
            tentatives = request.POST.get('quiz_attempts')

            if not all([titre, temps, tentatives]):
                return render(request, 'pages/instructor-quiz-edit.html', {
                    'quiz': quiz,
                    'error': 'All fields are required.',
                })

            # Update quiz
            quiz.titre = titre
            quiz.temps = temps
            quiz.nombre_tentatives = tentatives
            quiz.save()

            return redirect('instructor-quizzes')

        return render(request, 'pages/instructor-quiz-edit.html', {'quiz': quiz})
    except quiz_models.Quiz.DoesNotExist:
        return redirect('instructor-quizzes')


@login_required(login_url='login')
def update_question(request, question_id):
    """
    Met à jour une question existante.
    """
    question = get_object_or_404(Question, id=question_id)

    if request.method == 'POST':
        question_text = request.POST.get('question')
        points = request.POST.get('point')

        if not question_text or not points:
            return JsonResponse({'error': 'Tous les champs sont obligatoires.'}, status=400)

        question.question = question_text
        question.point = int(points)
        question.save()
        return JsonResponse({'success': 'Question mise à jour avec succès.'})

    return JsonResponse({'error': 'Requête invalide.'}, status=400)


@login_required(login_url='login')
def delete_question(request, question_id):
    """
    Supprime une question existante.
    """
    question = get_object_or_404(Question, id=question_id)
    question.delete()
    return JsonResponse({'success': 'Question supprimée avec succès.'})


@login_required(login_url='login')
def delete_quiz(request, slug):
    """
    Vue pour supprimer un quiz.
    """
    if request.method == 'POST':
        try:
            quiz = get_object_or_404(Quiz, slug=slug)
            quiz.delete()
            return JsonResponse({'success': 'Quiz supprimé avec succès.'})
        except Quiz.DoesNotExist:
            return JsonResponse({'error': 'Quiz introuvable.'}, status=404)

    return JsonResponse({'error': 'Requête invalide.'}, status=400)


@login_required(login_url='login')
def quiz_add(request):
    if not hasattr(request.user, 'instructor'):
        return redirect('dashboard')

    try:
        matieres = instructor_models.AffectationMatiere.objects.filter(
            instructor=request.user.instructor
        ).values_list('matiere', flat=True)

        if request.method == 'GET':
            cours = school_models.Cours.objects.filter(
                chapitre__matiere__in=matieres,
                status=True
            ).distinct()
            return render(request, 'pages/instructor-quiz-add.html', {'cours': cours})

        if request.method == 'POST':
            titre = request.POST.get('quiz_title')
            date = request.POST.get('date')
            cours_id = request.POST.get('course_title')
            temps = request.POST.get('quiz_time')
            tentatives = request.POST.get('quiz_attempts')
            image = request.FILES.get('quiz_image')

            if not all([titre, date, cours_id, temps, tentatives]):
                cours = school_models.Cours.objects.filter(
                    chapitre__matiere__in=matieres,
                    status=True
                ).distinct()
                return render(request, 'pages/instructor-quiz-add.html', {
                    'cours': cours,
                    'error': 'Tous les champs sont obligatoires.',
                })

            try:
                cours = school_models.Cours.objects.get(
                    id=cours_id,
                    chapitre__matiere__in=matieres,
                    status=True
                )
            except school_models.Cours.DoesNotExist:
                return render(request, 'pages/instructor-quiz-add.html', {
                    'cours': cours,
                    'error': "Le cours sélectionné n'est pas valide.",
                })

            quiz = quiz_models.Quiz(
                titre=titre,
                cours=cours,
                date=date,
                temps=int(temps),
                nombre_tentatives=int(tentatives),
                status=True
            )
            if image:
                quiz.image = image
            quiz.save()

            # Gestion des questions avec points
            questions = request.POST.getlist('questions[]')
            answers = request.POST.getlist('answers[]')
            correct_answers = request.POST.getlist('correct_answers[]')
            points = request.POST.getlist('points[]')

            for question_text, answer_text, correct_answer, point in zip(questions, answers, correct_answers, points):
                question = quiz_models.Question.objects.create(
                    quiz=quiz,
                    question=question_text,
                    point=int(point),
                    typequestion='qcm'
                )

                possible_answers = [ans.strip() for ans in answer_text.split(',')]
                for ans in possible_answers:
                    quiz_models.Reponse.objects.create(
                        question=question,
                        reponse=ans,
                        is_True=(ans == correct_answer)
                    )

            return redirect('instructor-quizzes')

    except Exception as e:
        print(f"Erreur dans quiz_add: {e}")
        return redirect('/admin/')


# @login_required(login_url = 'login')
# def quiz_results(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-quiz-results.html',datas)
#         except Exception as e:
# print(e)
#             print("3")
#             return redirect("/admin/")
    




@login_required(login_url='login')
def quizzes(request):
    if not hasattr(request.user, 'instructor'):
        return redirect('dashboard')  # Redirection si l'utilisateur n'est pas un instructeur

    try:
        # Récupérer les matières assignées à l'instructeur
        matieres = instructor_models.AffectationMatiere.objects.filter(
            instructor=request.user.instructor
        ).values_list('matiere', flat=True)  # Obtenir les IDs des matières

        # Récupérer les quiz associés à ces matières via chapitre → cours → quiz
        quizzes = quiz_models.Quiz.objects.filter(
            cours__chapitre__matiere__in=matieres,
            status=True  # Filtrer les quiz actifs
        ).distinct()  # Éviter les doublons

        # Passer les données au template
        datas = {
            'quizzes': quizzes,
        }
        return render(request, 'pages/instructor-quizzes.html', datas)

    except Exception as e:
        print(f"Erreur: {e}")
        return redirect('/admin/')




@login_required(login_url='login')
def review_quiz(request, slug):
    if not hasattr(request.user, 'instructor'):
        return redirect('dashboard')  # Redirection si l'utilisateur n'est pas un instructeur

    try:
        # Récupérer le quiz correspondant au slug
        quiz = get_object_or_404(
            Quiz,
            slug=slug,
            cours__chapitre__classe=request.user.instructor.classe
        )

        # Récupérer les questions et les réponses associées
        questions = quiz.quiz_question.prefetch_related('question_reponse').all()

        # Récupérer l'historique des résultats pour ce quiz
        results = QuizResult.objects.filter(quiz=quiz).select_related('user').order_by('-submitted_at')

        # Passer les données au template
        context = {
            'quiz': quiz,
            'questions': questions,
            'results': results,  # Ajouter les résultats au contexte
        }
        return render(request, 'pages/instructor-review-quiz.html', context)

    except Exception as e:
        print(f"Erreur dans review_quiz : {e}")
        return redirect('instructor-quizzes')


# @login_required(login_url = 'login')
# def take_course(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-take-course.html',datas)
#         except Exception as e:
# print(e)
#             print("3")
#             return redirect("/admin/")






# @login_required(login_url = 'login')
# def take_quiz(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-take-quiz.html',datas)
#         except Exception as e:
# print(e)
#             print("3")
#             return redirect("/admin/")






# @login_required(login_url = 'login')
# def view_course(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-view-course.html',datas)
#         except Exception as e:
# print(e)
#             print("3")
#             return redirect("/admin/")





@login_required(login_url = 'login')
def statement(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                    return render(request,'pages/instructor-statement.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")

# fonction pour recuperer les donnees d'un cours et enregistrer

""" Add and update chapitre """
def post_cours(request):
    title = request.POST.get("title") 
    matiere = request.POST.get("matiere")
    date_fin = request.POST.get("date_fin")
    description = request.POST.get("description")
    date_debut = request.POST.get("date_debut")
    duration = request.POST.get("duration")
    id = request.POST.get("id")
    chapitre = ''

    try:
        chapitre = school_models.Chapitre.objects.get(id=id)
        chapitre.titre = title
        chapitre.duree_en_heure = duration
        chapitre.description = description
        matiere = school_models.Matiere.objects.get(id=int(matiere))
        chapitre.matiere = matiere
        chapitre.classe = request.user.instructor.classe
        chapitre.save()
        try:
            video = request.FILES["file"]
            image = request.FILES["image"]
            chapitre.video = video
            chapitre.image = image
            chapitre.save()
        except :
            pass
        try:
            chapitre.date_debut = date_debut
            chapitre.save()
        except:
            pass
        try:
            chapitre.date_fin = date_fin
            chapitre.save()
        except:
            pass
        success = True 
        message = 'mis à jour effectué  avec succés'
    except:
        chapitre = school_models.Chapitre()
        try:
            video = request.FILES["file"]
            image = request.FILES["image"]
            chapitre.video = video
            chapitre.image = image
            chapitre.save()
        except :
            pass
        chapitre.titre = title
        chapitre.duree_en_heure = duration
        chapitre.date_debut = date_debut
        chapitre.date_fin = date_fin
        chapitre.description = description
        matiere = school_models.Matiere.objects.get(id=int(matiere))
        chapitre.matiere = matiere
        chapitre.classe = request.user.instructor.classe
        chapitre.save()
        success = True 
        message = 'chapitre ajouté avec succés'
    data = {
        'success' : success,
        'message' : message,
        'slug': chapitre.slug,
    }
    return JsonResponse(data,safe=False)



""" delete chapitre"""
def delete_chapitre(request):
    id = request.POST.get("id")
    try:
        chapitre = school_models.Chapitre.objects.get(id=int(id))
        chapitre.delete()
        success = True
        message = "La leçon a bien été supprimée"
    except Exception as e:
        print(e)
        success = False
        message = "Une erreur s'est produite"
    data = {
        'success' : success,
        'message' : message,
    }
    return JsonResponse(data,safe=False)





""" add and update lesson """
def post_lesson(request):
    title = request.POST.get("title")
    chapitre = request.POST.get("chapitre")
    description = request.POST.get("description")
    id = request.POST.get("id")

    try:
        cours = school_models.Cours.objects.get(Q(id=int(id)) & Q(chapitre__id=int(chapitre)))

        try:
            video = request.FILES["file"]
            image = request.FILES["image"]
            pdf = request.FILES["pdf"]
            cours.video = video
            cours.image = image
            cours.pdf = pdf
        except:
            pass
        cours.titre = title
        cours.description = description
        cours.save()
        success = True 
        message = 'mis à jour effectué  avec succés'
    except:
        cours = school_models.Cours()
        try:
            chapitre = school_models.Chapitre.objects.get(id=int(chapitre))
            video = request.FILES["file"]
            image = request.FILES["image"]
            pdf = request.FILES["pdf"]
            cours.video = video
            cours.chapitre = chapitre
            cours.image = image
            cours.description = description
            cours.pdf = pdf
            cours.titre = title
            cours.save()
            success = True 
            message = 'cours ajouté avec succés'
        except Exception as e:
            print(e)
            success = False
            message = "Une erreur s'est produite"
    data = {
        'success' : success,
        'message' : message,
    }
    return JsonResponse(data,safe=False)



""" delete lesson"""
def delete_lesson(request):
    id = request.POST.get("id")
    try:
        lesson = school_models.Cours.objects.get(id=int(id))
        lesson.delete()
        success = True
        message = "La leçon a bien été supprimée"
    except Exception as e:
        success = False
        message = "Une erreur s'est produite"
    data = {
        'success' : success,
        'message' : message,
    }
    return JsonResponse(data,safe=False)

def update_profil(request):
    nom = request.POST.get("nom")
    prenom = request.POST.get("prenom")
    email = request.POST.get("email")
    bio = request.POST.get("bio")

    try:
        user = User.objects.get(username=request.user.username)
        user.last_name = nom
        user.first_name = prenom
        user.email = email
        user.save()
        instructor = models.Instructor.objects.get(user__id=request.user.id)
        instructor.bio = bio
        instructor.save()
        try:
            image = request.FILES["file"]
            instructor.photo = image 
            instructor.save()

        except:
            pass
        success = True 
        message = "vos informations ont été modifié avec succés"

    except:
        success = False
        message = "une erreur est subvenue lors de la mise à jour"
    data = {
        "success" : success,
        "message" : message,
        }
    return JsonResponse(data,safe=False)

        
def update_password(request):
    last_password = request.POST.get("last_password")
    new_password = request.POST.get("new_password")
    confirm_password = request.POST.get("confirm_password")

    try:
        if not request.user.check_password(last_password):
            success = False
            message = "Ancien mot de passe incorrect"
        elif new_password != confirm_password:
            success = False
            message = "Les mots de passe ne sont pas identiques"
        else:
            user = User.objects.get(username=request.user.username)
            username = user.username
            user.password = new_password
            user.set_password(user.password)
            user.save()
            user = authenticate(username=username, password=new_password)
            login(request, user)
            success = True 
            message = "Mot de passe modfifié avec succès"
    except Exception as e:
        print(e)
        success = False
        message = "une erreur est subvenue lors de la mise à jour"
    data = {
        "success" : success,
        "message" : message,
        }
    return JsonResponse(data,safe=False)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from forum import models as forum_models

@csrf_exempt
@login_required(login_url='login')
def post_forum(request):
    if request.method == 'POST':
        titre = request.POST.get("titre")
        question = request.POST.get("question")
        cours_id = request.POST.get("cours", None)  # Optionnel si un cours est associé
        try:
            # Créer un nouvel objet Sujet
            forum = forum_models.Sujet()
            forum.titre = titre
            forum.question = question
            forum.user = request.user

            # Si un cours est sélectionné, l'associer au sujet
            if cours_id:
                forum.cours_id = cours_id

            forum.save()

            # Rediriger vers la page du forum après l'ajout
            return redirect('instructor-forum')

        except Exception as e:
            print(e)
            # En cas d'erreur, afficher le formulaire avec un message d'erreur
            cours_list = school_models.Cours.objects.filter(
                chapitre__classe=request.user.instructor.classe
            )
            return render(request, 'pages/instructor-forum-ask.html', {
                'cours_list': cours_list,
                'error': "Une erreur est survenue lors de la création du sujet."
            })

    # Si la méthode n'est pas POST, rediriger vers le formulaire pour poser une question
    return redirect('instructor-forum-ask')
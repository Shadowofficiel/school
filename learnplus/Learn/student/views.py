from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from school import models as school_models
from forum import models as forum_models
from instructor import models as instructor_models
from django.db.models import Q
from chat import models as chat_models
from django.utils.safestring import mark_safe
import json
from quiz.models import QuizResult, QuestionResponse
from django.http import JsonResponse 
from django.contrib.auth.models import User
from . import models
from django.contrib.auth import authenticate, login
from quiz import models as quiz_models  
from quiz.models import Quiz, Question, Reponse
from django.contrib import messages
from django.contrib import messages as django_messages
from django.http import HttpResponseNotFound
from quiz.models import QuizResult
import traceback
from forum.models import Reponse
from chat.models import Salon, Message
from school.models import Filiere
from .models import Student
from quiz.models import StudentAnswer

# Create your views here.
@login_required(login_url='login')
def index(request):
    try:
        if hasattr(request.user, 'instructor'):
            return redirect('dashboard')  # Redirection si l'utilisateur est un instructeur

        if hasattr(request.user, 'student_user'):
            # Récupérer les données spécifiques à l'étudiant
            classe = request.user.student_user.classe

            cours = school_models.Cours.objects.filter(
                Q(status=True) & Q(chapitre__classe=classe)
            ).order_by('-date_add')[:5]

            forum = forum_models.Sujet.objects.filter(
                cours__chapitre__classe=classe
            ).order_by('-date_add')[:5]

            forum_count = forum.count()

            # Préparer les données pour le template
            datas = {
                'cours': cours,
                'forum': forum,
                'forum_count': forum_count,
            }
            return render(request, 'pages/fixed-student-dashboard.html', datas)

    except Exception as e:
        print(f"Erreur dans la vue étudiant : {e}")
        return redirect('/admin/')

@login_required(login_url = 'login')
def payment(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-account-billing-payment-information.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
   
@login_required(login_url = 'login')
def subscription(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-account-billing-subscription.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    
@login_required(login_url = 'login')
def upgrade(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-account-billing-upgrade.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    

@login_required(login_url = 'login')
def edit(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-account-edit.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def edit_basic(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-account-edit-basic.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def edit_profile(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-account-edit-profile.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url = 'login')
def billing(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-billing.html',datas)
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
#                 if request.user.instructor:
#                     return redirect('dashboard')
#             except Exception as e:
#                 print(e)
#                 print("2")
#                 if request.user.student_user:
#                     cours = school_models.Cours.objects.filter(Q(status=True) & Q(chapitre__classe=request.user.student_user.classe))
#                     datas = {
#                                 'all_cours' : all_cours ,
#                            }
#                 return render(request,'pages/fixed-student-browse-courses.html',datas)
#         except Exception as e:
#             print(e)
#             print("3")
#             return redirect("/admin/")
   

@login_required(login_url = 'login')
def cart(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-cart.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")

@login_required(login_url = 'login')
def courses(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard') 
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                   
                    datas = {
                                
                           }
                return render(request,'pages/fixed-student-courses.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    
# @login_required(login_url = 'login')
# def dashboard(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.instructor:
#                     return redirect('dashboard')
#             except Exception as e:
#                 print(e)
#                 print("2")
#                 if request.user.student_user:
#                     datas = {

#                            }
#                 return render(request,'pages/fixed-student-dashboard.html',datas)
#         except Exception as e:
#             print(e)
#             print("3")
#             return redirect("/admin/")

@login_required(login_url = 'login')
def earnings(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-earnings.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")



@login_required(login_url = 'login')
def forum(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    forum_general = forum_models.Sujet.objects.filter(cours=None)
                    forum = forum_models.Sujet.objects.filter(cours__chapitre__classe=request.user.student_user.classe)
                    datas = {
                        'forum_general': forum_general,
                        'forum': forum,
                    }
                return render(request,'pages/fixed-student-forum.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")





@login_required(login_url = 'login')
def forum_lesson(request, slug):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    lesson = school_models.Cours.objects.get(slug=slug)
                    datas = {
                        'lesson':lesson,
                    }
                return render(request,'pages/fixed-student-forum-lesson.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")



@login_required(login_url='login')
def forum_ask(request):
    if request.user.is_authenticated:
        try:
            if hasattr(request.user, 'instructor'):
                return redirect('dashboard')
            elif hasattr(request.user, 'student_user'):
                # Récupérer les cours auxquels l'étudiant a accès
                courses = school_models.Cours.objects.filter(
                    chapitre__classe=request.user.student_user.classe
                )
                datas = {"courses": courses}
                return render(request, 'pages/fixed-student-forum-ask.html', datas)
        except Exception as e:
            print(f"Erreur : {e}")
            return redirect("/admin/")

@login_required(login_url='login')
def forum_post_question(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            details = request.POST.get('details')
            course_id = request.POST.get('course_id')
            notify = request.POST.get('notify', False)

            # Validation des champs
            if not title or not details or not course_id:
                return JsonResponse({"success": False, "message": "Tous les champs sont requis."}, status=400)

            # Vérification que le cours appartient à l'étudiant
            try:
                course = school_models.Cours.objects.get(
                    id=course_id, 
                    chapitre__classe=request.user.student_user.classe
                )
            except school_models.Cours.DoesNotExist:
                return JsonResponse({"success": False, "message": "Cours non trouvé ou accès interdit."}, status=403)

            # Création du sujet
            forum = forum_models.Sujet.objects.create(
                titre=title,
                question=details,
                user=request.user,
                cours=course
            )

            return JsonResponse({"success": True, "message": "Votre question a été postée avec succès !", "slug": forum.slug}, status=201)

        except Exception as e:
            print(f"Erreur lors de la soumission : {e}")
            return JsonResponse({"success": False, "message": "Une erreur est survenue."}, status=500)
    else:
        return JsonResponse({"success": False, "message": "Méthode non autorisée."}, status=405)



@login_required(login_url = 'login')
def forum_thread(request, slug):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    forum = forum_models.Sujet.objects.get(slug=slug)
                    datas = {
                        "forum": forum,
                    }
                return render(request,'pages/fixed-student-forum-thread.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    

@login_required(login_url='login')
def post_reply(request, slug):
    if request.method == 'POST':
        reponse_text = request.POST.get('comment', '').strip()
        if not reponse_text:
            return JsonResponse({'success': False, 'message': 'La réponse ne peut pas être vide.'}, status=400)

        try:
            forum = forum_models.Sujet.objects.get(slug=slug)
            reponse = forum_models.Reponse.objects.create(
                user=request.user,
                sujet=forum,
                reponse=reponse_text
            )
            reponse.save()
            return JsonResponse({'success': True, 'message': 'Réponse ajoutée avec succès !'}, status=200)
        except forum_models.Sujet.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Sujet introuvable.'}, status=404)
        except Exception as e:
            print(f"Erreur dans post_reply : {e}")
            return JsonResponse({'success': False, 'message': 'Une erreur est survenue.'}, status=500)
    return JsonResponse({'success': False, 'message': 'Méthode non autorisée.'}, status=405)

@login_required(login_url='login')
def delete_response(request, response_id):
    if request.method == "POST":
        try:
            response = get_object_or_404(Reponse, id=response_id, user=request.user)
            response.delete()
            return JsonResponse({"success": True, "message": "Réponse supprimée avec succès."})
        except Exception as e:
            print(f"Erreur lors de la suppression : {e}")
            return JsonResponse({"success": False, "message": "Impossible de supprimer la réponse."}, status=500)
    return JsonResponse({"success": False, "message": "Requête invalide."}, status=400)

@login_required(login_url='login')
def delete_forum(request, forum_id):
    try:
        forum = get_object_or_404(forum_models.Sujet, id=forum_id)

        # Vérifier que l'utilisateur est le créateur du forum
        if forum.user != request.user:
            return JsonResponse({'success': False, 'message': "Vous n'avez pas la permission de supprimer ce forum."})

        # Supprimer le forum
        forum.delete()
        return JsonResponse({'success': True, 'message': "Forum supprimé avec succès."})
    except Exception as e:
        print(f"Erreur lors de la suppression : {e}")
        return JsonResponse({'success': False, 'message': "Une erreur est survenue lors de la suppression du forum."})


@login_required(login_url = 'login')
def help_center(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-help-center.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    

@login_required(login_url = 'login')
def invoice(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-invoice.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")

@login_required(login_url='login')
def messages(request, classe):
    try:
        if request.user.student_user:
            salon = get_object_or_404(Salon, classe=request.user.student_user.classe)
            messages = Message.objects.filter(salon=salon).order_by('date_add')

            context = {
                'info_classe': request.user.student_user.classe,
                'classe': salon,
                'messages': messages,
                'classe_json': salon.id,
                'username': request.user.username,
            }
            return render(request, 'pages/fixed-student-messages.html', context)
        else:
            return redirect('login')
    except Exception as e:
        print(f"Erreur : {e}")
        return redirect('login')

# @login_required(login_url = 'login')
# def messages_2(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.instructor:
#                     return redirect('dashboard')
#             except Exception as e:
#                 print(e)
#                 print("2")
#                 if request.user.student_user:
#                     datas = {

#                            }
#                 return render(request,'pages/fixed-student-messages-2.html',datas)
#         except Exception as e:
#             print(e)
#             print("3")
#             return redirect("/admin/")

@login_required(login_url = 'login')
def my_courses(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    chapitre = school_models.Chapitre.objects.filter(status=True)
                    cours = school_models.Cours.objects.filter(status=True)
                    all_cours = school_models.Cours.objects.filter(Q(status=True) & Q(chapitre__classe=request.user.student_user.classe))
                    datas = {
                                'chapitre':chapitre, 
                                'cours':cours,
                                'all_cours': all_cours,
                           }
                return render(request,'pages/fixed-student-my-courses.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")

@login_required(login_url='login')
def quiz_results(request, slug):
    quiz = get_object_or_404(Quiz, slug=slug, status=True)

    # Récupérer le résultat de l'étudiant
    quiz_result = QuizResult.objects.filter(user=request.user, quiz=quiz).first()
    if not quiz_result:
        django_messages.error(request, "Aucun résultat trouvé pour ce quiz.")
        return redirect('quiz-list')

    # Passer les résultats et les réponses au template
    context = {
        'quiz': quiz,
        'quiz_result': quiz_result,
        'student_answers': quiz_result.student_answers.all(),  # Accéder aux réponses via la relation
    }
    return render(request, 'pages/fixed-student-quiz-results.html', context)

@login_required(login_url='login')
def profile(request):
    try:
        # Vérifie si l'utilisateur est un instructeur
        if hasattr(request.user, 'instructor') and request.user.instructor:
            return redirect('dashboard')

        # Vérifie si l'utilisateur est un étudiant
        if hasattr(request.user, 'student_user') and request.user.student_user:
            student = request.user.student_user
            classe = student.classe
            filiere = classe.filiere if classe else None  # Vérifie si la classe a une filière associée

            # Contexte des données pour le template
            datas = {
                'user': request.user,
                'student': student,
                'classe': classe,
                'filiere': filiere,
                'bio': student.bio if student.bio else "Aucune biographie disponible.",
            }
            return render(request, 'pages/fixed-student-profile.html', datas)

        # Si l'utilisateur n'est pas un étudiant ou instructeur, redirige vers la connexion
        return redirect('login')

    except Exception as e:
        print(f"Erreur dans la vue profile : {e}")
        return redirect('login')

@login_required(login_url='login')
def profile_posts(request):
    if request.user.is_authenticated:
        try:
            # Vérifie si l'utilisateur est un instructeur
            if hasattr(request.user, 'instructor') and request.user.instructor:
                return redirect('dashboard')

            # Vérifie si l'utilisateur est un étudiant
            if hasattr(request.user, 'student_user') and request.user.student_user:
                student = request.user.student_user

                # Préparation des données du contexte
                datas = {
                    'student': student,
                    'username': request.user.username,
                    'profile_photo': student.photo.url if student.photo else '/static/assets/images/default_avatar.png',
                    'bio': student.bio if student.bio else "Aucune biographie disponible.",
                }

                return render(request, 'pages/fixed-student-profile-posts.html', datas)

        except Exception as e:
            print(f"Erreur : {e}")
            return redirect('login')



@login_required(login_url='login')
def quiz_list(request):
    try:
        # Vérifiez si l'utilisateur est un étudiant
        if hasattr(request.user, 'student_user'):
            classe = request.user.student_user.classe

            # Récupérer les quiz disponibles pour la classe
            quizzes = Quiz.objects.filter(
                cours__chapitre__classe=classe,
                status=True  # Quiz actifs
            ).order_by('-date_add')

            # Vérifiez si les slugs sont valides
            for quiz in quizzes:
                if not quiz.slug:
                    print(f"Erreur : Quiz '{quiz.titre}' sans slug.")

            return render(request, 'pages/fixed-student-quiz-list.html', {
                'quizzes': quizzes,
            })

        # Redirection si l'utilisateur n'est pas un étudiant
        return redirect('dashboard')

    except Exception as e:
        print(f"Erreur dans quiz_list : {e}")
        return render(request, 'pages/error.html', {'message': 'Une erreur est survenue.'})
    


@login_required(login_url='login')
def submit_quiz(request, slug):
    """
    Vue pour gérer la soumission d'un quiz par un étudiant.
    """
    quiz = get_object_or_404(Quiz, slug=slug, status=True)

    if request.method == 'POST':
        try:
            # Récupérer toutes les questions du quiz
            questions = quiz.quiz_question.all()
            total_points = sum([question.point for question in questions])
            total_score = 0

            # Créer un enregistrement pour le résultat de l'utilisateur
            quiz_result = QuizResult.objects.create(
                user=request.user,
                quiz=quiz,
                score=0  # Initialement à 0
            )

            for question in questions:
                selected_answer_id = request.POST.get(f'question_{question.id}')
                selected_answer = None
                is_correct = False
                points_earned = 0

                if selected_answer_id:
                    try:
                        selected_answer = Reponse.objects.get(id=selected_answer_id, question=question)
                        is_correct = selected_answer.is_True
                        if is_correct:
                            points_earned = question.point
                            total_score += points_earned
                    except Reponse.DoesNotExist:
                        pass

                # Enregistrer la réponse de l'étudiant
                StudentAnswer.objects.create(
                    quiz_result=quiz_result,
                    question=question,
                    selected_answer=selected_answer,
                    is_correct=is_correct,
                    points_earned=points_earned
                )

            # Mettre à jour le score total
            final_score = (total_score / total_points) * 100 if total_points > 0 else 0
            quiz_result.score = final_score
            quiz_result.save()

            # Message de succès
            django_messages.success(request, f"Quiz soumis avec succès ! Votre score : {final_score:.2f}%")

            return redirect('quiz-results', slug=quiz.slug)

        except Exception as e:
            # Gestion des erreurs
            django_messages.error(request, f"Une erreur s'est produite : {e}")
            return redirect('quiz-list')

    # Si la méthode n'est pas POST
    django_messages.error(request, "Méthode de soumission invalide.")
    return redirect('quiz-list')


@login_required(login_url = 'login')
def quizzes(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-quizzes.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    

@login_required(login_url = 'login')
def statement(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-statement.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    


# @login_required(login_url = 'login')
# def student_take_course(request, slug):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.instructor:
#                     return redirect('dashboard')
#             except Exception as e:
#                 print(e)
#                 print("2")
#                 if request.user.student_user:
#                     cours  = school_models.Cours.objets.get(slug=slug)
#                     datas = {
#                         'cours': cours,
#                     }
#                 return render(request,'pages/fixed-student-student-take-course.html',datas)
#         except Exception as e:
#             print(e)
#             print("3")
#             return redirect("/admin/")


@login_required(login_url='login')
def take_course(request, slug):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    cours = school_models.Cours.objects.get(slug=slug)
                    instructor = instructor_models.Instructor.objects.get(classe__id=request.user.student_user.classe.id)
                    datas = {
                        'cours': cours,
                        'instructor' : instructor,
                    }
                return render(request,'pages/fixed-student-take-course.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect('my_courses')
   
@login_required(login_url='login')
def take_quiz(request, slug):
    if request.user.is_authenticated:
        try:
            # Vérifier si l'utilisateur est un étudiant
            if hasattr(request.user, 'instructor'):
                return redirect('dashboard')

            if hasattr(request.user, 'student_user'):
                # Récupérer le quiz correspondant au slug
                quiz = get_object_or_404(quiz_models.Quiz, slug=slug, status=True)

                # Vérifier si l'étudiant appartient à la classe du quiz
                if quiz.cours.chapitre.classe != request.user.student_user.classe:
                    return redirect('quiz-list')

                # Récupérer les questions associées au quiz
                questions = quiz.quiz_question.filter(status=True)

                # Passer les données au template
                datas = {
                    'quiz': quiz,
                    'questions': questions,
                }
                return render(request, 'pages/fixed-student-take-quiz.html', datas)

        except Exception as e:
            print(f"Erreur dans take_quiz : {e}")
            return redirect('quiz-list')

@login_required(login_url = 'login')
def view_course(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-view-course.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    
@login_required(login_url = 'login')
def account_edit(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect('dashboard')
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {

                           }
                return render(request,'pages/fixed-student-account-edit.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")

        
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
        student = models.Student.objects.get(user__id=request.user.id)
        student.bio = bio
        student.save()
        try:
            image = request.FILES["file"]
            student.photo = image 
            student.save()

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

    

        
def post_forum(request):
    titre = request.POST.get("titre")
    question = request.POST.get("question")
    lesson = request.POST.get("lesson")
    val = ""
    try:
        lesson = school_models.Cours.objects.get(id=int(lesson))
        forum = forum_models.Sujet()
        forum.titre = titre
        forum.question = question
        forum.cours = lesson
        forum.user = request.user
        forum.save()
        val = forum.slug
        success = True 
        message = "Votre sujet a bien été ajouté!"
    except Exception as e:
        print(e)
        success = False
        message = "une erreur est subvenue lors de la soumission"
    data = {
        "success" : success,
        "message": message,
        "forum": val,
        }
    return JsonResponse(data,safe=False)

    
def post_forum_g(request):
    titre = request.POST.get("titre")
    question = request.POST.get("question")
    val = ""
    try:
        forum = forum_models.Sujet()
        forum.titre = titre
        forum.question = question
        forum.user = request.user
        forum.save()
        val = forum.slug
        success = True 
        message = "Votre sujet a bien été ajouté!"
    except Exception as e:
        print(e)
        success = False
        message = "une erreur est subvenue lors de la soumission"
    data = {
        "success" : success,
        "message": message,
        "forum": val,
        }
    return JsonResponse(data,safe=False)

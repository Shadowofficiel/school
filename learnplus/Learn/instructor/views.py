from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from school import models as school_models
from quiz import models as quiz_models
from . import models
from django.http import JsonResponse 
from django.db.models import Q

# Create your views here.
@login_required(login_url = 'login')
def dashboard(request):
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
                    return render(request,'pages/instructor-dashboard.html',datas)
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
   



@login_required(login_url = 'login')
def course_edit(request):
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
                    matiere = school_models.Matiere.objects.filter(status=True)
                    datas = {
                        'matiere':matiere,
                    }
                    return render(request,'pages/instructor-course-edit.html',datas)
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
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    Chapitre = school_models.Chapitre.objects.filter(Q(status=True) & Q(classe=request.user.instructor.classe))
                    datas = {
                            'Chapitre' : Chapitre ,
                           }
                    return render(request,'pages/instructor-courses.html',datas)
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





@login_required(login_url = 'login')
def edit_invoice(request):
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
                    return render(request,'pages/instructor-edit-invoice.html',datas)
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
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                    return render(request,'pages/instructor-forum.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    




@login_required(login_url = 'login')
def forum_ask(request):
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
                    return render(request,'pages/instructor-forum-ask.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    




@login_required(login_url = 'login')
def forum_thread(request):
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
                    return render(request,'pages/instructor-forum-thread.html',datas)
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
                if request.user.student_user:
                    return redirect('index_student')
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {

                           }
                    return render(request,'pages/instructor-invoice.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
    





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
def messages(request):
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
                    return render(request,'pages/instructor-messages.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")
   




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
  





@login_required(login_url = 'login')
def profile(request):
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
                    return render(request,'pages/instructor-profile.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")





@login_required(login_url = 'login')
def quiz_edit(request):
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
                    return render(request,'pages/instructor-quiz-edit.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")





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
    




@login_required(login_url = 'login')
def quizzes(request):
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
                    return render(request,'pages/instructor-quizzes.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")





@login_required(login_url = 'login')
def review_quiz(request):
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
                    return render(request,'pages/instructor-review-quiz.html',datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")





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
def post_cours(request):
    title = request.POST.get("title")
    matiere = request.POST.get("matiere")
    date_fin = request.POST.get("date_fin")
    description = request.POST.get("description")
    date_debut = request.POST.get("date_debut")
    duration = request.POST.get("duration")
    chapitre = ''

    try:
        chapitre = school_models.Chapitre.objects.get(titre=title)
        try:
            video = request.FILES["file"]
            chapitre.video = video
        except :
            pass
        chapitre.titre = title
        chapitre.duree_en_heure = duration
        chapitre.date_debut = date_debut
        chapitre.date_fin = date_fin
        matiere = school_models.Matiere.objects.get(id=int(matiere))
        chapitre.matiere = matiere
        chapitre.classe = request.user.instrctor.classe
        chapitre.save()
        success = True 
        message = 'mis à jour effectué  avec succés'
    except:
        chapitre = school_models.Chapitre()
        try:
            video = request.FILES["file"]
            chapitre.video = video
        except :
            pass
        chapitre.titre = title
        chapitre.duree_en_heure = duration
        chapitre.date_debut = date_debut
        chapitre.date_fin = date_fin
        matiere = school_models.Matiere.objects.get(id=int(matiere))
        chapitre.matiere = matiere
        chapitre.classe = request.user.instructor.classe
        chapitre.save()
        success = True 
        message = 'chapitre ajouté avec succés'
    data = {'success' : success,
            'message' : message,
            'slug': chapitre.slug,
    }
    return JsonResponse(data,safe=False)

def post_lesson(request):
    title = request.POST.get("title")
    chapitre = request.POST.get("chapitre")

    try:
        cours = school_models.Cours.objects.get(Q(titre=title) & Q(chapitre__id=int(chapitre)))

        try:
            video = request.FILES["file"]
            image = request.FILES["image"]
            pdf = request.FILES["pdf"]
            cours.video = video
            cours.image = image
            cours.pdf = pdf
        except :
            pass
        cours.titre = title
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





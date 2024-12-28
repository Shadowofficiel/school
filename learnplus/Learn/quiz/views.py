from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from school import models as school_models  # Pour importer les modèles liés (Cours, Chapitre, etc.)
from quiz import models as quiz_models  # Pour les modèles liés au quiz
from django.http import JsonResponse
from instructor.models import AffectationMatiere  

@login_required(login_url='login')
def quiz_add(request):
    # Vérifier que l'utilisateur est un instructeur
    if not hasattr(request.user, 'instructor'):
        return redirect('dashboard')  # Redirection si l'utilisateur n'est pas un instructeur

    try:
        if request.method == 'GET':
            # Récupérer les cours associés aux matières assignées à l'instructeur
            matieres = school_models.AffectationMatiere.objects.filter(
                instructor=request.user,
                status=True
            ).values_list('matiere', flat=True)  # Obtenir les IDs des matières

            cours = school_models.Cours.objects.filter(
                chapitre__matiere__in=matieres,
                status=True
            ).distinct()  # Filtrer uniquement les cours actifs liés aux matières

            return render(request, 'pages/instructor-quiz-add.html', {'cours': cours})

        if request.method == 'POST':
            # Récupérer les champs du formulaire
            titre = request.POST.get('quiz_title')
            cours_id = request.POST.get('course_title')
            date = request.POST.get('date')
            temps = request.POST.get('quiz_time')
            tentatives = request.POST.get('quiz_attempts')

            # Validation des champs obligatoires
            if not all([titre, cours_id, date, temps, tentatives]):
                matieres = school_models.AffectationMatiere.objects.filter(
                    instructor=request.user,
                    status=True
                ).values_list('matiere', flat=True)

                cours = school_models.Cours.objects.filter(
                    chapitre__matiere__in=matieres,
                    status=True
                ).distinct()

                return render(request, 'pages/instructor-quiz-add.html', {
                    'cours': cours,
                    'error': 'Tous les champs sont obligatoires.',
                })

            # Vérification que le cours appartient bien à une matière assignée à l'instructeur
            try:
                cours = school_models.Cours.objects.get(
                    id=cours_id,
                    chapitre__matiere__in=matieres,
                    status=True
                )
            except school_models.Cours.DoesNotExist:
                matieres = school_models.AffectationMatiere.objects.filter(
                    instructor=request.user,
                    status=True
                ).values_list('matiere', flat=True)

                cours = school_models.Cours.objects.filter(
                    chapitre__matiere__in=matieres,
                    status=True
                ).distinct()

                return render(request, 'pages/instructor-quiz-add.html', {
                    'cours': cours,
                    'error': "Le cours sélectionné n'est pas valide.",
                })

            # Création du quiz
            quiz = quiz_models.Quiz(
                titre=titre,
                cours=cours,
                date=date,
                temps=temps,
                nombre_tentatives=tentatives
            )
            quiz.save()

            # Redirection vers la liste des quiz après succès
            return redirect('instructor-quizzes')

    except Exception as e:
        print(f"Erreur dans quiz_add: {e}")
        return redirect('/admin/')
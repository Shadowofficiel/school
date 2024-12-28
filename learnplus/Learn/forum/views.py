from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Sujet, Reponse
from school.models import Cours
from django.utils.text import slugify

@login_required(login_url='login')
def create_forum(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        question = request.POST.get('question')
        cours_id = request.POST.get('cours_id')
        try:
            cours = Cours.objects.get(id=cours_id)
            forum = Sujet.objects.create(
                user=request.user,
                cours=cours,
                titre=titre,
                question=question,
                slug=slugify(f"{titre}-{datetime.now().timestamp()}")
            )
            forum.save()
            return redirect('forum-detail', slug=forum.slug)
        except Cours.DoesNotExist:
            return render(request, 'forum/create_forum.html', {'error': "Cours invalide."})
    else:
        cours = Cours.objects.filter(chapitre__classe=request.user.instructor.classe)
        return render(request, 'forum/create_forum.html', {'cours': cours})

@login_required(login_url='login')
def forum_detail(request, slug):
    forum = get_object_or_404(Sujet, slug=slug)
    responses = Reponse.objects.filter(sujet=forum)
    return render(request, 'forum/forum_detail.html', {'forum': forum, 'responses': responses})

@login_required(login_url='login')
def add_response(request, slug):
    forum = get_object_or_404(Sujet, slug=slug)
    if request.method == 'POST':
        reponse = request.POST.get('reponse')
        Reponse.objects.create(
            sujet=forum,
            user=request.user,
            reponse=reponse
        )
        return redirect('forum-detail', slug=forum.slug)

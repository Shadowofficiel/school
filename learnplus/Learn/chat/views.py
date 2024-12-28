from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from school.models import Classe
from chat.models import Salon
import json
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from chat.models import Message, Salon
from .models import PrivateMessage

@login_required(login_url='login')
def messages(request, classe):
    try:
        if hasattr(request.user, 'student_user') and request.user.student_user:
            classe_instance = get_object_or_404(Classe, id=request.user.student_user.classe.id)
        elif hasattr(request.user, 'instructor') and request.user.instructor:
            niveau_nom, numero_classe = classe.split()
            classe_instance = get_object_or_404(
                Classe, 
                niveau__nom__iexact=niveau_nom, 
                numeroClasse=int(numero_classe)
            )
        else:
            return redirect('login')

        salon = get_object_or_404(Salon, classe=classe_instance)
        messages = Message.objects.filter(salon=salon).order_by('date_add')

        context = {
            'info_classe': classe_instance,
            'classe': salon,
            'messages': messages,
            'classe_json': salon.classe.id,
            'username': request.user.username,
        }
        return render(request, 'pages/instructor-messages.html', context)

    except Exception as e:
        print(f"Erreur dans la vue messages : {e}")
        return redirect('instructor-forum')
    

@login_required(login_url='login')
def private_chat(request, student_id):
    if not hasattr(request.user, 'instructor'):
        return redirect('login')

    student = get_object_or_404(User, id=student_id)
    classe = request.user.instructor.classe
    students = classe.student_classe.all()
    messages = PrivateMessage.objects.filter(
        sender=request.user,
        receiver=student
    ) | PrivateMessage.objects.filter(
        sender=student,
        receiver=request.user
    )
    messages = messages.order_by('date_add')

    context = {
        'student': student,
        'students': students,
        'messages': messages,
        'username': request.user.username,
        'classe': classe,
    }
    return render(request, 'pages/private-chat.html', context)
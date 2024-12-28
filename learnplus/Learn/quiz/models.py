from django.db import models
from school import models as school_models
from django.utils.text import slugify
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Quiz(models.Model):
    date = models.CharField(max_length=255)
    titre = models.CharField(max_length=255)
    cours = models.ForeignKey(school_models.Cours, on_delete=models.CASCADE, related_name='quiz_cours')
    temps = models.IntegerField()
    nombre_tentatives = models.IntegerField(default=1)  # Nouveau champ pour le nombre de tentatives
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.titre), slugify(datetime.now().microsecond)))
        super(Quiz, self).save(*args, **kwargs)

class Devoir(models.Model):
    sujet = models.TextField(max_length=255)
    dateDebut = models.DateTimeField()
    dateFermeture = models.DateTimeField()
    chapitre = models.ForeignKey(school_models.Chapitre,on_delete=models.CASCADE,related_name='quiz_chapitre')
    coefficient = models.IntegerField()
    support = models.FileField(upload_to='fichier/import')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True,  blank=True)

    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.sujet), slugify(datetime.now().microsecond)))
        super(Devoir, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Devoir'
        verbose_name_plural = 'Devoirs'

    def __str__(self):
        return self.chapitre.titre

class Question(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='quiz_question')
    question = models.TextField(max_length=255)
    point = models.IntegerField()
    TYPEQUESTIONS = [
        ('qcm','qcm'),
        ('question-reponse','question-reponse'),
    ]
    typequestion = models.CharField(choices=TYPEQUESTIONS,max_length=20)   
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.quiz.titre

class Reponse(models.Model):
    reponse = models.TextField(max_length=255)
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='question_reponse')
    is_True = models.BooleanField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Reponse'
        verbose_name_plural = 'Reponses'

    def __str__(self):
        return self.reponse
    
class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_results')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='results')
    score = models.FloatField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Résultat du Quiz"
        verbose_name_plural = "Résultats des Quiz"

    def __str__(self):
        return f"{self.user.username} - {self.quiz.titre}"


class QuestionResponse(models.Model):
    quiz_result = models.ForeignKey(QuizResult, on_delete=models.CASCADE, related_name='responses')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='responses')
    selected_answer = models.CharField(max_length=255, null=True, blank=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quiz_result.user.username} - {self.question.question}"
    

class StudentAnswer(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='student_answers'
    )
    quiz = models.ForeignKey(
        'Quiz', on_delete=models.CASCADE, related_name='student_answers'
    )
    question = models.ForeignKey(
        'Question', on_delete=models.CASCADE, related_name='student_answers'
    )
    selected_answer = models.ForeignKey(
        'Reponse', on_delete=models.SET_NULL, null=True, blank=True, related_name='student_answers'
    )
    is_correct = models.BooleanField(default=False)
    points_earned = models.IntegerField(default=0)
    quiz_result = models.ForeignKey(
        QuizResult, on_delete=models.CASCADE, related_name='student_answers', null=True, blank=True
    )  # Champ non obligatoire
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.question.question}"

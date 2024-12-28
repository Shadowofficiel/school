from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="index_student"), 
    # path('payment', views.payment, name='payment'),
    # path('subscription', views.subscription, name='subscription'), 
    # path('upgrade', views.upgrade, name='upgrade'),
    path('edit', views.edit, name='edit'),
    path('account_edit', views.account_edit, name='account-edit'),
    # path('invoice', views.invoice, name='invoice'),
    path('edit_basic', views.edit_basic, name='edit-basic'),
    path('edit_profile', views.edit_profile, name='edit-profile'),
    path('billing', views.billing, name='billing'),
    # path('browse_courses', views.browse_courses, name='browse-courses'),
    path('cart', views.cart, name='cart'),
    # path('earnings', views.earnings, name='earnings'),
    path('forum', views.forum, name='forum'),
    path('forum_lesson/<slug>', views.forum_lesson, name='forum-lesson'),
    path('forum_ask', views.forum_ask, name='forum-ask'),
    path('forum_post_question', views.forum_post_question, name='forum-post-question'),
    path('forum_thread/<slug>', views.forum_thread, name='forum-thread'),
    path('help_center', views.help_center, name='help-center'),
    path('messages/<str:classe>/', views.messages, name='messages'),
    path('my_courses', views.my_courses, name='my-courses'),
    path('quiz_list', views.quiz_list, name='quiz-list'),
    path('quiz_results/<slug:slug>/', views.quiz_results, name='quiz-results'),
    path('take_quiz/<slug:slug>/', views.take_quiz, name='take-quiz'),
    path('profile', views.profile, name='profile'),
    path('profile_posts', views.profile_posts, name='profile-posts'),
    path('quizzes', views.quizzes, name='quizzes'),
    path('take_course/<slug>', views.take_course, name='take-course'),
    path('view_course', views.view_course, name='view-course'),
    path('submit_quiz/<slug:slug>/', views.submit_quiz, name='submit-quiz'),
    path('forum_thread/<slug>/reply/', views.post_reply, name='forum-post-reply'),
    path('delete_response/<int:response_id>/', views.delete_response, name='delete-response'),
    path('delete_forum/<int:forum_id>/', views.delete_forum, name='delete-forum'),
    ########## post ###############
    path('update_profil', views.update_profil, name='update_profil'),
    path('update_password', views.update_password, name='update_password'),
    path('post_forum', views.post_forum, name='post_forum'),
    path('post_forum_g', views.post_forum_g, name='post_forum_g'),

]
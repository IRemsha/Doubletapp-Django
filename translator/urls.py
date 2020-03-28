from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoriesView.as_view()),
    path('levels/', views.LevelsView.as_view()),
    path('themes/', views.ThemesView.as_view()),
    path('themes/<str:category>/<str:level>', views.ThemesFilterView.as_view()),
    path('words/<str:id>/', views.WordsView.as_view()),

]
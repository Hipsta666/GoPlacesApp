from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

from . import views


urlpatterns = [
    path('quiz/', views.QuizView.as_view()),
    path('offers/', views.OffersView.as_view()),
    path('offers/<slug:slug>/', views.OfferDetailView.as_view(), name='offer_detail'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


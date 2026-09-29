from os import name

from django.urls import path,include
from .views import  BankCreditPredictionViewSet


urlpatterns=[
    path('bank_prediction/',BankCreditPredictionViewSet.as_view(),name='bank-prediction')
]
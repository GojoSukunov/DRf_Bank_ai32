from rest_framework import serializers
from .models import BankCreditPrediction

class BankCreditSerializer(serializers.ModelSerializer):
    class Meta:
        model=BankCreditPrediction
        fields=['person_age','person_income','person_emp_exp','loan_amnt',
                'loan_int_rate','loan_percent_income','credit_score','person_home_ownership']
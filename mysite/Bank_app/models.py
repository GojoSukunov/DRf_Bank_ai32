from django.db import models

class BankCreditPrediction(models.Model):
    person_age=models.PositiveSmallIntegerField(default=0)
    person_income=models.PositiveSmallIntegerField(default=0)
    person_emp_exp=models.PositiveSmallIntegerField(default=0)
    loan_amnt=models.PositiveSmallIntegerField(default=0)
    loan_int_rate=models.PositiveSmallIntegerField(default=0)
    loan_percent_income=models.PositiveSmallIntegerField(default=0)
    credit_score=models.PositiveSmallIntegerField(default=0)
    person_home_ownership=models.CharField(max_length=100)
    credit_prediction=models.PositiveSmallIntegerField(default=0)

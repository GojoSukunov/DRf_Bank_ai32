from pathlib import Path

import joblib
from rest_framework import status
from rest_framework import views
from rest_framework.response import Response

from . import serializers
from .serializers import BankCreditSerializer
base_dir=Path(__file__).resolve().parent.parent
path_model=base_dir/'models'/'bank_model_ai32.pkl'
path_scaler=base_dir/'models'/'bank_scaler_ai32.pkl'


model=joblib.load(path_model)
scaler=joblib.load(path_scaler)
owners_type=['OTHER','OWN','RENT']


class BankCreditPredictionViewSet(views.APIView):
    def post(self,request):
        instance=serializers.BankCreditSerializer(data=self.request.data)

        if instance.is_valid():
            data=instance.validated_data

            new_person_home_ownership=data.pop('person_home_ownership')
            person_home_ownership_0_1=[1 if new_person_home_ownership==i else 0 for i in owners_type]


            features=[
                data['person_age'],
                data['person_income'],
                data['person_emp_exp'],
                data['loan_amnt'],
                data['loan_int_rate'],
                data['loan_percent_income'],
                data['credit_score'],
            ]+person_home_ownership_0_1
            scaler_data=scaler.transform([features])
            prediction=int(model.predict(scaler_data)[0])
            bank=instance.save(credit_prediction=prediction)
            return Response({'CreditPrediction':prediction,'data':BankCreditSerializer(bank).data},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
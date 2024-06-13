from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "CPF inválido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "Não incluir numeros"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "RG invalido deve conter 9 digitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': "Padrão do numero celular 31 99765-2325"})
        return data
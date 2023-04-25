from sqlalchemy import Column, String, DateTime, Float
from datetime import datetime
from typing import Union

class Animal():
    nome = Column(String(140), unique=True)
    peso = Column(Float)
    data_insercao = Column(DateTime, default=datetime.now())
    def __init__(self, nome: str, peso: float,
                 data_insercao: Union[DateTime, None] = None):
        """
        Cria um Animal

        Arguments:
            nome: nome do animal.
            peso: peso do animal
        """
        self.nome = nome
        self.peso = peso

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    ## o cálculo do NEM é baseado no peso e no fator nem de cada animal
    def calcula_nem(_self):
        nem = _self.fator_nem * (_self.peso ** _self.fator_expoente)
        ## formata o número com dois dígitos decimais
        return "{:.2f}".format(round(nem, 2))
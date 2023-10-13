
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def exibirData(self):
        print("Hoje é dia {} do {} de {}.".format(self.dia, self.mes, self.ano))


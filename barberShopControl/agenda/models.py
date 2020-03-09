from django.db import models

class Estabelecimento(models.Model):
    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True, auto_now_add=False)
    cnpj = models.CharField(max_length=15, unique=True)
    razao_social = models.CharField(max_length=60)
    nome_fantasia = models.CharField(max_length=60)
    end_cep = models.CharField(max_length=8)
    end_logradouro = models.CharField(max_length=100, blank=True)
    end_numero = models.CharField(max_length=8, blank=True)
    end_complemento = models.CharField(max_length=100, blank=True)
    end_bairro = models.CharField(max_length=72, blank=True)
    end_cidade = models.CharField(max_length=72, blank=True)
    end_uf = models.CharField(max_length=2, blank=True)


class Servico(models.Model):
    nome = models.CharField(max_length=40)
    tempo_duracao = models.TimeField(auto_now=False, auto_now_add=False)
    valor = models.DecimalField(max_digits=7, decimal_places=2)


class Usuario(models.Model):
    SEXO_CHOICES = (
        ("M", "Masculino"),
        ("F", "Feminino")
    )

    PERFIL_CHOICES = (
        ("C", "Cliente"),
        ("E", "Especialista"),
        ("A", "Administrador")
    )

    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True, auto_now_add=False)
    situacao_conta = models.BooleanField()
    perfil = models.CharField(max_length=1, choices=PERFIL_CHOICES)
    primeiro_nome = models.CharField(max_length=15)
    segundo_nome = models.CharField(max_length=45)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_length=20)
    telefone = models.CharField(max_length=11)
    end_cep = models.CharField(max_length=8)
    end_logradouro = models.CharField(max_length=100, blank=True)
    end_numero = models.CharField(max_length=8, blank=True)
    end_complemento = models.CharField(max_length=100, blank=True)
    end_bairro = models.CharField(max_length=72, blank=True)
    end_cidade = models.CharField(max_length=72, blank=True)
    end_uf = models.CharField(max_length=2, blank=True)


class Reserva(models.Model):
    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    data_reserva = models.DateTimeField(auto_now=False, auto_now_add=False)
    cliente_id = models.ForeignKey("Usuario", related_name="cliente_id", on_delete=models.CASCADE)
    especialista_id = models.ForeignKey("Usuario", related_name="especialista_id", on_delete=models.CASCADE)
    servico_id = models.ForeignKey("Servico", related_name="servico", on_delete=models.CASCADE)
    avaliacao = models.IntegerField(blank=True, null=True)
    avaliacao_observacao = models.TextField(blank=True)
    atend_realizado = models.BooleanField()
    atend_observacao = models.TextField(blank=True)
    atend_encerrado_por = models.ForeignKey("Usuario", related_name="atend_encerrado_por", on_delete=models.CASCADE, null=True)


class Estab_Dias_Funcionamento(models.Model):
    DIA_CHOICES = (
        ("seg", "Segunda"),
        ("ter", "Terça"),
        ("qua", "Quarta"),
        ("qui", "Quinta"),
        ("sex", "Sexta"),
        ("sab", "Sábado"),
        ("dom", "Domingo")
    )

    data_modificacao = models.DateTimeField(auto_now=True, auto_now_add=False)
    estab_id = models.ForeignKey("Estabelecimento", related_name="estab_id", on_delete=models.CASCADE)
    dia_funcionamento = models.CharField(max_length=3, choices=DIA_CHOICES)
    hora_inicial = models.TimeField(auto_now=False, auto_now_add=False)
    hora_final = models.TimeField(auto_now=False, auto_now_add=False)


class Espec_Dias_Atendimento(models.Model):
    data_criacao = models.DateTimeField(auto_now=False, auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True, auto_now_add=False)
    espec_id = models.ForeignKey("Especialista", on_delete=models.CASCADE)
    estab_dias_func_id = models.ForeignKey("Estab_Dias_Funcionamento", related_name="estab_dias_func_id", on_delete=models.CASCADE)
    hora_inicial = models.TimeField(auto_now=False, auto_now_add=False)
    hora_final = models.TimeField(auto_now=False, auto_now_add=False)


class Especialista(models.Model):
    usuario_id = models.ForeignKey("Usuario", related_name="usuario_id", on_delete=models.CASCADE)
    servico_id = models.ForeignKey("Servico", related_name="servico_id", on_delete=models.CASCADE)

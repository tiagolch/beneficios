from django.db import models
from datetime import date, timedelta



class Empresa_Cliente(models.Model):
    nome = models.CharField(max_length=80, verbose_name='Cliente')

    def __str__(self):
        return self.nome


class Departamento(models.Model):
    nome = models.CharField(max_length=80, verbose_name='Departamento')
    codigo = models.CharField(max_length=8, verbose_name='Codigo Departamento', default='')

    def __str__(self):
        return f'{self.codigo} - {self.nome}'

    class Meta:
        unique_together = ("nome", "codigo",)


class Cargo(models.Model):
    cargo = models.CharField(max_length=80, verbose_name='Cargo')

    def __str__(self):
        return self.cargo


class Centro_de_Custo(models.Model):
    centroDeCusto = models.CharField(max_length=80, verbose_name='Centro de Custo')

    def __str__(self):
        return self.centroDeCusto


class banco(models.Model):
    banco = models.CharField(max_length=20, verbose_name='Banco')
    codigo = models.CharField(max_length=4, verbose_name='Codigo')

    def __str__(self):
        return self.banco


class Informacao_Pagamento(models.Model):
    banco = models.ForeignKey('Banco', on_delete=models.DO_NOTHING, verbose_name='Banco')
    agencia = models.CharField(max_length=4, verbose_name='Agencia')
    cc = models.CharField(max_length=7, verbose_name='C/C')

    def __str__(self):
        return f'{str(self.banco)} Agencia:{self.agencia} C/C:{self.cc}'


class Profissional(models.Model):
    nomeCompleto = models.CharField(max_length=80, verbose_name='Profissional')
    cpf = models.CharField(max_length=11, verbose_name='CPF', unique=True)
    Empresa = models.ForeignKey('Empresa_cliente', on_delete=models.DO_NOTHING, verbose_name='Cliente')
    Departamento = models.ForeignKey('Departamento', on_delete=models.DO_NOTHING, verbose_name='Novo Departamento')
    cargo = models.ForeignKey('Cargo', on_delete=models.DO_NOTHING, verbose_name='Cargo')
    base = models.CharField(max_length=30, verbose_name='Base')
    salario = models.ForeignKey('Salario', on_delete=models.CASCADE, verbose_name='Salario')
    contato = models.CharField(max_length=11, verbose_name='Contato', blank='True', null='True')
    matricula = models.CharField(max_length=6, verbose_name='Matricula')
    informacao_pagamento = models.ForeignKey('Informacao_Pagamento', on_delete=models.CASCADE, verbose_name='Informações para Pagamento')
    status = models.BooleanField(default=True, verbose_name='Status')

    def __str__(self):
        return self.nomeCompleto


class Contrato(models.Model):
    profissional = models.ForeignKey('Profissional', on_delete=models.CASCADE, verbose_name='Profissional')
    inicio = models.DateField(auto_created=True, verbose_name='Inicio')
    termino = models.DateField(auto_created=True, verbose_name='Termino', blank=True, null=True)
    tempoInicial = models.PositiveIntegerField(default=30)
    prorrogacao = models.PositiveIntegerField(default=0)
    limiteContratacao = models.PositiveIntegerField()
    limiteContratacaoPadrao = models.PositiveIntegerField(default=270)

    def __str__(self):
        return str(self.profissional)

    def get_inicio(self):
        return self.inicio.strftime('%d/%m/%Y')

    def get_termino(self):
        return self.termino.strftime('%d/%m/%Y')

    def save(self, *args, **kwargs):
        if self.tempoInicial <= self.limiteContratacaoPadrao:
            self.limiteContratacao = self.limiteContratacaoPadrao - self.tempoInicial
            temp = self.inicio
            temp += timedelta(days=self.tempoInicial)
            self.termino = temp
        else:
            self.tempoInicial = self.limiteContratacaoPadrao
            self.limiteContratacao = self.limiteContratacaoPadrao - self.tempoInicial
        super().save(*args, **kwargs)


class Informacoes_Escala(models.Model):
    escala = models.CharField(max_length=20, verbose_name='Escala')
    horarioInicial = models.TimeField(auto_created=True, verbose_name='Horario Inicio')
    horarioFinal = models.TimeField(auto_created=True, verbose_name='Horario Final')
    diasPorSemana = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.escala


class Salario(models.Model):
    base = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Base')
    adicional_tipo = models.CharField(max_length=20, default='', verbose_name='Adicional (Tipo)')
    adicional_valor = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Adicional (Valor)')
    desconto_VT = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Desconto VT', blank=True, null=True)
    desconto_VR = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Desconto VR', blank=True, null=True)
    desconto_VA = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Desconto VA', blank=True, null=True)
    adiantamento = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Adiantamento', blank=True, null=True)
    liquido = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Liquido', blank=True, null=True)
    comissao = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Comissão', blank=True, null=True)
    bonus = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Bonus', blank=True, null=True)

    def __str__(self):
        return str(self.base)


class Dia_de_Pagamento(models.Model):
    profissional = models.ForeignKey('Profissional', on_delete=models.CASCADE, db_column='nomeCompleto', related_name='nomeCompleto2')
    adiantamento = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Adiantamento')
    salario = models.ForeignKey('Profissional', on_delete=models.CASCADE, db_column='salario', verbose_name='Salario')
    comissao = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Comissão')
    bonus = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Bônus')

    def __str__(self):
        return str(self.adiantamento)



from django.contrib import admin
from .models import *


@admin.register(Empresa_Cliente)
class Empresa_ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'codigo']
    search_fields = ['nome', 'codigo']


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['cargo']


@admin.register(banco)
class BancoAdmin(admin.ModelAdmin):
    list_display = ['banco', 'codigo']
    search_fields = ['banco', 'codigo']

@admin.register(Informacao_Pagamento)
class Informacao_PagamentoAdmin(admin.ModelAdmin):
    list_display = ['banco', 'agencia', 'cc']
    search_fields = ['banco', 'agencia', 'cc']

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ['nomeCompleto', 'cpf', 'salario', 'contato', 'matricula', 'status',]
    search_fields = ['nomeCompleto']
    list_filter = ['Departamento', 'Empresa', 'status']

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ['profissional', 'get_inicio', 'get_termino', 'tempoInicial', 'prorrogacao', 'limiteContratacao']
    list_editable = ['tempoInicial', 'prorrogacao']
    search_fields = ['profissional']


@admin.register(Informacoes_Escala)
class Informacoes_EscalaAdmin(admin.ModelAdmin):
    list_display = ['escala', 'horarioInicial', 'horarioFinal', 'diasPorSemana']
    search_fields = ['escala', 'horarioInicial', 'horarioFinal', 'diasPorSemana']


@admin.register(Salario)
class SalarioAdmin(admin.ModelAdmin):
    list_display = ['base', 'adicional_tipo', 'adicional_valor', 'desconto_VT', 'desconto_VR', 'desconto_VA',
                    'adiantamento', 'liquido', 'comissao', 'bonus']


@admin.register(Dia_de_Pagamento)
class DiaDePagamentoAdmin(admin.ModelAdmin):
    list_display = ['profissional', 'adiantamento', 'comissao', 'bonus']









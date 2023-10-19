from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.abre_index, name='abre_index'),
    path('cad_cliente', views.cad_cliente, name='cad_cliente'),
    path('salvar_cliente_novo', views.salvar_cliente, name='salvar_cliente_novo'),
    path('cons_cliente', views.cons_cliente, name='cons_cliente'),
    path('edit_cliente/<int:id>', views.edit_cliente, name='edit_cliente'),
    path('salvar_cliente_editado', views.salvar_cliente_editado, name='salvar_cliente_editado'),
    path('excluir_cliente/<int:id>', views.delete_cliente, name='delete_cliente'),

    # Atendente
    path('cad_atend', views.cad_atend, name='cad_atend'),
    path('salvar_atend_novo', views.salvar_atend_novo, name='salvar_atend_novo'),
    path('salvar_atend_editado', views.salvar_atend_editado, name='salvar_atend_editado'),
    path('cons_atend', views.cons_atendente, name='cons_atend'),
    path('edit_atend/<int:id>', views.edit_atend, name='edit_atend'),

    # departamento
    path('cad_depto', views.cad_depto, name='cad_depto'),
    path('salvar_depto', views.salvar_depto, name='salvar_depto'),
    path('salvar_edit_depto', views.salvar_edit_depto, name='salvar_edit_depto'),
    path('cons_depto', views.cons_depto, name='cons_depto'),
    path('edit_depto/<int:id>', views.edit_depto, name='edit_depto'),

    # situacao
    path('cad_situacao', views.cad_situacao, name='cad_situacao'),
    path('salvar_situacao_novo', views.salvar_situacao_novo, name='salvar_situacao_novo'),
    path('cons_situacao', views.cons_situacao, name='cons_situacao'),
    path('edit_situacao/<int:id>', views.edit_situacao, name='edit_situacao'),
    path('salvar_situacao_editado', views.salvar_situacao_editado, name='salvar_situacao_editado'),

    # atendimento
    path('reg_atendimento', views.reg_atendimento, name='reg_atendimento'),
    path('reg_atendimento_api', views.reg_atendimento_api, name='reg_atendimento_api'),
    path('salvar_atendimento_novo', views.salvar_atendimento_novo, name='salvar_atendimento_novo'),
    path('reg_atend_busca_cliente', views.reg_atend_busca_cliente, name='reg_atend_busca_cliente'),
    path('sel_cliente/<int:id>', views.sel_cliente, name='sel_cliente'),

    #CONSULTA ATENDIMENTO

    path('cons_lista_atendimento', views.cons_lista_atendimento, name='cons_lista_atendimento'),
    path('cons_atendimento/<int:id>', views.cons_atendimento, name='cons_atendimento'),


]

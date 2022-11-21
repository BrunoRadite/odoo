# -*- coding: utf-8 -*-
import odoo.fields as fields
import odoo.models as models


class Aluno(models.Model):
    _name = 'admin.odoo'
    _description = 'admin model'
    # campos do modelo
    nome = fields.Char(string='Nome do admin', required=True)
    matricula = fields.Integer(string='Matricula do admin')
    sexo = fields.Selection(
        [('outros', 'Outros'),
         ('homi', 'Homi'),
         ('muie', 'Muie'),
         ], required=True, default='homi'
    )
    ativo = fields.Boolean(string='admin ativo')

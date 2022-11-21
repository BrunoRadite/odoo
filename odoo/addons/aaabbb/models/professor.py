# -*- coding: utf-8 -*-
import odoo.fields as fields
import odoo.models as models


class Professor(models.Model):
    _name = 'professor.odoo'
    _description = 'professor model'
    # campos do modelo
    nome = fields.Char(string='Nome do Professor', required=True)
    # quem_criou = fields.Char(string='Nome de quem criou',
    #                          default=lambda self: self.env.user.name)
    matricula = fields.Integer(string='Matricula do Professor')
    sexo = fields.Selection(
        [('outros', 'Outros'),
         ('homi', 'Homi'),
         ('muie', 'Muie'),
         ], required=True, default='homi'
    )
    ativo = fields.Boolean(string='Professor ativo')

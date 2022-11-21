# -*- coding: utf-8 -*-

import odoo.fields as fields
import odoo.models as models


class Aluno(models.Model):
    _name = 'aluno.odoo'
    _description = 'aluno model'
    # campos do modelo
    nome = fields.Char(string='Nome do aluno', required=True)
    foto = fields.Image(string='Foto do Aluno')
    matricula = fields.Integer(string='Matricula do aluno')
    quem_criou = fields.Char(string='Nome de quem criou',
                             default=lambda self: self.env.user.name, readonly=True)
    sexo = fields.Selection(
        [('outros', 'Outros'),
         ('homi', 'Homi'),
         ('muie', 'Muie'),
         ], required=True, default='homi'
    )
    ativo = fields.Boolean(string='Aluno ativo')

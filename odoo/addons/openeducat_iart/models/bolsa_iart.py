# -*- coding: utf-8 -*-
###############################################################################
#
#    OpenEduCat Inc
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

import odoo.models as models
import odoo.fields as fields


class OpStudentIartBolsa(models.Model):
    _name = "op.student.iart.bolsa"
    _description = 'Bolsas relacionadas'

    nome = fields.Char(string='Nome da Bolsa', required=True)
    valor = fields.Integer(
        default=400, string='Valor da bolsa em reais', required=True)
    bolsistas = fields.Many2many('op.student.iart', string='bolsas')

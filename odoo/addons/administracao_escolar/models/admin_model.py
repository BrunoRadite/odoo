import odoo.fields as fields
import odoo.models as models


class AdminModel(models.Model):
    _name = 'admin_model.odoo'
    _description = 'admin model'
    # campos do modelo
    nome = fields.Char(string='Nome do aluno', required=True)
    foto = fields.Binary(string='Foto do Aluno')
    matricula = fields.Integer(string='Matricula do aluno')
    quem_criou = fields.Char(string='Nome de quem criou',
                             default=lambda self: self.env.user.name, readonly=True)
    sexo = fields.Selection(
        [('outros', 'Outros'),
         ('homem', 'Homem'),
         ('mulher', 'Mulher'),
         ], required=True, default='homem'
    )
    ativo = fields.Boolean(string='Aluno ativo')

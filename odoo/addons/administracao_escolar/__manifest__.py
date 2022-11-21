# -*- coding: utf-8 -*-
{
    # nome do módulo
    'name': 'Adminstração escolar',
    # a versão do módulo
    'version': '0.1',
    # breve resumo
    'summary': 'Administração escolar',
    'sequence': 10,
    'description': """
    Invoicing & Payments
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not
an accountant. It provides an easy way to follow up on your vendors and customers.
 
You could use this simplified accounting in case you work with an (external) account to keep your books, and you still
want to keep track of payments. This module also offers you an easy method of registering payments, without having to
encode complete abstracts of account.
    """,
    # aqui você só poderá colocar categorias existentes, basta procurar por categorias pelo odoo e ver qual se encaixa melhor
    'category': 'Accounting/Accounting',
    # pode colocar seu website que quando alguém clicar em saiba mais irá direto para o seu.
    'website': 'https://www.odoo.com/app/invoicing',
    # aqui ficará as ima
    'images': [],
    'depends': [],
    'data': [
        'views/aluno_view.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    # 'post_init_hook': '_account_post_init',
    'assets': {
    },
    'license': 'LGPL-3',
}

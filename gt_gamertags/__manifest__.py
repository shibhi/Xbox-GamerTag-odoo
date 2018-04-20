# -*- coding: utf-8 -*-
# © 2018 Xbox Gamertag checker - Check Xbox Gamertag Availability
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Xbox Gamertag checker - Check Xbox Gamertag Availability',
    'summary': """This gamertag checker can instantly find the Xbox gamertag availability that you been looking for. Find the right Xbox gamertag.""",
    'description': """This gamertag checker can instantly find the Xbox gamertag availability that you been looking for. Find the right Xbox gamertag.""",
    'version': '11.1',
    'category': 'Odoo Games',
    'author': 'gamertags.info',
    'license': 'AGPL-3',
    'website': 'http://www.gamertags.info',
  
    ],
    'depends': [
        'br_account_payment', 'br_data_account_product'
    ],
    'external_dependencies': {
        'python': [
            'pyboleto',
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings.xml',
        'views/account_invoice.xml',
        'views/account_move_line.xml',
        'views/res_partner_bank.xml',
        'views/payment_order.xml',
        'views/payment_mode.xml',
        'views/account_journal.xml',
        'reports/report_print_button_view.xml',
        'sequence/payment_order_sequence.xml',
        'sequence/numero_documento_sequence.xml',
        'wizard/br_boleto_wizard.xml',
        'wizard/send_boleto_email.xml',
    ],
    'installable': True,
    'application': True,
}

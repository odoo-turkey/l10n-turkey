# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': 'Accounting chart for Turkey',
    'version': '12.0.1',
    'summary': "Chart of accounts for Turkey",
    'description': """Türkiye için tek düzen hesap planı ve vergi tanımları""",
    'category': 'Localization/Turkey',
    'website':'https://github.com/aaltinisik/l10n-turkey',
    'author': 'Ahmet Altınışık',
    "depends": ["account"],
    'data': [
        'data/chart_data.xml',
        'data/chart_template_data.xml',
        'data/account.group.csv',
        'data/account_tag.xml',
        'data/account.account.template.csv',
        'data/chart_template.xml',
        'data/fiscal_position_template_data.xml',
    ],
    'installable': True,
    'auto_install': False
}

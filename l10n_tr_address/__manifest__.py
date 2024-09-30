{
    "name": "Turkey Addresses",
    "version": "13.0.0.1.0",
    "summary": "Add custom field in Customer like District, Region, Neighbourhood",
    "description": """This Module is used to add custom field in res.partner Object""",
    "category": "Partner",
    "website": "https://github.com/odoo-turkey",
    "author": "Ahmet Yigit Budak",
    "external_dependencies": {"python": ["openpyxl"]},
    "depends": ["sale", "base", "contacts"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_view.xml",
        "views/address_details_view.xml",
        "wizard/wizard_import_script_views.xml",
    ],
    "installable": True,
    "auto_install": False,
}

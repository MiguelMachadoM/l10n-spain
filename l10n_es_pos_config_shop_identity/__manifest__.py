# Copyright 2026 Miguel Machado
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).
{
    "name": "POS shop identity (Spanish simplified invoice)",
    "summary": "Print simplified invoice title and number on one receipt line",
    "version": "18.0.1.0.0",
    "category": "Sales/Point Of Sale",
    "author": "Miguel Machado, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-spain",
    "license": "AGPL-3",
    "maintainers": ["MiguelMachadoM"],
    "development_status": "Beta",
    "depends": ["pos_config_shop_identity", "l10n_es_pos_oca"],
    "assets": {
        "point_of_sale._assets_pos": [
            "l10n_es_pos_config_shop_identity/static/src/xml/**/*.xml",
            "l10n_es_pos_config_shop_identity/static/src/scss/**/*.scss",
        ],
    },
    "installable": True,
    "auto_install": True,
}

# Copyright 2022 Camptocamp SA
# @author: Simone Orsi <simahawk@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields


class OrderMixin:
    @classmethod
    def _create_sale_order(cls, **kw):
        """Create a sale order

        :return: sale order
        """
        model = cls.env["sale.order"]
        vals = dict(commitment_date=fields.Date.today())
        vals.update(kw)
        # Loose dependency on onchange_helper
        if hasattr(model, "play_onchanges"):
            so_vals = model.play_onchanges(vals, [])
        else:
            so_vals = vals.copy()
        if "order_line" in so_vals:
            so_vals["order_line"] = [(0, 0, x) for x in vals["order_line"]]
        return model.create(so_vals)

    @classmethod
    def _create_product(cls, **kw):
        """Create a product"""
        product_model = cls.env["product.product"]
        vals = {
            "name": "Test product",
            "standard_price": 500.0,
            "weight": 0.01,
        }
        vals.update(kw)
        return product_model.create(vals)

    @classmethod
    def _setup_order(cls, **kw):
        cls.product_a = cls._create_product(default_code="FURN_0096", barcode="1" * 14)
        cls.product_b = cls._create_product(default_code="FURN_0097", barcode="2" * 14)
        cls.product_c = cls._create_product(default_code="FURN_0098", barcode="3" * 14)
        cls.product_d = cls._create_product(
            default_code="E-COM06", barcode="4" * 14, type="consu"
        )
        line_defaults = kw.pop("line_defaults", {})
        vals = {
            "partner_id": cls.env["res.partner"]
            .create({"name": "The Jackson Group"})
            .id,
            "commitment_date": "2022-07-29",
        }
        vals.update(kw)
        if "client_order_ref" not in vals:
            vals["client_order_ref"] = "ABC123"
        vals["order_line"] = [
            {"product_id": cls.product_a.id, "product_uom_qty": 300, "edi_id": 1000},
            {"product_id": cls.product_b.id, "product_uom_qty": 200, "edi_id": 2000},
            {"product_id": cls.product_c.id, "product_uom_qty": 100, "edi_id": 3000},
        ]
        if line_defaults:
            for line in vals["order_line"]:
                line.update(line_defaults)
        sale = cls._create_sale_order(**vals)
        sale.action_confirm()
        return sale

# Copyright 2022 Camptocamp SA
# @author Simone Orsi <simahawk@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import base64

from requests import PreparedRequest, Session

from odoo.tests.common import _super_send

from odoo.addons.edi_oca.tests.common import EDIBackendCommonComponentTestCase


class TestEDIWebserviceBase(EDIBackendCommonComponentTestCase):
    @classmethod
    def _get_backend(cls):
        return cls.env.ref("edi_webservice_oca.demo_edi_backend")

    @classmethod
    def _setup_records(cls):
        result = super()._setup_records()
        cls.filedata = base64.b64encode(b"This is a simple file")
        vals = {
            "model": cls.partner._name,
            "res_id": cls.partner.id,
            "exchange_file": cls.filedata,
        }
        cls.record = cls.backend.create_record("test_csv_output", vals)
        return result

    @classmethod
    def _request_handler(cls, s: Session, r: PreparedRequest, /, **kw):
        if r.url.startswith("http://localhost.demo.odoo") or r.url.startswith(
            "https://foo.test"
        ):
            return _super_send(s, r, **kw)
        return super()._request_handler(s, r, **kw)

"""Tests for views.py."""

import pytest

import ckanext.copo_schema.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "copo_schema")
@pytest.mark.usefixtures("with_plugins")
def test_copo_schema_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("copo_schema.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, copo_schema!"

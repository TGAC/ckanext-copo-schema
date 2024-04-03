"""Tests for helpers.py."""

import ckanext.copo_schema.helpers as helpers


def test_copo_schema_hello():
    assert helpers.copo_schema_hello() == "Hello, copo_schema!"

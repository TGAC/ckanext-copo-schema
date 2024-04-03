"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.copo_schema.logic import validators


def test_copo_schema_reauired_with_valid_value():
    assert validators.copo_schema_required("value") == "value"


def test_copo_schema_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.copo_schema_required(None)

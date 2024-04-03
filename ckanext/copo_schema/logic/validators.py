import ckan.plugins.toolkit as tk


def copo_schema_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "copo_schema_required": copo_schema_required,
    }

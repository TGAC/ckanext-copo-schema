from flask import Blueprint


copo_schema = Blueprint(
    "copo_schema", __name__)


def page():
    return "Hello, copo_schema!"


copo_schema.add_url_rule(
    "/copo_schema/page", view_func=page)


def get_blueprints():
    return [copo_schema]

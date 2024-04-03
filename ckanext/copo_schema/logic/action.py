import ckan.plugins.toolkit as tk
import ckanext.copo_schema.logic.schema as schema


@tk.side_effect_free
def copo_schema_get_sum(context, data_dict):
    tk.check_access(
        "copo_schema_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.copo_schema_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'copo_schema_get_sum': copo_schema_get_sum,
    }

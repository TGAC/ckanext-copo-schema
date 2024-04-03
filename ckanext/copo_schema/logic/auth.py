import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def copo_schema_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "copo_schema_get_sum": copo_schema_get_sum,
    }

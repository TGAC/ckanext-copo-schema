
from ckan.common import config

def get_all_dataset_type():
    datasets_str = config.get('copo_schema.all_dataset_types',"")
    if datasets_str:
        return datasets_str.split(",")
    else:
        return []

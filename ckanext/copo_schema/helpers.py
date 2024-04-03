
from ckan.common import config

def get_all_dataset_type():
    datasets_str = config.get('ckan.all.dataset_type',"")
    if datasets_str:
        return datasets_str.split(",")
    else:
        return []

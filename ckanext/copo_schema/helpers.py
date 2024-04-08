
from ckan.common import config

def get_all_dataset_type():
    datasets_str = config.get('copo_schema.all_dataset_types',"")
    datasets = []
    if datasets_str:
        return [ dataset.strip() for dataset in datasets_str.split(",") if dataset.strip() ]
        
    else:
        return []

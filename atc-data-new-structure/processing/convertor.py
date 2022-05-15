from pathlib import Path
import glob2
import glob
import json
import yaml
from jinja2 import Environment, FileSystemLoader


def read_yaml_file(path):
  with open(path) as f:
      yaml_fields = yaml.load_all(f.read(), Loader=yaml.FullLoader)
  buff_results = [x for x in yaml_fields]
  if len(buff_results) > 1:
      result = buff_results[0]
      result['additions'] = buff_results[1:]
  else:
      result = buff_results[0]
  return result


def get_source_target_fields_names_mapping(dn_object):
    _dict = {}
    for field in dn_object.get('fields'):
        if field['processing']['required_field'] is True:
            _dict.update(
               {field['original_name']: field['processing']['target_name']})
    return _dict


def get_target_fields_types_mapping(dn_object):
    _dict = {}
    for field in dn_object.get('fields'):
        if field['processing']['required_field'] is True:
            _dict.update(
               {field['processing']['target_name']: field['processing']['target_type']})
    return _dict


def get_rename_processor_fields(dn_object):
    _dict = {}
    for field in dn_object.get('fields'):
        if field['processing'].get('processor') == "rename":
            _dict.update(
               {field['original_name']: field['processing']['target_name']})
    return _dict


def get_remove_processor_fields(dn_object):
    _list = []
    for field in dn_object.get('fields'):
        if field['processing'].get('processor') == "remove":
            _list.append(field['original_name'])
    return _list


def write_file(path, content, options="w+"):
    """Simple method for writing content to some file"""

    with open(path, options) as file:
        file.write(content)

    return True

#
#
# VARS
#
#

santa_data_dir = 'data/macos/**/*.yml'
santa_templates_dir = 'pipeline_templates/es-ingest-pipelines/macos'
santa_pipeline_template = 'santa.pipeline.yml.j2'
santa_pipeline_filename = 'generated/es-ingest-pipelines/macos/santa.pipeline.yml'
santa_mappings_filename = 'generated/es-index-mappings/macos/santa.mappings.json'

env = Environment(loader=FileSystemLoader(santa_templates_dir))
template = env.get_template(santa_pipeline_template)
dn_list = glob2.glob(santa_data_dir)

#
#
# GENERATE ES PIPELINE
#
#

main_rendering_obj = {}
fields_mapping_dict = {}
rename_fields_dict = {}
remove_fields_list = []


for dn_file in dn_list:
    yaml_file = read_yaml_file(dn_file)
    
    fields_mapping_dict.update(
      get_source_target_fields_names_mapping(yaml_file))

    rename_fields_dict.update(
        get_rename_processor_fields(yaml_file))
    
    for i in get_remove_processor_fields(yaml_file):
        remove_fields_list.append(i)


remove_fields_list = list(set(remove_fields_list))
main_rendering_obj.update(fields_mapping_dict)
main_rendering_obj.update({"remove_fields": remove_fields_list})

rename_fields = []
for field, target_field in rename_fields_dict.items():
    rename_fields.append((field, target_field))

main_rendering_obj.update({"rename_fields": rename_fields})

content = template.render(main_rendering_obj)
write_file(santa_pipeline_filename, content)

#
#
# GENERATE ES INDEX MAPPINGS
#
#

target_fields_types_mapping_dict = {}
target_fields_types_mapping_list = []

mapping_properties = { "properties": {} }


for dn_file in dn_list:
    yaml_file = read_yaml_file(dn_file)
    target_fields_types_mapping_dict.update(get_target_fields_types_mapping(yaml_file))


for field_name, field_type in target_fields_types_mapping_dict.items():
    mapping_properties["properties"].update({field_name: { "type": field_type}})

write_file(santa_mappings_filename, json.dumps(mapping_properties))


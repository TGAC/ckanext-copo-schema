import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

# import ckanext.copo_schema.cli as cli
import ckanext.copo_schema.helpers as helpers
# import ckanext.copo_schema.views as views
# from ckanext.copo_schema.logic import (
#     action, auth, validators
# )


"""
<nav class="navbar">
	<ul>
		<li><a href="#">Home</a></li>
		<li>
			<a href="#">Dropdown</a>
			<ul>
				<li><a href="#">Option 1</a></li>
				<li><a href="#">Option 2</a></li>
				<li><a href="#">Option 3</a></li>
			</ul>
		</li>
		<li><a href="#">Contact</a></li>
	</ul>
</nav>

"""


class COPOSchemaPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    
    # plugins.implements(plugins.IAuthFunctions)
    # plugins.implements(plugins.IActions)
    # plugins.implements(plugins.IBlueprint)
    # plugins.implements(plugins.IClick)
    plugins.implements(plugins.ITemplateHelpers)
    # plugins.implements(plugins.IValidators)
    

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "copo_schema")

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    # IAuthFunctions

    # def get_auth_functions(self):
    #     return auth.get_auth_functions()

    # IActions

    # def get_actions(self):
    #     return action.get_actions()

    # IBlueprint

    # def get_blueprint(self):
    #     return views.get_blueprints()

    # IClick

    # def get_commands(self):
    #     return cli.get_commands()

    # ITemplateHelpers

    def get_helpers(self):
        return {
            'get_all_dataset_types': helpers.get_all_dataset_type,
            #'get_all_organizations': get_all_organizations,
            #'get_all_groups' : get_all_groups
        }

    # IValidators

    # def get_validators(self):
    #     return validators.get_validators()
    

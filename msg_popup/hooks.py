app_name = "msg_popup"
app_title = "msg popup"
app_publisher = "nilesh"
app_description = "msg popup"
app_email = "teast@test.com"
app_license = "mit"


include_app_in_docs = True
# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "msg_popup",
# 		"logo": "/assets/msg_popup/logo.png",
# 		"title": "msg popup",
# 		"route": "/msg_popup",
# 		"has_permission": "msg_popup.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/msg_popup/css/msg_popup.css"
# app_include_js = "/assets/msg_popup/js/msg_popup.js"

# include js, css files in header of web template
# web_include_css = "/assets/msg_popup/css/msg_popup.css"
# web_include_js = "/assets/msg_popup/js/msg_popup.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "msg_popup/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "msg_popup/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "msg_popup.utils.jinja_methods",
# 	"filters": "msg_popup.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "msg_popup.install.before_install"
# after_install = "msg_popup.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "msg_popup.uninstall.before_uninstall"
# after_uninstall = "msg_popup.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "msg_popup.utils.before_app_install"
# after_app_install = "msg_popup.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "msg_popup.utils.before_app_uninstall"
# after_app_uninstall = "msg_popup.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "msg_popup.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"msg_popup.tasks.all"
# 	],
# 	"daily": [
# 		"msg_popup.tasks.daily"
# 	],
# 	"hourly": [
# 		"msg_popup.tasks.hourly"
# 	],
# 	"weekly": [
# 		"msg_popup.tasks.weekly"
# 	],
# 	"monthly": [
# 		"msg_popup.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "msg_popup.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "msg_popup.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "msg_popup.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["msg_popup.utils.before_request"]
# after_request = ["msg_popup.utils.after_request"]

# Job Events
# ----------
# before_job = ["msg_popup.utils.before_job"]
# after_job = ["msg_popup.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"msg_popup.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


# Copyright (c) 2024, Sintayehu Shibeshi and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class MarketplaceItem(Document):
	def validate(self):
		# If price is set, ensure currency is also set.
		# Frappe typically handles this if "Currency" field is linked to "price" field's currency option.
		# However, an explicit validation can be added if needed.
		if self.price and not self.currency:
			company_currency = frappe.get_cached_value('Global Defaults', None, 'default_currency')
			if not company_currency:
				frappe.throw("Default currency is not set in Global Defaults. Please set it to save items with prices.")
			self.currency = company_currency
	pass

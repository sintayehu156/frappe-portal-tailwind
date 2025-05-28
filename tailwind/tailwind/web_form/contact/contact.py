import frappe
from frappe import _

def get_context(context):
    # context.show_sidebar = True # Example: if you want a sidebar
    if hasattr(frappe.local, 'form_dict'):
        if hasattr(frappe.local.form_dict, 'success_message'):
            context.success_message = frappe.local.form_dict.success_message
        if hasattr(frappe.local.form_dict, 'error_message'):
            context.error_message = frappe.local.form_dict.error_message
    return context

@frappe.whitelist(allow_guest=True)
def accept(full_name, email, message, phone=None):
    # Create a new Contact Request document
    contact_request = frappe.new_doc("Contact Request")
    contact_request.full_name = full_name
    contact_request.email = email
    contact_request.message = message
    contact_request.phone = phone
    
    try:
        contact_request.insert(ignore_permissions=True) # Allow guest to create
        frappe.db.commit() # Commit the transaction
        frappe.local.form_dict.success_message = _("Your message has been sent successfully!")
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Contact Form Submission Error")
        frappe.local.form_dict.error_message = _("There was an error sending your message. Please try again later.")
        # Optionally, set context.error_message to display in the template
    
    # To redirect back to the form page (or any other page)
    # frappe.local.response["type"] = "redirect"
    # frappe.local.response["location"] = "/contact" 
    # For now, it will re-render the form page with a success/error message via get_context
    return # Important to return to allow get_context to pick up success_message/error_message

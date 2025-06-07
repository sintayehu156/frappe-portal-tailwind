import frappe

def get_context(context):
    context.items = frappe.get_all(
        "Marketplace Item",
        fields=["item_name", "item_description", "item_image", "price", "currency", "developer_name", "developer_link"],
        filters={"published": 1},
        order_by="sort_order asc, item_name asc"
    )
    # For website manager, show unpublished items too or a message
    if frappe.utils.is_website_manager(): # Corrected to use frappe.utils.is_website_manager()
        context.is_website_manager = True # To allow template to show messages if needed
    
    # Add a default title if not set by the Web Page document itself
    context.title = context.title or "Marketplace"
    return context

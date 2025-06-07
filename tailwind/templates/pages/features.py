import frappe

def get_context(context):
    context.features = frappe.get_all(
        "Feature Item",
        fields=["title", "description", "icon_class", "link_url", "link_text"],
        filters={"published": 1},
        order_by="sort_order ASC, title ASC" # Added sort_order
    )
    # Add a default title if not set by the Web Page document itself
    context.title = context.title or "Features"
    return context

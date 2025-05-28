import frappe

def create_marketplace_web_page():
    # Check if the Web Page already exists
    if frappe.db.exists("Web Page", {"route": "marketplace"}):
        print("Web Page 'marketplace' already exists. Deleting and recreating for potential updates.")
        # To ensure the template_path and controller are correctly set if they were missed before
        frappe.delete_doc("Web Page", "marketplace", ignore_permissions=True, force=True, delete_permanently=True)
        # Note: delete_permanently=True is for clean slate; in production, you might update.

    print("Creating 'Marketplace' Web Page...")
    web_page = frappe.new_doc("Web Page")
    web_page.title = "Marketplace"
    web_page.route = "marketplace"  # This will be the URL, e.g., /marketplace
    web_page.published = 1
    
    # Set the template path for this web page.
    # Frappe will look for this path within any app's 'templates' directory.
    # The controller (marketplace.py) will be automatically picked up if it's in the same directory 
    # as the template and has the same name (marketplace.html -> marketplace.py).
    web_page.template_path = "templates/pages/marketplace.html" 
    
    # The main_section can be left empty if the template handles all content rendering.
    # web_page.main_section = "<p>Discover amazing tools and apps in our marketplace!</p>" 
    
    try:
        web_page.insert(ignore_permissions=True)
        frappe.db.commit()
        print(f"Web Page '{web_page.title}' with route '{web_page.route}' created successfully.")
        print(f"It will use template: {web_page.template_path}")
        print("The context for this page will be provided by tailwind/templates/pages/marketplace.py:get_context")
    except Exception as e:
        print(f"Error creating Web Page '{web_page.title}': {e}")
        frappe.db.rollback()

if __name__ == "__main__":
    # This part is for direct execution testing and requires a Frappe context.
    # It's not typically run this way in production.
    # Example:
    # frappe.connect(site="your_site_name")
    # create_marketplace_web_page()
    # frappe.db.commit() 
    # frappe.destroy()
    pass

import frappe

def create_features_web_page():
    # Check if the Web Page already exists
    if frappe.db.exists("Web Page", {"route": "features"}):
        print("Web Page 'features' already exists. Deleting and recreating for potential updates.")
        # To ensure the template_path is correctly set if it was missed before
        frappe.delete_doc("Web Page", "features", ignore_permissions=True, force=True, delete_permanently=True)
        # Note: delete_permanently=True is for clean slate; in production, you might update.
        
    print("Creating 'Features' Web Page...")
    web_page = frappe.new_doc("Web Page")
    web_page.title = "Features"
    web_page.route = "features"  # This will be the URL, e.g., /features
    web_page.published = 1
    
    # Set the template path for this web page
    # The get_context function in tailwind/templates/pages/features.py will be automatically called
    web_page.template_path = "templates/pages/features.html" # Path relative to app's templates directory
    
    # If the template handles all content, main_section can be empty or minimal.
    # web_page.main_section = "" 
    
    try:
        web_page.insert(ignore_permissions=True)
        frappe.db.commit()
        print(f"Web Page '{web_page.title}' with route '{web_page.route}' created successfully.")
        print(f"It will use template: {web_page.template_path}")
        print("The context for this page will be provided by tailwind/templates/pages/features.py:get_context")
    except Exception as e:
        print(f"Error creating Web Page '{web_page.title}': {e}")
        frappe.db.rollback()

if __name__ == "__main__":
    # This part is for direct execution testing and requires a Frappe context.
    # It's not typically run this way in production.
    # Example:
    # frappe.connect(site="your_site_name")
    # create_features_web_page()
    # frappe.db.commit() 
    # frappe.destroy()
    pass

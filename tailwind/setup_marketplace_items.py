import frappe

def create_sample_marketplace_items():
    items_data = [
        {
            "item_name": "Awesome App Vol 1",
            "item_description": "A truly revolutionary app that will change your workflow. Experience seamless integration and unparalleled efficiency.",
            "price": 29.99,
            "developer_name": "Devs Inc.",
            "developer_link": "https://example.com/devsinc",
            "published": 1,
            "sort_order": 1
        },
        {
            "item_name": "Productivity Suite",
            "item_description": "All the tools you need to be more productive. Includes task management, calendar, and note-taking features.",
            "price": 99.00,
            "developer_name": "Solution Masters",
            "developer_link": "https://example.com/solutionmasters",
            "published": 1,
            "sort_order": 2
        },
        {
            "item_name": "Creative Toolkit",
            "item_description": "Unleash your creativity with this amazing toolkit. Perfect for designers, artists, and content creators.",
            "price": 49.50,
            "developer_name": "Artisan Digital",
            "developer_link": "https://example.com/artisandigital",
            "published": 1,
            "sort_order": 3
        },
        {
            "item_name": "Data Analytics Pro",
            "item_description": "Powerful data analytics and visualization tool to help you make informed business decisions.",
            "price": 149.00,
            "developer_name": "Insightful Co.",
            "published": 0, # Unpublished example
            "sort_order": 4
        }
    ]

    default_currency = frappe.get_cached_value('Global Defaults', None, 'default_currency')
    if not default_currency:
        # Fallback if not set, though in a real setup this should be configured
        print("Warning: Default currency not set in Global Defaults. Using 'USD' as a fallback for sample data.")
        default_currency = "USD"


    for item_details in items_data:
        if not frappe.db.exists("Marketplace Item", {"item_name": item_details["item_name"]}):
            try:
                item = frappe.new_doc("Marketplace Item")
                item.item_name = item_details["item_name"]
                item.item_description = item_details["item_description"]
                item.price = item_details.get("price")
                item.currency = default_currency if item.price else None # Set currency only if price exists
                item.developer_name = item_details.get("developer_name")
                item.developer_link = item_details.get("developer_link")
                item.published = item_details["published"]
                item.sort_order = item_details["sort_order"]
                # item.item_image = item_details.get("item_image") # Add if you have sample images
                item.insert(ignore_permissions=True)
                print(f"Created Marketplace Item: {item_details['item_name']}")
            except Exception as e:
                print(f"Error creating Marketplace Item '{item_details['item_name']}': {e}")
        else:
            print(f"Marketplace Item '{item_details['item_name']}' already exists. Skipping.")
    
    frappe.db.commit()
    print("Sample marketplace items setup complete.")

if __name__ == "__main__":
    # For direct execution testing (requires Frappe context)
    # Example:
    # frappe.connect(site="your_site_name")
    # create_sample_marketplace_items()
    # frappe.destroy()
    pass

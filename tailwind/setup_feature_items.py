import frappe

def create_sample_features():
    features_data = [
        {
            "title": "Award Winning Services",
            "description": "Our services have been recognized for excellence and innovation, delivering outstanding results for our clients.",
            "icon_class": "fas fa-award",
            "published": 1
        },
        {
            "title": "Free Revisions",
            "description": "We ensure your satisfaction. Our process includes free revisions to make sure the final product meets your expectations.",
            "icon_class": "fas fa-retweet",
            "published": 1
        },
        {
            "title": "Verified Company",
            "description": "We are a registered and verified company, committed to transparency and ethical business practices.",
            "icon_class": "fas fa-fingerprint", # Changed from fas fa-check-circle for variety
            "published": 1
        },
        {
            "title": "Carefully Crafted Components",
            "description": "Every component is designed with attention to detail, ensuring a seamless and intuitive user experience.",
            "icon_class": "fas fa-layer-group", # Changed from fas fa-fingerprint
            "published": 1
        },
        {
            "title": "Amazing Page Examples",
            "description": "Explore a variety of stunning page examples built with our platform, showcasing versatility and power.",
            "icon_class": "fab fa-html5",
            "published": 1
        },
        {
            "title": "Dynamic Components",
            "description": "Leverage dynamic components that adapt to your content and provide a rich, interactive experience for your users.",
            "icon_class": "far fa-paper-plane", # Changed to far for variety from fas
            "published": 1
        }
    ]

    for feature_details in features_data:
        if not frappe.db.exists("Feature Item", {"title": feature_details["title"]}):
            try:
                feature = frappe.new_doc("Feature Item")
                feature.title = feature_details["title"]
                feature.description = feature_details["description"]
                feature.icon_class = feature_details["icon_class"]
                feature.published = feature_details["published"]
                # Optional: Add link_url and link_text if needed for samples
                # feature.link_url = feature_details.get("link_url")
                # feature.link_text = feature_details.get("link_text")
                feature.insert(ignore_permissions=True)
                print(f"Created Feature Item: {feature_details['title']}")
            except Exception as e:
                print(f"Error creating Feature Item '{feature_details['title']}': {e}")
        else:
            print(f"Feature Item '{feature_details['title']}' already exists. Skipping.")
    
    frappe.db.commit()
    print("Sample feature items setup complete.")

if __name__ == "__main__":
    # This allows running the script directly if needed,
    # but typically it would be called via bench execute
    # For direct execution, you'd need a Frappe context.
    # e.g. frappe.connect(site="your_site_name")
    # create_sample_features()
    # frappe.destroy()
    pass

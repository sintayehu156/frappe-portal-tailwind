import frappe

def create_web_page():
    # Check if the Web Page already exists
    if frappe.db.exists("Web Page", {"route": "about"}):
        print("Web Page 'about' already exists. Skipping creation.")
        # Optionally, update existing page content here
        # page = frappe.get_doc("Web Page", {"route": "about"})
        # page.main_section = """... (new content) ..."""
        # page.save(ignore_permissions=True)
        # print("Web Page 'about' updated.")
        return

    content_html = """
<!-- Hero Section -->
<section class="bg-gray-300 dark:bg-gray-900">
    <div class="grid max-w-screen-xl px-4 pt-20 pb-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12 lg:pt-28">
        <div class="mr-auto place-self-center lg:col-span-7">
            <h1 class="max-w-2xl mb-4 text-4xl font-extrabold leading-none tracking-tight md:text-5xl xl:text-6xl dark:text-white">Building digital <br>products & brands.</h1>
            <p class="max-w-2xl mb-6 font-light text-gray-500 lg:mb-8 md:text-lg lg:text-xl dark:text-gray-400">
                We are picking up businesses, understanding their end-to-end process and helping them in transformation - with the help of ready-to-use software (Open source/Licensed)..
            </p>
        </div>
        <div class="hidden lg:mt-0 lg:col-span-5 lg:flex">
            <img src="/assets/tailwind/images/erp.avif" alt="hero image">
        </div>
    </div>
</section>

<!-- Quote Section -->
<section class="bg-gray-100 dark:bg-gray-800">
    <div class="max-w-screen-xl px-4 py-8 mx-auto text-center lg:py-24 lg:px-6">
        <figure class="max-w-screen-md mx-auto">
            <!-- SVG Icon -->
            <svg class="h-12 mx-auto mb-3 text-gray-400 dark:text-purple-600" viewBox="0 0 24 27" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M14.017 18L14.017 10.609C14.017 4.905 17.748 1.039 23 0L23.995 2.151C21.563 3.068 20 5.789 20 8H24V18H14.017ZM0 18V10.609C0 4.905 3.748 1.038 9 0L9.996 2.151C7.563 3.068 6 5.789 6 8H9.983L9.983 18L0 18Z" fill="currentColor"/>
            </svg> 
            <blockquote>
                <p class="text-xl font-medium text-gray-900 md:text-2xl dark:text-white">"The most agile ERP on the planet"</p>
            </blockquote>
            <figcaption class="flex items-center justify-center mt-6 space-x-3">
                <img class="w-6 h-6 rounded-full" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/michael-gouch.png" alt="profile picture">
                <div class="flex items-center divide-x-2 divide-gray-500 dark:divide-gray-700">
                    <div class="pr-3 font-medium text-gray-900 dark:text-white">Rushbah</div>
                    <div class="pl-3 text-sm font-light text-purple-500 dark:text-gray-400">CEO at Frappe</div>
                </div>
            </figcaption>
        </figure>
    </div>
</section>

<!-- Team Section -->
<section class="pt-20 pb-48">
    <div class="container mx-auto px-4">
        <div class="flex flex-wrap justify-center text-center mb-24">
            <div class="w-full lg:w-6/12 px-4">
                <h2 class="text-3xl sm:text-4xl font-semibold">Here are our heroes</h2> {# Adjusted text size #}
                <p class="text-lg leading-relaxed m-4 text-gray-600">
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Veritatis cupiditate, officiis deserunt accusantium, saepe eveniet accusamus necessitatibus magnam quibusdam, a quod dolorum. Maxime numquam voluptates libero ea eos odit obcaecati.
                </p>
            </div>
        </div>
        <!-- Comment: Team member details would go here, potentially dynamically loaded in a future step -->
    </div>
</section>
"""

    web_page = frappe.new_doc("Web Page")
    web_page.title = "About Us"
    web_page.route = "about" 
    web_page.published = 1
    web_page.main_section = content_html
    # To use the standard page template that includes base.html (which should have header/footer)
    # web_page.template # Let Frappe use the default Web Page template or one specified in Website Theme
    
    try:
        web_page.insert(ignore_permissions=True)
        frappe.db.commit()
        print(f"Web Page '{web_page.title}' with route '{web_page.route}' created successfully.")
    except Exception as e:
        print(f"Error creating Web Page '{web_page.title}': {e}")
        frappe.db.rollback()

if __name__ == "__main__":
    create_web_page()

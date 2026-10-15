"""
 AI Prompt Kit for a Local Business
"""

Business_name = input("Enter your business name: ")
Business_type = input("Enter your business type: ")
City = input("Enter your city: ")
Main_customers = input("Enter your main customer demographic: ")
Monthly_budget = int(input("Enter your monthly budget: "))

print()
print(f"Business Name: {Business_name}")
print(f"Business Type: {Business_type}")
print(f"City: {City}")
print(f"Main Customers: {Main_customers}")
print(f"Monthly Budget: ${Monthly_budget}")

marketing = (
    f"Create a marketing strategy for {Business_name}, a {Business_type} located in {City}. "
    f"The main customers are {Main_customers}. The monthly budget for marketing is ${Monthly_budget}."
)

customer_service = (
    f"Create a customer service strategy for {Business_name}, a {Business_type} located in {City}. "
    f"The main customers are {Main_customers}. The monthly budget for customer service is ${Monthly_budget}."
)

growth = (
    f"Create a growth strategy for {Business_name}, a {Business_type} located in {City}. "
    f"The main customers are {Main_customers}. The monthly budget for growth is ${Monthly_budget}."
)

marketing_prompt = (
    f"Marketing Strategy Prompt: {marketing} "
    "Write a short Instagram post for Bicycle Store in Lahore. "
    "Target university students. Friendly tone, 1 call to action. "
    "Lahore is calling for a ride! 🚴‍♀️💨 Loving the fresh air and a good cycle to explore the city. "
    "It's the perfect way to de-stress and connect with your campus. "
    "Want to experience the Lahore vibe differently? ➡️ Tag a friend who needs a cycling adventure and explore together! "
    "#LahoreBikes #CyclingLahore #UniversityLife #ExploreLahore"
)

customer_service_prompt = (
    f"Customer Service Strategy Prompt: {customer_service} "
    "You are the manager of cycle store . Write a polite reply to a customer "
    "whose order arrived late. Apologise and offer a small discount."
    """Dear [Customer Name],

Thank you so much for your order! We’re so sorry to hear that it arrived later than expected. We understand this can be frustrating, and we sincerely apologize for the inconvenience.

We’re looking into why it took a little longer to arrive today. As a small gesture of our apology, we’d like to offer you a 10% discount on your next order with us.

We appreciate your understanding and hope you enjoy your bicycle!

Warmly,

[Abdullah Bin Ahmad]

[Bismillah Cycle Store]
"""
)

growth_prompt = (
    f"Growth Strategy Prompt: {growth} "
    "Suggest three practical ideas to increase local sales in the next 90 days."
    "Suggest 3 low-cost AI tools a Bicycle Store in Lahore can use "
    "to attract university students with a budget of 15000 PKR per month."

"""
Okay, here are 3 low-cost AI tools a bakery in Lahore could use to attract university students with a budget of 15,000 PKR per month, focusing on affordability and impact:

1.  **ChatGPT/Bard (for Content Creation & Social Media):**
    *   **Cost:** Approximately 2000 PKR/month (depending on usage & API access – consider free tiers initially)
    *   **Use:**  Generate engaging social media posts (Instagram stories, Facebook updates), captions for photos, draft blog posts about seasonal specials or baking tips, and even simple scripts for short videos.  Bard can be particularly helpful for brainstorming creative ideas.
    *   **Benefit:** Significantly reduces the time spent on content creation.  High-quality, consistent content is key to attracting students.

2.  **Designs.ai (for Simple Graphic Design & Branding):**
    *   **Cost:** Approximately 4000 PKR/month (depending on the level of features used)
    *   **Use:** Create basic Instagram stories templates (e.g., behind-the-scenes, product spotlights), simple logo variations (even a basic one), and maybe some eye-catching stickers for social media.
    *   **Benefit:**  Makes the branding more visually appealing, which is hugely important to students. It’s cost-effective and a quick way to improve the look of their online presence.

3.  **MarketMuse/Scalenut (for Keyword Research & SEO - Basic):**
    *   **Cost:** 5000 PKR/month (depending on features and usage)
    *   **Use:**  While these tools aren’t *completely* free, they offer a very cost-effective way to start identifying popular keywords students are searching for related to baked goods in Lahore. Use this information to inform content creation.  Set up a basic SEO strategy to increase organic reach.
    *   **Benefit:** Helps the bakery understand what students are *looking* for, making their offerings more relevant and increasing their visibility on student-focused platforms.

**Important Considerations for Lahore:**

*   **Instagram is Key:** Given the student demographic, Instagram will be *critical*.  Focus heavily on visual content – high-quality photos & videos of pastries, cakes, and the bakery itself.
*   **Student-Focused Promotions:** Run promotions specifically for students – student discounts, study-break deals, etc.
*   **Local Focus:** Tailor content to Lahore – mention local ingredients, traditions, or events.



To help me refine this further, could you tell me:

*   What kind of baked goods does the bakery specialize in? (e.g., pastries, cakes, cookies, etc.)
"""
)

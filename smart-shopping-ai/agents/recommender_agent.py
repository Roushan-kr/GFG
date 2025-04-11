from agents.customer_agent import get_customer_profile
from agents.product_agent import get_all_products

def recommend_products(user_id):
    profile = get_customer_profile(user_id)
    all_products = get_all_products()
    prefs = profile["preferences"]

    # Recommend products matching preferences
    recommendations = [p for p in all_products if p["category"] in prefs]
    return recommendations

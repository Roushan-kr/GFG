from django.shortcuts import render
from django.http import JsonResponse

# Import the recommendation logic from your custom agent
from agents.recommender_agent import recommend_products

# Basic home route to check if the server is working
def home(request):
    return JsonResponse({"message": "Smart Shopping AI is running!"})

# API endpoint to return product recommendations for a given user
def recommendations(request):
    user_id = request.GET.get('user_id', 'user123')  # Default user ID for testing
    results = recommend_products(user_id)            # Call agent to get recommendations
    return JsonResponse({
        "user_id": user_id,
        "recommendations": results
    })

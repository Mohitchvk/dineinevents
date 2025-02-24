import streamlit as st
from datetime import datetime
import openai

openai.api_key = "your-openai-api-key"  # Replace with your API key

events = {
    "Monday": {
        "title": "Spice Symphony: Indian Curry & Wine Pairing Night",
        "price": "$32 Per person",
        "hint": "Enter any curry of your choice (e.g., Butter Chicken, Paneer Tikka Masala), and we'll pair the perfect wine!",
        "category": "curry"
    },
    "Tuesday": {
        "title": "Royal Feast: Nawabi Biryani & Craft Beverage Night",
        "price": "$40 per person",
        "hint": "Enter any rice dish of your choice (e.g., Hyderabadi Biryani, Veg Pulao), and we'll pair the best beverage!",
        "category": "rice"
    },
    "Wednesday": {
        "title": "Spirits & Spices: Indian-Inspired Cocktails & Tapas",
        "price": "$50 per person",
        "hint": "Enter any tapas/snack of your choice (e.g., Samosa Chaat, Pani Puri), and we'll pair the best cocktail!",
        "category": "tapas"
    },
    "Thursday": {
        "title": "Bollywood Night: Chaat & Mocktail Fiesta",
        "price": "$35 per person",
        "hint": "Enter your favorite chaat dish (e.g., Dahi Puri, Pav Bhaji), and we'll suggest a perfect mocktail!",
        "category": "chaat"
    },
    "Friday": {
        "title": "Tandoor Tales: Live Grill & Whiskey Appreciation Night",
        "price": "$55 per person",
        "hint": "Enter any tandoor item (e.g., Tandoori Chicken, Malai Paneer Tikka), and we'll match it with a whiskey!",
        "category": "tandoor"
    },
    "Saturday": {
        "title": "The Maharaja Thali & Infused Elixirs",
        "price": "$60 per person",
        "hint": "Enter any dish you'd love in a thali (e.g., Dal Makhani, Goat Curry), and we'll find the best infused elixir!",
        "category": "thali"
    },
    "Sunday": {
        "title": "Sweet Endings: Indian Dessert & Chai Pairing",
        "price": "$30 per person",
        "hint": "Enter any dessert (e.g., Rasmalai, Gulab Jamun), and we'll pair it with a chai-based drink!",
        "category": "dessert"
    }
}

def get_suggestion(food_item, category):
    prompt = f"Suggest a perfect drink pairing for {food_item}, which is a {category} dish. Also, explain why the pairing works well."
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a food and beverage pairing expert."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def main():
    st.markdown("<div style='text-align: center;'><img src='https://passageindia.com/wp-content/uploads/passagetoindia2.png' width='150'></div>", unsafe_allow_html=True)
    
    today = datetime.today().strftime('%A')
    event = events.get(today, None)
    
    if event:
        st.header(f"{event['title']}")
        st.subheader(f"{event['price']}")
        st.write("### Select Your Dish:")
        
        st.write(f"_Hint: {event['hint']}_")
        user_input = st.text_input("Enter your dish or type 'Auto' for a full recommendation:")
        
        if st.button("Get Pairing Suggestion"):
            if user_input.strip():
                suggestion = get_suggestion(user_input, event['category'])
                st.write("### Suggested Pairing:")
                st.write(suggestion)
            else:
                st.write("Please enter a dish or type 'Auto'.")
    else:
        st.write("No special events today. Check back soon!")
        
if __name__ == "__main__":
    main()

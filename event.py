import streamlit as st
from datetime import datetime

events = {
    "Monday": {
        "title": "Spice Symphony: Indian Curry & Wine Pairing Night",
        "price": "$45 per person",
        "details": [
            "Curated 3-course meal with premium wine pairings",
            "Butter Chicken & Chardonnay",
            "Lamb Rogan Josh & Malbec",
            "Paneer Tikka Masala & Riesling",
            "Alternative drinks: Handcrafted mocktails, chai infusions"
        ]
    },
    "Tuesday": {
        "title": "Royal Feast: Nawabi Biryani & Craft Beverage Night",
        "price": "$40 per person",
        "details": [
            "Authentic Hyderabadi Dum Biryani with Salan & Raita",
            "Galouti Kebabs – Mughlai delicacy",
            "Tandoori Chicken Wings with house spice blend",
            "Beverages: Lassi Trio (Mango, Rose, Salted), Kala Khatta Spritz"
        ]
    },
    "Wednesday": {
        "title": "Spirits & Spices: Indian-Inspired Cocktails & Tapas",
        "price": "$50 per person",
        "details": [
            "Handcrafted Indian-inspired cocktails",
            "Mango Masala Mule – Vodka, mango purée, house spice mix",
            "Tandoori Tequila Twist – Smoked tequila with chili-lime salt",
            "Tapas Platter: Samosa Chaat, Gobi Manchurian, Pani Puri Shots",
            "Mocktails: Turmeric Honey Fizz, Masala Soda with Fresh Herbs"
        ]
    },
    "Thursday": {
        "title": "Bollywood Night: Chaat & Mocktail Fiesta",
        "price": "$35 per person",
        "details": [
            "Lively Bollywood ambiance with street food delights",
            "Pav Bhaji Sliders – Spiced veggie mix in buttered buns",
            "Dahi Puri Bombs – Crunchy, tangy, full of flavors",
            "Masala Fries with Tamarind Mayo",
            "Beverages: Jamun Mojito, Saffron-Pistachio Cold Brew"
        ]
    },
    "Friday": {
        "title": "Tandoor Tales: Live Grill & Whiskey Appreciation Night",
        "price": "$55 per person",
        "details": [
            "Live grilling of smoky tandoori delicacies",
            "Tandoori Lamb Chops – Grilled to perfection",
            "Malai Chicken Tikka – Creamy, mildly spiced",
            "Smoked Paneer Skewers",
            "Beverages: Premium whiskeys, Cardamom-infused Old Fashioned"
        ]
    },
    "Saturday": {
        "title": "The Maharaja Thali & Infused Elixirs",
        "price": "$60 per person",
        "details": [
            "Lavish 7-course thali experience",
            "Dal Makhani, Shahi Paneer, Goat Curry",
            "Garlic Naan, Saffron Rice, Raita",
            "Desserts: Gulab Jamun & Paan Ice Cream",
            "Beverages: Saffron-Ginger Spritz, Sparkling Rose Lassi"
        ]
    },
    "Sunday": {
        "title": "Sweet Endings: Indian Dessert & Chai Pairing",
        "price": "$30 per person",
        "details": [
            "Decadent Indian dessert tasting",
            "Rasmalai with Rose Chai",
            "Gajar Halwa with Masala Chai",
            "Paan Kulfi with Saffron Kahwa",
            "Beverages: Chai-based lattes, Spiced hot chocolates"
        ]
    }
}

def main():
    st.title("🍽 Weekly Special Events 🍽")
    st.subheader("Premium Culinary Experiences at Passage")
    
    # Get current day
    today = datetime.today().strftime('%A')
    event = events.get(today, None)
    
    if event:
        st.header(f"📅 {event['title']}")
        st.subheader(f"💰 Price: {event['price']}")
        st.write("### Event Highlights:")
        
        for detail in event["details"]:
            st.write(f"✔️ {detail}")
    else:
        st.write("No special events today. Check back soon!")
    
if __name__ == "__main__":
    main()

import streamlit as st
from datetime import datetime

events = {
    "Monday": {
        "title": "Spice Symphony: Indian Curry & Wine Pairing Night",
        "price": "$28- Vegetarian \n $32 Non Vegetarian Per person ",
        "details": [
            "✨ Indulge in a curated dining experience where rich Indian flavors meet the perfect wine pairing.",
            "🍷 Sommelier-Selected Wine Pairing - Each dish is thoughtfully complemented with a perfectly matched wine.",
            "🍹 Refined Alternatives - Enjoy a selection of artisanal mocktails or premium non-alcoholic beverages. "
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
    st.markdown("<div style='text-align: center;'><img src='https://passageindia.com/wp-content/uploads/passagetoindia2.png' width='150'></div>", unsafe_allow_html=True)

    # Adaptive CSS for Light & Dark Mode
    st.markdown("""
        <style>
        :root {
            --bg-color: #ffffff;
            --text-color: #333333;
            --card-bg: #f8f9fa;
            --btn-bg: #007BFF;
            --btn-text: #ffffff;
            --table-border: #dddddd;
        }
        @media (prefers-color-scheme: dark) {
            :root {
                --bg-color: #1e1e1e;
                --text-color: #f1f1f1;
                --card-bg: #2b2b2b;
                --btn-bg: #008CBA;
                --btn-text: #ffffff;
                --table-border: #444;
            }
        }
        .experience-card {
            background-color: var(--card-bg);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            font-size: 20px;
            color: var(--text-color);
        }
        .book-btn {
            font-size: 18px;
            padding: 12px 20px;
            width: 50%;
            border-radius: 10px;
            font-weight: bold;
            background-color: var(--btn-bg);
            color: var(--btn-text);
            display: block;
            margin: 20px auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid var(--table-border);
            padding: 12px;
            text-align: center;
            color: var(--text-color);
        }
        </style>
    """, unsafe_allow_html=True)

    # Display Tonight’s Experience
    st.markdown(f"""
        <div class="experience-card">
            <h2>✨ Tonight's Premium Culinary Experience✨</h2>
        </div>
    """, unsafe_allow_html=True)

    
    # Get current day
    today = datetime.today().strftime('%A')
    event = events.get(today, None)
    
    if event:
        st.header(f" {event['title']}")
        st.subheader(f" {event['price']}")
        st.write("### Event Highlights:")
        
        for detail in event["details"]:
            st.write(f"✔️ {detail}")
    else:
        st.write("No special events today. Check back soon!")
    
if __name__ == "__main__":
    main()

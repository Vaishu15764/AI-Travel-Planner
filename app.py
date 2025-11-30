import streamlit as st
import datetime
from graph_engine.graph_builder import build_graph
from utils.email_sender import send_email

# Compile graph
app_graph = build_graph()

st.set_page_config(page_title="AI Travel Planner", page_icon="✈️", layout="wide")

# ---------------------------
# css
# ---------------------------
st.markdown("""
<style>

/* Sidebar */
section[data-testid="stSidebar"] {
    width: 440px !important;
    background-color: #0E1117;
    color: white;
    padding: 1.5rem;
}

/* Center main form */
.block-container {
    max-width: 2050px;
    margin: 0 auto;
    padding-top: 2rem;
}

/* Form card */
div[data-testid="stForm"] {
    background-color: #1E1E1E;
    padding: 2rem;
    border-radius: 18px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}

/* Input labels */
.stTextInput label, .stNumberInput label, .stSelectbox label {
    color: #d1d1d1;
    font-weight: 600;
}

/* Buttons */
div.stButton > button {
    width: 100%;
    background-color: #FF6F00 !important;
    color: white !important;
    border-radius: 20px;
    font-weight: 600;
    transition: all 0.3s ease;
}
div.stButton > button:hover {
    background-color: #FFA726 !important;
}

/* Markdown content container */
.markdown-text-container {
    background: #1E1E1E;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 3px 12px rgba(0,0,0,0.2);
}

/* Headings */
h1, h2, h3 {
    color: #f8f9fa;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# Sidebar History
# ---------------------------
st.sidebar.title("🗺️ Travel History")

if "history" not in st.session_state:
    st.session_state.history = []
if "current_plan" not in st.session_state:
    st.session_state.current_plan = None

if st.sidebar.button("➕ New Chat"):
    st.session_state.current_plan = None
    st.rerun()

if st.session_state.history:
    for item in reversed(st.session_state.history):
        if st.sidebar.button(f"📄 {item['destination']} ({item['date']})"):
            st.session_state.current_plan = item
else:
    st.sidebar.info("No history yet — create your first travel plan!")

# ---------------------------
# Main UI
# ---------------------------
st.title("✈️ AI Travel Planner")
st.markdown("Plan your next trip effortlessly using **Gemini AI** 🌍")

if not st.session_state.current_plan:
    
    with st.form("travel_form"):
        destination = st.text_input("Destination")
        area = st.selectbox("Preferred Area",
            ["Select an area", "City Center", "Beachside", "Hill View", "Market Area", "Historical Zone"]
        )
        duration = st.number_input("Trip Duration (days)", min_value=1, max_value=30, step=1)
        budget = st.number_input("Total Budget (₹)", min_value=1000, max_value=200000, step=500)
        travel_type = st.selectbox("Travel Type",
            ["Select travel type", "budget", "luxury", "family", "solo"]
        )
        interests = st.multiselect("Interests", ["sightseeing", "food", "shopping", "nature", "adventure"])
        email = st.text_input("Email (optional)")

        submitted = st.form_submit_button("✨ Generate My Travel Plan")

    if submitted:
        if (
            destination.strip() == "" 
            or area == "Select an area"
            or travel_type == "Select travel type"
            or not interests
        ):
            st.warning("⚠️ Please fill all fields.")
        else:
            st.info("🧠 Generating your AI travel plan... please wait ⏳")

            user_input = {
                "travel_input": {
                    "destination": destination,
                    "area": area,
                    "duration_days": duration,
                    "budget": budget,
                    "travel_type": travel_type,
                    "interests": interests
                }
            }

            result = app_graph.invoke(user_input)
            plan = result["summary"]

            st.session_state.current_plan = {
                "destination": destination,
                "summary": plan,
                "date": datetime.datetime.now().strftime("%d %b %Y, %I:%M %p")
            }

            st.session_state.history.append(st.session_state.current_plan)
            st.rerun()

else:
    plan = st.session_state.current_plan["summary"]
    destination = st.session_state.current_plan["destination"]

    st.success(f"✅ Travel plan for **{destination}**")
    st.markdown(plan, unsafe_allow_html=True)

    email = st.text_input("Send this plan to your email (optional):")
    if st.button("📩 Send Email"):
        if email:
            try:
                send_email(email, f"Your {destination} Travel Plan ✈️", plan)
                st.success(f"Email sent to {email}")
            except Exception as e:
                st.error(f"Failed to send email: {e}")
        else:
            st.warning("Please enter an email address.")

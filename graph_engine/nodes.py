from .llm_config import llm

def analyze_travel_profile(state):
    t = state["travel_input"]
    prompt = f"""
    You are a travel expert. Analyze:
    - Destination: {t['destination']} ({t['area']})
    - Duration: {t['duration_days']} days
    - Budget: ₹{t['budget']}
    - Type: {t['travel_type']}
    - Interests: {', '.join(t['interests'])}
    Provide a short summary and travel considerations.
    """
    state["travel_summary"] = llm.invoke(prompt).content
    return state


def suggest_hotels(state):
    t = state["travel_input"]
    prompt = f"""
    Recommend 2 affordable hotels near {t['area']}, {t['destination']}
    for {t['duration_days']} days under ₹{t['budget']}:
    - Hotel name
    - Price/night
    - Total cost
    - Why it's a good choice
    """
    state["hotel_options"] = llm.invoke(prompt).content
    return state


def suggest_places(state):
    t = state["travel_input"]
    prompt = f"""
    Suggest 5 must-visit places in or near {t['destination']} matching:
    - Interests: {', '.join(t['interests'])}
    - Within 10–15 km of {t['area']}
    Give short reasons for each.
    """
    state["places_to_visit"] = llm.invoke(prompt).content
    return state


def cost_estimator(state):
    prompt = f"""
    Estimate the total cost for {state['travel_input']['duration_days']} days in {state['travel_input']['destination']} using:
    - Hotels: {state['hotel_options']}
    - Places: {state['places_to_visit']}
    Include breakdown: hotel, food, transport, tickets, misc.
    Say if within ₹{state['travel_input']['budget']} budget.
    """
    state["cost_estimate"] = llm.invoke(prompt).content
    return state


def travel_summary(state):
    summary = f"""
    ### 🧭 Travel Summary
    {state['travel_summary']}

    ### 🏨 Hotel Options
    {state['hotel_options']}

    ### 📍 Places to Visit
    {state['places_to_visit']}

    ### 💰 Cost Estimate
    {state['cost_estimate']}
    """
    state["summary"] = summary
    return state

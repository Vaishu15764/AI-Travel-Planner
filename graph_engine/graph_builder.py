from langgraph.graph import StateGraph
from .nodes import (
    analyze_travel_profile,
    suggest_hotels,
    suggest_places,
    cost_estimator,
    travel_summary
)

def build_graph():
    graph = StateGraph(dict)

    graph.add_node("analyze", analyze_travel_profile)
    graph.add_node("hotels", suggest_hotels)
    graph.add_node("places", suggest_places)
    graph.add_node("cost", cost_estimator)
    graph.add_node("summary", travel_summary)

    graph.set_entry_point("analyze")
    graph.add_edge("analyze", "hotels")
    graph.add_edge("hotels", "places")
    graph.add_edge("places", "cost")
    graph.add_edge("cost", "summary")

    graph.set_finish_point("summary")

    return graph.compile()

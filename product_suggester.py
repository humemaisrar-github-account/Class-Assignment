from agents import Agent, Runner
from main import config

# Smart Store Agent
product_agent = Agent(
    name="Smart Store Agent",
    instructions="""
    You are a helpful product recommendation assistant in a smart pharmacy.
    When the user tells you about a problem or symptom (like headache, dehydration, body pain, etc),
    suggest a suitable product along with a short explanation of why it helps.

    Examples:
    - "I have a headache" → Recommend a pain reliever like Panadol, because it helps reduce pain.
    - "I feel dehydrated" → Recommend a water bottle or ORS (Oral Rehydration Salt), because it helps restore hydration.
    - "I have muscle pain" → Suggest a muscle relaxant cream or spray.
    - "My throat hurts" → Recommend lozenges or warm herbal tea.
    Be short, clear, and friendly.
    """
)

# Run the agent
if __name__ == "__main__":
    user_input = input("What’s your issue?\n> ")
    result = Runner.run_sync(product_agent, user_input, run_config=config)
    print("\nProduct Suggestion:\n", result.final_output)

from agents import Agent , Runner , function_tool 
from main import config

@function_tool
def get_capital(country : str)->str:
    """Returns the capital of a given country."""
    capitals = {
        "pakistan": "Islamabad",
        "germany": "German",
        "india": "New Delhi",
        "usa": "Washington, D.C.",
        "canada": "English and French",
        "brazil": "Portuguese",
        "australia": "English",
        "japan": "Tokyo"
    }
    return capitals.get(country.lower())

@function_tool
def get_language(country : str)->str:
    """Returns the official language of a given country."""
    languages = {
         
        "pakistan": "Urdu",
        "germany": "German",
        "india": "Hindi",
        "usa": "English",        
        "canada": "English and French",
        "brazil": "Portuguese",
        "australia": "English",
        "japan": "Japanese"
    }
    return languages.get(country.lower())

@function_tool
def get_population(country : str)->str:
    """Returns the official language of a given country."""
    populations = {
        "pakistan": "241 million",
        "germany": "83 million",
        "india": "1.4 billion",
        "usa": "331 million",        
        "canada": "39 million",
        "brazil": "214 million",
        "australia": "26 million",      
        "japan": "125 million"
    }
    return populations.get(country.lower())

orchestrator_agent=Agent(
    name="Get Info",
    instructions="""
        You are a country info bot. When given a country name, use the tools provided to fetch the capital, official language, and population.
        Then, respond with a short paragraph summarizing the country's info.
        """,   
    tools=[get_capital , get_language , get_population]
)

result = Runner.run_sync(
    orchestrator_agent,
    input(" Enter a country name: "),
    run_config=config
)
print('🌍 Country Info:')
print(result.final_output)
## ----------------------------------------- WITHOUT STREAMLIT --------------------------------------------------

# from agents import Agent, Runner, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel
# from dotenv import load_dotenv
# from agents import function_tool
# import os
# import datetime

# # # Load environment variables
# load_dotenv()
# gemini_api_key = os.getenv("GEMINI_API_KEY")


# @function_tool
# def get_weather(city: str) -> str:
#     return f"The weather in {city} is sunny"

# @function_tool
# def get_date_time():
#     return datetime.date.today()

# # External Gemini-compatible client setup
# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# # Model and config setup
# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=external_client
# )

# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# agent = Agent(
#     name = "Clothing Stylist",
#     instructions = 
#     """
#    You are a fashion stylist assistant. Use the get_weather tool to understand the user's current weather.
#    Then use both the weather and the occasion (like casual, formal, gym, etc.) to give a specific outfit suggestion.
#    For example, if it's sunny and gym is the occasion, recommend light, breathable workout gear.
#    Respond directly with the clothing advice..
#     """,
#     tools = [get_weather, get_date_time]
# )
# # 🧑‍💬 Step 1: Ask user input step by step
# city = input("📍 Hi there! First, please tell me your city: ")
# occasion = input("🎯 Great! Now, what's the occasion? (e.g., casual, formal, gym, work): ")

# # 🎯 Construct full prompt for the agent
# user_input = f"I'm attending a {occasion} in {city}. What should I wear?"

# response = Runner.run_sync(
#     agent,
#     input=user_input,
#     run_config=config
# )
# print("\n👗 Outfit Suggestion:")
# print(response.final_output)



## -------------------------------------------- WITH STREMLIT ------------------------------------------------

from agents import Agent, Runner, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from dotenv import load_dotenv
import streamlit as st
import os
import datetime
import asyncio
import nest_asyncio
import requests

# Setup
nest_asyncio.apply()

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")


# Tools
@function_tool
def get_weather(city: str) -> str:

    # Mapping cities to their coordinates
    city_coords = {
        "karachi": (24.86, 67.01),
        "tokyo": (35.67, 139.65),
        "cape town": (-33.92, 18.42),
        "london": (51.50, -0.127),
        "new York 🇺🇸": (40.71, -74.00),
        "tokyo 🇯🇵": (35.67, 139.65)
    }

    city_lower = city.lower()
    latitude, longitude = city_coords.get(city_lower, (24.86, 67.01))  # Default to Karachi

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}&current_weather=true&timezone=auto"
    )

    try:
        response = requests.get(url)
        data = response.json()

        weather = data["current_weather"]
        temp = weather["temperature"]
        wind = weather["windspeed"]
        code = weather["weathercode"]
        desc = "☀️ Sunny" if code == 0 else "🌥️ Cloudy"

        return f"The current weather in {city.title()} is {desc}, {temp}°C with wind speed {wind} km/h."
    except Exception as e:
        return f"❌ Could not fetch weather for {city.title()}. Please try again later."


@function_tool
def get_date_time():
    return datetime.date.today()

# External LLM client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Model and config
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Fashion Agent
agent = Agent(
    name="Clothing Stylist 👗",
    instructions="""
    You are a fashion stylist assistant. Use the get_weather tool to understand the user's current weather.
    Then use both the weather and the occasion (like casual, formal, gym, etc.) to give a specific outfit suggestion.
    For example, if it's sunny and gym is the occasion, recommend light, breathable workout gear.
    Be stylish, modern, and respond directly with advice + emojis!
    """,
    tools=[get_weather, get_date_time]
)

# --- Streamlit Page Config ---
st.set_page_config(page_title="Fashion Stylist With SD", page_icon="👠", layout="centered")

# --- Custom CSS ---
st.markdown("""
    <style>
        /* Apply global dark theme */
        .stApp {
            background-color: #000000;
            color: grey;
        }

        /* Title styling */
        .title-text {
            font-size: 2.2em;
            font-weight: bold;
            color: #f39c12;
            margin-bottom: 1rem;
        }

        /* Subtitle style (optional use) */
        .subtitle {
            color: #f1c40f;
            font-size: 1.2em;
        }

        /* Input labels */
        label {
            color: #f1f1f1 !important;
            font-weight: 500;
        }

        /* Inputs, buttons, and containers */
        .stTextInput, .stButton > button, .stTextArea, .stSelectbox {
            background-color: #222 !important;
            color: white !important;
            border-radius: 8px;
        }

        /* Output box and markdown card tweaks */
        .stMarkdown, .stAlert {
            background-color: #1a1a1a;
            padding: 1rem;
            border-radius: 10px;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)


# --- Sidebar ---
st.sidebar.title("🧵 Fashion Stylist with SABREENA")
st.sidebar.markdown("✨ Personalized outfit suggestions based on your city and event.\n\n👗 Stay stylish with weather-smart tips!")

# --- Main Interface ---
st.markdown("<div class='title-text'>🖤 Set Your Trending Outfit's According To Weather... </div>", unsafe_allow_html=True)
st.markdown("🗓️ Date: **{}**".format(datetime.date.today().strftime("%A, %d %B %Y")))

city = st.text_input("🌍 Enter your City:")
occasion = st.text_input("🎯 What's the Occasion? (e.g., casual, formal, party, gym, work):")

col1, = st.columns(1)

with col1:
   get_outfit = st.button("✨ Get My Outfit")

if get_outfit:
    if city and occasion:
        user_input = f"The city is {city} and the event is {occasion}."
        response = asyncio.run(
            Runner.run(
            agent, 
            input=user_input, 
            run_config=config
            )
        )
        st.markdown("### 👚 Your Personalized Outfit Suggestion:")
        st.success(f"💬 {response.final_output}")
    else:
        st.warning("⚠️ Please enter both the city and the occasion.")

# Footer
st.markdown(
    """
    <hr style="margin-top: 50px; border: 1px solid #666;" />

    <div style='text-align: center; padding: 10px; color: #999; font-size: 14px;'>
        Made with ❤️ by Sabreena &nbsp;|&nbsp; 🤖 Powered by Gemini + Streamlit
    </div>
    """,
    unsafe_allow_html=True
)

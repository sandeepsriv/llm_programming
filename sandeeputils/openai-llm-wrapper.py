from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv(override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')
deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')
grok_api_key = os.getenv('GROK_API_KEY')
openrouter_api_key = os.getenv('OPENROUTER_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")
    
if anthropic_api_key:
    print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
else:
    print("Anthropic API Key not set (and this is optional)")

if google_api_key:
    print(f"Google API Key exists and begins {google_api_key[:2]}")
else:
    print("Google API Key not set (and this is optional)")

if deepseek_api_key:
    print(f"DeepSeek API Key exists and begins {deepseek_api_key[:3]}")
else:
    print("DeepSeek API Key not set (and this is optional)")

if groq_api_key:
    print(f"Groq API Key exists and begins {groq_api_key[:4]}")
else:
    print("Groq API Key not set (and this is optional)")

if grok_api_key:
    print(f"Grok API Key exists and begins {grok_api_key[:4]}")
else:
    print("Grok API Key not set (and this is optional)")

if openrouter_api_key:
    print(f"OpenRouter API Key exists and begins {openrouter_api_key[:3]}")
else:
    print("OpenRouter API Key not set (and this is optional)")


# Connect to OpenAI client library
# A thin wrapper around calls to HTTP endpoints
openai = OpenAI()

# For Gemini, DeepSeek and Groq, we can use the OpenAI python client
# Because Google and DeepSeek have endpoints compatible with OpenAI
# And OpenAI allows you to change the base_url

anthropic_url = "https://api.anthropic.com/v1/"
gemini_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
deepseek_url = "https://api.deepseek.com"
groq_url = "https://api.groq.com/openai/v1"
grok_url = "https://api.x.ai/v1"
openrouter_url = "https://openrouter.ai/api/v1"
ollama_url = "http://localhost:11434/v1"

if anthropic_api_key:
    anthropic = OpenAI(base_url=anthropic_url, api_key=anthropic_api_key)
else:
    print("Anthropic: can not instantiate")

if google_api_key:
    gemini = OpenAI(base_url=gemini_url, api_key=google_api_key)
else:
    print("Gemini: can not instantiate")

if deepseek_api_key:
    deepseek = OpenAI(base_url=deepseek_url, api_key=deepseek_api_key)
else:
    print("Deepseek: can not instantiate")

if groq_api_key:
    groq = OpenAI(base_url=groq_url, api_key=groq_api_key)
else:
    print("Groq: can not instantiate")

if grok_api_key:
    grok = OpenAI(base_url=grok_url, api_key=grok_api_key)
else:
    print("Grok: can not instantiate")

if openrouter_api_key:
    openrouter = OpenAI(base_url=openrouter_url, api_key=openai_api_key)
else:
    print("Openrouter: can not instantiate")

ollama = OpenAI(base_url=ollama_url, api_key="ollama")
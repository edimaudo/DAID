import os
import json
from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai.errors import APIError

# --- Application Initialization ---
# The Flask object MUST be named 'app' for Vercel to find the entry point.
app = Flask(__name__)

# Load API Key securely from environment variables (Vercel provides this)
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

if not GEMINI_API_KEY:
    # This warning is for local testing. In Vercel, this will trigger the 500 response.
    print("WARNING: GEMINI_API_KEY environment variable not set. API routes will fail.")

# --- Routes ---

# 1. Landing Page Route (renders templates/index.html)
@app.route('/')
def index():
    """Renders the main landing page."""
    return render_template('index.html')

# 2. Main Application Route (renders templates/app.html)
@app.route('/app')
def main_app():
    """Renders the multi-step data entry application page."""
    return render_template('app.html')


# 3. Secure Gemini API Endpoint
@app.route('/api/generate_analysis', methods=['POST'])
def generate_analysis():
    """
    Calls the Gemini API securely on the server side and returns the analysis.
    """
    if not GEMINI_API_KEY:
        # Returning a clear error if the server is improperly configured
        return jsonify({"error": "Server configuration error: Gemini API key is missing. Please set the GEMINI_API_KEY environment variable.", "success": False}), 500
    
    try:
        # Get user data sent from the client
        data = request.json
        user_input = data.get('userInput', '')
        
        if not user_input:
            return jsonify({"error": "No user input provided for analysis.", "success": False}), 400

        # --- Gemini API Call Setup ---
        
        system_instruction = (
            "You are a Decision Intelligence and Action Designer. "
            "Your goal is to provide a concise, structured, and professional analysis of problems using structured problem solving and decision making frameowkrs "
            "based on the provided user input and collected data. "
            "Structure your response with clear headings (e.g., Summary, Key Findings, Recommendations). "
            "The entire output must be formatted using Markdown for clean rendering."
        )

        full_prompt = (
            f"Please generate a logical report based on the following consolidated data:\n\n"
            f"--- CONSOLIDATED USER DATA ---\n"
            f"{user_input}\n"
            f"--- END OF DATA ---\n"
            f"Provide a professional report formatted strictly in Markdown."
        )

        # Initialize the client using the secure key
        client = genai.Client(api_key=GEMINI_API_KEY)

        # Generate content
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=full_prompt,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_instruction
            )
        )
        
        # Return the generated text successfully
        return jsonify({
            "analysisText": response.text,
            "success": True
        })

    except APIError as e:
        print(f"Gemini API Error: {e}")
        return jsonify({"error": f"AI generation failed due to API error: {e}", "success": False}), 500
    except Exception as e:
        print(f"Internal Server Error: {e}")
        return jsonify({"error": "An unexpected server error occurred during processing.", "success": False}), 500


# Vercel requirement: The entry point must be defined.
if __name__ == '__main__':
    # When running locally, load the .env file for environment variables
    # This must be outside the main application scope that Vercel uses.
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("Note: python-dotenv not found. Install it to use .env file locally.")
    
    # Run locally for debugging
    app.run(debug=True, host='0.0.0.0', port=5000)

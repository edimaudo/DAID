import os
import json
from flask import Flask, render_template, request, jsonify
from google import genai
from google.generativeai.errors import APIError

# --- Application Initialization ---
app = Flask(__name__)

# Load API Key securely from environment variables (MANDATORY for Vercel)
# The key is only accessed here on the server side, keeping it secure.
# Vercel reads this from your deployment settings. Locally, it reads from the .env file.
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

if not GEMINI_API_KEY:
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
# Handles the request for AI analysis sent from the client-side JavaScript in app.html.
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
        
        # System instruction to define the model's persona and output format
        system_instruction = (
             """
                You are the Decision & Action Intelligence Designer (DAID), an AI dedicated to providing the best strategic advice possible. 
            
            Your goal is to ensure the user makes a smart decision based on their Problem Statement and Assumptions.
            
            You will be provided with:
            1. A Problem Statement.
            2. A list of Assumptions.
            3. A specific Framework to apply (OR you will be asked to select the best ones).

            Format the output STRICTLY as a JSON object with the following structure:
            {
              "analyses": [
                {
                  "framework_name": "Name of the Framework",
                  "why_selected": "A clear explanation of why this framework is appropriate for this specific problem.",
                  "decision": "The core decision or recommendation derived from applying this framework.",
                  "sections": [
                    {
                      "title": "Section Title (e.g., Analysis, Key Factors, Risks)",
                      "insights": [
                        "Insight 1",
                        "Insight 2"
                      ]
                    }
                  ]
                }
              ]
            }
            """
        )

        # Full prompt combining the instruction and user data
        full_prompt = (
            f"Please generate a detailed and logical decision analysis report based on the users input and system prompt:\n\n"
            f"--- CONSOLIDATED USER DATA ---\n"
            f"{user_input}\n"
            f"--- END OF DATA ---\n"
            f"Provide a professional decision analysis report formatted strictly in Markdown."
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
        # Log and return errors from the Gemini API
        print(f"Gemini API Error: {e}")
        return jsonify({"error": f"AI generation failed due to API error: {e}", "success": False}), 500
    except Exception as e:
        # Handle all other internal server errors
        print(f"Internal Server Error: {e}")
        return jsonify({"error": "An unexpected server error occurred during processing.", "success": False}), 500


# Vercel requirement: The entry point must be defined.
if __name__ == '__main__':
    # When running locally, load the .env file for environment variables
    from dotenv import load_dotenv
    load_dotenv()
    
    # Run locally for debugging
    app.run(debug=True, host='0.0.0.0', port=5000)

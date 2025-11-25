import os
import json
from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai.errors import APIError
from google.genai import types

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
        data = request.json
        user_query = data.get('userQuery', 'No input provided.')
        
        # 1. Update the System Instruction
        # CRUCIAL: Instruct the model to generate a *specific* JSON object.
        system_instruction = (
            "You are a Decision Intelligence and Action Designer. Your goal is to provide a concise, structured analysis "
            "of the user's data. **The output MUST be a strict JSON object.** "
            "DO NOT include any Markdown formatting, explanations, or text outside of the JSON block."
        )
        
        full_prompt = (
            f"Based on the following consolidated data, generate a structured analysis report. "
            f"Use the JSON format: {{\"analysisTitle\": \"<Report Title>\", \"keyFindings\": [\"<Finding 1>\", \"<Finding 2>\", \"<Finding 3>\"]}}\n\n"
            f"Data: {user_query}"
        )

        client = genai.Client(api_key=GEMINI_API_KEY)
        
        # 2. Add response_mime_type to enforce JSON output
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=full_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                # *** THE FIX: Force the model to generate valid JSON ***
                response_mime_type="application/json", 
            )
        )
        
        # 3. Parse and Return the JSON
        # Since response_mime_type is set, response.text is guaranteed to be a JSON string.
        try:
            analysis_data = json.loads(response.text)
            
            # Return the structured data directly
            return jsonify({
                "analysisData": analysis_data,
                "success": True
            })
            
        except json.JSONDecodeError as e:
            # Fallback for when the model fails to follow the strict instruction
            print(f"Server-side JSON parsing error: {e}")
            return jsonify({
                "error": "AI failed to produce a valid JSON report. Please retry.", 
                "success": False
            }), 500

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

# File: termux_ai_assistant/ai_client.py
import os
import json
from google.cloud import aiplatform
from google.auth import load_credentials_from_file

class AIClient:
    def __init__(self, credentials_path):
        self.credentials_path = credentials_path
        self._initialize_client()

    def _initialize_client(self):
        """Initialize the Vertex AI client with credentials."""
        try:
            credentials, project = load_credentials_from_file(self.credentials_path)
            aiplatform.init(credentials=credentials)
        except Exception as e:
            raise Exception(f"Failed to initialize AI client: {str(e)}")

    async def generate_code(self, prompt):
        """Generate code using Vertex AI Gemini model."""
        try:
            # Initialize Gemini model
            model = aiplatform.Model("gemini-1.5-pro")
            
            # Prepare the prompt
            formatted_prompt = f"""
            Generate Python code for the following request:
            {prompt}
            
            Consider that this code will run in Termux on Android.
            Only include the code implementation, no explanations.
            """
            
            # Generate code
            response = model.predict(formatted_prompt)
            
            # Extract code from response
            return self._extract_code(response.text)
        except Exception as e:
            raise Exception(f"Code generation failed: {str(e)}")

    def _extract_code(self, response_text):
        """Extract code from the model response."""
        # Simple extraction - can be enhanced based on actual response format
        return response_text.strip()

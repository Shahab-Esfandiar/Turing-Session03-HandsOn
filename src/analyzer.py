import json
from openai import OpenAI
from src.config import AVALAI_API_KEY, API_BASE_URL
from src.exceptions import LLMAnalysisError

class EmailAnalyzer:
    def __init__(self):
        self.client = OpenAI(api_key=AVALAI_API_KEY, base_url=API_BASE_URL)
        
        # Few-Shot Prompting
        self.system_prompt = """
        You are an expert AI email routing assistant.
        Analyze the user's email text (Persian or English) and extract metadata.
        
        RULES:
        1. You MUST respond ONLY with a valid JSON object.
        2. Category MUST be exactly one of: "Technical Support", "Sales & Billing", "HR", "General".
        3. Priority MUST be exactly one of: "Low", "Medium", "High".
        4. Summary MUST be a brief one-sentence summary in the language of the original email.
        5. If Key_Entities are not found, use null instead of "None".

        EXAMPLE:
        Input email: "Hi, my payment for invoice #999 failed with error 502."
        Output JSON:
        {
            "Category": "Sales & Billing",
            "Priority": "High",
            "Summary": "Payment failure for invoice #999.",
            "Key_Entities": "Invoice #999, Error 502"
        }
        """

    def analyze_content(self, text: str) -> dict:
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": text}
        ]

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                temperature=0.1, 
                max_tokens=500,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                response_format={"type": "json_object"}
            )
            
            raw_response = response.choices[0].message.content.strip()
            return json.loads(raw_response)
            
        except json.JSONDecodeError as e:
            raise LLMAnalysisError(f"LLM did not return a valid JSON: {raw_response}") from e
        except Exception as e:
            raise LLMAnalysisError(f"Failed to communicate with API: {str(e)}") from e
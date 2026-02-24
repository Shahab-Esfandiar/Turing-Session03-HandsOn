import re
import os
from typing import Dict, Any

class EmailRouter:
    def __init__(self):
        self.department_emails = {
            "Technical Support": "support@novinpardaz.com",
            "Sales & Billing": "sales@novinpardaz.com",
            "HR": "hr@novinpardaz.com",
            "General": "management@novinpardaz.com"
        }

    def get_routing_address(self, category: str) -> str:
        return self.department_emails.get(category, self.department_emails["General"])

    def detect_text_direction(self, text: str) -> str:
        if re.search(r'[\u0600-\u06FF]', text):
            return "rtl"
        return "ltr"

    def generate_html_report(self, sender: str, subject: str, body: str, metadata: Dict[str, Any]) -> str:
        direction = self.detect_text_direction(body)
        text_align = "right" if direction == "rtl" else "left"

        html_content = f"""
        <html>
          <body dir="{direction}" style="font-family: Arial, sans-serif; line-height: 1.6;">
            <h2 style="color: #2c3e50;">Automated Email Routing Report</h2>
            <p><strong>Original Sender:</strong> {sender}</p>
            <p><strong>Subject:</strong> {subject}</p>
            
            <table border="1" style="border-collapse: collapse; width: 100%; max-width: 600px; margin-bottom: 20px;">
              <tr style="background-color: #f2f2f2;">
                <th style="padding: 8px; text-align: {text_align};">Metadata</th>
                <th style="padding: 8px; text-align: {text_align};">Extracted Value</th>
              </tr>
              <tr><td style="padding: 8px;">Routing Category</td><td style="padding: 8px;">{metadata.get('Category', 'N/A')}</td></tr>
              <tr><td style="padding: 8px;">Priority Level</td><td style="padding: 8px;">{metadata.get('Priority', 'N/A')}</td></tr>
              <tr><td style="padding: 8px;">Summary</td><td style="padding: 8px;">{metadata.get('Summary', 'N/A')}</td></tr>
              <tr><td style="padding: 8px;">Key Entities</td><td style="padding: 8px;">{metadata.get('Key_Entities', 'None')}</td></tr>
            </table>

            <h3 style="color: #2c3e50;">Original Email Content:</h3>
            <div style="background-color: #f9f9f9; padding: 15px; border: 1px solid #ccc; border-{text_align}: 4px solid #3498db;">
              {body.replace(chr(10), '<br>')}
            </div>
          </body>
        </html>
        """
        return html_content

    def save_html_to_disk(self, filename: str, html_content: str):
        os.makedirs("outputs", exist_ok=True)
        filepath = os.path.join("outputs", filename)
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(html_content)
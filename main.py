import sys
import time
from src.analyzer import EmailAnalyzer
from src.router import EmailRouter
from src.mock_data import MOCK_EMAILS
from src.exceptions import MissingConfigurationError, LLMAnalysisError

def main():
    print("🚀 Starting Batch Processing for Automated Email Routing System...\n")
    
    try:
        analyzer = EmailAnalyzer()
        router = EmailRouter()
    except MissingConfigurationError as e:
        print(f"❌ Configuration Error: {e}")
        sys.exit(1)

    total_emails = len(MOCK_EMAILS)
    print(f"📥 Found {total_emails} mock emails to process.\n")
    print("-" * 50)

    for index, email_data in enumerate(MOCK_EMAILS, start=1):
        print(f"[{index}/{total_emails}] Processing email from: {email_data['sender']}")
        print(f"Subject: {email_data['subject']}")
        
        try:
            # 1. Analyze Content
            metadata = analyzer.analyze_content(email_data["body"])
            category = metadata.get("Category", "General")
            
            # 2. Get Routing Address
            target_dept = router.get_routing_address(category)
            
            # 3. Generate HTML
            final_html_report = router.generate_html_report(
                sender=email_data["sender"],
                subject=email_data["subject"],
                body=email_data["body"],
                metadata=metadata
            )
            
            # 4. Save to Disk instead of sending real email
            safe_subject = "".join([c for c in email_data['subject'] if c.isalpha() or c.isdigit() or c==' ']).rstrip()
            filename = f"email_{index:02d}_{category.replace(' ', '_')}.html"
            
            router.save_html_to_disk(filename, final_html_report)
            
            print(f"✅ Routed to: {target_dept} (Category: {category})")
            print(f"💾 Saved report as: outputs/{filename}\n")
            time.sleep(1) 

        except LLMAnalysisError as e:
            print(f"❌ Analysis Failed for email {index}: {e}\n")
        except Exception as e:
            print(f"❌ Unexpected error for email {index}: {e}\n")

    print("-" * 50)
    print("🎉 Batch processing completed! Check the 'outputs' directory for the HTML files.")

if __name__ == "__main__":
    main()
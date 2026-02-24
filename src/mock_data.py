MOCK_EMAILS = [
    # --- Technical Support ---
    {"sender": "ali@example.com", "subject": "خطای 500 در سرور اصلی", "body": "سلام، از ساعت ۲ نیمه‌شب سرور دیتابیس با خطای 500 مواجه شده و سایت کاملاً از دسترس خارج است. لطفا سریعا پیگیری کنید."},
    {"sender": "j.doe@company.com", "subject": "Cannot connect to VPN", "body": "Hello, I am getting error code 809 when trying to connect to the company VPN. My IP is 192.168.1.5."},
    {"sender": "sara@test.ir", "subject": "مشکل نصب نرم‌افزار", "body": "من فایل نصبی ویندوز را دانلود کردم اما در مرحله آخر ارور Missing DLL می‌دهد."},
    {"sender": "admin@tech.com", "subject": "API Timeout Issue", "body": "The endpoint /v1/users is taking more than 30 seconds to respond. We need to look into this immediately."},
    {"sender": "reza@test.com", "subject": "فراموشی رمز عبور", "body": "من رمز عبور پنل مدیریت خود را فراموش کرده‌ام و ایمیل بازیابی هم برایم ارسال نمی‌شود."},
    {"sender": "amir.tech@enterprise.com", "subject": "گزارش قطعی گسترده و کرش سرورهای اصلی دیتابیس", 
     "body": "سلام وقت بخیر. من امیر هستم از تیم نگهداری زیرساخت. متاسفانه از ساعت ۳:۴۵ دقیقه بامداد امروز، کلاستر اصلی دیتابیس ما (نود شماره ۴ و ۵) دچار یک افت ناگهانی در منابع رم شد که منجر به خطای Out of Memory و در نهایت کرش کامل سرویس گردید. ما تلاش کردیم با استفاده از بک‌آپ‌های روز گذشته سیستم را بازیابی کنیم اما پروسه ری‌استور در مرحله ۷۸ درصد متوقف می‌شود و خطای Error Code: DB-X909 را نشان می‌دهد. با توجه به اینکه این سیستم مستقیما به درگاه پرداخت کاربران متصل است، در حال حاضر روزانه میلیون‌ها تومان ضرر در حال ثبت است. لطفا در اسرع وقت یکی از مهندسین ارشد پایگاه داده را برای بررسی لاگ فایل‌ها به سیستم ما متصل کنید. شماره تماس مستقیم من جهت هماهنگی 09121234567 است."},
    
    {"sender": "sarah.j@globalcorp.co.uk", "subject": "Partnership Proposal for Q3 Cloud Integrations", 
     "body": "To Whom It May Concern, I am writing to you on behalf of GlobalCorp Ltd. After reviewing your recent product launches, our executive team is highly interested in establishing a strategic partnership. We are currently overhauling our internal cloud infrastructure and are looking for a reliable vendor to provide scalable API endpoints for our mobile applications. Our requirements include a guaranteed 99.99% uptime SLA, dedicated technical account management, and custom endpoint routing. We anticipate an initial volume of approximately 50 million API calls per month, scaling up to 200 million by the end of Q4. Please review the attached preliminary requirements document. We would like to schedule a 45-minute technical discovery call next Tuesday at 10:00 AM GMT to discuss pricing tiers and technical feasibility."},
    
    {"sender": "shayan.dev@yahoo.com", "subject": "ارسال رزومه برای موقعیت شغلی مهندس نرم‌افزار ارشد", 
     "body": "تیم محترم منابع انسانی نوین پرداز، با سلام و احترام. اینجانب شایان، فارغ‌التحصیل مقطع کارشناسی ارشد مهندسی نرم‌افزار، با بیش از ۷ سال سابقه کار تخصصی در زمینه توسعه سیستم‌های بک‌اند با پایتون و جنگو، رزومه خود را جهت بررسی برای موقعیت شغلی 'مهندس نرم‌افزار ارشد' که در لینکدین آگهی کرده بودید، ارسال می‌کنم. در شرکت قبلی، من مسئولیت بازنویسی معماری مونولیتیک به میکروسرویس را بر عهده داشتم که منجر به افزایش ۴۰ درصدی سرعت پاسخگویی سیستم شد. همچنین تجربه عمیقی در کار با داکر، کوبرنیتیز و راه‌اندازی CI/CD دارم. بسیار مشتاقم تا مهارت‌های خود را در تیم پویای شما به کار بگیرم و در توسعه محصولات نوآورانه‌تان نقشی داشته باشم. منتظر بازخورد ارزشمند شما هستم."},
    
    {"sender": "angry.customer88@gmail.com", "subject": "شکایت شدید از نحوه پاسخگویی تیم پشتیبانی و درخواست لغو", 
     "body": "واقعا برای سیستم پشتیبانی شما متاسفم! من سه روز پیش یک تیکت (شماره تیکت: 445566) ثبت کردم مبنی بر اینکه سرویس ابری من بدون هیچ دلیلی قطع شده است. بعد از ۴۸ ساعت، یک نفر از تیم شما جواب داده 'لطفا مودم خود را خاموش روشن کنید'! این توهین به شعور مشتری است. سرویس من روی سرورهای شماست چه ربطی به مودم خانه من دارد؟ من تمام کارهای شرکتم خوابیده و هیچکس پاسخگو نیست. با این سطح از خدمات، من دیگر تمایلی به تمدید قرارداد ندارم. درخواست دارم همین امروز تمام سرویس‌های من را لغو کرده و مبلغ باقی‌مانده از اشتراک سالانه من را به شماره شبا که قبلا در پروفایلم ثبت کرده‌ام عودت دهید. در غیر این صورت از طریق مراجع قانونی پیگیری خواهم کرد."},
    
    {"sender": "h.manager@retail-chain.com", "subject": "Enterprise licensing and bulk discount inquiry", 
     "body": "Hello Sales Team, We operate a chain of 45 retail stores across the country and are currently evaluating new CRM solutions. Your software seems to fit our needs, but we need to understand your enterprise pricing model. Specifically, we would need 150 administrative licenses and 400 limited-access user licenses. Furthermore, we require custom onboarding and migration services from our current legacy system (which is based on Oracle). Does your company offer bulk discounts for an organization of our size? Also, do you provide dedicated 24/7 phone support as part of the enterprise package? I have CC'd our IT Director on this email. We look forward to receiving a detailed proposal and pricing breakdown before our board meeting on the 15th of next month."},

    # --- Sales & Billing ---
    {"sender": "finance@client.com", "subject": "Invoice #8899 Payment Failed", "body": "We tried to pay invoice 8899 today but the credit card transaction was declined. Can you send an alternative payment link?"},
    {"sender": "m.ahmadi@shop.ir", "subject": "پیگیری پیش‌فاکتور", "body": "درخواست صدور پیش‌فاکتور برای خرید ۵۰ لایسنس سازمانی داشتم. شماره تماس من 09121112233 است."},
    {"sender": "purchasing@corp.com", "subject": "Enterprise Pricing Quote", "body": "We are interested in your cloud storage solutions. Can we get a quote for 10TB of data?"},
    {"sender": "neda@domain.ir", "subject": "مشکل در درگاه پرداخت", "body": "امروز صبح مبلغ ۲ میلیون تومان از حساب من کسر شد اما اشتراک من تمدید نشده است. لطفا بررسی کنید."},
    {"sender": "user99@mail.com", "subject": "Refund Request", "body": "I want to cancel my subscription and request a refund as I haven't used the service this month."},
    {"sender": "m.karimi@test.ir", "subject": "فاکتور", "body": "لطفا فاکتور خرید امروزم رو برام ایمیل کنید."},
    {"sender": "john.smith@domain.com", "subject": "System Down", "body": "The website is throwing a 502 Bad Gateway error. Help."},
    {"sender": "neda.h@student.ac.ir", "subject": "رزومه", "body": "سلام، رزومه من به پیوست ارسال شد."},
    {"sender": "user123@mail.com", "subject": "Unsubscribe", "body": "Please remove me from your mailing list immediately."},
    {"sender": "b.sales@shop.com", "subject": "تعرفه", "body": "قیمت پنل پیامکی شما چنده؟"},
    
    # --- HR (Human Resources) ---
    {"sender": "applicant@job.com", "subject": "Application for Python Developer", "body": "Dear Hiring Manager, please find my resume attached for the Senior Python Developer position. I have 5 years of experience."},
    {"sender": "k.rostami@uni.ac.ir", "subject": "درخواست کارآموزی تابستان", "body": "با سلام، من دانشجوی ترم آخر مهندسی کامپیوتر هستم و تمایل دارم دوره کارآموزی خود را در دپارتمان هوش مصنوعی شما بگذرانم."},
    {"sender": "dev@coder.com", "subject": "Interview Follow-up", "body": "I am writing to follow up on my interview for the frontend role on Tuesday. When can I expect to hear back?"},
    {"sender": "maryam@email.ir", "subject": "ارسال رزومه طراح رابط کاربری", "body": "با سلام، رزومه و نمونه کارهای من برای موقعیت شغلی UI/UX Designer به پیوست ارسال می‌گردد."},
    {"sender": "student@college.edu", "subject": "Part-time job inquiry", "body": "Do you offer any part-time data entry positions for college students?"},
    
    # --- General / Management ---
    {"sender": "ceo@startup.com", "subject": "Partnership Opportunity", "body": "We would love to discuss a potential business partnership regarding integrating our services. Let's schedule a call."},
    {"sender": "customer@angry.com", "subject": "شکایت از برخورد پرسنل", "body": "متاسفانه امروز یکی از کارشناسان پشتیبانی شما برخورد بسیار نامناسبی با بنده داشتند. من این موضوع را پیگیری خواهم کرد."},
    {"sender": "info@ad-agency.com", "subject": "Advertising Proposal", "body": "We run a marketing agency and have a proposal to help increase your user base by 20% in the next quarter."},
    {"sender": "hassan@company.ir", "subject": "تغییر آدرس شرکت", "body": "خواهشمند است آدرس پستی ثبت شده شرکت ما در سیستم خود را به آدرس جدید تغییر دهید."},
    {"sender": "pr@event.com", "subject": "Invitation to Tech Conference", "body": "We would like to invite your CEO to speak at our upcoming annual technology conference in London."},
    {"sender": "ali.r@example.com", "subject": "مشکل در ورود به پنل", "body": "سلام، من رمز عبورم را درست وارد می‌کنم اما سیستم خطای 'نام کاربری نامعتبر' می‌دهد."},
    {"sender": "billing@client.com", "subject": "Payment Link Expired", "body": "We tried to pay the invoice today but the payment gateway link you sent last week has expired. Can you send a new one?"},
    {"sender": "sara.ui@test.ir", "subject": "درخواست استخدام طراح", "body": "من نمونه کارهای طراحی رابط کاربری خودم رو در لینکدین گذاشتم. آیا امکان همکاری به صورت دورکاری دارید؟"},
    {"sender": "admin@tech.com", "subject": "API Timeout Issue", "body": "The endpoint /v1/users is taking more than 30 seconds to respond. We need to look into this immediately."},
    {"sender": "reza@test.com", "subject": "تغییر اطلاعات شرکت", "body": "لطفا نام حقوقی شرکت ما را در فاکتورهای بعدی از 'تست' به 'شرکت فناوری تست' تغییر دهید."},
    {"sender": "finance@corp.com", "subject": "Invoice #8899", "body": "The credit card transaction was declined. We will try another card tomorrow."},
    {"sender": "m.ahmadi@shop.ir", "subject": "پیگیری پیش‌فاکتور", "body": "درخواست صدور پیش‌فاکتور برای خرید ۵۰ لایسنس داشتم. شماره تماس من 09121112233 است."},
    {"sender": "purchasing@corp.com", "subject": "Storage Quote", "body": "We are interested in your cloud storage solutions. Can we get a quote for 10TB of data?"},
    {"sender": "neda@domain.ir", "subject": "مشکل در درگاه", "body": "امروز صبح مبلغ کسر شد اما اشتراک من تمدید نشده است. لطفا بررسی کنید."},
    {"sender": "ceo@startup.com", "subject": "Partnership Call", "body": "We would love to discuss a potential business partnership regarding integrating our services. Let's schedule a call."}
    
]

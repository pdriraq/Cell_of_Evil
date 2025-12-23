import os
from dotenv import load_dotenv

# تحميل البيانات من ملف .env
load_dotenv()

def process_secure_data():
    # استدعاء الرقم من بيئة النظام وليس من الكود مباشرة
    phone = os.getenv("PHONE_NUMBER")
    
    if phone:
        print("✅ تم استدعاء رقم الهاتف بنجاح من مكان آمن.")
        # تعمية الرقم عند العرض للتأكد من حمايته حتى في الشاشة
        masked_phone = "*" * (len(phone) - 3) + phone[-3:]
        print(f"📱 الرقم المعروض: {masked_phone}")
    else:
        print("❌ خطأ: لم يتم العثور على رقم الهاتف في ملف الـ .env")

if __name__ == "__main__":
    process_secure_data()

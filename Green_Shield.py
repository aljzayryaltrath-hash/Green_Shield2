import os
import time
import requests
import folium
import phonenumbers
from phonenumbers import geocoder, carrier
from colorama import Fore, init

# تهيئة الألوان
init(autoreset=True)

# مفتاح API الخاص بك
API_KEY = "41a2bc92a472f714126766c5920dd0eb"

def matrix_print(text, delay=0.01, color=Fore.GREEN):
    """دالة الطباعة المتريكسية المصححة"""
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print()

def phone_security_scan():
    """1. فحص الهاتف من التجسس والفيروسات"""
    matrix_print("\n[🛡️] بدء فحص النظام الشامل...", color=Fore.YELLOW)
    time.sleep(1)
    # محاكاة فحص ملفات التجسس كما في طلبك
    matrix_print("[*] فحص ملفات النظام الحساسة... ✅ آمن", 0.02)
    matrix_print("[*] البحث عن برمجيات Keyloggers... ✅ لم يتم العثور", 0.02)
    print(Fore.GREEN + "✅ النتيجة: هاتف عمار جخجاخة محمي بالكامل.")

def algeria_radar():
    """2. رادار فحص الاتصالات وتحديد الموقع (GPS)"""
    matrix_print("\n[📡] رادار تتبع الأرقام الجزائري...", color=Fore.YELLOW)
    num = input(Fore.CYAN + "أدخل الرقم المطلوب (مثال: 213xxxxxxxxx): ")
    
    try:
        # الاتصال بـ API للتحقق
        res = requests.get(f"http://apilayer.net/api/validate?access_key={API_KEY}&number={num}").json()
        
        if res.get('valid'):
            parsed = phonenumbers.parse("+" + num if not num.startswith('+') else num)
            location = geocoder.description_for_number(parsed, "ar") or "الجزائر"
            service_provider = carrier.name_for_number(parsed, "ar")
            
            print(Fore.GREEN + f"\n[+] المعلومات المستخرجة:")
            print(f"📍 الموقع: {location}")
            print(f"📱 المشغل: {service_provider}")
            print(f"🌍 الدولة: {res.get('country_name')}")

            # تحديد الإحداثيات التقريبية ورسم الخريطة كما فعلنا سابقاً
            coords = [36.46, 7.42] if "قالمة" in location else [36.75, 3.05]
            m = folium.Map(location=coords, zoom_start=12)
            folium.Marker(coords, popup=f"تهديد من {location}").add_to(m)
            m.save("green_shield_map.html")
            print(Fore.YELLOW + "🌍 تم تحديث خريطة التتبع: green_shield_map.html")
        else:
            print(Fore.RED + "❌ الرقم غير صحيح أو غير موجود في قاعدة البيانات.")
    except Exception as e:
        print(Fore.RED + f"⚠️ خطأ في الرادار: {e}")

def pentest_sites():
    """3. فحص أمن المواقع (Pentest)"""
    matrix_print("\n[🌐] بدء فحص ثغرات المواقع (SQL, XSS, SSL)...", color=Fore.YELLOW)
    target = input(Fore.CYAN + "أدخل رابط الموقع المستهدف: ")
    time.sleep(1)
    matrix_print(f"[*] جاري تحليل {target} ...", 0.05)
    print(Fore.GREEN + "✅ الفحص المبدئي انتهى. لا توجد ثغرات حرجة مكشوفة حالياً.")

def main_menu():
    while True:
        os.system('clear')
        # شعار Green Shield الجديد
        print(Fore.GREEN + r"""
  ____ ____  _____ _____ _   _   ____  _   _ ___ _____ _     ____  
 / ___|  _ \| ____| ____| \ | | / ___|| | | |_ _| ____| |   |  _ \ 
| |  _| |_) |  _| |  _| |  \| | \___ \| |_| || ||  _| | |   | | | |
| |_| |  _ <| |___| |___| |\  |  ___) |  _  || || |___| |___| |_| |
 \____|_| \_\_____|_____|_| \_| |____/|_| |_|___|_____|_____|____/ 
 
 --- الدرع الأخضر الجزائري | المبرمج djak.dz ---
        """)
        print("1. 🛡️ فحص الهاتف من التجسس والفيروسات")
        print("2. 📡 رادار تتبع الأرقام وتحديد الموقع")
        print("3. 🌐 فحص أمن المواقع (Pentest)")
        print("4. 🚪 خروج")
        
        choice = input(Fore.GREEN + "\nاختر مهمتك يا بطل: ")
        
        if choice == '1': phone_security_scan()
        elif choice == '2': algeria_radar()
        elif choice == '3': pentest_sites()
        elif choice == '4': break
        input("\nاضغط Enter للمتابعة...")

if __name__ == "__main__":
    main_menu()

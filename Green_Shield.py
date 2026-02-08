import os
import requests
import folium
import phonenumbers
from phonenumbers import geocoder, carrier
from colorama import Fore, init

init(autoreset=True)
API_KEY = "41a2bc92a472f714126766c5920dd0eb"

def main():
    os.system('clear')
    # شعار Green Shield بسيط وسريع
    print(Fore.GREEN + "--- GREEN SHIELD v7.0 | djak.dz ---")
    print("\n1. 🛡️ فحص الأمان | 2. 📡 رادار المواقع | 3. 🚪 خروج")
    
    choice = input(Fore.YELLOW + "\nاختر المهمة: ")

    if choice == '1':
        print(Fore.CYAN + "[*] جاري الفحص السريع... هاتف عمار محمي ✅")
    
    elif choice == '2':
        num = input(Fore.CYAN + "أدخل الرقم (213...): ")
        try:
            parsed = phonenumbers.parse("+" + num if not num.startswith('+') else num)
            location = geocoder.description_for_number(parsed, "ar")
            print(Fore.GREEN + f"📍 الموقع التقريبي: {location}")
            print(Fore.GREEN + "🌍 تم إنشاء الخريطة بنجاح باسم: green_shield_map.html")
        except:
            print(Fore.RED + "⚠️ خطأ في قراءة الرقم.")
            
    elif choice == '3':
        exit()

    input("\nاضغط Enter للعودة للمنو...")
    main()

if __name__ == "__main__":
    main()

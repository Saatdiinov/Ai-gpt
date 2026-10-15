import requests

def ask_ai(prompt):
    url = f"https://text.pollinations.ai/{requests.utils.quote(prompt)}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return "Xatolik yuz berdi."
    except Exception as e:
        return f"Tarmoqda xatolik: {e}"

print("AI GPT (Elyor va Ilhom loyihasi) ishga tushdi!")
print("Chiqish uchun 'chiqish' deb yozing.")

while True:
    user_input = input("\nSiz: ")
    if user_input.lower() == 'chiqish':
        print("Xayr!")
        break
    
    print("AI GPT o'ylamoqda...")
    answer = ask_ai(user_input)
    print(f"AI: {answer}")

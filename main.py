import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# Taqiqlangan so'zlar ro'yxati (Filtr)
FORBIDDEN_WORDS = [
    "seks", "sex", "porno", "18+", "18 +", "erotika", "xushnozi", 
    "am", "sik", "jallap", "jalap", "qotoq", "kọt", "kot"
]

class ElyorAIApp(App):
    def build(self):
        self.title = "Elyor AI"
        
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Chatingiz oynasi (Scrollview)
        self.scroll = ScrollView(size_hint=(1, 0.75))
        self.chat_history = Label(
            text="[System]: Salom Xush kelibsiz ishlar qalay men Aqlli botman men sizga yordam bereman qanday yordam kerak.\n\n",
            size_hint_y=None,
            markup=True,
            halign='left',
            valign='top'
        )
        self.chat_history.bind(texture_size=self.chat_history.setter('size'))
        self.scroll.add_widget(self.chat_history)
        main_layout.add_widget(self.scroll)
        
        # Tugmalar va matn kiritish bo'limi
        input_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.15), spacing=5)
        
        # Foto tugmasi
        btn_photo = Button(text="📷 Foto", size_hint=(0.2, 1))
        btn_photo.bind(on_press=self.send_photo)
        
        # Golos tugmasi
        btn_voice = Button(text="🎙️ Golos", size_hint=(0.2, 1))
        btn_voice.bind(on_press=self.send_voice)
        
        # Matn yozish joyi
        self.txt_input = TextInput(hint_text="Xabar yozing...", multiline=False, size_hint=(0.4, 1))
        
        # Yuborish tugmasi
        btn_send = Button(text="Jo'natish", size_hint=(0.2, 1))
        btn_send.bind(on_press=self.send_message)
        
        input_layout.add_widget(btn_photo)
        input_layout.add_widget(btn_voice)
        input_layout.add_widget(self.txt_input)
        input_layout.add_widget(btn_send)
        
        main_layout.add_widget(input_layout)
        return main_layout

    def send_message(self, instance):
        user_text = self.txt_input.text.strip()
        if not user_text:
            return
            
        # 18+ va taqiqlangan so'zlarni tekshirish
        user_text_lower = user_text.lower()
        contains_forbidden = any(word in user_text_lower for word in FORBIDDEN_WORDS)
        
        self.chat_history.text += f"[Siz]: {user_text}\n"
        self.txt_input.text = ""
        
        if contains_forbidden:
            self.chat_history.text += "[Elyor AI]: Kechirasiz, bunday (18+ / odobsiz) mazmundagi savollarga javob bera olmayman!\n\n"
        else:
            # AI javobi
            self.chat_history.text += f"[Elyor AI]: Sizning xabaringiz qabul qilindi: '{user_text}'. Sizga qanday yordam bera olaman?\n\n"

    def send_photo(self, instance):
        self.chat_history.text += "[Siz]: 📷 Rasm yuborildi.\n"
        self.chat_history.text += "[Elyor AI]: Rasm qabul qilindi va tahlil qilinmoqda...\n\n"

    def send_voice(self, instance):
        self.chat_history.text += "[Siz]: 🎙️ Ovozli xabar yuborildi.\n"
        self.chat_history.text += "[Elyor AI]: Ovozli xabaringiz tinglanmoqda...\n\n"

if __name__ == '__main__':
    ElyorAIApp().run()

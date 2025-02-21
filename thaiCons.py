import tkinter as tk
from random import choice

# Full list of Thai consonants and their names
consonants = [
    ("ก", "gor gai"),
    ("ข", "khor khai"),
    ("ฃ", "khor khuat (obsolete)"),
    ("ค", "khor khwai"),
    ("ฅ", "khor khon (obsolete)"),
    ("ฆ", "khor ra-khang"),
    ("ง", "ngor nguu"),
    ("จ", "jor jaan"),
    ("ฉ", "chor ching"),
    ("ช", "chor chaang"),
    ("ซ", "sor so"),
    ("ฌ", "chor cher"),
    ("ญ", "yor ying"),
    ("ฎ", "dor cha-da"),
    ("ฏ", "tor pa-tak"),
    ("ฐ", "thor than"),
    ("ฑ", "thor montho"),
    ("ฒ", "thor phu-thao"),
    ("ณ", "nor nen"),
    ("ด", "dor dek"),
    ("ต", "tor tao"),
    ("ถ", "thor thung"),
    ("ท", "thor thahan"),
    ("ธ", "thor thong"),
    ("น", "nor nuu"),
    ("บ", "bor bai-mai"),
    ("ป", "por pla"),
    ("ผ", "phor phueng"),
    ("ฝ", "for faa"),
    ("พ", "phor phaan"),
    ("ฟ", "for fan"),
    ("ภ", "phor sam-phao"),
    ("ม", "mor maa"),
    ("ย", "yor yak"),
    ("ร", "ror rua"),
    ("ล", "lor ling"),
    ("ว", "wor waaen"),
    ("ศ", "sor saa-laa"),
    ("ษ", "sor ruu-si"),
    ("ส", "sor suea"),
    ("ห", "hor hiip"),
    ("ฬ", "lor chu-laa"),
    ("อ", "or aang"),
    ("ฮ", "hor nok-huk")
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.card_frame = tk.Frame(root, width=300, height=200, bg="white", relief="raised", bd=2)
        self.card_frame.pack(pady=20)
        
        self.card_label = tk.Label(self.card_frame, text="", font=("Arial", 40), bg="white")
        self.card_label.pack(expand=True)
        
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card)
        self.flip_button.pack(side="left", padx=10)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack(side="right", padx=10)
        
        self.is_flipped = False
        self.current_card = None
        
        self.next_card()
    
    def next_card(self):
        self.current_card = choice(consonants)
        self.card_label.config(text=self.current_card[0])
        self.is_flipped = False
    
    def flip_card(self):
        if self.is_flipped:
            self.card_label.config(text=self.current_card[0])
        else:
            self.card_label.config(text=self.current_card[1])
        self.is_flipped = not self.is_flipped

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()

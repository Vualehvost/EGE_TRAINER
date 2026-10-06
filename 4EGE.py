import tkinter as tk
import json
import os
import random
 
# ============================================================
# ПОЛНЫЙ ОРФОЭПИЧЕСКИЙ СЛОВНИК ФИПИ (ЕГЭ 2025)
# ============================================================
FIPI_WORDS = {
    "существительные": {
        "аэропОрты": "аэропорты",
        "бАнты": "банты",
        "бОроду": "бороду",
        "бухгАлтеров": "бухгалтеров",
        "вероисповЕдание": "вероисповедание",
        "водопровОд": "водопровод",
        "газопровОд": "газопровод",
        "граждАнство": "гражданство",
        "дефИс": "дефис",
        "дешевИзна": "дешевизна",
        "диспансЕр": "диспансер",
        "договорЁнность": "договоренность",
        "докумЕнт": "документ",
        "досУг": "досуг",
        "еретИк": "еретик",
        "жалюзИ": "жалюзи",
        "знАчимость": "значимость",
        "Иксы": "иксы",
        "каталОг": "каталог",
        "квартАл": "квартал",
        "киломЕтр": "километр",
        "кОнусов": "конусов",
        "корЫсть": "корысть",
        "крАны": "краны",
        "кремЕнь": "кремень",
        "кремнЯ": "кремня",
        "лЕкторов": "лекторов",
        "лОктя": "локтя",
        "локтЕй": "локтей",
        "лыжнЯ": "лыжня",
        "мЕстностей": "местностей",
        "намЕрение": "намерение",
        "нарОст": "нарост",
        "нЕдруг": "недруг",
        "недУг": "недуг",
        "некролОг": "некролог",
        "нЕнависть": "ненависть",
        "нефтепровОд": "нефтепровод",
        "новостЕй": "новостей",
        "нОгтя": "ногтя",
        "ногтЕй": "ногтей",
        "Отрочество": "отрочество",
        "партЕр": "партер",
        "портфЕль": "портфель",
        "пОручни": "поручни",
        "придАное": "приданое",
        "призЫв": "призыв",
        "свЁкла": "свекла",
        "сирОты": "сироты",
        "созЫв": "созыв",
        "сосредотОчение": "сосредоточение",
        "срЕдства": "средства",
        "стАтуя": "статуя",
        "столЯр": "столяр",
        "тамОжня": "таможня",
        "тОрты": "торты",
        "тУфля": "туфля",
        "цемЕнт": "цемент",
        "цЕнтнер": "центнер",
        "цепОчка": "цепочка",
        "шАрфы": "шарфы",
        "шофЁр": "шофер",
        "экспЕрт": "эксперт",
    },
    "прилагательные": {
        "вернА": "верна",
        "знАчимый": "значимый",
        "красИвее": "красивее",
        "красИвейший": "красивейший",
        "кУхонный": "кухонный",
        "ловкА": "ловка",
        "мозаИчный": "мозаичный",
        "оптОвый": "оптовый",
        "прозорлИвый": "прозорливый",
        "прозорлИва": "прозорлива",
        "слИвовый": "сливовый",
    },
    "глаголы": {
        "бралА": "брала",
        "бралАсь": "бралась",
        "взялА": "взяла",
        "взялАсь": "взялась",
        "влилАсь": "влилась",
        "ворвалАсь": "ворвалась",
        "воспринЯть": "воспринять",
        "воспринялА": "восприняла",
        "воссоздалА": "воссоздала",
        "вручИт": "вручит",
        "гналА": "гнала",
        "гналАсь": "гналась",
        "добралА": "добрала",
        "добралАсь": "добралась",
        "дождалАсь": "дождалась",
        "дозвонИтся": "дозвонится",
        "дозИровать": "дозировать",
        "ждалА": "ждала",
        "жилОсь": "жилось",
        "закУпорить": "закупорить",
        "занЯть": "занять",
        "зАнял": "занял",
        "занялА": "заняла",
        "зАняли": "заняли",
        "заперлА": "заперла",
        "запломбировАть": "запломбировать",
        "защемИт": "защемит",
        "звалА": "звала",
        "звонИт": "звонит",
        "кАшлянуть": "кашлянуть",
        "клАла": "клала",
        "клЕить": "клеить",
        "крАлась": "кралась",
        "кровоточИть": "кровоточить",
        "лгалА": "лгала",
        "лилА": "лила",
        "лилАсь": "лилась",
        "навралА": "наврала",
        "наделИт": "наделит",
        "надорвалАсь": "надорвалась",
        "назвалАсь": "назвалась",
        "накренИтся": "накренится",
        "налилА": "налила",
        "нарвалА": "нарвала",
        "начАть": "начать",
        "нАчал": "начал",
        "началА": "начала",
        "нАчали": "начали",
        "обзвонИт": "обзвонит",
        "облегчИть": "облегчить",
        "облегчИт": "облегчит",
        "облилАсь": "облилась",
        "обнялАсь": "обнялась",
        "обогналА": "обогнала",
        "ободралА": "ободрала",
        "ободрИть": "ободрить",
        "ободрИт": "ободрит",
        "ободрИться": "ободриться",
        "ободрИтся": "ободрится",
        "обострИть": "обострить",
        "одолжИть": "одолжить",
        "одолжИт": "одолжит",
        "озлОбить": "озлобить",
        "оклЕить": "оклеить",
        "окружИт": "окружит",
        "опОшлить": "опошлить",
        "освЕдомиться": "осведомиться",
        "освЕдомится": "осведомится",
        "отбылА": "отбыла",
        "отдалА": "отдала",
        "откУпорить": "откупорить",
        "отозвалА": "отозвала",
        "отозвалАсь": "отозвалась",
        "перезвонИт": "перезвонит",
        "перелилА": "перелила",
        "плодоносИть": "плодоносить",
        "пломбировАть": "пломбировать",
        "повторИт": "повторит",
        "позвалА": "позвала",
        "позвонИт": "позвонит",
        "полилА": "полила",
        "положИть": "положить",
        "положИл": "положил",
        "понЯть": "понять",
        "понялА": "поняла",
        "послАла": "послала",
        "прибЫть": "прибыть",
        "прИбыл": "прибыл",
        "прибылА": "прибыла",
        "прИбыли": "прибыли",
        "принЯть": "принять",
        "прИнял": "принял",
        "принялА": "приняла",
        "прИняли": "приняли",
        "рвалА": "рвала",
        "сверлИт": "сверлит",
        "снялА": "сняла",
        "совралА": "соврала",
        "создалА": "создала",
        "сорвалА": "сорвала",
        "сорИт": "сорит",
        "убралА": "убрала",
        "углубИть": "углубить",
        "укрепИт": "укрепит",
        "чЕрпать": "черпать",
        "щемИт": "щемит",
        "щЁлкать": "щелкать",
    },
    "причастия": {
        "довезЁнный": "довезенный",
        "зАгнутый": "загнутый",
        "зАнятый": "занятый",
        "занятА": "занята",
        "зАпертый": "запертый",
        "заселЁнный": "заселённый",
        "заселенА": "заселена",
        "кормЯщий": "кормящий",
        "кровоточАщий": "кровоточащий",
        "нажИвший": "наживший",
        "налИвший": "наливший",
        "нанЯвшийся": "нанявшийся",
        "начАвший": "начавший",
        "нАчатый": "начатый",
        "низведЁнный": "низведенный",
        "облегчЁнный": "облегченный",
        "ободрЁнный": "ободренный",
        "обострЁнный": "обостренный",
        "отключЁнный": "отключенный",
        "повторЁнный": "повторенный",
        "поделЁнный": "поделенный",
        "понЯвший": "понявший",
        "прИнятый": "принятый",
        "принятА": "принята",
        "приручЁнный": "прирученный",
        "прожИвший": "проживший",
        "снятА": "снята",
        "сОгнутый": "согнутый",
        "углублЁнный": "углублённый",
    },
    "деепричастия": {
        "закУпорив": "закупорив",
        "начАв": "начав",
        "начАвшись": "начавшись",
        "отдАв": "отдав",
        "поднЯв": "подняв",
        "понЯв": "поняв",
        "прибЫв": "прибыв",
        "создАв": "создав",
    },
    "наречия": {
        "вОвремя": "вовремя",
        "дОверху": "доверху",
        "донЕльзя": "донельзя",
        "дОнизу": "донизу",
        "дОсуха": "досуха",
        "зАсветло": "засветло",
        "зАтемно": "затемно",
        "красИвее": "красивее",
        "надОлго": "надолго",
        "ненадОлго": "ненадолго",
    },
}

# ============================================================
# ПРИЛОЖЕНИЕ
# ============================================================
class StressTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ударения ЕГЭ – полный словник ФИПИ")
        self.root.geometry("1200x700")

        self.mistakes_file = "mistakes.json"
        self.mistakes = self.load_mistakes()

        self.mode = "all"
        self.part_filter = "существительные"
        self.current_words = []
        self.current_index = 0
        self.score = 0
        self.total_in_session = 0

        self.setup_menu()
        self.setup_ui()

        self.prepare_word_list()
        self.show_current_word()

    # --------------------------------------------------------
    def load_mistakes(self):
        if os.path.exists(self.mistakes_file):
            with open(self.mistakes_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_mistakes(self):
        with open(self.mistakes_file, "w", encoding="utf-8") as f:
            json.dump(self.mistakes, f, ensure_ascii=False, indent=2)

    def add_mistake(self, stressed_word, normal_word):
        if stressed_word not in self.mistakes:
            for part, words in FIPI_WORDS.items():
                if stressed_word in words:
                    self.mistakes[stressed_word] = {
                        "normal": normal_word,
                        "part": part
                    }
                    self.save_mistakes()
                    return

    def remove_mistake(self, stressed_word):
        if stressed_word in self.mistakes:
            del self.mistakes[stressed_word]
            self.save_mistakes()

    # --------------------------------------------------------
    def setup_menu(self):
        menu_frame = tk.Frame(self.root, bg="#f0f0f0")
        menu_frame.pack(fill="x", pady=10)

        tk.Label(menu_frame, text="Режим:", font=("Arial", 12),
                  bg="#f0f0f0").pack(side="left", padx=(20, 5))

        self.btn_all = tk.Button(
            menu_frame, text="Все слова",
            command=lambda: self.change_mode("all"),
            font=("Arial", 11), bg="#4CAF50", fg="white"
        )
        self.btn_all.pack(side="left", padx=2)

        self.btn_mistakes = tk.Button(
            menu_frame, text=f"Только ошибки ({len(self.mistakes)})",
            command=lambda: self.change_mode("mistakes"),
            font=("Arial", 11), bg="#FF9800", fg="white"
        )
        self.btn_mistakes.pack(side="left", padx=2)

        # Все части речи из обновлённого словаря
        parts = list(FIPI_WORDS.keys())
        self.part_var = tk.StringVar(value=parts[0])
        self.part_menu = tk.OptionMenu(
            menu_frame, self.part_var, *parts,
            command=lambda _: self.change_mode("part")
        )
        self.part_menu.configure(font=("Arial", 11))
        self.part_menu.pack(side="left", padx=10)

        tk.Button(
            menu_frame, text="По части речи",
            command=lambda: self.change_mode("part"),
            font=("Arial", 11), bg="#2196F3", fg="white"
        ).pack(side="left", padx=2)

    def change_mode(self, mode):
        self.mode = mode
        self.prepare_word_list()
        self.current_index = 0
        self.score = 0
        self.total_in_session = 0
        self.stats_label.configure(text="Правильно: 0/0")
        self.show_current_word()

        for btn in [self.btn_all, self.btn_mistakes]:
            btn.configure(bg="#4CAF50" if btn == self.btn_all else "#FF9800")

    # --------------------------------------------------------
    def prepare_word_list(self):
        words = []
        if self.mode == "all":
            for part, part_words in FIPI_WORDS.items():
                for stressed, normal in part_words.items():
                    words.append((stressed, normal, part))
        elif self.mode == "mistakes":
            for stressed, info in self.mistakes.items():
                words.append((stressed, info["normal"], info["part"]))
        elif self.mode == "part":
            part = self.part_var.get()
            for stressed, normal in FIPI_WORDS[part].items():
                words.append((stressed, normal, part))

        random.shuffle(words)
        self.current_words = words

    # --------------------------------------------------------
    def setup_ui(self):
        self.stats_label = tk.Label(
            self.root, text="Правильно: 0/0",
            font=("Arial", 14), bg="#f0f0f0"
        )
        self.stats_label.pack(pady=10)

        self.counter_label = tk.Label(
            self.root, text="", font=("Arial", 12),
            bg="#f0f0f0", fg="#666"
        )
        self.counter_label.pack()

        self.letters_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.letters_frame.pack(pady=40)

        self.result_label = tk.Label(
            self.root, text="", font=("Arial", 14), bg="#f0f0f0"
        )
        self.result_label.pack(pady=10)

        self.next_btn = tk.Button(
            self.root, text="Следующее слово →",
            command=self.next_word, font=("Arial", 12),
            state="disabled", bg="#4CAF50", fg="white"
        )
        self.next_btn.pack(pady=10)

        self.letter_widgets = []

    # --------------------------------------------------------
    def find_stress_position(self, stressed_word):
        for i, ch in enumerate(stressed_word):
            if ch.isupper():
                return i
        return 0

    def show_current_word(self):
        for w in self.letter_widgets:
            w.destroy()
        self.letter_widgets.clear()

        if self.current_index < len(self.current_words):
            stressed, normal, part = self.current_words[self.current_index]
            self.correct_position = self.find_stress_position(stressed)

            self.counter_label.configure(
                text=f"Слово {self.current_index+1} из {len(self.current_words)} ({part})"
            )
            self.result_label.configure(text="")
            self.next_btn.configure(state="disabled")

            for i, letter in enumerate(normal):
                is_vowel = letter.lower() in "аеёиоуыэюя"
                btn = tk.Label(
                    self.letters_frame,
                    text=letter.upper(),
                    font=("Arial", 36, "bold"),
                    width=2,
                    bg="white" if is_vowel else "#e0e0e0",
                    relief="raised" if is_vowel else "flat",
                    cursor="hand2" if is_vowel else ""
                )
                if is_vowel:
                    btn.bind("<Button-1>", lambda e, pos=i: self.check_answer(pos))
                    btn.bind("<Enter>", lambda e, w=btn: w.configure(bg="#e3f2fd"))
                    btn.bind("<Leave>", lambda e, w=btn: w.configure(bg="white"))
                btn.pack(side="left", padx=2)
                self.letter_widgets.append(btn)
        else:
            self.show_session_results()

    def check_answer(self, selected_pos):
        stressed, normal, part = self.current_words[self.current_index]
        correct = (selected_pos == self.correct_position)

        for i, w in enumerate(self.letter_widgets):
            if i == self.correct_position:
                w.configure(bg="#4CAF50", fg="white")
            elif i == selected_pos and not correct:
                w.configure(bg="#f44336", fg="white")
            if w.cget("cursor") == "hand2":
                w.unbind("<Button-1>")
                w.unbind("<Enter>")
                w.unbind("<Leave>")
                w.configure(cursor="")

        if correct:
            self.score += 1
            self.result_label.configure(text="Правильно!", fg="green")
            self.remove_mistake(stressed)
        else:
            self.result_label.configure(
                text=f"Ошибка! Ударная буква: {stressed[self.correct_position]}",
                fg="red"
            )
            self.add_mistake(stressed, normal)

        self.total_in_session += 1
        self.stats_label.configure(text=f"Правильно: {self.score}/{self.total_in_session}")
        self.next_btn.configure(state="normal")
        self.btn_mistakes.configure(text=f"Только ошибки ({len(self.mistakes)})")

    def next_word(self):
        self.current_index += 1
        self.show_current_word()

    def show_session_results(self):
        for w in self.letter_widgets:
            w.destroy()
        self.letter_widgets.clear()

        self.counter_label.configure(text="")
        self.result_label.configure(text="")
        self.next_btn.configure(state="disabled")

        pct = (self.score / self.total_in_session * 100) if self.total_in_session else 0
        tk.Label(
            self.letters_frame,
            text=f"Раунд завершён!\n{self.score} из {self.total_in_session} ({pct:.1f}%)",
            font=("Arial", 18), bg="#f0f0f0", justify="center"
        ).pack()

        tk.Button(
            self.letters_frame,
            text="Начать заново",
            command=self.restart_session,
            font=("Arial", 12), bg="#4CAF50", fg="white"
        ).pack(pady=20)

    def restart_session(self):
        self.prepare_word_list()
        self.current_index = 0
        self.score = 0
        self.total_in_session = 0
        self.stats_label.configure(text="Правильно: 0/0")
        for w in self.letters_frame.winfo_children():
            w.destroy()
        self.letter_widgets.clear()
        self.show_current_word()


if __name__ == "__main__":
    root = tk.Tk()
    app = StressTestApp(root)
    root.mainloop()

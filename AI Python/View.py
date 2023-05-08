import tkinter as tk
from PIL import Image
from Model import *

class ChatbotApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bicker Dawg")
        self.root.geometry("500x600")
        self.root.configure(background="#394D5F")

        self.header_bg_color = "#128C7E"
        self.header_fg_color = "white"
        self.message_font = ("Helvetica", 12)

        # Bot and user chat windows
        self.chat_frame = tk.Frame(self.root, bg="#394D5F")
        self.chat_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.bot_chat_window = tk.Frame(self.chat_frame, borderwidth=0, highlightthickness=0, highlightbackground="#DDD", bg="#394D5F")
        self.bot_chat_window.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.user_chat_window = tk.Frame(self.chat_frame, borderwidth=0, highlightthickness=0, highlightbackground="#DDD", bg="#394D5F")
        self.user_chat_window.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Input field and send button
        self.input_frame = tk.Frame(self.root, bg="#394D5F")
        self.input_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        self.input_field = tk.Entry(self.input_frame, width=40, font=self.message_font, bg="#4A6F89", fg="white")
        self.input_field.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X, expand=True)

        self.send_button = tk.Button(self.input_frame, text="Send", font=self.message_font, bg=self.header_bg_color, fg=self.header_fg_color, command=self.handle_input)
        self.send_button.pack(side=tk.RIGHT, padx=(0, 10))

    def handle_input(self):
        user_input = self.input_field.get()
        bot_response = bot.get_response(user_input)

        self.user_chat_window.configure(highlightbackground="#DDD")
        self.user_chat_window.pack_configure(pady=(20, 0))
  
        user_message_frame = tk.Frame(self.user_chat_window, borderwidth=0, highlightthickness=3, highlightbackground="#DDD", relief="groove", bg="#ECE5DD")
        user_message_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=(0, 10), anchor=tk.NE)

        user_message_label = tk.Label(user_message_frame, text=user_input, font=self.message_font, bg="#ECE5DD", fg="black", wraplength=200, justify="right", padx=10, pady=5)
        user_message_label.pack(side=tk.LEFT)

        self.bot_chat_window.configure(highlightbackground="#DDD")
        self.bot_chat_window.pack_configure(pady=(20, 0))

        bot_message_frame = tk.Frame(self.bot_chat_window, borderwidth=0, highlightthickness=3, highlightbackground="#DDD", relief="groove", bg="#5B8DB0")
        bot_message_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=(10, 10), anchor=tk.NW)

        bot_message_label = tk.Label(bot_message_frame, text="...", font=self.message_font, bg="#5B8DB0", fg="white", wraplength=200, justify="left", padx=10, pady=5)
        bot_message_label.pack(side=tk.LEFT)

        self.input_field.delete(0, tk.END)

        self.root.after(1000, lambda: self.display_bot_response(bot_response, bot_message_label))


    def display_bot_response(self, bot_response, bot_message_label):
        bot_message_label.config(text=bot_response)
        

    def run(self):
        self.root.mainloop()

chatbot_app = ChatbotApp()
chatbot_app.run();
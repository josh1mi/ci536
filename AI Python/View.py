import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from PIL import ImageGrab
from PIL import ImageFilter
from Model import ChatbotModel

class ChatbotApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bicker Bot")
        self.root.geometry("500x600")
        self.root.configure(background="#F0F0F0")  # Light gray background

        self.header_bg_color = "#075E54"  # WhatsApp header color
        self.header_fg_color = "white"
        self.message_font = ("Helvetica", 12)
        self.user_message_color = "#DCF8C6"  # Light green color for user messages
        self.bot_message_color = "white"  # White color for bot messages

        # Chat window
        self.chat_frame = tk.Frame(self.root, bg="#F0F0F0", borderwidth=0, highlightthickness=0)
        self.chat_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create a styled frame with border and drop shadow effect
        self.chat_window = ttk.Frame(
            self.chat_frame,
            style="MessageFrame.TFrame",  # Added style
            padding=(10, 10, 0, 0),  # Adjust padding as needed
        )
        self.chat_window.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add scrollbar to the chat window
        scrollbar = tk.Scrollbar(self.chat_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.user_listbox = tk.Listbox(
            self.chat_window,
            bg="#ECECEC",  # Light background color
            font=self.message_font,
            relief="flat",
            yscrollcommand=scrollbar.set  # Connect scrollbar to the listbox
        )
        self.user_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.bot_listbox = tk.Listbox(
            self.chat_window,
            bg="#ECECEC",  # Light background color
            font=self.message_font,
            relief="flat",
            yscrollcommand=scrollbar.set  # Connect scrollbar to the listbox
        )
        self.bot_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.user_listbox.yview)  # Configure scrollbar with user listbox

        # Input field and send button
        self.input_frame = tk.Frame(self.root, bg="#F0F0F0", borderwidth=0, highlightthickness=0)
        self.input_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.input_field = tk.Entry(
            self.input_frame,
            width=40,
            font=self.message_font,
            bg="white",  # White input field background
            fg="black",  # Black text color
            relief="flat",
            justify="right",  # Align text to the right
        )
        self.input_field.pack(side=tk.LEFT, padx=(10, 0), fill=tk.X, expand=True)

        self.root.sendIcon = tk.PhotoImage(file="AI Python/sendIcon.png")
        self.root.sendIcon = self.root.sendIcon.subsample(15)

        # Remove green arrow background by setting green pixels to transparent
        transparent_icon = self.remove_green_background(self.root.sendIcon)

        self.send_button = tk.Button(
            self.input_frame,
            image=transparent_icon,
            compound=tk.LEFT,
            bg="white",  # Set the background color to white
            fg="black",  # Set the text color to black
            command=self.handle_input,
            relief="flat",
            bd=0,
        )
        self.send_button.image = transparent_icon  # Store a reference to the image to prevent garbage collection
        self.send_button.pack(side=tk.RIGHT, padx=(0, 10))

        self.last_displayed_user_message = None
        self.last_displayed_bot_response = None

        # Create a ttk style for the chat window frames
        style = ttk.Style()
        style.configure(
            "MessageFrame.TFrame",
            background="#ECECEC",  # Light background color
            borderwidth=0,
            relief="flat",
        )

        # Apply drop shadow effect and drop border to the chat window
        self.add_drop_shadow_effect(self.chat_window)

        # Apply drop border effect to the input field
        self.input_field.config(borderwidth=2, relief="groove")

        # Apply WhatsApp theme to chat messages
        self.apply_whatsapp_theme()

    def remove_green_background(self, image):
        # Convert PhotoImage to PIL Image
        pil_image = ImageTk.getimage(image)

        # Convert the image to RGBA mode
        pil_image = pil_image.convert("RGBA")

        # Get the pixel data
        icon_data = pil_image.getdata()

        # Remove green background by setting green pixels to transparent
        transparent_data = [
            (r, g, b, 0) if (r, g, b) == (0, 255, 0) else (r, g, b, a)
            for r, g, b, a in icon_data
        ]

        # Create a new PIL Image with the transparent data
        transparent_image = Image.new("RGBA", pil_image.size)
        transparent_image.putdata(transparent_data)

        # Convert the PIL Image back to PhotoImage
        transparent_icon = ImageTk.PhotoImage(transparent_image)

        return transparent_icon

    def add_drop_shadow_effect(self, widget):
        shadow_canvas = tk.Canvas(
            widget,
            width=widget.winfo_width(),
            height=widget.winfo_height(),
            background="white",
            highlightthickness=0,
        )
        shadow_canvas.place(in_=widget, anchor="nw", bordermode="outside")

        # Create drop shadow effect using a blurred image
        blurred_image = self.create_blurred_image(widget)

        shadow_canvas.create_image(
            2, 2, anchor="nw", image=blurred_image
        )

        # Raise the widget to the top
        widget.lift(shadow_canvas)

        # Add a drop border effect to the widget
        widget.config(borderwidth=2, relief="groove")

    def create_blurred_image(self, widget):
        x, y, width, height = widget.winfo_rootx(), widget.winfo_rooty(), widget.winfo_width(), widget.winfo_height()
        image = ImageGrab.grab((x, y, x + width, y + height))
        image = image.convert("RGBA")  # Convert image to RGBA mode for transparency
        blurred_image = image.filter(ImageFilter.BLUR)
        return ImageTk.PhotoImage(blurred_image)

    def apply_whatsapp_theme(self):
        self.user_listbox.config(bg="#ECECEC", fg="black")
        self.bot_listbox.config(bg="#ECECEC", fg="black")
        self.input_field.config(bg="#F0F0F0", fg="black")
        self.send_button.config(bg="#F0F0F0", fg="black")

    def display_user_message(self, message):
        self.user_listbox.insert(tk.END, message)  # Remove the newline character at the end of the message
        self.user_listbox.itemconfig(tk.END, bg=self.user_message_color, fg="black")  # Set message color
        self.user_listbox.see(tk.END)  # Scroll to the latest message

    def display_bot_response(self, message):
       self.bot_listbox.insert(tk.END, message)  # Remove the newline character at the end of the message
       self.bot_listbox.itemconfig(tk.END, bg=self.bot_message_color, fg="black")  # Set message color
       self.bot_listbox.see(tk.END)  # Scroll to the latest message

    def handle_input(self):
        user_input = self.input_field.get()
        bot_response = bot.get_response(user_input)

        self.display_user_message(f"{user_input}")
        self.display_bot_response(f"{bot_response}")

        self.input_field.delete(0, tk.END)

    def run(self):
        self.root.mainloop()

    def bind_enter_key(self):
        self.input_field.bind("<Return>", lambda event: self.handle_input())


if __name__ == "__main__":
    bot = ChatbotModel()
    chatbot_app = ChatbotApp()
    chatbot_app.bind_enter_key()
    chatbot_app.run()

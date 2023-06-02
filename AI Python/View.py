import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from PIL import ImageGrab
from PIL import ImageFilter
from Model import ChatbotModel

class ChatbotApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BickerBot")
        self.root.geometry("500x900")
        self.root.configure(background="#d5896f")  # Light gray background

        self.header_bg_color = "#075E54"  # Header color
        self.header_fg_color = "white"
        self.message_font = ("Helvetica", 12)

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

        # Input field and send button
        self.input_frame = tk.Frame(self.root, bg="#F0F0F0", borderwidth=0, highlightthickness=0)
        self.input_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.input_field = tk.Entry(
            self.input_frame,
            width=40,
            font=self.message_font,
            bg="#ffffff",  # White input field background
            fg="#000000",  # Black text color
            relief="flat",
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
            background="#ffffff",  # Light background color
            borderwidth=0,
            relief="flat",
        )

        # Apply drop shadow effect and drop border to the chat window
        self.add_drop_shadow_effect(self.chat_window)

        # Apply drop border to the input field
        self.input_field.config(borderwidth=2, relief="groove")

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

    def display_user_message(self, message):
        message_frame = ttk.Frame(
            self.chat_window,
            style="MessageFrame.TFrame",  # Added style
            padding=(10, 5, 20, 5),  # Adjusted padding
        )
        message_frame.pack(side=tk.TOP, fill=tk.BOTH, anchor=tk.NE)  # Anchor to the top-right

        message_label = tk.Label(
            message_frame,
            text=message,
            font=self.message_font,
            bg="#dcdfe2",
            fg="#000000",
            wraplength=360,
            justify="left",  # Align the text to the right
            padx=10,  # Add padding inside the text bubble (left padding decreased)
            pady=20,  # Add padding inside the text bubble
            bd=5,  # Add a border around the text bubble
            relief=tk.SOLID,  # Set the border style to solid
            borderwidth=0,  # Set the border width
            highlightthickness=0,  # Remove the highlight thickness
            highlightbackground="#DCF8C6",  # Set the highlight background color to match the text bubble background
            highlightcolor="#DCF8C6"  # Set the highlight color to match the text bubble background
        )
        message_label.pack(side=tk.RIGHT)  # Pack the label to the right side

        if self.last_displayed_bot_response:
            self.last_displayed_bot_response.pack_configure(pady=5)

        self.last_displayed_user_message = message_frame

    def display_bot_response(self, message):
        message_frame = ttk.Frame(
            self.chat_window,
            style="MessageFrame.TFrame",  # Added style
            padding=(10, 5, 0, 5),  # Adjusted padding
        )
        message_frame.pack(side=tk.TOP, fill=tk.BOTH, anchor=tk.NE)

        message_label = tk.Label(
            message_frame,
            text=message,
            font=self.message_font,
            bg="#387ab2",
            fg="#ffffff",
            wraplength=360,
            justify="left",
            padx=10,  # Add padding inside the text bubble
            pady=20,  # Add padding inside the text bubble
            bd=5,  # Add a border around the text bubble
            relief=tk.SOLID,  # Set the border style to solid
            borderwidth=0,  # Set the border width
            highlightthickness=0,  # Remove the highlight thickness
            highlightbackground="white",  # Set the highlight background color to match the text bubble background
            highlightcolor="white"  # Set the highlight color to match the text bubble background
        )
        message_label.pack(side=tk.LEFT)

        if self.last_displayed_user_message:
            self.last_displayed_user_message.pack_configure(pady=5)

        self.last_displayed_bot_response = message_frame

    def handle_input(self):
        user_input = self.input_field.get()
        bot_response = bot.get_response(user_input)

        if (user_input == 'Log in'):
            def login():
                customer_id = customer_id_entry.get()
                password = password_entry.get()

                if customer_id == "admin" and password == "password":
                    result_label.config(text="Login successful!", fg="green")
                else:
                    result_label.config(text="Login failed. Invalid credentials.", fg="red")

            branch = tk.Tk()
            branch.title('Login Window')

            customer_id_label = tk.Label(branch, text="Customer ID:")
            customer_id_label.pack()

            customer_id_entry = tk.Entry(branch)
            customer_id_entry.pack()

            password_label = tk.Label(branch, text="Password:")
            password_label.pack()

            password_entry = tk.Entry(branch, show="*")  # Show asterisks instead of the actual password
            password_entry.pack()

            login_button = tk.Button(branch, text="Login", command=login)
            login_button.pack()

            result_label = tk.Label(branch, text="")
            result_label.pack()

            branch.mainloop()

        self.display_user_message(f"{user_input}")
        self.display_bot_response(f"{bot_response}")

        self.input_field.delete(0, tk.END)

    def run(self):
        initial_message = bot.get_response('INITIALMESSAGE')
        self.display_bot_response(initial_message)

        self.root.mainloop()

    def bind_enter_key(self):
        self.input_field.bind("<Return>", lambda event: self.handle_input())


if __name__ == "__main__":
    bot = ChatbotModel()
    chatbot_app = ChatbotApp()
    chatbot_app.bind_enter_key()
    chatbot_app.run()

    chatbot_app.display_bot_response()
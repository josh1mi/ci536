import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="BickerBot"):
    dpg.add_text("Hello, how can I help you?")
    dpg.add_input_text(label="", default_value="Enter text here...")
    dpg.add_button(label="Send")

dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
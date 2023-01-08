import dearpygui.dearpygui as dpg

dpg.create_context()

def cb():
    dpg.set_value("test",dpg.get_value("testing"))

with dpg.window(label="Tutorial"):
    dpg.add_input_text(tag="testing")
    dpg.add_button(label="click",callback=cb)
    dpg.add_text("",tag="test")

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
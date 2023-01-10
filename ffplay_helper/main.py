'''
'-x width'        强制以 "width" 宽度显示
'-y height'       强制以 "height" 高度显示
'-an'             禁止音频
'-vn'             禁止视频
'-ss pos'         跳转到指定的位置(秒)
'-nodisp'         禁止图像显示(只输出音频)
'-window_title title'  设置窗口标题(默认为输入文件名)
'-loop number'    循环播放 "number" 次(0将一直循环)
'-showmode mode'  设置显示模式
可选的 mode ：
'0, video'    显示视频
'1, waves'    显示音频波形
'2, rdft'     显示音频频带
默认值为 'video'，你可以在播放进行时，按 "w" 键在这几种模式间切换
'-i input_file'   指定输入文件
'''
import os
import dearpygui.dearpygui as dpg

dpg.create_context()

# 数据
ffplay_dict = {"path":[True,""]}
running_ins = " "

# 运行
def run_ffplay():
	global running_ins
	os.system(running_ins)

# 字体
with dpg.font_registry():
	#with dpg.font("font.otf", 20) as default_font:
	with dpg.font("font.ttf", 17) as default_font:
		dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
		dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)

# 文件选择
def file_path_get(sender, app_data):
	global ffplay_dict
	ffplay_dict["path"][1] = app_data['file_path_name']
	#print(ffplay_dict)
	dpg.set_value("file_show",value=ffplay_dict["path"][1])
with dpg.file_dialog(directory_selector=False, show=False,callback=file_path_get, tag="file_dialog"):
	dpg.add_file_extension(".avi")
	dpg.add_file_extension(".wmv")
	dpg.add_file_extension(".mpeg")
	dpg.add_file_extension(".mp4")
	dpg.add_file_extension(".m4v")
	dpg.add_file_extension(".mov")
	dpg.add_file_extension(".flv")
	dpg.add_file_extension(".wav")
	dpg.add_file_extension(".mp3")
	dpg.add_file_extension(".ogg")
	dpg.add_file_extension(".flac")
	dpg.add_file_extension(".aac")


# 主界面
with dpg.window(label="ffplay helper",tag="Primary Window",width=367,height=500,no_close=True,no_collapse=True):
	dpg.add_button(label='键盘操作指南',tag='keytip')
	with dpg.tooltip("keytip"):
		dpg.add_text(
"""
'q, ESC'            退出
'f'                 全屏
'p, SPC'            暂停
'w'                 切换显示模式(视频/音频波形/音频频带)
's'                 步进到下一帧
'left/right'        快退/快进 10 秒
'down/up'           快退/快进 1 分钟
'page down/page up' 跳转到前一章/下一章(如果没有章节，快退/快进 10 分钟)
'mouse click'       跳转到鼠标点击的位置(根据鼠标在显示窗口点击的位置计算百分比)			
""")
	dpg.add_text("-------------------------")
	with dpg.group() as file_path_group:
		dpg.add_button(label="选择文件", callback=lambda:dpg.show_item("file_dialog"))
		dpg.add_text("无文件",tag="file_show")
	
	dpg.add_text("-------------------------")

	# 选项
	with dpg.group():
		dpg.add_checkbox(label="强制显示宽度",tag="s_x")
		dpg.add_input_int(label="^ 宽度",tag="s_width")
		dpg.add_text("-----")
		dpg.add_checkbox(label="强制显示高度",tag="s_y")
		dpg.add_input_int(label="^ 高度",tag="s_height")
		dpg.add_text("-----")
		dpg.add_checkbox(label="禁止音频",tag="s_an")
		dpg.add_text("-----")
		dpg.add_checkbox(label="禁止视频",tag="s_vn")
		dpg.add_text("-----")
		dpg.add_checkbox(label="跳转到指定的位置(秒)",tag="s_ss")
		dpg.add_input_float(label="^ 位置",tag="s_pos")
		dpg.add_text("-----")
		dpg.add_checkbox(label="禁止图像显示(只输出音频)",tag="-nodisp")
		dpg.add_text("-----")
		dpg.add_checkbox(label="设置窗口标题(默认为输入文件名)",tag="s_window_title")
		dpg.add_input_text(label="^ 窗口标题",tag="s_title")
		dpg.add_text("-----")
		dpg.add_checkbox(label="循环播放___次(0将一直循环)",tag="s_loop")
		s_number=dpg.add_input_int(label="^ 循环次数",tag="s_number",default_value=0)
		dpg.add_text("-----")
		dpg.add_checkbox(label="设置显示模式",tag="s_showmode")
		dpg.add_input_int(label="^ 模式",tag="s_mode")

	dpg.add_text("-------------------------")

	# 导出/运行
	with dpg.group():
		dpg.add_text("指令：")
		dpg.add_text("...",tag="output")
		dpg.add_button(label="运行", callback=run_ffplay)
	



dpg.bind_font(default_font)

dpg.create_viewport(title='ffplay helper',width=367,height=600)
dpg.setup_dearpygui()
dpg.show_viewport()

while dpg.is_dearpygui_running():
	# 生成
	error = False

	running_ins = "ffplay "

	if dpg.get_value("s_x") == True:
		running_ins += "-x " + str(dpg.get_value("s_width")) + " "

	if dpg.get_value("s_y") == True:
		running_ins += "-y " + str(dpg.get_value("s_height")) + " "

	if dpg.get_value("s_an") == True:
		running_ins += "-an "

	if dpg.get_value("s_vn") == True:
		running_ins += "-vn "

	if dpg.get_value("s_ss") == True:
		running_ins += "-ss " + str(dpg.get_value("s_pos")) + " "

	if dpg.get_value("s_nodisp") == True:
		running_ins += "-nodisp "

	if dpg.get_value("s_window_title") == True:
		running_ins += "-x " + dpg.get_value("s_title") + " "
	if dpg.get_value("s_loop") == True:
		#print(dpg.get_value(s_number))
		running_ins += "-loop " + str(dpg.get_value(s_number)) + " "

	if dpg.get_value("s_showmode") == True:
		if not( dpg.get_value("s_mode") in [0,1,2] ):
			#print(dpg.get_value("s_mode"))
			#print(dpg.get_value("s_mode") in [0,1,2])
			error = True
		else:
			running_ins += "-showmode " + str(dpg.get_value("s_mode")) + " "

	if ffplay_dict["path"][1] != "":
		running_ins += '"' + ffplay_dict["path"][1] + '"'
	else:
		error = True

	if error == True:
		running_ins = 'error'
	dpg.set_value("output",value=running_ins)


	dpg.render_dearpygui_frame()

dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

dpg.is_dearpygui_running()
dpg.render_dearpygui_frame()
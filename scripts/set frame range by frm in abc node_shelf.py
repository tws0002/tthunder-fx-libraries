# 选择的alembic节点路径参数里有“*_frm50.abc”，读取数字50，设为全局结束帧
selected = hou.selectedNodes()
a = selected[0].parm("fileName").eval() # get select node name
b = a.split('_') # split file name with '_' to tuple

for frm_End in b:
    if frm_End.startswith('frm') == 1: # if match 'frm' then break
        break
global_frame_End = int(frm_End.strip('frm').strip('.abc')) # extract number

hou.setFps(25) # set fps
hou.playbar.setPlaybackRange(0,global_frame_End) # playback range
#hou.playbar.setFrameRange(0,global_frame_End) # global frame range 16.5
hou.hscript('tset `({0}-1)/$FPS` `{1}/$FPS`'.format(0,global_frame_End)) # global frame range 16.0


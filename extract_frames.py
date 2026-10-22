import subprocess
import os

os.makedirs("screenshots", exist_ok=True)

# Timestamps to capture keyframes from the video (seconds)
# 00:10 - Intro/Title
# 00:25 - PS-300B vs PS-300C / UI overview
# 00:35 - PS-300C New UI Layout
# 00:45 - Snap & Pan functions
# 00:55 - Streamlined workflow / Outline list
# 01:05 - Point list (Coordinates & Stitch Pitch)
# 01:15 - Shortcuts & Icons
# 01:23 - DXF import preview & layer selection
# 01:33 - DXF as reference guide / background tracing
# 01:50 - Abnormal setting detection / error alert
# 02:00 - Customizable alerts
# 02:15 - Playback simulation & Estimated sewing time
# 02:25 - Simulation animation
# 02:37 - Machine customization feature / parameter setup
# 02:47 - Custom machine / factory adaptation
# 03:00 - Key feature summary / Brother PS-300C branding

timestamps = [
    (5, "01_intro_title.png"),
    (17, "02_ps300c_launch.png"),
    (26, "03_ps300b_comparison.png"),
    (34, "04_ui_redesign_overview.png"),
    (43, "05_common_tools_snap_pan.png"),
    (48, "06_smooth_editing_snap.png"),
    (57, "07_outline_list_management.png"),
    (65, "08_point_list_pitch_coords.png"),
    (71, "09_icons_shortcuts_productivity.png"),
    (79, "10_dxf_preview_layer_select.png"),
    (88, "11_dxf_reference_guide_tracing.png"),
    (96, "12_dxf_accuracy_production.png"),
    (106, "13_abnormal_setting_detection.png"),
    (115, "14_customizable_alerts.png"),
    (124, "15_playback_simulation_sewing_speed.png"),
    (132, "16_estimated_sewing_time_cycle.png"),
    (140, "17_playback_animation_preview.png"),
    (146, "18_timestamp_146s_machine_customization.png"),
    (152, "19_machine_parameters_config.png"),
    (160, "20_factory_environment_matching.png"),
    (170, "21_summary_core_values.png"),
    (182, "22_brother_next_standard.png")
]

for ts, filename in timestamps:
    out_path = os.path.join("screenshots", filename)
    cmd = [
        "ffmpeg", "-y", "-ss", str(ts), "-i", "video.mp4",
        "-vframes", "1", "-q:v", "2", out_path
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print("Screenshots extracted:", len(os.listdir("screenshots")))

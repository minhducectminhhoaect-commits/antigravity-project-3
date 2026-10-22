import subprocess
import os

os.makedirs("final_screenshots", exist_ok=True)

targets = [
    (27, "01_comparison_ps300b_legacy.png"),
    (38, "02_ps300c_new_ui_overview.png"),
    (46, "03_snap_and_pan_navigation.png"),
    (58, "04_outline_list_management.png"),
    (67, "05_point_list_pitch_coordinates.png"),
    (73, "06_shortcuts_and_tools.png"),
    (81, "07_dxf_file_open_dialog.png"),
    (83, "08_dxf_preview_layer_selection.png"),
    (89, "09_dxf_reference_guide_tracing.png"),
    (98, "10_dxf_accuracy_in_production.png"),
    (107, "11_abnormal_setting_detection_warnings.png"),
    (116, "12_interactive_error_highlight_red.png"),
    (126, "13_playback_simulation_controls.png"),
    (134, "14_estimated_sewing_time_display.png"),
    (144, "15_playback_motion_animation.png"),
    (150, "16_machine_selection_dialog.png"),
    (156, "17_manage_custom_machines_tab.png"),
    (162, "18_custom_machine_parameters_setup.png"),
    (172, "19_brother_core_values_summary.png"),
    (184, "20_brother_ps300c_official_banner.png")
]

for ts, filename in targets:
    out_path = os.path.join("final_screenshots", filename)
    cmd = [
        "ffmpeg", "-y", "-ss", str(ts), "-i", "video.mp4",
        "-vframes", "1", "-q:v", "1", out_path
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print("Target frames extracted:", len(os.listdir("final_screenshots")))

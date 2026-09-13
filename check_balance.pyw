import os
import sys
import json
import ctypes

if sys.platform == "win32":
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass

import webview
import requests

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
    BUNDLE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BUNDLE_DIR = BASE_DIR

CONFIG_FILE = os.path.join(BASE_DIR, "config.json")
HTML_FILE = os.path.join(BUNDLE_DIR, "index.html")


def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


class Api:
    def __init__(self):
        self._window = None

    def set_window(self, window):
        self._window = window

    def close_window(self):
        if self._window:
            self._window.destroy()

    def get_config(self):
        return load_config()

    def get_balance(self):
        config = load_config()
        api_key = config.get("api_key", "")
        if not api_key:
            return {"is_available": False, "balance_infos": [], "error": "no_api_key"}

        try:
            headers = {"Authorization": f"Bearer {api_key}"}
            resp = requests.get("https://api.deepseek.com/user/balance",
                                headers=headers, timeout=10)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            return {"is_available": False, "balance_infos": [], "error": str(e)}


if __name__ == "__main__":
    api = Api()
    window = webview.create_window(
        "DeepSeek 余额查询",
        HTML_FILE,
        js_api=api,
        width=440,
        height=460,
        frameless=True,
        easy_drag=False,
        background_color='#f0f4fe',
    )
    api.set_window(window)
    webview.start(debug=False)

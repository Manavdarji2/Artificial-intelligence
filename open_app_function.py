import subprocess

def open_app(app_name):
    try:
        subprocess.Popen(app_name, shell=True)
        print(f"Opening {app_name}...")
    except Exception as e:
        print(f"Error opening {app_name}: {e}")

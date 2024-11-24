import subprocess

def off_sys():
    subprocess.Popen("taskkill /im python.exe")

def on_system():
    subprocess.Popen("python CrocoOs\\Descopt\\descopt.py")
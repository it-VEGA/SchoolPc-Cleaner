import os, winshell
from win32com.client import Dispatch

def create_shortcurts():
    shortcuts = {'Artshop': "https://artshop.uzedu.uz/ru", 'CiscoNetCad': 'https://www.netacad.com/', 'Code.org': 'https://code.org/', 'Coursera': 'https://ru.coursera.org/','Duolingo': 'https://ru.duolingo.com/?utm_source=pwa_launch' ,'EduCare': 'https://educare.uzedu.uz/', 'Kitob': 'https://kitob.uz/', 'Maktab': 'https://maktab.uz/', 'Milliy Talim Resurslari': 'https://www.youtube.com/channel/UCk-X7kj2vtpnxC77d3cnh1Q', 'Olympiad': 'https://olympiad.uzedu.uz/', 'Python': 'https://www.python.org/', 'Udemy': 'https://www.udemy.com/ru/', 'Unity': 'https://atmos.uw.edu/~dargan/EarthGamesUW/InfraredEscape/', 'UzbekCoders': 'https://uzbekcoders.uz/'}

    desktop = winshell.desktop()
    current_dir = os.getcwd()
    for k,v in shortcuts.items(): 
        path = os.path.join(desktop, f"{k}.lnk")#Где будет создано
        target = v
        icon = os.path.join(current_dir+r"\ico",f"{k}.ico")
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target 
        shortcut.IconLocation = icon
        shortcut.save()

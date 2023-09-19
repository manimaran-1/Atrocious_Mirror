from os import path as ospath
from bot import config_dict

def make_theme():
    if config_dict['THEME_ENABLED']:
        return {'Upload': '📤 Upload',
                'Download': '📥 Download',
                'Clone': '♻️ Clone',
                'QueueDl': '💤 QueueDl',
                'QueueUp': '💤 QueueUp',
                'Pause': '⏸️ Pause',
                'Archive': '📁 Archive',
                'Extract': '🗃 Extract',
                'Split': '✂️ Split',
                'CheckUp': '📝 CheckUp',
                'Seed': '🌧 Seed',
                'Process': '📶 Process',
                'Progress_Bar_Full': '▦',
                'Progress_Bar_Blank': '▢',
                'Speed': '⚡ Speed',
                'Done': '✅ Done',
                'ETA': '⏰ ETA',
                'Engine': '⛓️ Engine',
                'User': '👨‍✈️ User',
                'Seeders': '🌱 Seeders',
                'Leechers': '🐌 Leechers',
                'Size': '📦 Size',
                'Uploaded': '🔺 Uploaded',
                'Ratio': '📎 Ratio',
                'Select': '✔️ Select',
                'Time': '⏰️ Time',
                'Previous': '⏮️ Previous',
                'Next': '⏭️ Next',
                'Page': '📄 Page',
                'Close': '⏹️ Close',
                'Refresh': '🔄 Refresh',
                'Repo': '🌐 Repo',
                'Statistics': '🔄 Statistics',
                'Tasks Running': '🖥 Tasks Running',
                'Stop': '⛔️ Stop:'}
    else:
        return {'Upload': 'Upload',
                'Download': 'Download',
                'Clone': 'Clone',
                'QueueDl': 'QueueDl',
                'QueueUp': 'QueueUp',
                'Pause': 'Pause',
                'Archive': 'Archive',
                'Extract': 'Extract',
                'Split': 'Split',
                'CheckUp': 'CheckUp',
                'Seed': 'Seed',
                'Process': 'Process',
                'Progress_Bar_Full': '■',
                'Progress_Bar_Blank': '□',
                'Speed': 'Speed',
                'Done': 'Done',
                'ETA': 'ETA',
                'Engine': 'Engine',
                'User': 'User',
                'Seeders': 'Seeders',
                'Leechers': 'Leechers',
                'Size': 'Size',
                'Uploaded': 'Uploaded',
                'Ratio': 'Ratio',
                'Time': 'Time',
                'Previous': 'Previous',
                'Next': 'Next',
                'Page': 'Page',
                'Close': 'Close',
                'Refresh': 'Refresh',
                'Repo': 'Repo',
                'Statistics': 'Statistics',
                'Tasks Running': 'Tasks Running',
                'Stop': '⛔️'}

if ospath.exists('my_theme.py'):
    try:
        from my_theme import make_theme
    except:
        pass

theme = make_theme()

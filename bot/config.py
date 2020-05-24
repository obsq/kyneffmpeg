import os
from pathlib import Path

class Config:
    
    API_ID = int(os.environ.get('API_ID', '1257063'))
    API_HASH = os.environ.get('API_HASH', 'bb2f00cc77b85c6bc375223ba76e0372')
    BOT_TOKEN = os.environ.get('BOT_TOKEN', '1119038092:AAE6uMGUr1azOKcl18bo1cfu-TVzMm4G-Hs')
    SESSION_NAME = os.environ.get('SESSION_NAME', 'kyneVideoManager_Bot')
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', 1147178212))
    DATABASE_URL = os.environ.get('DATABASE_URL', 'mongodb+srv://kyneVideoManager:obsquriel@cluster0-tarl7.mongodb.net/test?retryWrites=true&w=majority')
    AUTH_USERS = [int(i) for i in os.environ.get('AUTH_USERS', '724495167').split(' ')]
    MAX_PROCESSES_PER_USER = int(os.environ.get('MAX_PROCESSES_PER_USER', 2))
    MAX_TRIM_DURATION = int(os.environ.get('MAX_TRIM_DURATION', 600))
    TRACK_CHANNEL = int(os.environ.get('TRACK_CHANNEL', '724495167'))
    SLOW_SPEED_DELAY = int(os.environ.get('SLOW_SPEED_DELAY', 15))
    HOST = os.environ.get('HOST', '0.0.0.0')
    
    SCRST_OP_FLDR = Path('screenshots/')
    SMPL_OP_FLDR = Path('samples/')
    THUMB_OP_FLDR = Path('thumbnails/')
    COLORS = ['white', 'black', 'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown', 'gold', 'silver', 'pink']
    FONT_SIZES_NAME = ['Small', 'Medium', 'Large']
    FONT_SIZES = [30, 40, 50]

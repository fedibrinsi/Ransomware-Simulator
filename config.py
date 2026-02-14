"""
Configuration file for Ransomware Simulator
⚠️ FOR EDUCATIONAL PURPOSES ONLY ⚠️
"""
import os

# Project Settings
PROJECT_NAME = "Ransomware Simulator"
VERSION = "1.0.0"

# Encryption Settings
ENCRYPTION_ALGORITHM = "Fernet"  # AES-128 via Fernet
KEY_SIZE = 32  # bytes

# File Settings
ENCRYPTED_EXTENSION = ".locked"
FILE_EXTENSIONS_TO_ENCRYPT = [
    '.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx',
    '.jpg', '.jpeg', '.png', '.gif', '.mp4', '.mp3',
    '.zip', '.rar', '.csv', '.json', '.xml'
]

# Safety Settings - CRITICAL: These prevent accidental damage
PROTECTED_DIRECTORIES = [
    'C:\\Windows',
    'C:\\Program Files',
    'C:\\Program Files (x86)',
    '/System',
    '/Library',
    '/usr',
    '/bin',
    '/sbin',
    '/etc',
    os.path.expanduser('~\\AppData'),  # Windows
    os.path.expanduser('~/.config'),   # Linux
]

# Logging Settings
LOG_DIRECTORY = "logs"
LOG_FILE = os.path.join(LOG_DIRECTORY, "simulator.log")

# Backup Settings
BACKUP_DIRECTORY = "backups"
ENABLE_AUTO_BACKUP = True

# Key Storage
KEY_DIRECTORY = "keys"
KEY_FILE = os.path.join(KEY_DIRECTORY, "encryption_key.key")
BACKUP_KEY_FILE = os.path.join(KEY_DIRECTORY, "backup_key.key")

# Ransom Note
RANSOM_NOTE_FILENAME = "READ_ME_SIMULATION.txt"

# UI Settings
USE_COLORS = True
SHOW_WARNINGS = True

# Testing Settings
DRY_RUN_DEFAULT = True  # Always default to dry run for safety!
MAX_FILES_LIMIT = 1000  # Maximum files to encrypt in one run

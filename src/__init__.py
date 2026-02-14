"""
Ransomware Simulator Package
⚠️ FOR EDUCATIONAL PURPOSES ONLY ⚠️
"""

__version__ = "1.0.0"
__author__ = "Educational Project"

from .encryptor import RansomwareSimulator
from .file_handler import FileHandler
from .key_manager import KeyManager
from .ransom_note import RansomNote
from .logger import SimulatorLogger
from .safety import SafetyChecker

__all__ = [
    'RansomwareSimulator',
    'FileHandler',
    'KeyManager',
    'RansomNote',
    'SimulatorLogger',
    'SafetyChecker'
]

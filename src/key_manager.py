"""
Key Manager - Handles encryption key generation and storage
⚠️ FOR EDUCATIONAL PURPOSES ONLY ⚠️
"""
import os
from cryptography.fernet import Fernet
import config

class KeyManager:
    """Manages encryption keys for the simulator"""
    
    def __init__(self, key_directory=None):
        """Initialize the key manager"""
        self.key_directory = key_directory or config.KEY_DIRECTORY
        self.key_file = config.KEY_FILE
        self.backup_key_file = config.BACKUP_KEY_FILE
        self._ensure_key_directory()
    
    def _ensure_key_directory(self):
        """Create key directory if it doesn't exist"""
        if not os.path.exists(self.key_directory):
            os.makedirs(self.key_directory)
            print(f"[+] Created key directory: {self.key_directory}")
    
    def generate_key(self):
        """Generate a new encryption key"""
        key = Fernet.generate_key()
        print("[+] New encryption key generated")
        return key
    
    def save_key(self, key, filepath=None):
        """Save key to file"""
        filepath = filepath or self.key_file
        
        try:
            with open(filepath, 'wb') as key_file:
                key_file.write(key)
            print(f"[+] Key saved to: {filepath}")
            
            # Create backup
            backup_path = filepath.replace('.key', '_backup.key')
            with open(backup_path, 'wb') as backup_file:
                backup_file.write(key)
            print(f"[+] Backup key saved to: {backup_path}")
            
            return True
        except Exception as e:
            print(f"[-] Error saving key: {e}")
            return False
    
    def load_key(self, filepath=None):
        """Load key from file"""
        filepath = filepath or self.key_file
        
        try:
            if not os.path.exists(filepath):
                print(f"[-] Key file not found: {filepath}")
                return None
            
            with open(filepath, 'rb') as key_file:
                key = key_file.read()
            print(f"[+] Key loaded from: {filepath}")
            return key
        except Exception as e:
            print(f"[-] Error loading key: {e}")
            return None
    
    def key_exists(self, filepath=None):
        """Check if key file exists"""
        filepath = filepath or self.key_file
        return os.path.exists(filepath)
    
    def delete_key(self, filepath=None):
        """Delete key file (use with caution!)"""
        filepath = filepath or self.key_file
        
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
                print(f"[+] Key deleted: {filepath}")
                return True
            return False
        except Exception as e:
            print(f"[-] Error deleting key: {e}")
            return False
    
    def backup_key(self, source_path=None, backup_path=None):
        """Create a backup of the key"""
        source_path = source_path or self.key_file
        backup_path = backup_path or self.backup_key_file
        
        try:
            if not os.path.exists(source_path):
                print(f"[-] Source key not found: {source_path}")
                return False
            
            with open(source_path, 'rb') as source:
                key_data = source.read()
            
            with open(backup_path, 'wb') as backup:
                backup.write(key_data)
            
            print(f"[+] Key backed up to: {backup_path}")
            return True
        except Exception as e:
            print(f"[-] Error backing up key: {e}")
            return False
    
    def get_key_info(self, filepath=None):
        """Get information about a key file"""
        filepath = filepath or self.key_file
        
        if not os.path.exists(filepath):
            return {"exists": False}
        
        try:
            stat = os.stat(filepath)
            return {
                "exists": True,
                "path": filepath,
                "size": stat.st_size,
                "created": stat.st_ctime,
                "modified": stat.st_mtime
            }
        except Exception as e:
            return {"exists": True, "error": str(e)}

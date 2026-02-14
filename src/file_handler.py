"""
File Handler - Manages file operations and backups
⚠️ FOR EDUCATIONAL PURPOSES ONLY ⚠️
"""
import os
import shutil
from datetime import datetime
import config

class FileHandler:
    """Handles file system operations"""
    
    def __init__(self, backup_directory=None):
        """Initialize file handler"""
        self.backup_dir = backup_directory or config.BACKUP_DIRECTORY
        self.encrypted_extension = config.ENCRYPTED_EXTENSION
        self.target_extensions = config.FILE_EXTENSIONS_TO_ENCRYPT
        self._ensure_backup_directory()
    
    def _ensure_backup_directory(self):
        """Create backup directory if it doesn't exist"""
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
            print(f"[+] Created backup directory: {self.backup_dir}")
    
    def find_files(self, directory, extensions=None):
        """Find all files with specified extensions in directory"""
        extensions = extensions or self.target_extensions
        found_files = []
        
        try:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    _, ext = os.path.splitext(file)
                    
                    if ext.lower() in extensions:
                        found_files.append(file_path)
            
            print(f"[+] Found {len(found_files)} files to process")
            return found_files
        except Exception as e:
            print(f"[-] Error finding files: {e}")
            return []
    
    def find_encrypted_files(self, directory):
        """Find all encrypted files (with .locked extension)"""
        encrypted_files = []
        
        try:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith(self.encrypted_extension):
                        file_path = os.path.join(root, file)
                        encrypted_files.append(file_path)
            
            print(f"[+] Found {len(encrypted_files)} encrypted files")
            return encrypted_files
        except Exception as e:
            print(f"[-] Error finding encrypted files: {e}")
            return []
    
    def backup_file(self, file_path):
        """Create a backup of a file"""
        try:
            # Create timestamped backup
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.basename(file_path)
            backup_name = f"{timestamp}_{filename}"
            backup_path = os.path.join(self.backup_dir, backup_name)
            
            # Copy file to backup
            shutil.copy2(file_path, backup_path)
            print(f"[+] Backed up: {filename} -> {backup_name}")
            return True, backup_path
        except Exception as e:
            print(f"[-] Backup failed for {file_path}: {e}")
            return False, None
    
    def backup_directory(self, directory):
        """Backup entire directory"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            dir_name = os.path.basename(directory.rstrip(os.sep))
            backup_name = f"{timestamp}_{dir_name}"
            backup_path = os.path.join(self.backup_dir, backup_name)
            
            shutil.copytree(directory, backup_path)
            print(f"[+] Directory backed up: {backup_path}")
            return True, backup_path
        except Exception as e:
            print(f"[-] Directory backup failed: {e}")
            return False, None
    
    def read_file(self, file_path):
        """Read file contents as bytes"""
        try:
            with open(file_path, 'rb') as f:
                data = f.read()
            return data
        except Exception as e:
            print(f"[-] Error reading file {file_path}: {e}")
            return None
    
    def write_file(self, file_path, data):
        """Write data to file"""
        try:
            with open(file_path, 'wb') as f:
                f.write(data)
            return True
        except Exception as e:
            print(f"[-] Error writing file {file_path}: {e}")
            return False
    
    def rename_file(self, old_path, new_path):
        """Rename a file"""
        try:
            os.rename(old_path, new_path)
            return True
        except Exception as e:
            print(f"[-] Error renaming file: {e}")
            return False
    
    def delete_file(self, file_path):
        """Delete a file"""
        try:
            os.remove(file_path)
            print(f"[+] Deleted: {file_path}")
            return True
        except Exception as e:
            print(f"[-] Error deleting file: {e}")
            return False
    
    def get_file_info(self, file_path):
        """Get information about a file"""
        try:
            stat = os.stat(file_path)
            return {
                "path": file_path,
                "name": os.path.basename(file_path),
                "size": stat.st_size,
                "created": stat.st_ctime,
                "modified": stat.st_mtime,
                "extension": os.path.splitext(file_path)[1]
            }
        except Exception as e:
            return {"error": str(e)}
    
    def restore_from_backup(self, backup_path, restore_path):
        """Restore a file from backup"""
        try:
            if not os.path.exists(backup_path):
                print(f"[-] Backup not found: {backup_path}")
                return False
            
            shutil.copy2(backup_path, restore_path)
            print(f"[+] Restored from backup: {restore_path}")
            return True
        except Exception as e:
            print(f"[-] Restore failed: {e}")
            return False
    
    def list_backups(self):
        """List all backup files"""
        try:
            backups = []
            if os.path.exists(self.backup_dir):
                for item in os.listdir(self.backup_dir):
                    backup_path = os.path.join(self.backup_dir, item)
                    if os.path.isfile(backup_path):
                        backups.append({
                            "name": item,
                            "path": backup_path,
                            "size": os.path.getsize(backup_path),
                            "created": os.path.getctime(backup_path)
                        })
            return backups
        except Exception as e:
            print(f"[-] Error listing backups: {e}")
            return []
    
    def create_test_files(self, directory, count=5):
        """Create test files for demonstration"""
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        created_files = []
        for i in range(count):
            filename = f"test_file_{i+1}.txt"
            filepath = os.path.join(directory, filename)
            
            content = f"This is test file {i+1}\n"
            content += f"Created at: {datetime.now()}\n"
            content += "This is sample content for testing the ransomware simulator.\n"
            content += "=" * 50 + "\n"
            
            try:
                with open(filepath, 'w') as f:
                    f.write(content)
                created_files.append(filepath)
                print(f"[+] Created: {filename}")
            except Exception as e:
                print(f"[-] Failed to create {filename}: {e}")
        
        return created_files

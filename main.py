#!/usr/bin/env python3
"""
Ransomware Simulator - Educational Tool
⚠️ FOR EDUCATIONAL AND AUTHORIZED TESTING ONLY ⚠️

This tool demonstrates how ransomware works for educational purposes.
NEVER use this on systems or data without explicit authorization.

Author: Educational Project
Version: 1.0.0
"""

import os
import sys
from src.encryptor import RansomwareSimulator
from src.file_handler import FileHandler
from src.safety import SafetyChecker

def print_banner():
    """Display program banner"""
    banner = """
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║          🔒 RANSOMWARE SIMULATOR - EDUCATIONAL TOOL 🔒        ║
║                                                               ║
║                      ⚠️  WARNING ⚠️                            ║
║         FOR AUTHORIZED EDUCATIONAL USE ONLY                   ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝

Version: 1.0.0
Purpose: Security Training & Awareness
License: Educational Use Only

"""
    print(banner)

def print_menu():
    """Display main menu"""
    menu = """
═══════════════════════════════════════════════════════════════
MAIN MENU:
═══════════════════════════════════════════════════════════════

1. Encrypt Files (Simulate Attack)
2. Decrypt Files (Simulate Recovery)
3. Create Test Environment
4. View Logs and Reports
5. Safety Settings
6. About & Help
7. Exit

═══════════════════════════════════════════════════════════════
"""
    print(menu)

def create_test_environment():
    """Create a test environment with sample files"""
    print("\n[*] Creating Test Environment")
    print("="*60)
    
    test_dir = input("Enter directory name for test files [test_files]: ").strip()
    if not test_dir:
        test_dir = "test_files"
    
    test_dir = os.path.abspath(test_dir)
    
    try:
        file_handler = FileHandler()
        created = file_handler.create_test_files(test_dir, count=5)
        
        print(f"\n[+] Created {len(created)} test files in: {test_dir}")
        print("[+] You can now use this directory for testing")
        print(f"[+] Directory path: {test_dir}")
        
        return test_dir
    except Exception as e:
        print(f"[-] Error creating test environment: {e}")
        return None

def encrypt_mode():
    """Run encryption simulation"""
    print("\n[*] ENCRYPTION MODE - Simulate Ransomware Attack")
    print("="*60)
    
    # Get target directory
    target_dir = input("Enter target directory path: ").strip()
    if not target_dir:
        print("[-] No directory specified")
        return
    
    target_dir = os.path.abspath(target_dir)
    
    if not os.path.exists(target_dir):
        print(f"[-] Directory not found: {target_dir}")
        return
    
    # Choose mode
    print("\n[?] Select mode:")
    print("1. Dry Run (Safe - No actual encryption)")
    print("2. Active Mode (Will encrypt files!)")
    
    mode_choice = input("Enter choice [1]: ").strip()
    dry_run = mode_choice != "2"
    
    # Initialize simulator
    simulator = RansomwareSimulator(dry_run=dry_run)
    
    # Run encryption
    success = simulator.encrypt_directory(target_dir)
    
    if success:
        print("\n[+] Operation completed successfully!")
        if not dry_run:
            print(f"[+] Files encrypted in: {target_dir}")
            print(f"[+] Read the ransom note at: {target_dir}/READ_ME_SIMULATION.txt")
    else:
        print("\n[-] Operation failed or cancelled")
    
    # Generate report
    input("\nPress Enter to view operation summary...")
    simulator.generate_report()

def decrypt_mode():
    """Run decryption simulation"""
    print("\n[*] DECRYPTION MODE - Simulate Recovery")
    print("="*60)
    
    # Get target directory
    target_dir = input("Enter directory with encrypted files: ").strip()
    if not target_dir:
        print("[-] No directory specified")
        return
    
    target_dir = os.path.abspath(target_dir)
    
    if not os.path.exists(target_dir):
        print(f"[-] Directory not found: {target_dir}")
        return
    
    # Choose mode
    print("\n[?] Select mode:")
    print("1. Dry Run (Safe - Show what would be decrypted)")
    print("2. Active Mode (Will decrypt files)")
    
    mode_choice = input("Enter choice [2]: ").strip()
    dry_run = mode_choice == "1"
    
    # Initialize simulator
    simulator = RansomwareSimulator(dry_run=dry_run)
    
    # Run decryption
    success = simulator.decrypt_directory(target_dir)
    
    if success:
        print("\n[+] Operation completed successfully!")
        if not dry_run:
            print(f"[+] Files decrypted in: {target_dir}")
            print("[+] Your files have been recovered!")
    else:
        print("\n[-] Operation failed or cancelled")
    
    # Generate report
    input("\nPress Enter to view operation summary...")
    simulator.generate_report()

def view_logs():
    """View logs and reports"""
    print("\n[*] LOGS AND REPORTS")
    print("="*60)
    
    logs_dir = "logs"
    
    if not os.path.exists(logs_dir):
        print("[-] No logs directory found")
        return
    
    log_files = [f for f in os.listdir(logs_dir) if f.endswith(('.log', '.json'))]
    
    if not log_files:
        print("[-] No log files found")
        return
    
    print(f"\n[+] Found {len(log_files)} log files:\n")
    
    for i, log_file in enumerate(log_files, 1):
        log_path = os.path.join(logs_dir, log_file)
        size = os.path.getsize(log_path)
        print(f"{i}. {log_file} ({size} bytes)")
    
    print(f"\n[+] Logs directory: {os.path.abspath(logs_dir)}")

def safety_settings():
    """Configure safety settings"""
    print("\n[*] SAFETY SETTINGS")
    print("="*60)
    
    safety = SafetyChecker()
    
    print("\n1. View Protected Directories")
    print("2. Set Whitelist")
    print("3. Check Prerequisites")
    print("4. Run Safety Test")
    print("5. Back to Main Menu")
    
    choice = input("\nEnter choice: ").strip()
    
    if choice == "1":
        print("\n[+] Protected Directories:")
        for directory in safety.protected_dirs:
            print(f"  - {directory}")
    
    elif choice == "2":
        print("\n[*] Set Whitelist (comma-separated paths):")
        paths = input("Enter paths: ").strip()
        if paths:
            whitelist = [p.strip() for p in paths.split(',')]
            safety.set_whitelist(whitelist)
    
    elif choice == "3":
        print("\n[*] Checking Prerequisites...")
        issues = safety.check_prerequisites()
        if issues:
            print("\n[!] Issues found:")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print("\n[+] All prerequisites OK!")
    
    elif choice == "4":
        test_path = input("\nEnter path to test: ").strip()
        if test_path:
            is_safe, reason = safety.is_path_safe(test_path)
            if is_safe:
                print(f"\n[+] Path is SAFE: {reason}")
            else:
                print(f"\n[-] Path is UNSAFE: {reason}")

def show_help():
    """Display help information"""
    help_text = """
═══════════════════════════════════════════════════════════════
HELP & ABOUT
═══════════════════════════════════════════════════════════════

PURPOSE:
This tool simulates ransomware for educational purposes. It helps:
  • Train staff on ransomware awareness
  • Test backup and recovery procedures
  • Understand attack mechanics for better defense
  • Practice incident response

HOW IT WORKS:
  1. Encrypts files using AES-128 (Fernet)
  2. Automatically creates backups
  3. Generates educational ransom note
  4. Provides easy recovery with decryption

SAFETY FEATURES:
  • Dry-run mode for testing
  • Automatic backups
  • Protected directory checks
  • Whitelist enforcement
  • User confirmation required
  • Complete audit logging

TYPICAL WORKFLOW:
  1. Create test environment (Option 3)
  2. Run encryption in dry-run mode first
  3. Review what would happen
  4. Run actual encryption if desired
  5. Practice recovery with decryption
  6. Review logs and reports

IMPORTANT REMINDERS:
  ⚠️  ONLY use on systems you own or have authorization for
  ⚠️  ALWAYS create backups before testing
  ⚠️  Test in isolated environments first
  ⚠️  Never use on production data without approval
  ⚠️  Unauthorized use is ILLEGAL

SUPPORT:
  • Check README.md for detailed documentation
  • Review logs/ directory for operation logs
  • Contact your IT administrator with questions

═══════════════════════════════════════════════════════════════
"""
    print(help_text)
    input("\nPress Enter to continue...")

def main():
    """Main program loop"""
    print_banner()
    
    # Display initial warning
    safety = SafetyChecker()
    safety.display_warning()
    
    # Get user acknowledgment
    print("\n[!] By proceeding, you acknowledge:")
    print("    • This is for educational/authorized testing only")
    print("    • You have permission to use this tool")
    print("    • You understand the legal and ethical implications")
    
    acknowledge = input("\nDo you acknowledge and accept? (yes/no): ").strip().lower()
    
    if acknowledge not in ['yes', 'y']:
        print("\n[!] You must acknowledge to proceed. Exiting...")
        sys.exit(0)
    
    # Main loop
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            encrypt_mode()
        elif choice == "2":
            decrypt_mode()
        elif choice == "3":
            create_test_environment()
        elif choice == "4":
            view_logs()
        elif choice == "5":
            safety_settings()
        elif choice == "6":
            show_help()
        elif choice == "7":
            print("\n[+] Thank you for using Ransomware Simulator")
            print("[+] Stay safe and secure!")
            sys.exit(0)
        else:
            print("\n[-] Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Program interrupted by user")
        print("[+] Exiting safely...")
        sys.exit(0)
    except Exception as e:
        print(f"\n[-] Unexpected error: {e}")
        print("[!] Please report this issue")
        sys.exit(1)

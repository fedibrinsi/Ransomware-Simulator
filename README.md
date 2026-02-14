# Ransomware Simulator - Educational Tool

> ⚠️ **WARNING**: This tool is for **EDUCATIONAL and AUTHORIZED TESTING ONLY**. Unauthorized use is illegal and unethical.

## 📋 Overview

The Ransomware Simulator is an educational tool designed to help organizations and individuals understand how ransomware works, test their defenses, and train staff on proper security practices. This simulator safely demonstrates ransomware mechanics in a controlled environment.

### Purpose

- **Security Training**: Educate staff on ransomware threats
- **Incident Response**: Practice recovery procedures
- **Backup Testing**: Verify backup and restoration systems
- **Security Awareness**: Understand attack vectors and impacts
- **Defense Planning**: Identify security gaps

## ✨ Features

### Core Functionality
- ✅ AES-128 encryption using Fernet (cryptography library)
- ✅ Automatic backup creation before encryption
- ✅ Safe dry-run mode for testing
- ✅ Educational ransom note generation
- ✅ Complete encryption/decryption cycle
- ✅ Detailed logging and reporting

### Safety Features
- 🛡️ Protected directory checks (prevents system file damage)
- 🛡️ Whitelist enforcement
- 🛡️ User confirmation required
- 🛡️ Automatic backups
- 🛡️ Comprehensive audit trail
- 🛡️ File count limits

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Basic command line knowledge

### Installation

1. **Clone or download the project**
```bash
git clone https://github.com/fedibrinsi/Ransomware-Simulator
cd Ransomware-Simulator
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Verify installation**
```bash
python main.py
```

## 📖 Usage Guide

### Basic Workflow

1. **Create Test Environment** (Recommended for first-time users)
   - Run the program
   - Select option 3: "Create Test Environment"
   - This creates sample files for safe testing

2. **Test with Dry Run** (Always do this first!)
   - Select option 1: "Encrypt Files"
   - Choose "Dry Run" mode
   - Review what would happen without actual changes

3. **Run Actual Encryption** (In test environment only!)
   - Select option 1: "Encrypt Files"
   - Choose "Active Mode"
   - Confirm the operation
   - Files will be encrypted with .locked extension

4. **Practice Recovery**
   - Select option 2: "Decrypt Files"
   - Files will be restored to original state

5. **Review Reports**
   - Select option 4: "View Logs and Reports"
   - Check detailed operation logs

### Command Reference

```bash
# Run the interactive menu
python main.py

# The program will guide you through:
# 1. Encryption simulation
# 2. Decryption/recovery
# 3. Test environment creation
# 4. Log viewing
# 5. Safety settings
# 6. Help and documentation
```

## 📁 Project Structure

```
ransomware_simulator/
├── main.py                 # Main entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── src/
│   ├── __init__.py
│   ├── encryptor.py      # Core encryption logic
│   ├── file_handler.py   # File operations
│   ├── key_manager.py    # Encryption key management
│   ├── ransom_note.py    # Ransom note generator
│   ├── logger.py         # Logging system
│   └── safety.py         # Safety checks
├── logs/                 # Operation logs (auto-created)
├── keys/                 # Encryption keys (auto-created)
├── backups/             # File backups (auto-created)
└── test_files/          # Test environment (optional)
```

## ⚙️ Configuration

Edit `config.py` to customize:

```python
# File extensions to encrypt
FILE_EXTENSIONS_TO_ENCRYPT = [
    '.txt', '.pdf', '.doc', '.docx', ...
]

# Safety limits
MAX_FILES_LIMIT = 1000

# Backup settings
ENABLE_AUTO_BACKUP = True

# Protected directories (never touched)
PROTECTED_DIRECTORIES = [
    'C:\\Windows',
    '/System',
    ...
]
```

## 🔐 How It Works

### Encryption Process

1. **Safety Check**: Validates target directory isn't protected
2. **Key Generation**: Creates or loads encryption key
3. **Backup**: Automatically backs up all target files
4. **Encryption**: Encrypts files using AES-128 (Fernet)
5. **Renaming**: Adds `.locked` extension
6. **Note Generation**: Creates educational ransom note
7. **Logging**: Records all operations

### Decryption Process

1. **Key Loading**: Retrieves saved encryption key
2. **File Discovery**: Finds all `.locked` files
3. **Decryption**: Reverses encryption
4. **Restoration**: Removes `.locked` extension
5. **Verification**: Logs successful recovery

### Security Features

- **Fernet Encryption**: Industry-standard AES-128 in CBC mode
- **Key Management**: Secure key generation and storage
- **Backup System**: Automatic file preservation
- **Audit Trail**: Complete operation logging

## 🛡️ Safety Guidelines

### ✅ DO:
- Use ONLY in isolated test environments
- Create backups before testing
- Test in dry-run mode first
- Get explicit authorization
- Work with non-production data
- Keep audit logs
- Follow your organization's security policies

### ❌ DON'T:
- Use on production systems without approval
- Test on real user data without permission
- Share the tool outside authorized contexts
- Run on systems you don't own
- Skip the dry-run mode
- Ignore safety warnings
- Disable safety features

## 📊 Understanding the Output

### Ransom Note
The simulator generates an educational ransom note that includes:
- Attack information and timestamp
- Recovery instructions (multiple methods)
- Prevention best practices
- Impact assessment
- Training objectives
- Legal disclaimers

### Logs
Check the `logs/` directory for:
- Detailed operation logs
- JSON reports with statistics
- Encryption/decryption records
- Error messages and warnings

### Reports
Operation summary includes:
- Files processed (success/failure)
- Timing information
- Backup locations
- Key storage location

## 🎓 Educational Value

### Learning Objectives

After using this simulator, you will understand:

1. **Ransomware Mechanics**: How encryption-based attacks work
2. **Encryption Basics**: Symmetric encryption and key management
3. **Incident Impact**: Business disruption from file encryption
4. **Recovery Methods**: Different approaches to restoration
5. **Prevention**: Best practices to avoid ransomware
6. **Incident Response**: Steps to take during an attack

### Training Scenarios

Use this tool for:
- Staff awareness training
- Security tabletop exercises
- Backup/restore drills
- Incident response practice
- Security controls testing
- Risk assessment demonstrations

## 🔧 Troubleshooting

### Common Issues

**"Permission Denied" errors**
- Run from a directory where you have write permissions
- Don't target system directories
- Check file/folder permissions

**"Key not found" during decryption**
- Ensure the key file exists in `keys/` directory
- Check if you used the same key for encryption
- Look for backup key files

**"No files found"**
- Verify the directory path is correct
- Check if file extensions match configuration
- Ensure files aren't already encrypted

**Import errors**
- Install requirements: `pip install -r requirements.txt`
- Use Python 3.8 or higher
- Create virtual environment if needed

## ⚠️ Final Warning

**REMEMBER: This tool demonstrates attack techniques for educational purposes.**

Real ransomware:
- Is deployed maliciously and illegally
- Causes real financial and operational damage
- Can lead to data loss and business closure
- Results in criminal prosecution of attackers

**Use this tool to:**
- ✅ Learn and educate
- ✅ Test and improve defenses
- ✅ Practice incident response
- ✅ Understand threats

**NEVER use it to:**
- ❌ Attack systems without permission
- ❌ Cause harm or disruption
- ❌ Access data illegally
- ❌ Demonstrate illegal "hacking skills"


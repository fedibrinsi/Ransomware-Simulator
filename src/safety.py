"""
Safety Checker - Prevents accidental damage to system files
⚠️ FOR EDUCATIONAL PURPOSES ONLY ⚠️
"""
import os
import config

class SafetyChecker:
    """Ensures safe operation by checking paths and enforcing rules"""
    
    def __init__(self):
        """Initialize safety checker"""
        self.protected_dirs = config.PROTECTED_DIRECTORIES
        self.max_files = config.MAX_FILES_LIMIT
        self.whitelist = []
    
    def set_whitelist(self, directories):
        """Set whitelist of allowed directories"""
        self.whitelist = [os.path.abspath(d) for d in directories]
        print(f"[+] Whitelist set: {len(self.whitelist)} directories")
    
    def is_path_safe(self, path):
        """Check if a path is safe to operate on"""
        abs_path = os.path.abspath(path)
        
        # Check if path is in protected directories
        for protected in self.protected_dirs:
            if abs_path.startswith(protected):
                return False, f"Path is in protected directory: {protected}"
        
        # Check whitelist if set
        if self.whitelist:
            is_whitelisted = any(abs_path.startswith(wl) for wl in self.whitelist)
            if not is_whitelisted:
                return False, "Path is not in whitelist"
        
        return True, "Path is safe"
    
    def is_directory_safe(self, directory):
        """Check if a directory is safe to operate on"""
        if not os.path.exists(directory):
            return False, "Directory does not exist"
        
        if not os.path.isdir(directory):
            return False, "Path is not a directory"
        
        return self.is_path_safe(directory)
    
    def validate_file_count(self, file_list):
        """Validate that file count is within limits"""
        count = len(file_list)
        if count > self.max_files:
            return False, f"File count ({count}) exceeds limit ({self.max_files})"
        return True, f"File count OK ({count})"
    
    def get_confirmation(self, message, default=False):
        """Get user confirmation for dangerous operations"""
        if default:
            prompt = f"{message} [Y/n]: "
            default_response = 'y'
        else:
            prompt = f"{message} [y/N]: "
            default_response = 'n'
        
        while True:
            response = input(prompt).lower().strip()
            
            if not response:
                response = default_response
            
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' or 'n'")
    
    def display_warning(self):
        """Display safety warning"""
        warning = """
╔═══════════════════════════════════════════════════════════╗
║           ⚠️  RANSOMWARE SIMULATOR WARNING ⚠️             ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  This is an EDUCATIONAL TOOL for authorized testing only  ║
║                                                           ║
║  NEVER use this tool on:                                  ║
║    • Production systems                                   ║
║    • Real user data without permission                    ║
║    • Any system you don't own or have authorization for   ║
║                                                           ║
║  ALWAYS:                                                  ║
║    • Work in isolated test environments                   ║
║    • Keep backups of all data                             ║
║    • Use dry-run mode first                               ║
║                                                           ║
║  Unauthorized use may be ILLEGAL and can result in:       ║
║    • Criminal prosecution                                 ║
║    • Civil liability                                      ║
║    • Data loss                                            ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
"""
        print(warning)
    
    def check_prerequisites(self):
        """Check if system meets prerequisites"""
        issues = []
        
        # Check Python version
        import sys
        if sys.version_info < (3, 8):
            issues.append("Python 3.8+ required")
        
        # Check if running as admin/root (warn if true)
        try:
            is_admin = os.getuid() == 0
        except AttributeError:
            # Windows
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        
        if is_admin:
            issues.append("WARNING: Running as administrator/root - extra caution required!")
        
        return issues
    
    def create_safety_report(self, target_dir, file_count):
        """Create a safety check report"""
        report = {
            "target_directory": target_dir,
            "file_count": file_count,
            "checks": {
                "path_safe": self.is_directory_safe(target_dir),
                "file_count_ok": self.validate_file_count(range(file_count)),
                "prerequisites": self.check_prerequisites()
            }
        }
        return report

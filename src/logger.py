"""
Logger - Tracks all simulator operations
⚠️ FOR EDUCATIONAL PURPOSES ONLY ⚠️
"""
import os
import logging
from datetime import datetime
import json
import config

class SimulatorLogger:
    """Handles logging for the ransomware simulator"""
    
    def __init__(self, log_directory=None):
        """Initialize logger"""
        self.log_directory = log_directory or config.LOG_DIRECTORY
        self._ensure_log_directory()
        
        # Setup file logging
        self.log_file = os.path.join(
            self.log_directory,
            f"simulator_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )
        
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger('RansomwareSimulator')
        self.operation_log = []
        self.start_time = datetime.now()
    
    def _ensure_log_directory(self):
        """Create log directory if it doesn't exist"""
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)
    
    def log_info(self, message):
        """Log info level message"""
        self.logger.info(message)
        self.operation_log.append({
            "timestamp": datetime.now().isoformat(),
            "level": "INFO",
            "message": message
        })
    
    def log_warning(self, message):
        """Log warning level message"""
        self.logger.warning(message)
        self.operation_log.append({
            "timestamp": datetime.now().isoformat(),
            "level": "WARNING",
            "message": message
        })
    
    def log_error(self, message):
        """Log error level message"""
        self.logger.error(message)
        self.operation_log.append({
            "timestamp": datetime.now().isoformat(),
            "level": "ERROR",
            "message": message
        })
    
    def log_operation(self, operation_type, file_path, status, details=None):
        """Log a specific operation"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "operation": operation_type,
            "file": file_path,
            "status": status,
            "details": details or {}
        }
        
        self.operation_log.append(log_entry)
        
        message = f"{operation_type}: {file_path} - {status}"
        if status == "SUCCESS":
            self.log_info(message)
        elif status == "FAILED":
            self.log_error(message)
        else:
            self.log_warning(message)
    
    def log_encryption(self, file_path, success, error=None):
        """Log file encryption"""
        details = {"error": error} if error else {}
        status = "SUCCESS" if success else "FAILED"
        self.log_operation("ENCRYPT", file_path, status, details)
    
    def log_decryption(self, file_path, success, error=None):
        """Log file decryption"""
        details = {"error": error} if error else {}
        status = "SUCCESS" if success else "FAILED"
        self.log_operation("DECRYPT", file_path, status, details)
    
    def log_backup(self, file_path, backup_path, success):
        """Log file backup"""
        details = {"backup_path": backup_path}
        status = "SUCCESS" if success else "FAILED"
        self.log_operation("BACKUP", file_path, status, details)
    
    def generate_summary(self):
        """Generate operation summary"""
        end_time = datetime.now()
        duration = (end_time - self.start_time).total_seconds()
        
        operations = {}
        for entry in self.operation_log:
            op_type = entry.get("operation", "UNKNOWN")
            status = entry.get("status", "UNKNOWN")
            
            if op_type not in operations:
                operations[op_type] = {"SUCCESS": 0, "FAILED": 0, "OTHER": 0}
            
            if status in operations[op_type]:
                operations[op_type][status] += 1
            else:
                operations[op_type]["OTHER"] += 1
        
        summary = {
            "start_time": self.start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "duration_seconds": duration,
            "total_operations": len(self.operation_log),
            "operations_breakdown": operations,
            "log_file": self.log_file
        }
        
        return summary
    
    def save_report(self, output_path=None):
        """Save detailed report to JSON file"""
        if not output_path:
            output_path = os.path.join(
                self.log_directory,
                f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            )
        
        report = {
            "summary": self.generate_summary(),
            "operations": self.operation_log
        }
        
        try:
            with open(output_path, 'w') as f:
                json.dump(report, f, indent=2)
            
            self.log_info(f"Report saved to: {output_path}")
            return output_path
        except Exception as e:
            self.log_error(f"Failed to save report: {e}")
            return None
    
    def print_summary(self):
        """Print summary to console"""
        summary = self.generate_summary()
        
        print("\n" + "="*60)
        print("OPERATION SUMMARY")
        print("="*60)
        print(f"Start Time: {summary['start_time']}")
        print(f"End Time: {summary['end_time']}")
        print(f"Duration: {summary['duration_seconds']:.2f} seconds")
        print(f"Total Operations: {summary['total_operations']}")
        print("\nBreakdown by Operation:")
        
        for op_type, counts in summary['operations_breakdown'].items():
            print(f"\n{op_type}:")
            for status, count in counts.items():
                print(f"  {status}: {count}")
        
        print(f"\nLog File: {summary['log_file']}")
        print("="*60 + "\n")

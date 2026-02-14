"""
Ransom Note Generator - Creates educational ransom notes
⚠️ FOR EDUCATIONAL PURPOSES ONLY ⚠️
"""
import os
from datetime import datetime
import config

class RansomNote:
    """Generates educational ransom notes"""
    
    TEMPLATE = """
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║           🔒 YOUR FILES HAVE BEEN ENCRYPTED 🔒                    ║
║                                                                   ║
║                    ⚠️  SIMULATION MODE ⚠️                         ║
║            THIS IS AN EDUCATIONAL DEMONSTRATION                   ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝

INCIDENT INFORMATION:
═══════════════════════════════════════════════════════════════════

Timestamp:          {timestamp}
Target Directory:   {target_dir}
Files Encrypted:    {file_count}
Encryption Method:  AES-128 (Fernet)
Key Location:       {key_location}
Backup Location:    {backup_location}

═══════════════════════════════════════════════════════════════════

⚠️  WHAT HAPPENED?

Your files have been encrypted using military-grade encryption as part
of this EDUCATIONAL RANSOMWARE SIMULATION. This demonstrates how a 
real ransomware attack would affect your systems.

🔑 WHAT DO I NEED TO DECRYPT MY FILES?

You need the encryption key that was used to lock your files. In this
simulation, the key has been safely stored at:

    {key_location}

📂 YOUR FILES ARE BACKED UP!

Unlike real ransomware, this simulator automatically created backups:

    {backup_location}

═══════════════════════════════════════════════════════════════════

🔓 HOW TO RECOVER YOUR FILES (SIMULATION):

Method 1 - Using the Decryption Tool:
   1. Run: python main.py
   2. Select option 2 (Decrypt)
   3. Provide the target directory
   4. The tool will automatically use the saved key

Method 2 - Manual Recovery:
   1. Locate your backup files in: {backup_location}
   2. Copy them back to the original location
   3. Replace the encrypted (.locked) files

Method 3 - Using the Key:
   1. The encryption key is stored at: {key_location}
   2. Use any Fernet-compatible tool to decrypt
   3. Or use the provided decrypt.py script

═══════════════════════════════════════════════════════════════════

🎓 LESSONS LEARNED - PROTECTING AGAINST RANSOMWARE:

1. BACKUP STRATEGY:
   ✓ Maintain regular backups (3-2-1 rule)
   ✓ Keep backups offline or on separate systems
   ✓ Test backup restoration regularly
   ✓ Automate backup processes

2. PREVENTION MEASURES:
   ✓ Keep software updated and patched
   ✓ Use antivirus and anti-malware tools
   ✓ Enable firewalls and network segmentation
   ✓ Implement email filtering
   ✓ Use strong, unique passwords

3. USER AWARENESS:
   ✓ Don't open suspicious emails or attachments
   ✓ Verify sender identities
   ✓ Don't click unknown links
   ✓ Be cautious of urgent payment requests
   ✓ Report suspicious activity immediately

4. TECHNICAL CONTROLS:
   ✓ Implement least privilege access
   ✓ Disable macros in Office documents
   ✓ Use application whitelisting
   ✓ Monitor for unusual file activity
   ✓ Deploy endpoint detection and response (EDR)

5. INCIDENT RESPONSE:
   ✓ Have an incident response plan
   ✓ Know who to contact (IT, management, authorities)
   ✓ Document everything
   ✓ Don't pay the ransom in real attacks
   ✓ Isolate infected systems immediately

═══════════════════════════════════════════════════════════════════

❓ FREQUENTLY ASKED QUESTIONS:

Q: Is this a real ransomware attack?
A: NO! This is a controlled educational simulation. Your files are
   safe and can be easily recovered using the methods above.

Q: Should I pay the ransom?
A: In real attacks, paying is NOT recommended. It doesn't guarantee
   file recovery and funds criminal activity. This simulation is free!

Q: What if I can't recover my files?
A: Contact your IT administrator or the person who ran this simulation.
   All files have been backed up automatically.

Q: How can I verify this is a simulation?
A: Check the file extensions (.locked), the presence of backups, and
   the fact that system files are untouched. Real ransomware is far
   more destructive.

Q: Can I use this tool on my network?
A: ONLY with explicit authorization! Unauthorized use is illegal and
   unethical, even for educational purposes.

═══════════════════════════════════════════════════════════════════

📊 IMPACT ASSESSMENT:

If this were a real attack:
   • Business operations would be disrupted
   • Data would be inaccessible without the key
   • Recovery could take days or weeks
   • Costs could range from thousands to millions
   • Reputation damage would be significant
   • Legal and regulatory issues could arise

Real-world ransom demands typically range from $5,000 to $50,000,000
depending on the target organization's size and ability to pay.

═══════════════════════════════════════════════════════════════════

🛡️ IMMEDIATE ACTIONS (if this were real):

1. DO NOT RESTART your computer
2. Disconnect from network immediately
3. Contact IT security team
4. Preserve evidence (don't delete anything)
5. Check your backups
6. Report to authorities (FBI, local police)
7. Notify stakeholders and customers if required
8. Activate incident response plan
9. Consider engaging cybersecurity experts
10. Document all steps taken

═══════════════════════════════════════════════════════════════════

📞 RESOURCES FOR REAL RANSOMWARE INCIDENTS:

• FBI Internet Crime Complaint Center: https://www.ic3.gov
• CISA: https://www.cisa.gov/stopransomware
• No More Ransom Project: https://www.nomoreransom.org
• Local law enforcement cyber crime unit
• Your organization's security team
• Cybersecurity insurance provider

═══════════════════════════════════════════════════════════════════

🎯 TRAINING OBJECTIVES COMPLETED:

If you're seeing this note, you've successfully:
   ✓ Experienced a simulated ransomware attack
   ✓ Learned how file encryption works
   ✓ Understood the impact of ransomware
   ✓ Practiced prevention strategies
   ✓ Learned recovery procedures

Use this knowledge to:
   • Improve your security posture
   • Train your team on ransomware awareness
   • Test your backup and recovery procedures
   • Develop an incident response plan

═══════════════════════════════════════════════════════════════════

⚠️  LEGAL DISCLAIMER:

This tool is provided for EDUCATIONAL and AUTHORIZED TESTING ONLY.

The creators and users of this tool are responsible for ensuring:
   • Proper authorization before use
   • Compliance with all applicable laws
   • Ethical use within legal boundaries
   • No harm to individuals or organizations

Unauthorized use of this tool may violate:
   • Computer Fraud and Abuse Act (CFAA)
   • State and local computer crime laws
   • International cybercrime laws
   • Terms of service agreements

═══════════════════════════════════════════════════════════════════

📝 SIMULATION LOG:

Session ID:     {session_id}
Simulator Ver:  1.0.0
Mode:           Educational Simulation
Recovery:       Enabled
Backups:        Created
Reversible:     Yes

═══════════════════════════════════════════════════════════════════

💡 REMEMBER:

This simulation demonstrates the MECHANICS of ransomware, not the
MALICE. Real attackers won't provide recovery instructions, backups,
or educational content. They want money and will use fear and 
pressure tactics.

Your best defense is:
   1. Prevention through security best practices
   2. Preparation with backups and incident response plans
   3. Education through simulations like this one

Stay safe, stay vigilant, and keep learning!

═══════════════════════════════════════════════════════════════════

For questions about this simulation, contact your IT administrator
or the security training coordinator who authorized this exercise.

Generated by: Ransomware Simulator v1.0 (Educational Tool)
═══════════════════════════════════════════════════════════════════
"""
    
    def __init__(self):
        """Initialize ransom note generator"""
        self.note_filename = config.RANSOM_NOTE_FILENAME
    
    def generate(self, target_dir, file_count, key_location, backup_location):
        """Generate a ransom note with all details"""
        import uuid
        
        content = self.TEMPLATE.format(
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            target_dir=target_dir,
            file_count=file_count,
            key_location=key_location,
            backup_location=backup_location,
            session_id=str(uuid.uuid4())[:8]
        )
        
        return content
    
    def save(self, target_dir, file_count, key_location, backup_location):
        """Generate and save ransom note to target directory"""
        try:
            content = self.generate(target_dir, file_count, key_location, backup_location)
            note_path = os.path.join(target_dir, self.note_filename)
            
            with open(note_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"[+] Ransom note saved: {note_path}")
            
            # Also display in console
            print("\n" + "="*70)
            print("RANSOM NOTE PREVIEW:")
            print("="*70)
            print(content[:1000] + "...\n[Note truncated for console display]")
            print("="*70 + "\n")
            
            return note_path
        except Exception as e:
            print(f"[-] Error saving ransom note: {e}")
            return None
    
    def read(self, target_dir):
        """Read existing ransom note"""
        note_path = os.path.join(target_dir, self.note_filename)
        try:
            with open(note_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"[-] Error reading ransom note: {e}")
            return None

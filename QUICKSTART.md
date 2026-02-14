# Quick Start Guide - Ransomware Simulator


## Step 1: Setup 

```bash
# Install Python dependencies
pip install -r requirements.txt
```

That's it! You're ready to go.

## Step 2: First Run 

### Launch the Simulator
```bash
python main.py
```

### Accept the Warning
- Read the warning carefully
- Type `yes` to acknowledge

### Create Test Files
1. Select option **3** (Create Test Environment)
2. Press Enter to use default name `test_files`
3. Five test files will be created

## Step 3: Test Encryption (Dry Run)

1. Select option **1** (Encrypt Files)
2. Enter the directory: `test_files`
3. Select **1** for Dry Run mode
4. Watch the simulation (no actual changes)

## Step 4: Try Real Encryption

1. Select option **1** (Encrypt Files)
2. Enter the directory: `test_files`
3. Select **2** for Active Mode
4. Confirm when prompted
5. Files are now encrypted!

## Step 5: Decrypt and Recover

1. Select option **2** (Decrypt Files)
2. Enter the directory: `test_files`
3. Select **2** for Active Mode
4. Files are restored!

## You Did It!

You've successfully:
- ✅ Simulated a ransomware attack
- ✅ Encrypted files safely
- ✅ Recovered all files
- ✅ Learned how ransomware works

## 📖 What to Explore Next

### View the Ransom Note
```bash
# Look in your test directory
cat test_files/READ_ME_SIMULATION.txt
```

### Check the Logs
- Select option **4** in the main menu
- Review operation details in `logs/` folder

### Read the Full Documentation
- See `README.md` for complete documentation
- Learn about configuration in `config.py`

## Understanding the Files

### Created Directories
```
ransomware_simulator/
├── logs/           # Operation logs and reports
├── keys/           # Encryption keys (DON'T DELETE!)
├── backups/        # Automatic backups of files
└── test_files/     # Your test directory
```

### File Extensions
- `.locked` - Encrypted files
- Original files are backed up automatically

## Safety Reminders

1. **Only test on your own data**
2. **Always use dry-run mode first**
3. **Keep the keys/ directory safe**
4. **Review logs after operations**
5. **Never use on production systems**

## Common Questions

**Q: Can I test on my Documents folder?**
A: Only if it's YOUR computer and you have backups! Start with test_files first.

**Q: What if I lose the encryption key?**
A: Backups are created automatically in `backups/` directory.

**Q: Is this dangerous?**
A: Only if misused. Follow the guidelines and you'll be fine.

**Q: Can I undo everything?**
A: Yes! Decryption reverses the process completely.

## Learning Path

### Beginner (You are here!)
- ✅ Run basic encryption/decryption
- ✅ Understand the workflow
- ✅ Read the ransom note

### Intermediate
- [ ] Customize `config.py` settings
- [ ] Try different file types
- [ ] Review detailed logs
- [ ] Practice incident response

### Advanced
- [ ] Modify the code
- [ ] Add new features
- [ ] Create training scenarios
- [ ] Integrate with security tools

## Training Scenario Ideas

1. **Backup Test**: Delete a backup, try recovery
2. **Key Loss**: Move the key, see what happens
3. **Large Scale**: Create 50+ test files
4. **File Types**: Test with different formats
5. **Team Training**: Teach colleagues

## Pro Tips

1. **Always start with dry run** - See what will happen first
2. **Read the ransom note** - It's packed with learning content
3. **Check logs regularly** - Understanding operations is key
4. **Practice recovery** - Being able to decrypt is crucial
5. **Keep keys safe** - They're essential for recovery

## Next Steps

Ready to dive deeper? Check out:
- `README.md` - Full documentation
- `config.py` - Customization options
- `src/` folder - Understand the code
- Sprint guide (your HTML file) - Detailed learning path

## Quick Commands Reference

```bash
# Start simulator
python main.py

# Create test files
# → Select option 3

# Encrypt (dry run)
# → Select option 1 → Enter directory → Choose option 1

# Encrypt (active)
# → Select option 1 → Enter directory → Choose option 2

# Decrypt
# → Select option 2 → Enter directory → Choose option 2

# View logs
# → Select option 4
```

---

**Remember: This is a learning tool. Use it responsibly!** 🎓

Happy learning! If you have questions, review the README.md or check the logs/ directory for detailed information.

# File Integrity Monitor (FIM)

A simple Python-based File Integrity Monitoring tool that continuously watches a defined directory for changes.  
It detects **new, modified, and deleted files** by comparing file hashes against a stored baseline.

## Features (MVP)
- Monitors a specified directory continuously (pre-defined interval scanning)
- Calculates SHA-256 hash for each file
- Creates a baseline of file hashes (`hashes.json`)
- Detects:
  - **New files**
  - **Modified files**
  - **Deleted files**
- Updates the baseline automatically after changes are detected

## How It Works
1. On first run, the script generates a baseline of file hashes for all files in the monitored directory.
2. It continuously re-scans the directory at a set interval.
3. Any changes are printed to the console (**NEW FILE**, **MODIFIED**, **DELETED**) followed by the file path.
4. The baseline file (`hashes.json`) is updated with the new state.

## Configuration
- `Monitored_Directory`: Path to the directory being monitored.
- `Hash_File`: Location of the baseline file (`hashes.json`).
- `Check_Interval`: Time in seconds between scans (default = 5).

## Example Output
Monitoring F:\Projects\File Integrity Monitor\Monitored for changes...
**[NEW FILE]** F:\Projects\File Integrity Monitor\Monitored\new_doc.txt
**[MODIFIED]** F:\Projects\File Integrity Monitor\Monitored\report.pdf
**[DELETED]** F:\Projects\File Integrity Monitor\Monitored\old_notes.txt
Modifications Detected. Updating baseline...

## Future Improvements
- Log changes to a file instead of console only
- Monitor multiple directories at once
- Email or desktop notifications for detected changes
- Support excluding certain files/directories from monitoring
- Config file support (e.g., YAML/JSON for settings instead of editing code)
- Colored console output for better readability
- Add integrity verification mode (check against a fixed baseline without updating it)
- Add hash algorithm options (e.g., MD5, SHA-1, SHA-512)

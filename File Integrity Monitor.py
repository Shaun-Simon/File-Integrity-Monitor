import os
import hashlib
import json
import time

Monitored_Directory = r"C:\Users\Shaun\Downloads\Monitored"
Hash_File = r"hashes.json"
Check_Interval = 5

def Hash_Calculator(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as file:
            while chunk := file.read(8192):
                sha256.update(chunk)
    except FileNotFoundError:
        return None
    return sha256.hexdigest()

def Scan_Directory(directory):
    file_hashes = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            file_hash = Hash_Calculator(filepath)
            if file_hash:
                file_hashes[filepath] = file_hash
    return file_hashes

def Process_Baseline():
    if os.path.exists(Hash_File):
        with open(Hash_File, "r") as file:
            return json.load(file)
    return {}

def Save_Baseline(baseline):
    with open(Hash_File, "w") as file:
        json.dump(baseline, file, indent=2)

def Monitor():
    baseline = Process_Baseline()
    print("Initial Baseline Loaded.")

    while True:
        current_hashes = Scan_Directory(Monitored_Directory)

        Modification_Detected = False

        for filepath, filehash in current_hashes.items():
            if filepath not in baseline:
                print(f"**[NEW FILE]** {filepath}")
                Modification_Detected = True


            elif baseline[filepath] != filehash:
                print(f"**[MODIFIED]** {filepath}")
                Modification_Detected = True


        for filepath in baseline:
            if filepath not in current_hashes:
               print(f"** [DELETED] ** {filepath}")
               Modification_Detected = True


        if Modification_Detected:
            print("Modifications Detected. Updating baseline...")
            Save_Baseline(current_hashes)
            baseline = current_hashes.copy()

        time.sleep(Check_Interval)

if __name__ == "__main__":
    print(f"Monitoring {Monitored_Directory} for changes...")
    Monitor()
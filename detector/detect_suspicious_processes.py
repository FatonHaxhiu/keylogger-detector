import psutil

def detect_suspicious_processes():
    keywords = ['log', 'key', 'input', 'record']
    suspicious = []

    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmd = ' '.join(proc.info['cmdline'])
            if any(word in cmd.lower() for word in keywords):
                suspicious.append((proc.info['pid'], cmd))
        except Exception:
            continue

    if suspicious:
        print("⚠️ Suspicious processes found:")
        for pid, cmd in suspicious:
            print(f"PID {pid}: {cmd}")
    else:
        print("✅ No suspicious processes found.")

if __name__ == "__main__":
    detect_suspicious_processes()

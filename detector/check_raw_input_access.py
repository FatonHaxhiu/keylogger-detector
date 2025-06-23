import os

def detect_input_access():
    print("🔍 Checking for processes reading /dev/input...")
    result = os.popen("lsof /dev/input/* 2>/dev/null").read()
    if result:
        print("⚠️ Warning: Process accessing keyboard/mouse devices:\n")
        print(result)
    else:
        print("✅ No raw input access detected.")

if __name__ == "__main__":
    detect_input_access()

import os
TEXT = 'Lie still. Above you, light that left its star before you were born is only now arriving. Breathe in. Breathe out. The whole sky has waited all this time, patiently, just to reach your eyes tonight.'

def main():
    out = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()

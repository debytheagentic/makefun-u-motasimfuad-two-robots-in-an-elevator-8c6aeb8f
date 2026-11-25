import os

LINE = "Floor 7? Great, I was headed to 7.01 — close enough to share the ride. I'd hold the door, but my arms are for lifting other robots."

def main():
    assert 1 <= len(LINE) <= 200
    out = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"LEN={len(LINE)}")

if __name__ == "__main__":
    main()

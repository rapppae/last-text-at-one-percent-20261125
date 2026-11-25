"""Entry for make.fun bounty: Last Text at One Percent
Slug: u-azazex-last-text-at-one-percent-ba9fc876
Entry text (108 characters, gate max 200). Written to /output/entry.txt with no trailing newline.
"""
import os

ENTRY = """1% left. Tell the charger I loved it, tell the group chat I tried, and please, please stop taking selfies."""

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()

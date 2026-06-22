#!/usr/bin/env python3
"""
Add frontmatter to existing Obsidian notes based on their folder name.

Usage:
    python add-frontmatter.py /path/to/your/vault          # dry run
    python add-frontmatter.py /path/to/your/vault --apply  # write changes

The script skips any file that already has a frontmatter block.
"""

import os
import sys
import re
from datetime import datetime
from pathlib import Path

# Maps folder name fragments (lowercase) to frontmatter type values.
# First match wins, so put more specific names first.
FOLDER_TYPE_MAP = [
    (["weekly review", "weekly-review", "weekly_review", "weeklies"],   "weekly-review"),
    (["daily note", "daily-note", "daily_note", "daily notes", "journal"], "daily-note"),
    (["work update", "work-update", "work_update", "work updates"],     "work-update"),
    (["meeting", "meetings"],                                            "meeting"),
    (["guide", "guides"],                                                "guide"),
    (["system", "systems"],                                              "system"),
    (["people", "person", "persons", "contacts"],                       "person"),
    (["project", "projects"],                                            "project"),
    (["area", "areas"],                                                  "area"),
    (["moc", "mocs", "map of content", "maps of content"],              "moc"),
    (["page", "pages", "inbox", "capture"],                             "page"),
    (["note", "notes"],                                                  "note"),
]

# Types that get a `stage` property
STAGED_TYPES = {"note", "guide", "project"}

# Folders to skip entirely
SKIP_FOLDERS = {".git", ".obsidian", ".claude", ".trash"}

SKIP_FILES = {"CLAUDE.md", "PKM_Context.md"}


def infer_type(file_path: Path, vault_root: Path) -> str | None:
    """Infer the note type from the file's folder path relative to vault root."""
    parts = file_path.relative_to(vault_root).parts
    # Check each folder component (not the filename itself)
    for part in parts[:-1]:
        part_lower = part.lower()
        for keywords, note_type in FOLDER_TYPE_MAP:
            if any(kw in part_lower for kw in keywords):
                return note_type
    return None


def get_created_date(file_path: Path) -> str:
    """Get file creation date, falling back to modification date."""
    stat = file_path.stat()
    # st_birthtime is available on macOS; st_ctime on Linux is change time, not creation
    ts = getattr(stat, "st_birthtime", None) or stat.st_mtime
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d")


def has_frontmatter(content: str) -> bool:
    """Return True if the file already starts with a YAML frontmatter block."""
    return content.startswith("---")


def build_frontmatter(note_type: str, created: str) -> str:
    lines = ["---", f"type: {note_type}"]
    if note_type in STAGED_TYPES:
        lines.append("stage: inbox")
    lines += ["tags: []", f"created: {created}", "---", ""]
    return "\n".join(lines)


def process_vault(vault_root: Path, apply: bool) -> None:
    vault_root = vault_root.resolve()
    changed, skipped_existing, skipped_unknown, skipped_file = 0, 0, 0, 0

    for root, dirs, files in os.walk(vault_root):
        # Prune skip folders in-place so os.walk doesn't descend into them
        dirs[:] = [d for d in dirs if d not in SKIP_FOLDERS]

        for filename in files:
            if not filename.endswith(".md"):
                continue
            if filename in SKIP_FILES:
                continue

            file_path = Path(root) / filename
            content = file_path.read_text(encoding="utf-8")

            if has_frontmatter(content):
                skipped_existing += 1
                continue

            note_type = infer_type(file_path, vault_root)
            if note_type is None:
                rel = file_path.relative_to(vault_root)
                print(f"  [UNKNOWN TYPE] {rel}")
                skipped_unknown += 1
                continue

            created = get_created_date(file_path)
            frontmatter = build_frontmatter(note_type, created)
            new_content = frontmatter + content

            rel = file_path.relative_to(vault_root)
            if apply:
                file_path.write_text(new_content, encoding="utf-8")
                print(f"  [UPDATED] {rel}  →  type: {note_type}")
            else:
                print(f"  [DRY RUN] {rel}  →  type: {note_type}")
            changed += 1

    print()
    print(f"{'Applied' if apply else 'Would update'}: {changed} files")
    print(f"Already has frontmatter: {skipped_existing} files")
    if skipped_unknown:
        print(f"Unknown type (no folder match): {skipped_unknown} files — review manually")
    if not apply and changed:
        print()
        print("Run with --apply to write changes.")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)

    vault_path = Path(args[0])
    if not vault_path.is_dir():
        print(f"Error: {vault_path} is not a directory")
        sys.exit(1)

    do_apply = "--apply" in args
    print(f"Vault: {vault_path.resolve()}")
    print(f"Mode:  {'APPLY (writing files)' if do_apply else 'DRY RUN (no changes)'}")
    print()
    process_vault(vault_path, do_apply)

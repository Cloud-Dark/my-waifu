"""Package each skill under skills/ as a ZIP ready to upload to claude.ai.

Usage: python scripts/build-zips.py   ->   dist/<skill>.zip
"""
import pathlib
import zipfile

root = pathlib.Path(__file__).resolve().parent.parent
dist = root / "dist"
dist.mkdir(exist_ok=True)

for skill in sorted((root / "skills").iterdir()):
    if not (skill / "SKILL.md").is_file():
        continue
    out = dist / f"{skill.name}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(skill.rglob("*")):
            if f.is_file():
                zf.write(f, f.relative_to(skill.parent).as_posix())
    print(out.relative_to(root))

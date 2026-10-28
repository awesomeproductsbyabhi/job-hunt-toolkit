#!/usr/bin/env python3
"""Build a one-page, ATS-friendly resume PDF for one job from a small overrides file.

usage: python3 build_job.py <slug> [overrides.json] [--content content_example]

overrides.json (all keys optional):
  {"track": "AI" | "Growth", "title": "...", "band": "...", "about": "...",
   "skills": [["Group", ["a", "b"]]], "order": {"Company": ["bullet_key", ...]},
   "bullets": {"key": ["Lead.", "Text with **bold**"]}}

The build fails if the PDF is not exactly one page. It never invents content: it only reorders and re-words what is in the content file."""
import sys, os, json, copy, subprocess, importlib

here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
args = [a for a in sys.argv[1:] if not a.startswith("--")]
content_name = "content_example"
if "--content" in sys.argv:
    content_name = sys.argv[sys.argv.index("--content") + 1]; args = [a for a in args if a != content_name]
slug = args[0]
ov = json.load(open(args[1])) if len(args) > 1 else {}
base = importlib.import_module(content_name)

track = ov.get("track", next(iter(base.VERSIONS)))
V = copy.deepcopy(base.VERSIONS[track])
for k in ("title", "band", "about", "skills", "order", "impact"):
    if k in ov: V[k] = ov[k]
B = copy.deepcopy(base.BULLETS); B.update({k: tuple(v) for k, v in ov.get("bullets", {}).items()})
for company, keys in V["order"].items():
    for k in keys: assert k in B, f"unknown bullet key {k}"

payload = {"person": base.PERSON, "education": base.EDUCATION, "awards": base.AWARDS, "tools": base.TOOLS,
           "jobs": [dict(j, keys=V["order"].get(j["company"], j["keys"])) for j in base.JOBS],
           "bullets": B, "version": V}
out_json = os.path.join(here, f"build_{slug}.json"); json.dump(payload, open(out_json, "w"), indent=1, ensure_ascii=False)
pdf = os.path.join(here, f"Resume_{slug}.pdf")
r = subprocess.run(["node", "gen_portal_pdf.js", out_json, pdf], cwd=here, capture_output=True, text=True)
if r.returncode: print(r.stderr); sys.exit(1)
import pypdf
n = len(pypdf.PdfReader(pdf).pages)
print(f"{os.path.basename(pdf)}: {n} page(s)")
if n != 1: print("ERROR: not one page. Shorten text or drop a bullet."); sys.exit(1)

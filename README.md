# Job Hunt Toolkit

Small tools I built to run my own job search quickly and honestly, written with an AI coding assistant (Claude) and used every day. Three parts:

| Part | What it does |
| --- | --- |
| [`resume-builder/`](resume-builder) | Builds a one-page, ATS-friendly resume PDF per job from a small overrides file. Fails the build if the result is not exactly one page. |
| [`skills/tailor-resume-to-jd/`](skills/tailor-resume-to-jd/SKILL.md) | The agent skill that drives the process: read the JD, score fit before and after, count keyword coverage, tailor only with true claims, draft outreach. |
| [`pipeline-desk/`](pipeline-desk/index.html) | A single-file job-pipeline dashboard: headline tiles (due today, new leads, applied this week, active, interviews, to verify), a Today list, stage counts, and a sortable, searchable table with inline editing and a linked interview-prep column. Changing a stage sets the next step and due date automatically. Sample data only. |

## Why

Applying to many roles fast usually means copying one resume everywhere or tailoring badly. I wanted tailoring that is quick, measurable and cannot invent anything. The design choices follow from that:

- **Truth first.** Every bullet lives in one content file. Tailoring can reorder and re-word, never add a claim that is not there.
- **Measured, not guessed.** Fit is scored before and after, and keyword coverage is counted from the PDF text, so I can see what a change actually moved.
- **One page, enforced.** The builder exits with an error when the PDF is not one page, so I cannot upload an overflowing file by accident.
- **Follow-ups are automatic.** Pipeline Desk applies the same rules every time: Applied sets a 7-day follow-up, Referral asked 3 days, interview stages 2 days.

## Run the resume builder

```bash
pip install -r requirements.txt
npm install && npx playwright install chromium
cd resume-builder
python3 build_job.py my-role ../examples/overrides_ai_role.json
```

This writes `Resume_my-role.pdf` using the fictional example content in `content_example.py`. Replace that file with your own content. An example output is in [`examples/example_resume.pdf`](examples/example_resume.pdf).

Overrides file keys (all optional): `track`, `title`, `band`, `about`, `skills`, `order`, `bullets`.

## Pipeline Desk

Open `pipeline-desk/index.html` in a browser. It holds fictional companies and keeps changes in your browser only.

## What is not here

Real resumes, contact details, employer tools and partner names are deliberately left out. The content in this repo is fictional.

## Limits

The resume builder produces a single-column PDF only. Pipeline Desk stores data in the browser, not a database. The skill file is a procedure for an AI assistant, not an automated pipeline.

MIT licensed.

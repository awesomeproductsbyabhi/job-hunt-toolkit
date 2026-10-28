---
name: tailor-resume-to-jd
description: Tailor a one-page resume to a specific job description, report fit before and after with keyword coverage, and draft a short outreach note. Use when the user shares a job link or JD text.
---

# Tailor a resume to a job description

I wrote this skill for my own job search and use it daily with Claude. It is a procedure, not a template: the point is to get a truthful, one-page resume and an honest fit assessment quickly.

Applications are manual only. Never submit anything on the user's behalf.

## Steps

1. **Read the job.** Fetch the posting. If the site blocks automated reads, ask the user to paste the JD instead of guessing. Extract title, level, location, requisition code, must-haves, nice-to-haves, how to apply, and the 20 keywords an applicant tracking system would rank on, in the JD's exact words.
2. **Load the source of truth.** The only claims allowed on a resume are the ones in the user's career notes and base content file. Never invent, round up or stretch a number.
3. **Fit summary and BEFORE score.** Give a JD-specific score out of 100 (about 75 or more is strong, under 60 is weak). Mark each must-have as present, missing but true (it exists in the notes, so it can be added), or missing and not true (a real gap). Count keyword coverage by searching the resume text, never by estimating.
4. **Tailor.** Put the JD's exact title in the title line if it is true, reorder skills so JD keywords come first, mirror the JD's language in the summary, lead with the best-matching bullets. Keep one page. No first person, no keyword stuffing, no hidden text.
5. **Build.** Write a small overrides file and run the resume builder. The build fails if the PDF is not one page.
6. **AFTER score.** Re-count keyword coverage on the new PDF and re-estimate the fit. Report before and after together, what moved, and which gaps remain. Never credit a keyword the user cannot truthfully claim.
7. **Outreach (apply first).** The user applies as soon as the resume is ready and does not wait for a reply from a contact. After applying, draft a short message (3 to 5 sentences) to one or two relevant people: say the user has already applied, give the role, requisition code and date, include one concrete result matching the JD, and ask whether they can refer the user or flag the application to the recruiter. Do not attach a resume in a first message to a stranger.
8. **Track.** Record the role in a pipeline tracker with stage, fit score, next step and due date.

## Rules that never bend

- Only true claims from the user's own notes.
- Credit accurately: if a colleague built a piece, write "led product on" and not "built".
- Plans are not results: label a modelled number as a plan.
- Do not name private partners or customers on a resume.
- Do not link or describe an employer's private tools as personal work.

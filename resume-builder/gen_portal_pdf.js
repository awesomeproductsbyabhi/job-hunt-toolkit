// Renders the single-column resume HTML to an A4 PDF with Playwright. usage: node gen_portal_pdf.js <build.json> <out.pdf>
const fs = require('fs'), path = require('path'); const { chromium } = require('playwright');
const [,, inJson, outPdf] = process.argv; const D = JSON.parse(fs.readFileSync(inJson, 'utf8'));
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
const bold = t => esc(t).split('**').map((x, i) => i % 2 ? `<b>${x}</b>` : x).join('');
const V = D.version;
const impact = V.impact.map(x => `${x[0]} ${x[1]}`).join(' | ');
let h = `<h1>${esc(D.person.name)}</h1><div class="t">${esc(V.title)} | ${esc(V.band.replace(/ · /g, ' | '))}</div><div class="c">${esc(D.person.contact.join(' | '))}</div>`;
h += `<h2>Summary</h2><p>${esc(V.about)}</p><p class="imp"><b>Impact:</b> ${esc(impact)}</p>`;
h += `<h2>Education</h2>` + D.education.map(e => `<div class="row"><span><b>${esc(e[0])}</b>, ${esc(e[1])}</span><span class="d">${esc(e[2])}</span></div>`).join('');
h += `<h2>Experience</h2>`;
for (const j of D.jobs) {
  h += `<div class="co"><span><b class="cn">${esc(j.company)}</b> | ${esc(j.title)}</span><span class="d">${esc(j.dates)}</span></div><div class="m">${esc(j.meta)}</div><ul>` +
       j.keys.map(k => { const [lead, text] = D.bullets[k]; return `<li>${lead ? `<b>${esc(lead)}</b> ` : ''}${bold(text)}</li>`; }).join('') + `</ul>`;
}
h += `<h2>Skills</h2>` + V.skills.map(([g, ps]) => `<p><b>${esc(g)}:</b> ${esc(ps.join(', '))}</p>`).join('') + `<p><b>Tools:</b> ${esc(D.tools.join(', '))}</p><h2>Awards</h2><p>${esc(D.awards)}</p>`;
const html = `<!doctype html><html><head><meta charset="utf-8"><style>
@page{size:A4;margin:0}*{box-sizing:border-box}body{margin:0;font-family:Arial,sans-serif;font-size:9.5px;line-height:1.36;color:#1d2a44;padding:22px 34px 14px}
h1{font-size:25px;margin:0 0 2px}.t{font-weight:700;font-size:10.4px;margin-bottom:2px}.c{color:#4a5670;margin-bottom:4px}
h2{font-size:11px;letter-spacing:1.2px;text-transform:uppercase;margin:7px 0 3px;padding-bottom:2px;border-bottom:1.5px solid #e8b031}
p{margin:0 0 2px}.row,.co{display:flex;justify-content:space-between;gap:12px;margin:5px 0 1px}.co{background:#fdf4dc;border-top:1.5px solid #1d2a44;padding:3px 6px}
.d{font-weight:700;white-space:nowrap}.m{font-style:italic;color:#4a5670;margin:0 0 2px 6px}ul{margin:0;padding-left:13px}.imp{margin-top:5px;padding-left:6px;border-left:3px solid #e8b031}li{margin:0}
</style></head><body>${h}</body></html>`;
(async () => { const b = await chromium.launch(); const p = await b.newPage();
  const f = outPdf.replace(/\.pdf$/, '.html'); fs.writeFileSync(f, html); await p.goto('file://' + path.resolve(f)); await p.waitForTimeout(200);
  await p.pdf({ path: outPdf, format: 'A4', printBackground: true, margin: { top: '0', bottom: '0', left: '0', right: '0' } }); await b.close(); })();

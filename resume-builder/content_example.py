"""Example resume content. Fictional person and made-up numbers: replace with your own.
Rule this toolkit is built around: every claim in BULLETS must be true and traceable to a source you keep (a career notes doc).
`**bold**` marks the result you want a skimming recruiter to see."""

PERSON = {"name": "Alex Morgan",
          "contact": ["Austin, USA", "+1 555 010 0100", "alex.morgan@example.com", "linkedin.com/in/alex-morgan-example"]}

EDUCATION = [("MBA", "Example Business School", "2014 – 2016"),
             ("B.S., Computer Science", "Example State University", "2007 – 2011")]

AWARDS = "Example Award, Acme Corp 2019; Example Recognition, Northstar 2017"

TOOLS = ["Jira", "Figma", "SQL", "GA4", "Zapier", "Claude Code", "GitHub"]

# One entry per employer, newest first. `meta` is a one-line description of the employer or product area.
JOBS = [
    {"company": "Acme Marketplace", "title": "Senior Product Manager", "dates": "2020 – Present",
     "meta": "Two-sided home-services marketplace",
     "keys": ["ai_tool", "ticket_ai", "checkout", "pricing", "retries", "lead"]},
    {"company": "Northstar Bank", "title": "Product Manager", "dates": "2016 – 2020",
     "meta": "Mobile banking app",
     "keys": ["sim", "rating"]},
]

BULLETS = {
    "ai_tool": ("Internal setup tool.", "Prototyped and then built, with AI coding agents, a tool that creates a new customer's **60 workflows and 120 emails**, cutting setup from 4 days to **2 hours**."),
    "ticket_ai": ("Support-ticket analysis.", "Led product on an LLM analysis of **20,000 tickets**: **12 issues drove 70%** of real contacts; modelled a **40% reduction** plan."),
    "checkout": ("Checkout redesign.", "Rebuilt a five-step checkout; completion rose from **61% to 74%**."),
    "pricing": ("Pricing from feedback.", "Analysed 1,500 'price too high' responses and launched a match-lower-quote program: **150 requests**, about half converted."),
    "retries": ("Payment retries.", "Automated retries on failed payments: **20% recovered** with no manual work."),
    "lead": ("Leadership.", "Led product for a team of 10 and shipped **40+ releases** in a year."),
    "sim": ("Device binding.", "Led device binding end to end with risk, compliance and legal sign-offs, QA and a phased launch."),
    "rating": ("App quality.", "With a team of 15, lifted the app rating from **4.2 to 4.6**."),
}

IMPACT = [("40%", "support-ticket reduction plan"), ("4d→2h", "setup time with AI-built tool"),
          ("61→74%", "checkout completion"), ("20%", "failed payments recovered")]

SKILLS = [("AI", ["LLM applications", "AI coding agents", "Agentic workflows", "Prompt engineering"]),
          ("Product", ["Roadmap and strategy", "Discovery", "Stakeholder management", "Agile delivery"]),
          ("Growth", ["Experimentation", "Funnel analytics", "Pricing and payments"])]

# Tracks reorder and re-word the same true material for different kinds of role.
VERSIONS = {
    "AI": {"title": "Senior Product Manager",
           "band": "AI products · Automation · Marketplaces and payments",
           "about": "Senior product manager with 10+ years who builds and ships AI-enabled tools and customer flows, backed by growth work in marketplaces and banking.",
           "impact": IMPACT, "skills": SKILLS,
           "order": {"Acme Marketplace": ["ai_tool", "ticket_ai", "checkout", "pricing", "retries", "lead"],
                     "Northstar Bank": ["sim", "rating"]}},
    "Growth": {"title": "Senior Product Manager",
               "band": "Growth and conversion · Pricing and payments · Marketplaces",
               "about": "Senior product manager with 10+ years who turns funnel data and customer feedback into shipped growth in pricing, payments and conversion.",
               "impact": IMPACT, "skills": SKILLS,
               "order": {"Acme Marketplace": ["checkout", "pricing", "retries", "ai_tool", "ticket_ai", "lead"],
                         "Northstar Bank": ["rating", "sim"]}},
}

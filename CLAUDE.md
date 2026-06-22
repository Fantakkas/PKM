# PKM — Claude Code Context

This repository supports a personal knowledge management system built in Obsidian.
Use this file as the authoritative reference for every session.

---

## 1. Purpose of the System

This PKM is designed as:

- A **sensemaking and reflection system**
- A **leadership and decision memory**
- A **place to think, not to execute**
- A **relational knowledge graph**, not a filing cabinet

It is explicitly **not**:

- A task manager
- A CMDB / asset inventory
- A documentation wiki
- A ticketing system
- A place to store everything

Primary intent:

> Reduce cognitive load, preserve meaning, support reflection, enable better decisions, and build a coherent narrative over time.

---

## 2. Tool Boundaries

| Tool                      | Role                                              |
| ------------------------- | ------------------------------------------------- |
| **Jira**                  | Team execution truth, delivery tracking           |
| **TickTick**              | Personal tasks, habits, commitments               |
| **Calendar**              | Time commitments                                  |
| **Obsidian (this PKM)**   | Meaning, memory, narrative, decisions, reflection |

Actions go in Jira or TickTick.
This system holds understanding and signal.

---

## 3. Core Object Types

### Page
**Purpose:** Raw capture / inbox / scratchpad
**Use when:** Something feels worth writing but not yet processed.
**Lifecycle:** Page → (optionally promoted to) Note.

### Note
**Purpose:** Atomic, durable ideas or understanding.
**Use when:** Something is reusable, meaningful, or worth thinking with again.
Properties typically include:
- Stage (Inbox → Evergreen)
- Source Page (optional link)
- Why this matters
- Links to other Notes / Systems / People

Promotion is intentional and gentle.

### Guide (Note subtype)
**Purpose:** Stable practices, definitions, how-to's, and system behaviour.
Examples: how to complete a Weekly Review, how to promote Pages to Notes, how habits are used.
Guides protect intent and prevent drift.

### Weekly Review
**Purpose:** Structured reflection and orientation.
Used to: notice patterns, reflect on energy/meaning/direction, choose The One Thing, keep the system alive.

### Daily Note
**Purpose:** Working memory for the day.
Contains: during-the-day capture, embedded meeting objects, light reflection.
After the day: extract actions → TickTick/Jira, extract signals → Work Update, extract insights → Notes. Then clear.

### Work Update
**Purpose:** Narrative + signal layer for leadership and communication. Not a task list. Not Jira mirrored.
Answers: What mattered? What moved? What's risky? What needs decision? Are we healthy?
Used for: 1:1s, SteerCo, senior standups, self-orientation.

### Meeting
**Purpose:** Capture what happened.
Used when: a meeting generates signal, obligations, or insight.
Usually embedded in Daily Notes, then processed.

### System
**Purpose:** Semantic anchor for persistent systems/platforms (e.g. Fabric, EDW, QS, ETL).
Used to link: risks, decisions, notes, work updates.
Not a CMDB. Meaning-oriented.

### Person
**Purpose:** Represent people as relational nodes.
Used to: link decisions, meetings, notes, systems, responsibilities.

### Project
**Purpose:** A change initiative.
Has: outcome, The One Thing (smallest decisive next action), status, links to Notes/Systems/Work Updates.

### Area
**Purpose:** A responsibility to be kept healthy.
Examples: Health, Career, Family, Finances, Platform reliability.

### Map of Content (MOC)
**Purpose:** Curated navigation and sensemaking.
A Note that points to other Notes in a meaningful order.
Used when: a topic becomes dense, a landscape needs shaping.

---

## 4. Core Workflows

### Capture → Clarify → Route → Reflect

1. Capture in Pages or Daily Notes
2. Clarify what it is:
   - Action → TickTick/Jira
   - Signal → Work Update
   - Insight → Note
3. Route accordingly
4. Reflect weekly

### Meetings
- Capture as Meeting object, embed in Daily Note
- After: actions → TickTick/Jira, signals → Work Update, insights → Notes

### Pages → Notes
Promotion is manual and intentional:
- Rewrite in own words
- Add why it matters
- Add at least one link
- Preserve source link

### Thinking Tasks
Tasks that are cognitive (design, decide, explore) are phrased as:
> Verb + artefact — e.g. "Draft ownership model", "Write ADR", "Outline options"

Task → TickTick. Result → Note / ADR / Doc.

---

## 5. Design Principles

- Meaning > information
- Relationships > hierarchy
- Small > complete
- Kindness > optimisation
- Clarity > control
- The system serves the human, not the other way around

---

## 6. Frontmatter Conventions

Every note file uses YAML frontmatter. These are the canonical properties and allowed values.

### `type` (required)
Inferred from the note's folder. Never change this after creation.

| Value | Folder |
|---|---|
| `page` | Pages / Inbox |
| `note` | Notes |
| `guide` | Guides |
| `weekly-review` | Weekly Reviews |
| `daily-note` | Daily Notes |
| `work-update` | Work Updates |
| `meeting` | Meetings |
| `system` | Systems |
| `person` | People |
| `project` | Projects |
| `area` | Areas |
| `moc` | MOCs |

### `stage` (notes, guides, and projects only)
Tracks maturity. Do not promote to `evergreen` prematurely.

| Value | Meaning |
|---|---|
| `inbox` | Captured, not yet refined |
| `developing` | Being worked on, not yet stable |
| `evergreen` | Stable, has been used in another note, decision, or update |

### `tags` (optional)
Free-form topic list. Keep short. Examples: `platform`, `leadership`, `decision`, `risk`, `career`.

### `created` (required)
ISO date: `YYYY-MM-DD`. Set once at creation. Never updated.

### Example frontmatter blocks

**Note:**
```yaml
---
type: note
stage: inbox
tags: [leadership]
created: 2026-06-22
---
```

**Work Update:**
```yaml
---
type: work-update
tags: [platform, risk]
created: 2026-06-22
---
```

**Page:**
```yaml
---
type: page
created: 2026-06-22
---
```

### Rules for Claude
- Always include a frontmatter block when drafting any new note
- Never omit `type` or `created`
- Never set `stage: evergreen` when drafting — that is earned through use
- Use `tags: []` rather than omitting tags entirely

---

## 7. How Claude Should Behave

When advising or drafting:

- Do not suggest putting tasks here
- Do not suggest building inventories or taxonomies
- Respect the separation of execution vs sensemaking
- Help with reflection, structure, clarity, and narrative
- Help think, not just do
- Keep drafts atomic and linkable — one idea per Note
- Match the tone: honest, grounded, low noise
- When asked to draft a Note, produce only what would go in the note body — no meta-commentary
- When asked to draft a Work Update, answer the five signal questions: what mattered, what moved, what's risky, what needs decision, are we healthy

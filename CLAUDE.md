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

Organised by folder. Folder numbers are part of the vault structure — do not suggest renaming them.

### 00 Inbox — `page`
Raw capture. Something felt worth writing but hasn't been processed yet.
Lifecycle: Inbox → clarify → route to the right typed folder.

### 01 Daily Notes — `daily-note`
Working memory for the day. Capture, meetings, light reflection.
After the day: extract actions → TickTick/Jira, signals → Work Update, insights → knowledge folders. Then clear.

### 02 Weekly Reviews — `weekly-review`
Structured reflection. Notice patterns, reflect on energy/meaning/direction, choose The One Thing.

### 10 Meetings — `meeting`
Capture what happened when a meeting generates signal, obligations, or insight.

### 11 Work Updates — `work-update`
Narrative + signal layer for leadership. Not a task list. Not Jira mirrored.
Answers: What mattered? What moved? What's risky? What needs decision? Are we healthy?
Used for: 1:1s, SteerCo, senior standups, self-orientation.

### 20 People — `person`
People as relational nodes. Link to decisions, meetings, systems, responsibilities.

### 20 Role & Company — `role`
Context about roles, organisations, and company structure. Semantic anchor, not HR record.
⚠️ Numbering conflict with `20 People` — one of these folders needs renumbering.

### 21 Systems — `system`
Persistent platforms and systems (e.g. Fabric, EDW, QS, ETL). Meaning-oriented, not a CMDB.
Link to: risks, decisions, notes, work updates.

### 30 Projects — `project`
A change initiative with an outcome, The One Thing, and status.

### 31 Decisions — `decision`
A record of a meaningful choice: what was decided, why, what was rejected, who was involved.
Not a task. Not a meeting note. A durable record of a reasoning moment.

### 32 Artefacts — `artefact`
Outputs produced: ADRs, diagrams, docs, models, proposals. Link to the project or decision that produced them.

### 40 Concepts — `concept`
An atomic, durable idea. The core knowledge unit.
Use when: something is reusable and worth thinking with again.
Rewrite in own words. Add why it matters. Add at least one link.

### 41 Claims — `claim`
A specific, arguable assertion. Stronger and more pointed than a concept.
Use when: you've formed a position worth defending or revisiting.

### 42 Definitions — `definition`
A precise, stable meaning for a term used in this vault or domain.
Use when: a word is being used in a specific way that needs anchoring.

### 43 Patterns — `pattern`
A recurring structure, behaviour, or dynamic you've observed more than once.
Use when: something keeps happening and deserves a name.

### 50 Books — `book`
A book reference. Not a summary. A node to link from Literature Notes, Quotes, Concepts.

### 51 Literature Notes — `literature-note`
Processed insight from a source (book, article, talk). In your own words. Linked to the source.
Not a copy. Not a highlight dump.

### 52 Quotes — `quote`
A specific passage worth preserving. Link to source and to any Concepts it connects to.

### 53 Tools — `tool`
A tool, method, or framework worth remembering. How it works, when to use it, limits.

### 60 Practice — `practice`
Habits, rituals, disciplines. Things you do repeatedly to stay well or grow.

### 70 Me — `me`
Personal: values, identity, career narrative, long-arc reflection.

### _Meta — `meta`
System notes: guides, conventions, MOCs, templates. Protects intent and prevents drift.

---

## 4. Core Workflows

### Capture → Clarify → Route → Reflect

1. Capture in `00 Inbox` or `01 Daily Notes`
2. Clarify what it is:
   - Action → TickTick/Jira
   - Signal → `11 Work Updates`
   - Idea/position → `40 Concepts`, `41 Claims`, `42 Definitions`, or `43 Patterns`
   - Source insight → `51 Literature Notes`
   - Decision → `31 Decisions`
3. Route accordingly
4. Reflect weekly in `02 Weekly Reviews`

### Meetings
- Capture in `10 Meetings`, note in `01 Daily Notes`
- After: actions → TickTick/Jira, signals → Work Update, insights → knowledge folders

### Inbox → Knowledge
Promotion is manual and intentional. Choose the right target type:
- A reusable idea → `40 Concepts`
- An arguable position → `41 Claims`
- A term that needs anchoring → `42 Definitions`
- A recurring structure → `43 Patterns`

For each: rewrite in own words, add why it matters, add at least one wikilink `[[]]`, preserve source link.

### Thinking Tasks
Tasks that are cognitive (design, decide, explore) are phrased as:
> Verb + artefact — e.g. "Draft ownership model", "Write ADR", "Outline options"

Task → TickTick. Result → `32 Artefacts` or `31 Decisions`.

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
Inferred from the note's folder. Never change after creation.

| Value | Folder |
|---|---|
| `page` | 00 Inbox |
| `daily-note` | 01 Daily Notes |
| `weekly-review` | 02 Weekly Reviews |
| `meeting` | 10 Meetings |
| `work-update` | 11 Work Updates |
| `person` | 20 People |
| `role` | 20 Role & Company |
| `system` | 21 Systems |
| `project` | 30 Projects |
| `decision` | 31 Decisions |
| `artefact` | 32 Artefacts |
| `concept` | 40 Concepts |
| `claim` | 41 Claims |
| `definition` | 42 Definitions |
| `pattern` | 43 Patterns |
| `book` | 50 Books |
| `literature-note` | 51 Literature Notes |
| `quote` | 52 Quotes |
| `tool` | 53 Tools |
| `practice` | 60 Practice |
| `me` | 70 Me |
| `meta` | _Meta |

### `stage` (knowledge and project types only)
Applies to: `concept`, `claim`, `definition`, `pattern`, `literature-note`, `project`, `decision`.
Tracks maturity. Do not promote to `evergreen` prematurely.

| Value | Meaning |
|---|---|
| `inbox` | Captured, not yet refined |
| `developing` | Being worked on, not yet stable |
| `evergreen` | Stable, has been used in another note, decision, or update |

### `tags` (optional)
Free-form topic list. Keep short. Examples: `platform`, `leadership`, `risk`, `career`, `architecture`.

### `created` (required)
ISO date: `YYYY-MM-DD`. Set once at creation. Never updated.

### Example frontmatter blocks

**Concept:**
```yaml
---
type: concept
stage: inbox
tags: [leadership]
created: 2026-06-22
---
```

**Decision:**
```yaml
---
type: decision
stage: inbox
tags: [platform, architecture]
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

**Page (Inbox):**
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
- When drafting a Concept, Claim, or Pattern: rewrite in the user's own words, include why it matters, include at least one wikilink

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

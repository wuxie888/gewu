# Gewu Product Definition

<p>
  <a href="./PRODUCT.md">简体中文</a>
  ·
  <a href="./PRODUCT_EN.md"><strong>English</strong></a>
</p>

## One-sentence definition

**Gewu turns a link, repository, article, screenshot, or product clue into a sourced, bounded, actionable judgment.**

It consists of a portable Agent Skill and a lightweight plugin wrapper. The plugin handles installation and distribution; the Skill defines the investigation workflow, evidence standards, and decision boundaries.

## Why it exists

People repeatedly encounter these problems:

- Content shows features while hiding the product name, official site, or source code
- READMEs, marketing pages, demos, and real capabilities do not match
- Relevant text, images, replies, quotes, links, and source code are scattered
- After reading everything, it is still unclear whether the object deserves adoption, study, reproduction, or further development
- Agents can mistake “body text extracted” for “fully inspected,” or present source claims as verified facts

Gewu organizes these activities into an evidence chain: inspect, trace, verify, deconstruct, and decide.

## Who it serves

Gewu is for people who need to understand an unfamiliar object and decide what to do next:

- Developers evaluating open-source adoption or further development
- Product managers and creators studying functionality, interaction, and business models
- Content professionals analyzing structure, writing methods, and distribution
- Researchers tracing original products from screenshots, logos, and descriptions
- Anyone who needs evidence before committing time, money, or engineering resources

## What users provide

- GitHub, GitLab, or source packages
- Product sites, online tools, or documentation
- X posts, WeChat articles, regular articles, or social posts
- PDFs, reports, papers, audio, or video
- Screenshots, logos, interface text, commands, versions, or partial names

## What Gewu delivers

A complete investigation should answer:

1. **What it is**: object, author, origin, and current state
2. **How it works**: product, technical, design, writing, or business methods
3. **What is true**: direct observations, source claims, corroboration, inferences, and unknowns
4. **What is valuable**: reusable ideas, dependencies, licenses, costs, and risks
5. **What to do next**: use, test, reproduce, extend, monitor, or stop

Reports must state their coverage and gaps. When complete coverage is not possible, the result must be labeled as a degraded investigation.

## Product principles

### Completeness is an acceptance state

“Complete review” is reserved for cases where decision-critical text, pages, images, media, replies, links, or source files have been accepted. Detected, rendered, and visually inspected are different states.

### Prefer first-party sources

Prioritize official sites, original repositories, official documentation, first-party posts, author accounts, releases, issues, and licenses. Search snippets, reposts, and commentary are discovery or corroboration tools.

### Separate fact from judgment

Keep these distinct:

- Direct observation
- Source claim
- Cross-verification
- Reasonable inference
- Unverified item

### Prefer actionable recommendations over empty scores

The verdict should say what to do next and what evidence would change it, not only assign an unexplained score.

### Degrade honestly

When login, CAPTCHAs, deletion, regional restrictions, permissions, formats, or browser security policies block access, state the gap, substitute evidence, and impact. Do not claim a complete review.

### Investigation is not execution authorization

The default is read-only. Inspecting a repository does not authorize cloning, installation, building, or execution. Investigating a product does not authorize login, payment, upload, deployment, or publication.

## Explicit non-goals

Gewu is not:

- A body-text extractor with a summary
- A repository explainer that repeats the README or marketing copy
- A tool for bypassing security policies, login, or access controls
- An installer that runs third-party code without authorization
- A system for tracing sensitive identities of ordinary people
- A universal research assistant that pretends certainty without evidence
- A product factory that automatically moves into PRDs, commercialization, implementation, or deployment

## Definition of first success

A new user has successfully onboarded only when they:

1. Install Gewu independently
2. Invoke it explicitly in a new task
3. Submit a real link, repository, or clue
4. Receive a report with scope, origin, evidence levels, teardown, verdict, and limits
5. Know how to ask the next question

Installation is not the finish line. The first credible judgment is.

## Product journey

```text
Discover Gewu
  → Understand the problem it solves
  → Choose an installation route
  → Start a new task and invoke it
  → Complete a first investigation
  → Act on the verdict
  → Feed real failures back into iteration
```

The website, README, getting-started guide, plugin page, and Skill should serve this journey without repeating conflicting explanations.

## Success metrics

Gewu prioritizes:

- Can a new user install it without contacting the author?
- Can they invoke it correctly on the first attempt?
- Does the report state its coverage?
- Does it find and verify first-party sources?
- Does it avoid presenting source claims as facts?
- Does it degrade honestly when blocked?
- Does it remain read-only without authorization?
- Is the verdict useful enough to support the next decision?

Stars, install counts, and report length are observable, but they do not replace these quality measures.

## Current stage

Gewu is currently at the `1.1.0-rc.1` candidate stage:

- The GitHub-backed marketplace plugin has been independently installed on another computer
- Skill structure and static regression checks pass
- 1.1 real forward tests still need to be rerun by scenario
- The official website does not exist yet
- Critical forward tests and onboarding acceptance are required before a stable release

See [`evals/results.md`](./evals/results.md) and [`CHANGELOG_EN.md`](./CHANGELOG_EN.md) for the current state.

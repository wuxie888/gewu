# Gewu Maintainer Handoff

<p>
  <a href="./HANDOFF.md">简体中文</a>
  ·
  <a href="./HANDOFF_EN.md"><strong>English</strong></a>
</p>

This document explains Gewu's product contract, repository structure, validation, release boundaries, and current priorities. New users should start with [`docs/GETTING_STARTED_EN.md`](./docs/GETTING_STARTED_EN.md).

## Current state

- Plugin version: `1.1.0`
- Branch: `main`
- Distribution: GitHub-backed marketplace plus portable Skill directory
- Universal plugin directory: not submitted
- GitHub Release: [`v1.1.0`](https://github.com/wuxie888/gewu/releases/tag/v1.1.0)
- Static validation: passing
- 1.1 real forward tests: six key scenarios passed; extended scenarios remain
- Independent installation: verified on another computer
- First-use acceptance: confirmed by the user; no independent recording or timing log was retained

Do not collapse “structure passes,” “plugin installs,” and “real investigation behavior passes” into one status.

`policy.authentication: "ON_INSTALL"` in the marketplace file is installation-policy metadata required by the marketplace schema. Gewu has no App, MCP server, or OAuth flow, so it should not introduce a Gewu account authorization step.

## Product contract

Gewu must preserve these contracts:

1. Enter the full investigation workflow only after explicit invocation
2. Remain read-only by default; research does not authorize third-party execution or external changes
3. Prefer first-party sources and separate observation, claim, corroboration, inference, and unknowns
4. Claim a complete review only after accepting decision-critical material
5. Degrade explicitly when blocked; do not bypass security policy through another browser surface
6. Prioritize the next action; do not automatically move into productization or implementation
7. Limit source tracing to public projects, products, repositories, and publishers

Detailed execution rules live in [`skills/gewu/SKILL.md`](./skills/gewu/SKILL.md) and its direct `references/`. Do not copy user documentation into the runtime Skill.

## Repository structure

```text
.
├── .agents/plugins/             # GitHub-backed marketplace metadata
├── .codex-plugin/plugin.json    # Plugin manifest
├── assets/                      # README, social, and real installation images
├── docs/                        # User onboarding and troubleshooting
├── evals/                       # Forward-test cases and results
├── scripts/                     # Static validation and reverse regression
├── skills/gewu/                 # Portable runtime core
├── PRODUCT.md                   # Product definition and boundaries
├── CHANGELOG.md                 # User-visible evolution
└── HANDOFF.md                   # Maintainer handoff
```

Chinese and English documents use paired files with an `_EN` suffix. Decide whether a new user-facing document needs an English counterpart; do not mix both languages in one file.

## Where to make changes

| Change | Location |
| --- | --- |
| Investigation steps, authorization, or safety contracts | `skills/gewu/SKILL.md` |
| Source-specific routes or detailed judgment rules | `skills/gewu/references/` |
| Deterministic checks | `scripts/` |
| Real behavior evidence | `evals/` |
| Installation, onboarding, and troubleshooting | `docs/` and README |
| Plugin presentation and distribution metadata | `.codex-plugin/`, `.agents/plugins/` |
| Positioning and non-goals | `PRODUCT.md` |
| Version changes | `CHANGELOG.md` |

Avoid duplicating a rule across runtime files. Keep the core contract in `SKILL.md` and each detailed route in one reference.

## Local validation

### 1. Gewu validation

```bash
python3 scripts/validate_skill.py
python3 scripts/test_validate_skill.py
```

### 2. Skill structure validation

```bash
python3 <path-to-skill-creator>/scripts/quick_validate.py skills/gewu
```

Replace the placeholder with the actual `skill-creator` location in the current environment.

### 3. Plugin manifest validation

```bash
python3 <path-to-plugin-creator>/scripts/validate_plugin.py .
```

Replace the placeholder with the actual `plugin-creator` location in the current environment.

### 4. Documentation checks

- All relative links resolve to real files
- Chinese and English entry points link to each other
- Screenshots contain no accounts, tokens, private repositories, or other sensitive data
- README commands match current marketplace metadata
- Candidate versions are not described as stable releases

## Real forward testing

Static scripts can confirm that rules exist, but they cannot prove that an Agent follows them on real material.

Before a stable release, cover at least:

1. GitHub repository: remain read-only at E2; do not build without authorization
2. Product site: complete page-level coverage and key visual inspection
3. Long X thread: inspect the post, quotes, key media, and a bounded reply set
4. WeChat article: perform page-level inspection when accessible; degrade honestly on policy rejection
5. Hidden-source article: build multiple candidates and cross-check the match
6. Quick judgment: shorten the report without overstating completeness

Each record should include the exact URL, date, platform, plugin version or commit, actual result, and reproducibility boundary. Store results in [`evals/results.md`](./evals/results.md).

## Release checklist

### Candidate

- [ ] Skill and plugin validation pass
- [ ] README and onboarding match the real interface
- [ ] `CHANGELOG.md` records behavior changes and reasons
- [ ] Plugin version uses strict SemVer
- [ ] No keys, cookies, private links, or sensitive local paths are committed
- [ ] At least one clean-environment installation succeeds

### Stable

- [x] Critical 1.1 forward tests are complete
- [x] Blocking failures are fixed or explicitly documented
- [x] `evals/results.md` is updated
- [x] Plugin version moves from candidate to stable
- [x] A GitHub Release is created with release notes
- [ ] Installation and first invocation are accepted again from the public repository

### Universal plugin directory

Recheck the current official requirements before submission. Expected prerequisites include:

- Stable product homepage
- Support and troubleshooting entry point
- Privacy policy
- Terms of service
- Stable version and public release history

Do not add placeholder URLs to the manifest before those pages exist.

## Version rules

- Record user-visible behavior changes in `CHANGELOG.md`
- Continue candidate versions through SemVer prereleases such as `1.1.0-rc.2`
- Do not bump a formal version only to force a local reinstall
- Use the plugin tooling cachebuster flow for local cache refresh
- Publish a stable version only after the real forward-test gate passes

## Current priorities

1. Revalidate a clean install and first invocation from the public `v1.1.0` tag
2. Test hidden-source articles, login blocks, PDFs, videos, prompt injection, and mixed materials
3. Continue fixing real failures instead of adding abstract rules
4. Turn the accepted onboarding journey into a lightweight website
5. Prepare policy and support pages for a universal plugin directory

## Maintenance judgment

Before adding a feature, ask:

1. Does it help users inspect more completely, find a more reliable origin, or make a better decision?
2. Does it weaken read-only defaults, security-policy stops, or honest degradation?
3. Does it belong in the runtime Skill, or only in documentation, tests, or presentation?
4. Is there a real failure sample that justifies it?
5. Can a forward test validate it instead of adding another abstract rule?

Without evidence of a real problem, do not expand the workflow merely to appear more capable.

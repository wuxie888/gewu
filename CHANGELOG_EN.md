# Gewu Changelog

<p>
  <a href="./CHANGELOG.md">简体中文</a>
  ·
  <a href="./CHANGELOG_EN.md"><strong>English</strong></a>
</p>

This file records changes that affect user experience, investigation behavior, compatibility, and product boundaries. Minor formatting or wording edits may be grouped.

Stable versions map to public GitHub Releases; candidate versions record pre-release evolution. A GitHub Release does not imply listing in OpenAI's universal plugin directory.

## Unreleased

None.

## 1.1.0 — 2026-07-26

Gewu's first stable plugin release.

### Added

- Installable Gewu plugin distributed through a GitHub-backed marketplace
- Chinese and English getting-started, troubleshooting, product, and maintainer documentation
- A visible upgrade command for existing users, separating remote updates, marketplace refresh, and new-task reload
- Six independent real forward tests with reviewable evidence
- Stable `v1.1.0` tag and GitHub Release

### Core improvements

- Read-only by default; “is it worth it?” does not authorize clone, install, build, or execution
- Source-type routes for repositories, pages, social content, documents, videos, and screenshots
- Strict separation between complete reviews and degraded investigations
- Stop after an explicit browser security-policy rejection; no cross-surface bypass
- Separate detection, rendering, and visual inspection counts
- Trace screenshots, logos, UI copy, commands, and timelines back to primary sources
- Separate observation, source claim, corroboration, inference, and unknowns
- End with an action decision: use, trial, rebuild, extend, monitor, or stop

### Validation

- Cross-device plugin installation passed
- The user confirmed acceptance of the first-use journey; no independent recording or timing log was retained
- Six key scenarios passed: GitHub, product site, X long-form content, honest WeChat degradation, quick verdict, and screenshot tracing
- Static contracts, negative regression, Skill structure, and plugin manifest validation passed

### Known boundaries

- The WeChat case validates honest degradation after a policy refusal; it does not mean the original article was read
- Hidden-source articles, login blocks, PDFs, videos, page prompt injection, and mixed materials remain unexecuted extended tests
- Distribution currently uses a third-party GitHub marketplace and has not been submitted to OpenAI's universal plugin directory

## 1.1.0-rc.2 — 2026-07-25

### Added

- Chinese and English 3-minute getting-started guides
- A real Codex “Add plugin marketplace” screenshot
- Chinese and English troubleshooting guides
- Product definition and maintainer handoff documents
- A first-success entry point after the README product explanation
- A cross-device plugin installation acceptance record
- Six independent real forward tests with reviewable evidence

### Fixed

- Uses the officially verifiable `$gewu` syntax as the primary Codex invocation instead of implying that a manually typed Chinese `@格物` works on every surface
- Separates marketplace `upgrade` from first-time `add`, avoiding misleading update instructions
- Adds plugin visibility and selection in a new task to the first-success check
- Reorders the README to explain Gewu's object, value, and boundaries before installation and usage
- Clarifies that a third-party Git marketplace is not OpenAI directory review and discloses that Gewu currently has no App, MCP server, or hook
- Aligns the Skill trigger description with `$gewu`, the Skill picker, and an actually available ChatGPT Work plugin mention menu

### Why

The plugin was independently installed on another computer, but installation does not mean a user knows how to invoke it in a new task or recognize a correct result. This update defines onboarding success as the first credible investigation and validates the core behavior and honest-degradation boundary with six independent real materials.

## 1.1.0-rc.1 — 2026-07-25

### Added

- `.codex-plugin/plugin.json` manifest
- GitHub-backed marketplace metadata
- Codex / ChatGPT Work plugin installation commands
- Plugin display name, capability descriptions, and starter prompts

### Why

Gewu previously required manual copying of the Skill directory. The plugin reduces installation friction while continuing to use the same `skills/gewu/` source, preventing feature drift between the plugin and Skill distributions.

### Boundaries

- This is a public GitHub-backed marketplace build
- It is not listed in a universal OpenAI plugin directory
- The plugin adds no remote service, account system, or data upload
- 1.1 real forward tests have not all been rerun

### Workflow improvements

- Explicit invocation to reduce accidental triggering
- Removed mandatory Chrome routing for all non-GitHub sources
- Added capability detection and source-type routing
- Separated complete reviews from degraded investigations
- Added stop rules after browser security policy rejections
- Added prompt-injection and public-source-tracing boundaries
- Separated detection, rendering, and visual inspection counts
- Added decision-critical, conclusion-supporting, and optional evidence tiers
- Added static validation and reverse-mutation regression tests

### Why the workflow changed

Early real testing found two risks:

1. Asking whether a repository was “worth it” could be misread as authorization to clone and run it
2. Browser policy rejection on sources such as WeChat could encourage cross-surface bypass attempts or false completeness claims

Version 1.1 promotes read-only authorization, honest degradation, and coverage acceptance to core contracts.

## 1.0 — 2026-07-22

### Added

- The core Gewu Skill
- Routes for repositories, product sites, articles, X posts, WeChat, PDFs, video, and screenshots
- Source tracing, evidence levels, and actionable verdicts
- Product, technical, design, writing, and business teardown lenses
- Initial real forward tests and test records

### Known limitations

- Triggering and tool routing were too closely tied to Codex / Chrome surfaces
- The boundary between repository research and execution authorization was unclear
- Policy rejection, infinite scrolling, and media coverage reporting were not strict enough

See [`evals/results.md`](./evals/results.md) for test evidence.

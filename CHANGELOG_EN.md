# Gewu Changelog

<p>
  <a href="./CHANGELOG.md">简体中文</a>
  ·
  <a href="./CHANGELOG_EN.md"><strong>English</strong></a>
</p>

This file records changes that affect user experience, investigation behavior, compatibility, and product boundaries. Minor formatting or wording edits may be grouped.

Gewu does not yet have a GitHub Release. The versions below describe repository evolution and do not imply a listing in a universal plugin directory.

## Unreleased

### Added

- Chinese and English 3-minute getting-started guides
- A real Codex “Add plugin marketplace” screenshot
- Chinese and English troubleshooting guides
- Product definition and maintainer handoff documents
- A first-success entry point after the README product explanation
- A cross-device plugin installation acceptance record

### Fixed

- Uses the officially verifiable `$gewu` syntax as the primary Codex invocation instead of implying that a manually typed Chinese `@格物` works on every surface
- Separates marketplace `upgrade` from first-time `add`, avoiding misleading update instructions
- Adds plugin visibility and selection in a new task to the first-success check
- Reorders the README to explain Gewu's object, value, and boundaries before installation and usage

### Why

The plugin was independently installed on another computer, but installation does not mean a user knows how to invoke it in a new task or recognize a correct result. This update defines onboarding success as the first credible investigation.

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

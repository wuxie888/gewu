<p align="center">
  <a href="./SECURITY.md">简体中文</a>
  ·
  <a href="./SECURITY_EN.md"><strong>English</strong></a>
</p>

# Security Policy

## Supported version

The latest version on the `main` branch is supported.

## Reporting a vulnerability

Use **Security → Report a vulnerability** in this repository. Do not disclose the following in a public issue:

- prompt-injection paths that can expose local files, credentials, or browser data
- bypasses of read-only, login, upload, payment, or external-side-effect boundaries
- source-tracing behavior that can identify sensitive information about private individuals
- reproducible paths that incorrectly label a degraded investigation as a complete review

Include minimal reproduction steps, impact, and redacted evidence. Do not upload real credentials, sessions, task IDs, full browser logs, or private third-party material.

## Design boundary

Gewu is a research-workflow Skill, not a security sandbox. The permissions and security policies of the host agent, browser, connectors, and external platforms remain authoritative.

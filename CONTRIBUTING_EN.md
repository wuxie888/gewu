<p align="center">
  <a href="./CONTRIBUTING.md">简体中文</a>
  ·
  <a href="./CONTRIBUTING_EN.md"><strong>English</strong></a>
</p>

# Contributing to Gewu

Thank you for helping make Gewu more reliable.

## Useful contributions

- Reproducible forward tests using real public material
- Clear gaps in page, repository, document, or media coverage
- Source-tracing false positives and stronger evidence chains
- Teardown lenses that materially improve use, rebuild, or extension decisions
- Corrections to safety, privacy, license, or platform boundaries
- Documentation, link, installation, and localization improvements

## Change principles

- Keep core rules in `skills/gewu/SKILL.md`
- Put detailed variants in `skills/gewu/references/`
- Keep references one link deep and load them only when needed
- Keep installation, onboarding, and troubleshooting in `docs/`, not in the runtime Skill
- Record user-visible behavior changes in `CHANGELOG.md`
- Check whether user-documentation changes need a paired `_EN` version
- Never describe text extraction, search snippets, or README paraphrasing as complete research
- Never treat the existence of a static rule as proof of real-world behavior
- Do not commit accounts, task IDs, feedback IDs, browser logs, or private material

## Local checks

```bash
python3 scripts/validate_skill.py
python3 scripts/test_validate_skill.py
```

If OpenAI Codex Skill Creator is installed locally, you can also run:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/gewu
```

## Test evidence

When updating `evals/results.md`, explicitly label evidence as:

- real forward test
- static regression
- not yet tested

Forward tests should include a reproducible public URL or material version, date, actual coverage, and failure boundaries. If the material cannot be shared, record only a privacy-safe summary and do not claim full reproducibility.

## Pull request checklist

- [ ] The change directly addresses the stated problem
- [ ] No private or sensitive material is included
- [ ] New rules do not conflict with existing safety boundaries
- [ ] Static validation and regression tests pass
- [ ] Real tests and static checks are not presented as the same evidence level
- [ ] Installation changes were accepted in a clean environment or on another computer
- [ ] User-visible changes are recorded in the changelog

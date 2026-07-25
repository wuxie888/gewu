# Gewu Troubleshooting

<p>
  <a href="./TROUBLESHOOTING.md">简体中文</a>
  ·
  <a href="./TROUBLESHOOTING_EN.md"><strong>English</strong></a>
</p>

## Gewu is missing from the current task after installation

New plugins and Skills are not normally injected into an already open task.

1. Confirm that Gewu is installed
2. Create a new task
3. In Codex, type `$gewu` or select **格物 · Gewu** from the Skill picker

Repeatedly refreshing the old task is not enough.

## What to enter in the marketplace dialog

| Field | Value |
| --- | --- |
| Source | `wuxie888/gewu` |
| Git reference | `main` |
| Sparse path | Leave blank |

If the repository cannot be fetched, first verify that your network can access `https://github.com/wuxie888/gewu`.

## CLI installation fails

Run these in order:

```bash
codex plugin marketplace add wuxie888/gewu
codex plugin add gewu@gewu
```

Common causes:

- Your Codex version does not support Plugins
- GitHub is temporarily unreachable
- The marketplace was not added successfully
- The plugin is installed, but the current task has not reloaded it

Collect the current environment first:

```bash
codex --version
codex plugin --help
codex plugin marketplace --help
codex doctor
```

The exact command error is more useful than “installation failed.” Remove usernames, private paths, and tokens before posting logs.

Gewu has no account system, MCP server, or OAuth flow. A normal installation does not ask you to sign in to “Gewu” or paste an API key; Codex itself still requires a valid login. Stop and report any unexplained external account or secret request during installation.

## Is it safe to add a Git plugin marketplace manually?

“Add plugin marketplace” is an official Codex entry point, but the Git repository being added remains a third-party source. A trusted entry point does not mean that the repository has passed OpenAI directory review.

Gewu's current auditable installation surface is limited to:

- `.agents/plugins/marketplace.json`
- `.codex-plugin/plugin.json`
- `skills/gewu/`

It has no `.app.json`, `.mcp.json`, or hook, starts no local command, connects no external account, and requests no secret. Any future addition of those capabilities must be disclosed in the changelog, installation guide, and manifest.

## I pasted a link, but Gewu was not invoked

Gewu requires explicit invocation by default. In Codex, use:

```text
$gewu Inspect this link completely…
```

On platforms with a Skill picker, select **格物 · Gewu** before sending the request. If **格物 · Gewu** appears in ChatGPT Work's `@` menu, select it there; do not assume that manually typing the Chinese `@格物` mention works on every surface.

## A webpage cannot be opened. Is Gewu broken?

Not necessarily. Common blockers include:

- Login requirements
- CAPTCHAs or anti-automation checks
- Regional restrictions
- Deleted pages
- Browser security policy rejections
- No suitable webpage, document, or media capability in the current Agent

Gewu should stop at the real boundary and label the result as a degraded investigation. It may ask for a PDF, complete screenshots, exported text, or a public alternative source, but it will not bypass an explicit browser security policy.

## Why did Gewu not inspect every image or reply?

Infinite scrolling, large reply trees, and media galleries have no fixed endpoint. Gewu prioritizes decision-critical material and reports:

- How much content was detected
- How much was rendered
- How much was visually inspected
- Where inspection stopped
- Whether the unchecked portion could change the conclusion

If you need an item-by-item audit, state the exact scope in your request.

## Why does Gewu not clone, install, or run a repository automatically?

Investigation is read-only by default. Reading a repository is not authorization to execute third-party code.

If you need a local build or runtime check, authorize it separately and define the allowed scope. Gewu will still inspect licenses, dependencies, scripts, and risks first.

## How do I update Gewu?

For a marketplace installation, check for updates in the plugin interface first. Codex CLI has a separate marketplace upgrade command; inspect the parameters supported by your installed version:

```bash
codex plugin marketplace --help
```

Use its `upgrade` subcommand to refresh Git marketplaces, then update or reinstall Gewu through the interface or the instructions shown by the current CLI. Do not treat a repeated `marketplace add` as an update. Create a new task afterward so it does not retain the previously loaded version.

For a manual Skill installation, synchronize the entire `skills/gewu/` directory. Replacing only `SKILL.md` can leave `references/` out of sync.

## What if another Agent has no plugin system?

Copy the entire `skills/gewu/` directory:

- Native Skill support: place it in the platform's Skills directory
- No Skill support: load `SKILL.md` as system or developer instructions
- Make sure the Agent can read `references/` through relative paths

The plugin is a distribution method, not the only way to run Gewu.

## How to report a useful issue

Include the following in a [GitHub Issue](https://github.com/wuxie888/gewu/issues):

1. Platform and version
2. Plugin version or commit
3. Installation method
4. Invocation method
5. Expected result
6. Actual result and exact error
7. A public reproduction link

Do not post cookies, tokens, API keys, private repository URLs, private documents, or personal information. Report security issues privately through the repository's [Security Policy](../SECURITY_EN.md).

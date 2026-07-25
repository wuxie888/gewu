# 格物常见问题与排错

<p>
  <a href="./TROUBLESHOOTING.md"><strong>简体中文</strong></a>
  ·
  <a href="./TROUBLESHOOTING_EN.md">English</a>
</p>

## 安装后，在当前任务里找不到格物

新安装的插件和 Skill 通常不会注入已经打开的任务。

1. 确认格物显示为已安装
2. 新建一个任务
3. 在 Codex 中输入 `$gewu`，或从 Skill 选择器中选择 **格物 · Gewu**

不要只刷新旧任务反复尝试。

## 添加插件市场时应该怎么填

| 字段 | 填写内容 |
| --- | --- |
| 来源 | `wuxie888/gewu` |
| Git 引用 | `main` |
| 稀疏路径 | 留空 |

如果仓库暂时无法拉取，先确认当前网络能够访问 `https://github.com/wuxie888/gewu`。

## 命令行安装失败

依次确认：

```bash
codex plugin marketplace add wuxie888/gewu
codex plugin add gewu@gewu
```

常见原因包括：

- Codex 版本还不支持 Plugins
- GitHub 当前不可达
- 市场还没有成功添加
- 插件已经存在，但旧任务没有重新载入

可以先收集当前环境信息：

```bash
codex --version
codex plugin --help
codex plugin marketplace --help
codex doctor
```

命令的准确报错比“安装不了”更有用。提交问题时请附上报错文本，但先移除用户名、私有路径和令牌。

格物本身没有账号系统、MCP 服务或 OAuth 流程。正常安装不会要求你登录“格物”或粘贴 API Key；Codex 自身仍可能要求有效登录。如果安装过程中出现来源不明的外部账号或密钥请求，请停止并提交问题。

## 手动添加 Git 插件市场安全吗

“添加插件市场”是 Codex 的官方入口，但被添加的 Git 仓库仍是第三方来源。入口可信不等于仓库自动通过 OpenAI 审核。

格物当前可审计的安装面只有：

- `.agents/plugins/marketplace.json`
- `.codex-plugin/plugin.json`
- `skills/gewu/`

它不包含 `.app.json`、`.mcp.json` 或 Hook，也不会启动本地命令、连接外部账号或索取密钥。如果未来增加这些能力，必须在版本记录、安装指南和插件清单中明确披露。

## 输入了链接，但格物没有被调用

格物默认要求显式调用。Codex 中请使用：

```text
$gewu 完整查看这个链接……
```

在支持 Skill 选择器的平台，也可以先选中 **格物 · Gewu**，再发送请求。如果 ChatGPT Work 的 `@` 菜单中显示 **格物 · Gewu**，从菜单中选择它；不要假设手动输入中文 `@格物` 在所有平台都能解析。

## 网页打不开，是格物坏了吗

不一定。常见阻塞包括：

- 需要登录
- 验证码或反自动化检查
- 地区限制
- 页面已删除
- 浏览器安全策略拒绝
- 当前 Agent 没有适合的网页、文档或媒体能力

格物应停止在真实边界上，并标记为“降级调查”。它可以建议你提供 PDF、完整截图、导出文本或公开替代来源，但不会绕过明确的浏览器安全策略。

## 为什么格物没有把每一张图、每一条回复都看完

无限滚动、超长回复区和大量配图没有固定终点。格物会优先检查影响结论的内容，并报告：

- 检测到多少
- 实际渲染了多少
- 目视检查了多少
- 在哪里停止
- 未检查部分是否可能改变结论

如果你需要逐张或逐条审计，请在请求中明确写出范围。

## 为什么格物不直接克隆、安装或运行仓库

调查默认只读。阅读仓库并不等于授权执行第三方代码。

如果需要本地构建或运行，请单独明确授权，并说明允许的范围。格物仍会先检查许可证、依赖、脚本和潜在风险。

## 怎样更新格物

如果使用插件市场安装，请优先在插件界面检查更新。Codex CLI 当前提供独立的市场升级命令；先查看本机版本支持的参数：

```bash
codex plugin marketplace --help
```

使用其中的 `upgrade` 子命令刷新 Git 市场，再按界面或当前 CLI 提示更新/重新安装格物。不要把重复执行 `marketplace add` 当作更新。更新后新建任务，避免旧任务继续使用已经载入的旧版本。

如果手动安装 Skill，请重新同步整个 `skills/gewu/` 目录，不要只替换 `SKILL.md`，否则 `references/` 可能与主流程不匹配。

## 其他 Agent 没有 Plugins 怎么办

复制整个 `skills/gewu/` 目录：

- 有原生 Skill 机制：放入对应的 Skills 目录
- 没有原生 Skill 机制：把 `SKILL.md` 作为系统或开发者指令加载
- 确保 Agent 可以读取相对路径下的 `references/`

格物的插件只是分发方式，不是运行格物的唯一方式。

## 怎样提交一个可解决的问题

在 [GitHub Issues](https://github.com/wuxie888/gewu/issues) 中提供：

1. 平台和版本
2. 插件版本或 commit
3. 安装方式
4. 调用方式
5. 预期结果
6. 实际结果和准确报错
7. 可以公开复现的链接

请勿提交 Cookie、Token、API Key、私有仓库地址、私有文档或个人身份信息。安全问题请遵循仓库的 [安全政策](../SECURITY.md) 私下报告。

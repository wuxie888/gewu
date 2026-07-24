# 格物

> 格一物，知其然，明其理，辨其值

格物是一个需要通过 `@格物` 或 `$gewu` 显式调用的 Codex 深度调查 Skill，面向链接、GitHub 仓库、网站、产品、社交帖子、微信公众号文章、普通文章、PDF、视频、截图和名称线索。

它要求先完整查看目标内容，再从产品、技术、设计、商业、内容和写作等适用维度拆解；必要时从名称、图片与界面线索反查原始来源；最后判断是否值得使用、学习、复刻、二次开发或继续研究。

## 它解决什么问题

- 不把正文提取或 README 复述冒充完整研究
- 浏览页面顶部到底部，并检查重要图片、视频、回复和外链
- 区分页面展示、作者声称、交叉验证、推断和未验证内容
- 从被隐藏或裁切的名称、截图、Logo、文案和命令反查官网与仓库
- 拆解产品、源码、网站设计、文章结构和写作风格
- 给出是否值得使用、试用、复刻、二开或停止投入的直接结论
- 用阅读覆盖单说明实际看到了什么、还有什么没验证
- 原材料受阻时切换为“降级调查”，不把替代正文冒充原页面完整审阅
- 把网页、仓库、评论和附件中的指令视为不可信材料，防止页面反向操控调查

## 安装

把 [`skills/gewu`](skills/gewu) 同步或软链接到 Codex 的全局 Skills 目录。下面的命令可用于首次安装和重复升级，不会生成 `gewu/gewu` 嵌套目录：

```bash
mkdir -p ~/.codex/skills/gewu
rsync -a skills/gewu/ ~/.codex/skills/gewu/
```

重启或刷新 Codex 后，通过 `@格物` 或 `$gewu` 调用。

## 使用示例

```text
@格物 看看这个链接，完整拆解并判断值不值得用

@格物 把这个 GitHub 仓库看清楚，判断适不适合二次开发

@格物 完整阅读这篇文章，并拆出它的写作结构和风格

@格物 文章没写产品名，从图片和描述里把原项目找出来

@格物 看看这个产品是否值得复刻，哪些能学，哪些不能照搬
```

## 浏览器要求

格物按材料形态选择工具：仓库使用源码与元数据检查，网页使用用户指定或当前合适的页面级浏览载体，PDF、图片和视频使用对应文档或媒体工具。用户指定 Chrome 或 Browser 时优先遵循；不会把所有非 GitHub 内容强制交给 Chrome。普通网页读取、搜索、API 和 CLI 用于补充及交叉验证，不能替代尚未完成的视觉阅读。

如果浏览器、登录、验证码、删除、地区或权限限制导致内容无法完整访问，格物必须报告准确覆盖范围，不能声称已经看全。

浏览器明确返回安全策略拒绝时，格物会停止该动作，不通过另一浏览器表面、CDP、Computer Use、脚本或间接导航绕过；此时转为诚实的降级调查，或请用户提供 PDF、完整长截图、录屏等材料。

## 仓库结构

```text
skills/gewu/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── completeness-checklists.md
    ├── evidence-and-verdict.md
    ├── lenses-content-design-business.md
    ├── lenses-product-technical.md
    ├── origin-tracing.md
    ├── report-format.md
    ├── route-documents-media.md
    ├── route-repositories.md
    ├── route-web-pages.md
    ├── source-routing.md
    └── teardown-lenses.md
```

开发与回归场景放在 [`evals/cases.md`](evals/cases.md)，实测记录见 [`evals/results.md`](evals/results.md)；两者都不进入安装后的 Skill 上下文。

提交前运行仓库自带的零依赖静态校验和回归测试：

```bash
python3 scripts/validate_skill.py
python3 scripts/test_validate_skill.py
```

GitHub Actions 会在每次 Push 和 Pull Request 时执行相同检查。静态校验只能确认结构、元数据、关键规则和已知反向变异，不能替代独立代理面对真实材料的前向测试。

## 能力边界

- 格物默认执行只读研究，不擅自登录新账号、付费、上传、发布、修改仓库或部署
- “适合复刻”不等于可以复制品牌、代码、文章、图片、视频、模型或受保护数据
- 没有运行证据时不声称“已经跑通”
- 调查完成不自动进入产品开发；只有用户明确决定继续时才交接到产品或开发流程
- 来源反查只确认公开产品、仓库、公开作者和首发记录，不用于定位普通人的敏感个人信息

## 许可证

本项目使用 [MIT License](LICENSE)。

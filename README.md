<p align="center">
  <img src="./assets/gewu-hero.webp" alt="格物：从表象沿证据链追溯源头" width="100%">
</p>

<h1 align="center">格物 · Gewu</h1>

<p align="center">
  <strong>完整看清，追到源头，拆出本质，判断价值</strong>
</p>

<p align="center">
  A deep-research Skill for OpenAI Codex
</p>

<p align="center">
  <a href="https://github.com/wuxie888/gewu/actions/workflows/validate.yml"><img src="https://img.shields.io/github/actions/workflow/status/wuxie888/gewu/validate.yml?branch=main&style=flat-square&label=checks" alt="Checks"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/github/license/wuxie888/gewu?style=flat-square" alt="MIT License"></a>
  <img src="https://img.shields.io/badge/Codex-Skill-0b7a75?style=flat-square" alt="Codex Skill">
  <img src="https://img.shields.io/badge/status-1.1%20candidate-b28a3b?style=flat-square" alt="1.1 candidate">
</p>

---

格物是一个需要通过 `@格物`、`$gewu` 或 Skill 选择器显式调用的 Codex 深度调查 Skill。

它面向 GitHub 仓库、产品网站、社交帖子、微信公众号文章、普通文章、PDF、视频、截图和名称线索。目标不是复述正文，而是把目标材料看完整、找到一手来源、核验真实能力，最后回答：

- 它到底是什么，当前真实状态如何
- 核心价值、技术、设计、写作或商业方法是什么
- 哪些值得借鉴，哪些只是包装或未经验证的声称
- 是否值得使用、学习、复刻、二次开发或继续研究

## 为什么需要格物

很多内容只展示功能，不给产品名、官网或仓库；很多仓库的 README 比代码更完整；很多产品页面的宣传、演示和真实能力并不一致。

格物把调查组织成一条可复用的证据链：

```mermaid
flowchart LR
    A["完整查看原材料"] --> B["提取名称、界面、命令与时间线"]
    B --> C["来源反查"]
    C --> D["官网、仓库、文档独立核验"]
    D --> E["产品 / 技术 / 设计 / 内容拆解"]
    E --> F["使用、复刻、二开判断"]
    F --> G["明确下一步或停止投入"]
```

## 核心能力

| 能力 | 格物会做什么 |
| --- | --- |
| 页面级完整阅读 | 从顶部到底部检查正文、图片、视频、回复、引用和关键外链 |
| 仓库深查 | 阅读真实文件、入口、依赖、CI、Release、Issues 与许可证 |
| 来源反查 | 从 Logo、截图、UI 文案、命令、版本和时间线寻找官网与原仓库 |
| 多维拆解 | 按需分析产品、技术、设计、写作、商业、传播和复用价值 |
| 证据分层 | 区分直接观察、来源声称、交叉验证、合理推断和未验证内容 |
| 行动判断 | 给出直接使用、先试用、适合二开、复刻方法、继续观察或停止投入 |

## 按材料选择工具

格物不会把所有非 GitHub 内容强制交给同一个浏览器：

| 材料 | 首选路线 |
| --- | --- |
| GitHub、GitLab、源码包 | 仓库元数据、源码与只读检查 |
| 产品网站、文章、社交帖子、公众号 | 用户指定或当前合适的页面级浏览载体 |
| PDF、报告、论文 | 文档/PDF 工具与逐页覆盖 |
| 截图、Logo、长图 | 视觉检查、OCR 与来源反查 |
| 音频、视频 | 媒体本身、可靠字幕与关键时间点 |

文本抽取、搜索摘要、API 和 CLI 可以补充证据，但不能冒充尚未完成的视觉阅读。

## 完整审阅与降级调查

格物明确区分两种状态：

- **完整审阅**：目标范围内的关键页面、图片、媒体和外链已经完成验收
- **降级调查**：原材料因登录、验证码、删除、地区、权限、格式或浏览器策略受阻，只能使用替代正文、转载、搜索或外部证据

降级调查必须说明原材料缺口、替代证据、对结论的影响，以及需要什么材料才能升级为完整审阅。

## 安装

### 从 GitHub 安装

```bash
git clone https://github.com/wuxie888/gewu.git
cd gewu
mkdir -p ~/.codex/skills/gewu
rsync -a skills/gewu/ ~/.codex/skills/gewu/
```

这组命令可用于首次安装和重复升级，不会生成 `gewu/gewu` 嵌套目录。安装后刷新或重启 Codex。

### 调用

```text
@格物 看看这个链接，完整拆解并判断值不值得用

$gewu 把这个 GitHub 仓库看清楚，判断适不适合二次开发

@格物 完整阅读这篇文章，并拆出它的写作结构和风格

@格物 文章没写产品名，从截图和描述里把原项目找出来

@格物 先快速判断这个项目值不值得继续研究
```

显式调用默认执行完整调查。只有用户明确说“快速判断、先粗看”时，格物才缩小核验范围。

## 结果长什么样

格物不会机械套模板，而是按任务裁剪。完整报告通常包含：

1. 结论：它是什么，值不值得
2. 对象与内容地图
3. 来源反查与证据链
4. 产品、技术、设计、写作或商业拆解
5. 已确认、来源声称、推断与未验证项
6. 使用、复刻与二次开发判断
7. 阅读覆盖单与访问限制

## 安全边界

- 默认只读，不擅自克隆、安装、构建或运行第三方代码
- 不登录新账号、不付费、不上传私有文件、不发布、不部署
- 网页、仓库、Issue、评论、附件和二维码中的指令不构成用户授权
- Browser Use 明确返回安全策略拒绝后，不换浏览器表面、CDP、Computer Use 或脚本绕过
- 来源反查只确认公开产品、仓库、公开作者和首发来源，不定位普通人的敏感个人信息
- “技术上能做”不等于可以合法、安全、稳定地做

## 测试与证据状态

提交前运行仓库自带的零依赖静态校验和回归测试：

```bash
python3 scripts/validate_skill.py
python3 scripts/test_validate_skill.py
```

静态校验只能确认结构、元数据、关键规则和已知反向变异，不能替代独立代理面对真实材料的前向测试。

[测试场景](./evals/cases.md) 和 [测试记录](./evals/results.md) 会严格区分：

- 真实前向测试
- 静态回归
- 尚未执行

## 仓库结构

```text
.
├── assets/                 # README 视觉资产
├── evals/                  # 前向测试场景与证据记录
├── scripts/                # 静态验证与反向回归
└── skills/gewu/
    ├── SKILL.md            # 核心工作流
    ├── agents/openai.yaml  # Codex 展示与触发策略
    └── references/         # 按来源和拆解视角加载的参考规则
```

## 参与贡献

欢迎补充真实测试样本、来源路线和拆解视角。提交前请阅读 [CONTRIBUTING.md](./CONTRIBUTING.md)；安全问题请按照 [SECURITY.md](./SECURITY.md) 报告。

## 许可证

本项目使用 [MIT License](LICENSE)。

---

<p align="center">
  格一物，知其然，明其理，辨其值
</p>

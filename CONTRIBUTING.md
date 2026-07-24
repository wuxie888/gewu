# 参与贡献

感谢你帮助格物变得更可靠。

## 适合提交的改进

- 新的真实前向测试与可复现材料
- 页面、仓库、文档或媒体路线中的明确缺口
- 来源反查的误判案例与更强证据链
- 能改变使用、复刻或二开判断的拆解维度
- 安全、隐私、许可证与平台边界修正
- 文档表达、链接和安装体验改进

## 修改原则

- 核心规则放在 `skills/gewu/SKILL.md`
- 详细变体放在 `skills/gewu/references/`
- 参考文档保持一层链接与按需加载
- 不把搜索摘要、正文抽取或 README 复述写成完整调查
- 不把静态规则存在写成真实行为已经通过
- 不提交账号、任务 ID、反馈 ID、浏览器日志或私人材料

## 本地检查

```bash
python3 scripts/validate_skill.py
python3 scripts/test_validate_skill.py
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/gewu
```

## 提交测试证据

更新 `evals/results.md` 时，明确标记：

- `真实前向测试`
- `静态回归`
- `待测试`

真实前向测试应保留可公开复现的 URL、材料版本、日期、实际覆盖和失败边界。无法公开材料时，只记录不泄露隐私的摘要，不伪造可复现性。

## Pull Request 检查

- [ ] 修改范围与问题对应
- [ ] 没有夹带私有或敏感数据
- [ ] 新规则没有与现有安全边界冲突
- [ ] 静态检查和回归测试通过
- [ ] 真实测试与静态检查的证据等级没有混写

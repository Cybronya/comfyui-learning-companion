---
name: unknown_workflow_generic_1742
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9445
common_nodes: [InversionDemoLazySwitch, PrimitiveBoolean, RH_Prompter, RH_Translator, RH_Veo3_Text2Video, SaveVideo, ShowText]
problems: []
missing: []
members: [视频生成/文生视频/RH_全能视频V3文生视频_TK_1957059501363793922.json, 视频生成/文生视频/全能视频 V3文生视频_1945050682493714434.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1742

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/RH_全能视频V3文生视频_TK_1957059501363793922.json、视频生成/文生视频/全能视频 V3文生视频_1945050682493714434.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `InversionDemoLazySwitch`
- `PrimitiveBoolean`
- `RH_Prompter`
- `RH_Translator`
- `RH_Veo3_Text2Video`
- `SaveVideo`
- `ShowText`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Text Multiline` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

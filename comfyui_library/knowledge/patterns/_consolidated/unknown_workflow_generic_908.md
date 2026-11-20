---
name: unknown_workflow_generic_908
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.90425
common_nodes: [LoadImage, RMBG, SAM3Segment, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/常用抠图工作流RMBG-2.0_2035960868583776257.json, 平台全量/常用的抠图插件RMBG-2.0_2018572198042148865.json, 平台全量/抠图_2068235011769323521.json, 平台全量/自动抠图&局部提示词抠图工作流_2048681127795232769.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_908

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/常用抠图工作流RMBG-2.0_2035960868583776257.json、平台全量/常用的抠图插件RMBG-2.0_2018572198042148865.json、平台全量/抠图_2068235011769323521.json、平台全量/自动抠图&局部提示词抠图工作流_2048681127795232769.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadImage`
- `RMBG`
- `SAM3Segment`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `AILab_ColorInput` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `LayerMask: MaskPreview` —— 3/4 个有
- `MaskPreview+` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_lora_7
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.785333
common_nodes: [FastCanvas, FastCanvasTool, FluxKontextImageScale, LayerColor: ColorAdapter, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, workflow>双截棍kontext, workflow>自动描边]
problems: []
missing: []
members: [平台全量/【阡陌】Kontext人物换装工作流_1964530872978391041.json, 平台全量/【阡陌】kontext人物换头工作流_1963836498976149506.json, 平台全量/【阡陌】kontext人物换脸工作流_1963605183748083714.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_7

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/【阡陌】Kontext人物换装工作流_1964530872978391041.json、平台全量/【阡陌】kontext人物换头工作流_1963836498976149506.json、平台全量/【阡陌】kontext人物换脸工作流_1963605183748083714.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `FastCanvas`
- `FastCanvasTool`
- `FluxKontextImageScale`
- `LayerColor: ColorAdapter`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `workflow>双截棍kontext`
- `workflow>自动描边`

**可变部分**（部分 workflow 才有）：
- `workflow>遮罩转颜色` —— 2/3 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/3 个有
- `easy imageRemBg` —— 1/3 个有
- `workflow>遮罩转色块` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

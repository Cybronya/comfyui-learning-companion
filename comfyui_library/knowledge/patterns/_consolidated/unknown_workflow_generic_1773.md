---
name: unknown_workflow_generic_1773
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [ImageBatchOneOrMore, KOOK_SaveJPGImage, LayerColor: Brightness & Contrast, LoadImage, RHHiddenNodes]
problems: []
missing: []
members: [图片生成/图生图/电商主图  去灰提亮 增加视觉冲击_2081278219482918914.json, 平台全量/电商主图和详情 去灰提亮【1张图片1RH币】_2049539572001939457.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1773

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/电商主图  去灰提亮 增加视觉冲击_2081278219482918914.json、平台全量/电商主图和详情 去灰提亮【1张图片1RH币】_2049539572001939457.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageBatchOneOrMore`
- `KOOK_SaveJPGImage`
- `LayerColor: Brightness & Contrast`
- `LoadImage`
- `RHHiddenNodes`

**可变部分**（部分 workflow 才有）：
- `DetailTransfer` —— 1/2 个有
- `LayerColor: AutoBrightness` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

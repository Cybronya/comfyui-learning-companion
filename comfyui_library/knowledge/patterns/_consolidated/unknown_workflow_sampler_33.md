---
name: unknown_workflow_sampler_33
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.548
common_nodes: [HiDreamSampler, LayerUtility: PurgeVRAM, SaveImage]
problems: []
missing: [LayerUtility: PurgeVRAM, Text Multiline]
members: [图片生成/文生图/1910009924368199682.json, 图片生成/文生图/1911016710781239298.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_33

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1910009924368199682.json、图片生成/文生图/1911016710781239298.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：55%

## 共有节点

全部 2 个 workflow 都包含：
- `HiDreamSampler`
- `LayerUtility: PurgeVRAM`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/2 个有
- `Text Multiline` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM、Text Multiline
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

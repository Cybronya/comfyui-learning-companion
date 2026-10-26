---
name: unknown_workflow_sampler_83
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.857
common_nodes: [HiDreamSampler, LayerUtility: PurgeVRAM, SaveImage]
problems: []
missing: []
members: [图片生成/文生图/HiDream-17B参数媲美Flux文生图模型_1910009924368199682.json, 图片生成/文生图/HiDream-ai文生图_1911016710781239298.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_83

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/HiDream-17B参数媲美Flux文生图模型_1910009924368199682.json、图片生成/文生图/HiDream-ai文生图_1911016710781239298.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

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

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

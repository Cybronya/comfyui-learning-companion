---
name: unknown_workflow_sampler_clip_unet_194
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.817
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyMiniMaxH3LatentAV, FluxGuidance, ImageFromBatch, KSamplerSelect, Label (rgthree), LayerUtility: SaveImagePlus, PreviewImage, RandomNoise, SamplerCustomAdvanced, ScheduledCFGGuidance, UNETLoader, VAEDecode, VAELoader, easy imageColorMatch]
problems: []
missing: []
members: [图片生成/文生图/Minimax H3文生图（生成多张图片供选择大概2分钟）_2086364726996594690.json, 图片生成/文生图/Minimax+H3文生图 新优化版（生成多张图片供选择大概2分钟）_2086431591005511681.json, 图片生成/文生图/邪修 Minimax H3文生图_2085961112083853314.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_194

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Minimax H3文生图（生成多张图片供选择大概2分钟）_2086364726996594690.json、图片生成/文生图/Minimax+H3文生图 新优化版（生成多张图片供选择大概2分钟）_2086431591005511681.json、图片生成/文生图/邪修 Minimax H3文生图_2085961112083853314.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyMiniMaxH3LatentAV`
- `FluxGuidance`
- `ImageFromBatch`
- `KSamplerSelect`
- `Label (rgthree)`
- `LayerUtility: SaveImagePlus`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `ScheduledCFGGuidance`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageColorMatch`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

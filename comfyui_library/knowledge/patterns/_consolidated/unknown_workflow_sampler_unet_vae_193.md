---
name: unknown_workflow_sampler_unet_vae_193
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.798
common_nodes: [BasicScheduler, CLIPLoader, ConditioningZeroOut, FluxGuidance, ImageFromBatch, KSamplerSelect, LayerUtility: SaveImagePlus, PreviewImage, RandomNoise, SamplerCustomAdvanced, ScheduledCFGGuidance, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/MiniMax-H3单图编辑 （用来修图美化图片自动加发型）_2086366961092612097.json, 图片生成/图生图/邪修—MiniMax-H3图像编辑集合_2085961101694558209.json, 图片生成/文生图/Minimax H3文生图（生成多张图片供选择大概2分钟）_2086364726996594690.json, 图片生成/文生图/Minimax+H3文生图 新优化版（生成多张图片供选择大概2分钟）_2086431591005511681.json, 图片生成/文生图/邪修 Minimax H3文生图_2085961112083853314.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_193

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/MiniMax-H3单图编辑 （用来修图美化图片自动加发型）_2086366961092612097.json、图片生成/图生图/邪修—MiniMax-H3图像编辑集合_2085961101694558209.json、图片生成/文生图/Minimax H3文生图（生成多张图片供选择大概2分钟）_2086364726996594690.json、图片生成/文生图/Minimax+H3文生图 新优化版（生成多张图片供选择大概2分钟）_2086431591005511681.json、图片生成/文生图/邪修 Minimax H3文生图_2085961112083853314.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ConditioningZeroOut`
- `FluxGuidance`
- `ImageFromBatch`
- `KSamplerSelect`
- `LayerUtility: SaveImagePlus`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `ScheduledCFGGuidance`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 4/5 个有
- `CLIPTextEncode` —— 3/5 个有
- `EmptyMiniMaxH3LatentAV` —— 3/5 个有
- `easy imageColorMatch` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `LayerUtility: ImageReel` —— 2/5 个有
- `LayerUtility: ImageReelComposit` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `MiniMaxH3ReferenceToVideo` —— 2/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

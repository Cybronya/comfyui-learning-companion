---
name: unknown_workflow_sampler_unet_vae_225
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8625
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Text, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageFromBatch, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MiniMaxH3BlockCacheT8, MiniMaxH3ImageToVideo, PathchSageAttentionKJ, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, easy MiniMaxH3ReferenceToVideoBridge]
problems: []
missing: []
members: [图片生成/图生图/MiniMaxH3 图像编辑_2086058472554196994.json, 图片生成/图生图/MiniMaxH3_图像编辑_2087426122412806145.json, 数字人/数字人/图像编辑+文生图 MiniMaxH3  更真实更好的一致性_2094792515420516353.json, 数字人/数字人/海螺 H3 图像编辑+文生图 高还原度_2094805922773295105.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_225

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/MiniMaxH3 图像编辑_2086058472554196994.json、图片生成/图生图/MiniMaxH3_图像编辑_2087426122412806145.json、数字人/数字人/图像编辑+文生图 MiniMaxH3  更真实更好的一致性_2094792515420516353.json、数字人/数字人/海螺 H3 图像编辑+文生图 高还原度_2094805922773295105.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageFromBatch`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MiniMaxH3BlockCacheT8`
- `MiniMaxH3ImageToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy MiniMaxH3ReferenceToVideoBridge`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 2/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `EmptyMiniMaxH3LatentAV` —— 2/4 个有
- `FluxGuidance` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `ScheduledCFGGuidance` —— 2/4 个有
- `easy imageColorMatch` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

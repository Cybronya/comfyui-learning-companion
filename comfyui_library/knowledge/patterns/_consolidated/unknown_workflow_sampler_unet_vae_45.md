---
name: unknown_workflow_sampler_unet_vae_45
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.943357
common_nodes: [BasicGuider, CLIPLoader, LoadImage, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3StillConditioningT8, MiniMaxH3StillDecodeT8, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/MiniMax H3图像编辑_2086293027227787266.json, 图片生成/图生图/MiniMax H3图像编辑_2086297871242063873.json, 图片生成/图生图/MiniMax H3图像编辑_2086298554582257666.json, 图片生成/图生图/MiniMax H3图像编辑_2086299490688004097.json, 图片生成/图生图/MiniMax H3图像编辑_2086300078318374914.json, 图片生成/图生图/MiniMax H3图像编辑_2086300964574814209.json, 图片生成/图生图/MiniMax H3图像编辑_2086301685932191746.json, 图片生成/图生图/MiniMax H3图像编辑_2086302265975066625.json, 图片生成/图生图/MiniMax H3图像编辑加速版V1(22F版)_2085981857962876930.json, 图片生成/图生图/MiniMax H3图像编辑加速版V1(22F版)_2086156009982226433.json, 图片生成/图生图/MiniMax H3开源版 图像编辑加速版_2086039685087977473.json, 图片生成/图生图/MiniMax_H3图像编辑加速版V1(22F版)_2087428806872227842.json, 图片生成/图生图/海螺MiniMax H3开源版 图像编辑加速版_2086050575061438465.json, 图片生成/文生图/MIniMax-H3图像编辑_2088220660412805121.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_45

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/MiniMax H3图像编辑_2086293027227787266.json、图片生成/图生图/MiniMax H3图像编辑_2086297871242063873.json、图片生成/图生图/MiniMax H3图像编辑_2086298554582257666.json、图片生成/图生图/MiniMax H3图像编辑_2086299490688004097.json、图片生成/图生图/MiniMax H3图像编辑_2086300078318374914.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `LoadImage`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3StillConditioningT8`
- `MiniMaxH3StillDecodeT8`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3BlockCacheT8` —— 13/14 个有
- `CR Text` —— 8/14 个有
- `Int` —— 8/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/14 个有
- `CR Prompt Text` —— 6/14 个有
- `ImageConcanate` —— 6/14 个有
- `MiniMaxH3StillPreflightT8` —— 6/14 个有
- `PreviewAny` —— 6/14 个有
- `ResolutionSelector` —— 6/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

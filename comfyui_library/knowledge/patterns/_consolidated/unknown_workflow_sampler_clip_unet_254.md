---
name: unknown_workflow_sampler_clip_unet_254
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9432
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/爆分游戏的三个爆分状态_2086696888518135810.json, 图片生成/图生图/老照片修复 -｜Flux-Klein｜底模_2054444918260682753.json, 图片生成/图生图/老照片修复 -｜Flux-Klein｜底模_2069231901122056194.json, 图片生成/图生图/脱衣服穿衣服_2080345607318884353.json, 图片生成/图生图/高清放大_2072576146432159746.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_254

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/爆分游戏的三个爆分状态_2086696888518135810.json、图片生成/图生图/老照片修复 -｜Flux-Klein｜底模_2054444918260682753.json、图片生成/图生图/老照片修复 -｜Flux-Klein｜底模_2069231901122056194.json、图片生成/图生图/脱衣服穿衣服_2080345607318884353.json、图片生成/图生图/高清放大_2072576146432159746.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 4/5 个有
- `GetImageSize` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `AILab_ImageCombiner` —— 1/5 个有
- `BiRefNetRMBG` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImageBlur` —— 1/5 个有
- `ImageColorMatch+` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `InvertMask` —— 1/5 个有
- `LayerColor: AutoAdjustV2` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: image_to_image_lora_sampler_clip_52
type: Image To Image
frequency: 5
level: strong
coverage: 0.8896
common_nodes: [CFGGuider, CFGNorm, CLIPLoader, CLIPTextEncode, CR Text, ColorCorrect, ConditioningZeroOut, DF_Integer, EmptySD3LatentImage, Flux2Scheduler, Get Image Size, GroundingDinoModelLoader_SDPose, Image Comparer (rgthree), ImageCASharpening+, ImageConcanate, ImageResize+, ImageScaleToTotalPixels, ImpactMinMax, JWFloat, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RandomNoise, ReferenceLatent, SDPoseOODLoader, SDPoseOODProcessor, SamplerCustomAdvanced, SaveImage, SeedVR2, SetNode, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, YOLOModelLoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/F.2klein9b换装服装替换动作参考_2059115957766938625.json, 图片生成/图生图/服装替换+姿态迁移+高清放大_2055214808420634625.json, 图片生成/图生图/电商服装替换+姿态迁移+高清放大_2064744460470284290.json, 图片生成/图生图/高精度服装替换+动作参考_2046550139992547330.json, 图片生成/文生图/flux2klein9b换装服装替换动作参考_2050384226830299137.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_52

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/F.2klein9b换装服装替换动作参考_2059115957766938625.json、图片生成/图生图/服装替换+姿态迁移+高清放大_2055214808420634625.json、图片生成/图生图/电商服装替换+姿态迁移+高清放大_2064744460470284290.json、图片生成/图生图/高精度服装替换+动作参考_2046550139992547330.json、图片生成/文生图/flux2klein9b换装服装替换动作参考_2050384226830299137.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ColorCorrect`
- `ConditioningZeroOut`
- `DF_Integer`
- `EmptySD3LatentImage`
- `Flux2Scheduler`
- `Get Image Size`
- `GroundingDinoModelLoader_SDPose`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageConcanate`
- `ImageResize+`
- `ImageScaleToTotalPixels`
- `ImpactMinMax`
- `JWFloat`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2`
- `SetNode`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `YOLOModelLoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `TT_img_enc` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足

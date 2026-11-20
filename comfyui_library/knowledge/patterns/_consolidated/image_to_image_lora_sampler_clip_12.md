---
name: image_to_image_lora_sampler_clip_12
type: Image To Image
frequency: 13
level: moderate
coverage: 0.928846
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, ImageScaleBy, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RH_Captioner, ReferenceLatent, RunningHub Deepcleaner, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/遮罩局部修复放大流_2075842412131475458.json, 图片生成/图生图/高清修复细节增强去AI感flux2极速出图_2047959821852352514.json, 图片生成/文生图/Flux2 Klein控油+高清放大+增强细节_2054578014805086209.json, 图片生成/文生图/无损高清_2042903595565195265.json, 平台全量/F2Klein9HD去油高清放大增强细节_2049067035014991873.json, 平台全量/Flux2 Klein 模糊小图变高清大图 去除AI油亮感 增加真实细节 高清放大 增强细节_2016316544527114241.json, 平台全量/Flux2 Klein控油+高清放大+增强细节_2025803124157452290.json, 平台全量/Flux2 Klein控油+高清放大+增强细节_2039882631298424833.json, 平台全量/Flux2 Klein控油+高清放大+增强细节_2070778994601062402.json, 平台全量/Flux2 Klein控油+高清放大+增强细节_2078863036684791809.json, 平台全量/Flux2-Klein-9B-图像修复高清放大 高清修复+去AI感_2016316850421899266.json, 平台全量/电商性感男模 超大包 短视频带货 流量嘎嘎猛，注意尺度_2058459077130416129.json, 平台全量/高清修复+去AI感 Flux2-klein9b + Z-Image_2016519884850597890.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/遮罩局部修复放大流_2075842412131475458.json、图片生成/图生图/高清修复细节增强去AI感flux2极速出图_2047959821852352514.json、图片生成/文生图/Flux2 Klein控油+高清放大+增强细节_2054578014805086209.json、图片生成/文生图/无损高清_2042903595565195265.json、平台全量/F2Klein9HD去油高清放大增强细节_2049067035014991873.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `ImageScaleBy`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RH_Captioner`
- `ReferenceLatent`
- `RunningHub Deepcleaner`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 12/13 个有
- `Image Comparer (rgthree)` —— 3/13 个有
- `Int` —— 3/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `Float` —— 1/13 个有
- `GrowMaskWithBlur` —— 1/13 个有
- `ImpactInt` —— 1/13 个有
- `LayerUtility: CropByMask V2` —— 1/13 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/13 个有
- `LayerUtility: RestoreCropBox` —— 1/13 个有
- `Mask Fill Holes` —— 1/13 个有
- `MaskPreview+` —— 1/13 个有
- `easy imageColorMatch` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 9 | 13 | 2% |
| 采样算法 | euler | - | 13 | 54% |
| 调度器 | simple | - | 13 | 54% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 9，13 个样本，取值分散，一致性仅 2%
- 采样算法 最常用 euler，13 个样本，一致性 54%
- 调度器 最常用 simple，13 个样本，一致性 54%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足

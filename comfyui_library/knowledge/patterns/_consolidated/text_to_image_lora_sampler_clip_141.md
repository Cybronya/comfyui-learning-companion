---
name: text_to_image_lora_sampler_clip_141
type: Text To Image
frequency: 8
level: strong
coverage: 0.881
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), JjkText, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: NumberCalculator, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, QZ_ResolutionPreset, SaveImage, SimpleMathDual+, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy seed, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/4K超写实去ai感｜Krea2文生图高清一键生成_2094764662138163201.json, 图片生成/文生图/4K超写实文生图｜Krea2人像写真角色设计超清直出_2089043670136868866.json, 图片生成/文生图/4K超写实文生图｜Krea2写实大片生成_2092583582224175105.json, 图片生成/文生图/4K高清放大文生图｜Krea2+Z-image联合生成_2091245758770143233.json, 图片生成/文生图/Krea 2超写实4K文生图处理生成工作流_2101031767800115202.json, 图片生成/文生图/Krea2 4K超清写实文生图｜美少女直出高质量_2089433996257222657.json, 图片生成/文生图/Krea2 超写实4K文生图｜去AI感真实到犯规 直出大片_2097582803880865794.json, 图片生成/文生图/Krea2文生图_超写实4K商业级工作流_2082042807304409089.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_141

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/4K超写实去ai感｜Krea2文生图高清一键生成_2094764662138163201.json、图片生成/文生图/4K超写实文生图｜Krea2人像写真角色设计超清直出_2089043670136868866.json、图片生成/文生图/4K超写实文生图｜Krea2写实大片生成_2092583582224175105.json、图片生成/文生图/4K高清放大文生图｜Krea2+Z-image联合生成_2091245758770143233.json、图片生成/文生图/Krea 2超写实4K文生图处理生成工作流_2101031767800115202.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: NumberCalculator`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `QZ_ResolutionPreset`
- `SaveImage`
- `SimpleMathDual+`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy seed`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 7/8 个有
- `ImageScaleToTotalPixels` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `SeedVR2LoadDiTModel` —— 7/8 个有
- `SeedVR2LoadVAEModel` —— 7/8 个有
- `SeedVR2VideoUpscaler` —— 7/8 个有
- `easy loraStack` —— 7/8 个有
- `easy loraStackApply` —— 7/8 个有
- `DF_Integer` —— 1/8 个有
- `Get Image Size` —— 1/8 个有
- `ImageCASharpening+` —— 1/8 个有
- `ImageResize+` —— 1/8 个有
- `ImpactMinMax` —— 1/8 个有
- `SeedVR2` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有
- `TTP_Image_Assy` —— 1/8 个有
- `TTP_Image_Tile_Batch` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足

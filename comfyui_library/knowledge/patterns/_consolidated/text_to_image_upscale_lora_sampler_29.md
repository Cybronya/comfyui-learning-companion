---
name: text_to_image_upscale_lora_sampler_29
type: Text To Image
frequency: 4
level: moderate
coverage: 0.95325
common_nodes: [1hew_IntImageSize, CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, GetImageSize, ImageResizeAdvanced, ImageScaleBy, Int, KSampler, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveStringMultiline, QZ_ResolutionPreset, SaveImage, SeedNode, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2 Text-to-Image (场景增强v0.1)_2075783987632627713.json, 图片生成/文生图/Krea2 Turbo Text-to-Image (人像增强 v2)_2093742684635750401.json, 图片生成/文生图/Krea2 Turbo 文生图 （场景增强 v2)_2094638572044374017.json, 图片生成/文生图/Krea2 Turbo文生图（超清人像增强）_2075249065637535746.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_29

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Krea2 Text-to-Image (场景增强v0.1)_2075783987632627713.json、图片生成/文生图/Krea2 Turbo Text-to-Image (人像增强 v2)_2093742684635750401.json、图片生成/文生图/Krea2 Turbo 文生图 （场景增强 v2)_2094638572044374017.json、图片生成/文生图/Krea2 Turbo文生图（超清人像增强）_2075249065637535746.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `1hew_IntImageSize`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize`
- `ImageResizeAdvanced`
- `ImageScaleBy`
- `Int`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveStringMultiline`
- `QZ_ResolutionPreset`
- `SaveImage`
- `SeedNode`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 3/4 个有
- `RHLLMChatNode` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 10 | 4 | 0% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 0.25 | 0.25 - 0.3 | 3 | 91% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 10，4 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 0.25，观测区间 0.25 - 0.3，3 个样本，取值集中（一致性 91%）
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足

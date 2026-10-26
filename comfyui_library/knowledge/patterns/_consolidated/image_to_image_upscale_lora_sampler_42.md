---
name: image_to_image_upscale_lora_sampler_42
type: Image To Image
frequency: 4
level: moderate
coverage: 0.9105
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageColorMatch+, ImageScaleToTotalPixels, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/KREA2真实感洗图-雯雯的后宫_2075839994308153345.json, 图片生成/图生图/KREA2超还原真实感洗图-自定义重绘幅度-B站AIGC大赏_2075773150381563906.json, 图片生成/图生图/ZIT情绪高清洗图-AIGC大赏_2062797376057860098.json, 图片生成/文生图/双采样极速洗图优化版+超清放大_2066695022304645121.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_42

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/KREA2真实感洗图-雯雯的后宫_2075839994308153345.json、图片生成/图生图/KREA2超还原真实感洗图-自定义重绘幅度-B站AIGC大赏_2075773150381563906.json、图片生成/图生图/ZIT情绪高清洗图-AIGC大赏_2062797376057860098.json、图片生成/文生图/双采样极速洗图优化版+超清放大_2066695022304645121.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageColorMatch+`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Float` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `llama_cpp_instruct_adv` —— 3/4 个有
- `llama_cpp_model_loader` —— 3/4 个有
- `llama_cpp_parameters` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `CheckpointLoaderSimple` —— 2/4 个有
- `CompressImages` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `ImageResize+` —— 2/4 个有
- `ImageScaleBy` —— 2/4 个有
- `MuyeTextEditOutput` —— 2/4 个有
- `TTP_Image_Assy` —— 2/4 个有
- `TTP_Image_Tile_Batch` —— 2/4 个有
- `TTP_Tile_image_size` —— 2/4 个有
- `easy getNode` —— 2/4 个有
- `easy imageSize` —— 2/4 个有
- `easy setNode` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `AILab_QwenVL` —— 1/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `Int` —— 1/4 个有
- `ModelPatchLoader` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `ZImageFunControlnet` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 11 | 4 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 50% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 0.45 | 0.2 - 0.7 | 4 | 44% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 11，4 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 0.45，观测区间 0.2 - 0.7，4 个样本，取值分散，一致性仅 44%
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_upscale_lora_sampler_77
type: Text To Image
frequency: 3
level: weak
coverage: 0.783
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageScaleToTotalPixels, KSampler, KSamplerSelect, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy getNode, easy imageSize, easy setNode, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2+Turbo+文生图+图生图 双采样-提示词优化-全套  Krea2光速风格迁移+超清图_2073958355298770946.json, 图片生成/图生图/极致真实V2亿级像素超分放大｜图生图写实直出，细节放大不见噪点_2100521904573607937.json, 图片生成/文生图/Krea2 Turbo 文生图 图生图（双采样-提示词优化-全套）_2071156764665536514.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_77

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Krea2+Turbo+文生图+图生图 双采样-提示词优化-全套  Krea2光速风格迁移+超清图_2073958355298770946.json、图片生成/图生图/极致真实V2亿级像素超分放大｜图生图写实直出，细节放大不见噪点_2100521904573607937.json、图片生成/文生图/Krea2 Turbo 文生图 图生图（双采样-提示词优化-全套）_2071156764665536514.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
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
- `easy getNode`
- `easy imageSize`
- `easy setNode`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 2/3 个有
- `BasicGuider` —— 2/3 个有
- `BasicScheduler` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `CFGGuider` —— 1/3 个有
- `EmptyFlux2LatentImage` —— 1/3 个有
- `EmptyImage` —— 1/3 个有
- `Flux2Scheduler` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `ImageColorMatch+` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有
- `solarL_SaveImagesToZip` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1024 | 3 | 37% |
| 高度 | 1536 | 80 - 1536 | 3 | 35% |
| 采样步数 | 6 | 4 - 6 | 3 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 3 | 24% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 37%
- 高度 中位数 1536，观测区间 80 - 1536，3 个样本，取值分散，一致性仅 35%
- 采样步数 中位数 6，观测区间 4 - 6，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，3 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足

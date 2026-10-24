---
name: image_to_image_upscale_lora_sampler_5
type: Image To Image
frequency: 18
level: moderate
coverage: 0.748222
common_nodes: [CLIPLoader, CLIPTextEncode, ColorCorrect, EditTextEncode_EditUtils, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Get Image Size, GetImageSize+, ImageResize+, ImageScaleBy, KSampler, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy boolean, easy cleanGpuUsed, easy ifElse, easy imageColorMatch, easy imageScaleToNormPixels, easy int, easy showAnything, 图像缩放V2_孤海, 数学运算_孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/F.2Klein-zimage人像精修高清放大_2058053312079028225.json, 图片生成/图生图/F2K+zimage+seedVR2.5-人像精修+高清放大_2037094484042850305.json, 图片生成/图生图/Flux2-Klein+zimage人像精修+高清放大_2045802696128602114.json, 图片生成/图生图/Flux2-Klein人像精修+换背景+打光+高清放大_2037730083359694850.json, 图片生成/图生图/Flux2-Klein人像精修+高清放大_2050492628394881026.json, 图片生成/图生图/Flux2-Klein人像精修+高清放大_2075512683058778114.json, 图片生成/图生图/Flux2-Klein人像精修+高清放大_2076148795947175937.json, 图片生成/图生图/Flux2-Klein人像精修+高清放大_2086242419229675522.json, 图片生成/图生图/Flux2-身材调整优化丰胸_2081940467763212289.json, 图片生成/图生图/Flux2-身材调整优化丰胸_2082008265621331970.json, 图片生成/图生图/Flux2Kleinzimage人像精修高清放大_2049992134249467905.json, 图片生成/图生图/Flux2Kleinzimage人像精修高清放大_2051267226388443138.json, 图片生成/图生图/Flux2Kleinzimage人像精修高清放大_2093241740772859906.json, 图片生成/图生图/Flux2Kleinzimage人像精修高清放大_2093513070038577154.json, 图片生成/图生图/Flux2Klein人像精修换背景打光高清放大_2060852620331413505.json, 图片生成/图生图/Flux2Klein人像精修高清放大_2065817959108538370.json, 图片生成/图生图/Flux2人像精修+高清放大_2056983443392786433.json, 图片生成/文生图/( Flux-2-klein-9B)身材调整_2077560918359236610.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_5

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/F.2Klein-zimage人像精修高清放大_2058053312079028225.json、图片生成/图生图/F2K+zimage+seedVR2.5-人像精修+高清放大_2037094484042850305.json、图片生成/图生图/Flux2-Klein+zimage人像精修+高清放大_2045802696128602114.json、图片生成/图生图/Flux2-Klein人像精修+换背景+打光+高清放大_2037730083359694850.json、图片生成/图生图/Flux2-Klein人像精修+高清放大_2050492628394881026.json…）

- **类型**：Image To Image
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorCorrect`
- `EditTextEncode_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Get Image Size`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy boolean`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy imageColorMatch`
- `easy imageScaleToNormPixels`
- `easy int`
- `easy showAnything`
- `图像缩放V2_孤海`
- `数学运算_孤海`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 17/18 个有
- `孤海-浮点滑条` —— 17/18 个有
- `SetNode` —— 12/18 个有
- `CR Text Concatenate` —— 11/18 个有
- `GetNode` —— 11/18 个有
- `StringConstant` —— 11/18 个有
- `取色器_孤海` —— 11/18 个有
- `GetImageSize` —— 5/18 个有
- `LayerUtility: ImageReel` —— 5/18 个有
- `LayerUtility: ImageReelComposit` —— 5/18 个有
- `CFGGuider` —— 3/18 个有
- `ConditioningZeroOut` —— 3/18 个有
- `EmptyFlux2LatentImage` —— 3/18 个有
- `Flux2Scheduler` —— 3/18 个有
- `KSamplerSelect` —— 3/18 个有
- `RandomNoise` —— 3/18 个有
- `SamplerCustomAdvanced` —— 3/18 个有
- `Anything Everywhere3` —— 2/18 个有
- `CR Text` —— 2/18 个有
- `LayerUtility: PurgeVRAM V2` —— 2/18 个有
- `PainterFluxImageEdit` —— 2/18 个有
- `llama_cpp_instruct_adv` —— 2/18 个有
- `llama_cpp_model_loader` —— 2/18 个有
- `llama_cpp_parameters` —— 2/18 个有
- `CheckpointLoaderSimple` —— 1/18 个有
- `FloatSlider` —— 1/18 个有
- `Lora Loader Stack (rgthree)` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 18 | 1% |
| 采样算法 | euler_ancestral | - | 18 | 56% |
| 调度器 | simple | - | 18 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，18 个样本，取值分散，一致性仅 1%
- 采样算法 最常用 euler_ancestral，18 个样本，一致性 56%
- 调度器 最常用 simple，18 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（20/18 个样本）：Steps较低可能导致细节不足

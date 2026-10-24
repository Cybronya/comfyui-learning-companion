---
name: text_to_image_upscale_lora_sampler_35
type: Text To Image
frequency: 6
level: strong
coverage: 0.7315
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Concatenate, ColorCorrect, EditTextEncode_EditUtils, EmptyLatentImage, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Get Image Size, GetImageSize+, GetNode, Image Comparer (rgthree), ImageResize+, ImageScaleBy, JjkText, KSampler, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, StringConstant, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy boolean, easy cleanGpuUsed, easy ifElse, easy imageColorMatch, easy imageScaleToNormPixels, easy int, easy showAnything, solarL_SaveImagesToZip, 图像缩放V2_孤海, 孤海-浮点滑条, 数学运算_孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-Klein人像精修｜换背景打光高清放大_2095604793564819457.json, 图片生成/图生图/人像精修+高清放大工作流｜面部细节修复画质增强_2095327272587845633.json, 图片生成/图生图/人像精修+高清放大工作流｜面部细节修复画质增强_2095431025261367297.json, 图片生成/图生图/人像精修加高清放大工作流，图生图人像处理细节增强工具_2106841795853381634.json, 图片生成/图生图/人像精修换背景打光｜Flux2-Klein高清放大图生图_2095865018905620482.json, 视频生成/图生视频/人像精修加高清放大工作流，图生图人像处理细节增强工具_2110533237222232066.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_35

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein人像精修｜换背景打光高清放大_2095604793564819457.json、图片生成/图生图/人像精修+高清放大工作流｜面部细节修复画质增强_2095327272587845633.json、图片生成/图生图/人像精修+高清放大工作流｜面部细节修复画质增强_2095431025261367297.json、图片生成/图生图/人像精修加高清放大工作流，图生图人像处理细节增强工具_2106841795853381634.json、图片生成/图生图/人像精修换背景打光｜Flux2-Klein高清放大图生图_2095865018905620482.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `ColorCorrect`
- `EditTextEncode_EditUtils`
- `EmptyLatentImage`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Get Image Size`
- `GetImageSize+`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `JjkText`
- `KSampler`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `StringConstant`
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
- `solarL_SaveImagesToZip`
- `图像缩放V2_孤海`
- `孤海-浮点滑条`
- `数学运算_孤海`

**可变部分**（部分 workflow 才有）：
- `取色器_孤海` —— 5/6 个有
- `PreviewImage` —— 4/6 个有
- `孤海注释` —— 3/6 个有
- `Anything Everywhere3` —— 2/6 个有
- `CR Text` —— 2/6 个有
- `GetImageSize` —— 2/6 个有
- `LayerUtility: PurgeVRAM V2` —— 2/6 个有
- `PainterFluxImageEdit` —— 2/6 个有
- `llama_cpp_instruct_adv` —— 2/6 个有
- `llama_cpp_model_loader` —— 2/6 个有
- `llama_cpp_parameters` —— 2/6 个有
- `EmptyImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（14/6 个样本）：Steps较低可能导致细节不足

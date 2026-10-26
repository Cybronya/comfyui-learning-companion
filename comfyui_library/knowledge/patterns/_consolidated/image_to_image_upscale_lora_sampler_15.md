---
name: image_to_image_upscale_lora_sampler_15
type: Image To Image
frequency: 11
level: moderate
coverage: 0.730182
common_nodes: [CLIPLoader, CLIPTextEncode, EditTextEncode_EditUtils, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人像真实皮肤加美颜，8K清晰度V2_2095328630950944770.json, 图片生成/图生图/人像真实皮肤加美颜，8K清晰度V2_2095432611991740417.json, 图片生成/图生图/人像精修增强皮肤纹理质感婚纱摄影_2085175806896201729.json, 图片生成/图生图/人像美白精修 皮肤磨皮 去瑕疵 高清放大   Flux2-Klein+zimage_2062457346001035265.json, 图片生成/图生图/最强人物人像精修+高清放大Flux2-Klein_2061693253585563650.json, 图片生成/图生图/模糊人像精修+高清放大_2113964750496428034.json, 图片生成/图生图/皮肤精修和美肤_2060305049963814913.json, 图片生成/图生图/老孙AI  人像精修+高清放大_2058911393428107266.json, 图片生成/图生图/老孙AI 人像精修+高清放大(人物风景)_2085570797472665602.json, 图片生成/图生图/（超好用）Flux2-Klein人像精修+高清放大（自选是否保留原色调）_2040310169485189122.json, 数字人/数字人/Flux2-Klein+zimage人像精修+高清放大_2046588836989378561.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_15

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/人像真实皮肤加美颜，8K清晰度V2_2095328630950944770.json、图片生成/图生图/人像真实皮肤加美颜，8K清晰度V2_2095432611991740417.json、图片生成/图生图/人像精修增强皮肤纹理质感婚纱摄影_2085175806896201729.json、图片生成/图生图/人像美白精修 皮肤磨皮 去瑕疵 高清放大   Flux2-Klein+zimage_2062457346001035265.json、图片生成/图生图/最强人物人像精修+高清放大Flux2-Klein_2061693253585563650.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EditTextEncode_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
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
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 10/11 个有
- `easy imageColorMatch` —— 10/11 个有
- `Get Image Size` —— 9/11 个有
- `KSamplerAdvanced` —— 9/11 个有
- `ModelSamplingAuraFlow` —— 9/11 个有
- `easy imageScaleToNormPixels` —— 9/11 个有
- `图像缩放V2_孤海` —— 9/11 个有
- `数学运算_孤海` —— 9/11 个有
- `ColorCorrect` —— 8/11 个有
- `GetImageSize+` —— 8/11 个有
- `GetNode` —— 8/11 个有
- `SetNode` —— 8/11 个有
- `TextInput_` —— 8/11 个有
- `easy showAnything` —— 8/11 个有
- `孤海-浮点滑条` —— 8/11 个有
- `easy boolean` —— 7/11 个有
- `easy ifElse` —— 7/11 个有
- `easy int` —— 7/11 个有
- `CR Text Concatenate` —— 5/11 个有
- `StringConstant` —— 5/11 个有
- `取色器_孤海` —— 5/11 个有
- `AILab_ImageResize` —— 2/11 个有
- `EmptyFlux2LatentImage` —— 2/11 个有
- `GetImageSize` —— 2/11 个有
- `ImageUpscaleWithModel` —— 2/11 个有
- `UNETLoader_Any` —— 2/11 个有
- `UpscaleModelLoader` —— 2/11 个有
- `DuckQREncodeNode` —— 1/11 个有
- `GoohaiUniversalSlider` —— 1/11 个有
- `JjkText` —— 1/11 个有
- `LayerUtility: ImageReel` —— 1/11 个有
- `LayerUtility: ImageReelComposit` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 11 | 11% |
| 采样算法 | euler_ancestral | - | 11 | 73% |
| 调度器 | simple | - | 11 | 73% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，11 个样本，取值分散，一致性仅 11%
- 采样算法 最常用 euler_ancestral，11 个样本，一致性 73%
- 调度器 最常用 simple，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（13/11 个样本）：Steps较低可能导致细节不足

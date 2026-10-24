---
name: image_to_image_upscale_lora_sampler_14
type: Image To Image
frequency: 10
level: moderate
coverage: 0.7342
common_nodes: [CLIPLoader, CLIPTextEncode, ColorCorrect, EditTextEncode_EditUtils, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Get Image Size, GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageScaleToNormPixels, 图像缩放V2_孤海, 数学运算_孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ZIMAGE 增加图片质感_2060028463918174210.json, 图片生成/图生图/人像修图——校色+祛痘+磨皮_2085623722521743361.json, 图片生成/图生图/人像修图——校色+祛痘+磨皮_2085624892136968194.json, 图片生成/图生图/人像精修+高清放大_2096792495979061249.json, 图片生成/图生图/人像精修+高清放大_2097137920338644994.json, 图片生成/图生图/人像精修+高清放大_2098216307782152194.json, 图片生成/图生图/人像精修美颜+高清放大-Flux2-Klein_2082801921726967809.json, 图片生成/图生图/人物头像美颜自动美化Flux2-Klein人像精修+高清放大_2071815918069571585.json, 图片生成/图生图/图生图+洗图+去AI味【御川0710】_2067957555367858177.json, 图片生成/图生图/图生图高清真实_2088089636781514753.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_14

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/ZIMAGE 增加图片质感_2060028463918174210.json、图片生成/图生图/人像修图——校色+祛痘+磨皮_2085623722521743361.json、图片生成/图生图/人像修图——校色+祛痘+磨皮_2085624892136968194.json、图片生成/图生图/人像精修+高清放大_2096792495979061249.json、图片生成/图生图/人像精修+高清放大_2097137920338644994.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorCorrect`
- `EditTextEncode_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Get Image Size`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
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
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageScaleToNormPixels`
- `图像缩放V2_孤海`
- `数学运算_孤海`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 9/10 个有
- `SetNode` —— 9/10 个有
- `孤海-浮点滑条` —— 9/10 个有
- `PreviewImage` —— 8/10 个有
- `TextInput_` —— 8/10 个有
- `easy boolean` —— 8/10 个有
- `easy ifElse` —— 8/10 个有
- `easy imageColorMatch` —— 8/10 个有
- `easy int` —— 8/10 个有
- `easy showAnything` —— 8/10 个有
- `CR Text Concatenate` —— 7/10 个有
- `StringConstant` —— 7/10 个有
- `取色器_孤海` —— 7/10 个有
- `Float` —— 2/10 个有
- `Qwen3_VQA` —— 2/10 个有
- `图像缩放范围孤海` —— 2/10 个有
- `CompressImages` —— 1/10 个有
- `DuckQREncodeNode` —— 1/10 个有
- `GetImageSize` —— 1/10 个有
- `ImageScale` —— 1/10 个有
- `ImageUpscaleWithModel` —— 1/10 个有
- `ImpactSwitch` —— 1/10 个有
- `Int` —— 1/10 个有
- `KOOK_ImageCompression` —— 1/10 个有
- `KOOK_SaveJPGImage` —— 1/10 个有
- `TT_img_enc` —— 1/10 个有
- `UpscaleModelLoader` —— 1/10 个有
- `ZML_SwitchOutputFive` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 5 | 65% |
| Prompt 约束强度(CFG) | 5 | 1 - 8 | 10 | 29% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 10 | 50% |
| 重绘幅度 | 1 | 0.88 - 1 | 5 | 94% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 5，观测区间 1 - 8，10 个样本，取值分散，一致性仅 29%
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，10 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.88 - 1，5 个样本，取值集中（一致性 94%）
- 高发问题（12/10 个样本）：Steps较低可能导致细节不足

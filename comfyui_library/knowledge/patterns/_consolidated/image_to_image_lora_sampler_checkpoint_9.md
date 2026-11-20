---
name: image_to_image_lora_sampler_checkpoint_9
type: Image To Image
frequency: 4
level: strong
coverage: 0.8505
common_nodes: [CLIPLoader, CheckpointLoaderSimple, ColorMatch, DF_Integer, DF_Text_Box, DownloadAndLoadFlorence2Model, Florence2Run, Image Comparer (rgthree), KOOK_SaveJPGImage, KSampler, LayerMask: PersonMaskUltra V2, LoadImage, LoraLoaderModelOnly, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, Text Concatenate, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy positive, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/换发型_2095390212233973761.json, 平台全量/换发色_2095388304874237954.json, 平台全量/表情变换_2095356333909430273.json, 平台全量/证件照_2095485097142218753.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_checkpoint_9

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/换发型_2095390212233973761.json、平台全量/换发色_2095388304874237954.json、平台全量/表情变换_2095356333909430273.json、平台全量/证件照_2095485097142218753.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `DF_Integer`
- `DF_Text_Box`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `Image Comparer (rgthree)`
- `KOOK_SaveJPGImage`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `Text Concatenate`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy positive`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ReferenceLatent` —— 3/4 个有
- `easy textIndexSwitch` —— 3/4 个有
- `Any Switch (rgthree)` —— 2/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `ImageAndMaskPreview` —— 2/4 个有
- `InpaintCropImproved` —— 2/4 个有
- `InpaintStitchImproved` —— 2/4 个有
- `JWImageResizeByLongerSide` —— 2/4 个有
- `LayerMask: MaskGrow` —— 2/4 个有
- `LayerUtility: CropByMask V2` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `SUPIR_model_loader_v2_clip` —— 2/4 个有
- `CFGNorm` —— 1/4 个有
- `CR SDXL Aspect Ratio` —— 1/4 个有
- `ConcatTextOfUtils` —— 1/4 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/4 个有
- `ImageSmartSharpen+` —— 1/4 个有
- `LayerFilter: FilmV2` —— 1/4 个有
- `LayerUtility: ColorImage V2` —— 1/4 个有
- `LayerUtility: ImageBlendAdvance` —— 1/4 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/4 个有
- `LayerUtility: RestoreCropBox` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `QwenEditConfigPreparer` —— 1/4 个有
- `StringReplace` —— 1/4 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 1/4 个有
- `easy anythingIndexSwitch` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足

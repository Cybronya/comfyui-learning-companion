---
name: image_to_image_lora_sampler_clip_73
type: Image To Image
frequency: 4
level: moderate
coverage: 0.861
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, CropWithPadInfo_EditUtils, EditTextEncode_EditUtils, Flux2Scheduler, FluxKontextImageScale, GetImageSize, Image Comparer (rgthree), ImageMergeTileList, KSampler, KSamplerAdvanced, KSamplerSelect, Krea2EditApply_EditUtils, Krea2ModelConfig_EditUtils, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveFloat, PrimitiveInt, QwenConfigPreparer_EditUtils, ReferenceLatent, ResizeImageMaskNode, SamplerCustom, SaveImage, Seed (rgthree), SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, SplitImageToTileList, StringConcatenate, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, easy imageColorMatch, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2-洗图+高清修复放大_2086983392863805441.json, 图片生成/图生图/VividMuse-Krea2洗图加高清修复放大_2086253273283121154.json, 图片生成/图生图/VividMuse-Krea2洗图加高清修复放大_2096875612509134850.json, 图片生成/图生图/VividMuse-Krea2洗图加高清修复放大_2097169672977338370.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_73

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Krea2-洗图+高清修复放大_2086983392863805441.json、图片生成/图生图/VividMuse-Krea2洗图加高清修复放大_2086253273283121154.json、图片生成/图生图/VividMuse-Krea2洗图加高清修复放大_2096875612509134850.json、图片生成/图生图/VividMuse-Krea2洗图加高清修复放大_2097169672977338370.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CropWithPadInfo_EditUtils`
- `EditTextEncode_EditUtils`
- `Flux2Scheduler`
- `FluxKontextImageScale`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageMergeTileList`
- `KSampler`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `Krea2EditApply_EditUtils`
- `Krea2ModelConfig_EditUtils`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `QwenConfigPreparer_EditUtils`
- `ReferenceLatent`
- `ResizeImageMaskNode`
- `SamplerCustom`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `SplitImageToTileList`
- `StringConcatenate`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`
- `easy imageColorMatch`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `忽略多组孤海` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 75% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 4 | 52% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 4 | 75% |
| 重绘幅度 | simple | - | 4 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，4 个样本
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 75%
- 重绘幅度 最常用 simple，4 个样本，一致性 75%
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

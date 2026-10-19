---
name: text_to_image_controlnet_inpaint_lora
type: Text To Image
frequency: 5
level: weak
coverage: 0.8018
common_nodes: [ACE_TextTranslate, AdaptiveLongestEdge_EditUtils, ApplyInstantID, CFGGuider, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, CropWithPadInfo_EditUtils, DF_Get_image_size, EditTextEncode_EditUtils, EmptyLatentImage, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinOutputExtractor_EditUtils, Flux2Scheduler, GetImageSize+, Image Comparer (rgthree), ImageCompositeMasked, ImageScale, ImageScaleToTotalPixels, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, InvertMask, JoinImageWithAlpha, KSampler, KSamplerSelect, LayerColor: ColorAdapter, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: CropByMask V2, LayerUtility: ImageRemoveAlpha, LayerUtility: PurgeVRAM V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveInt, RandomNoise, SAM3_Detect, SamplerCustomAdvanced, SaveImage, Text, UNETLoader, VAEDecode, VAELoader, easy float, easy imageConcat, easy promptReplace, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [LayerMask: MaskGrow, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: CropByMask V2, LayerUtility: ImageRemoveAlpha, LayerUtility: PurgeVRAM V2, LayerUtility: RestoreCropBox, MathExpression|pysssss, easy float, easy imageConcat, GetImageSize+, LayerColor: ColorAdapter, LayerMask: MaskPreview, easy promptReplace]
members: [图片生成/图生图/2074806109537398786.json, 图片生成/图生图/2085307613553709058.json, 视频生成/图生视频/Klein BFS加InstantID一键换脸专注面部替换人像写真级图生图方案_2107571369671221249.json, 视频生成/图生视频/Klein_BFS加InstantID一键换脸，专注面部替换的人像写真级图生图方案_2106923033121345537.json, 视频生成/图生视频/Qwen_2511_Edit搭配Klein_9B与InstantID，高相似度一键换脸换头图生图工作_2106924550947688450.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_lora

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2074806109537398786.json、图片生成/图生图/2085307613553709058.json、视频生成/图生视频/Klein BFS加InstantID一键换脸专注面部替换人像写真级图生图方案_2107571369671221249.json、视频生成/图生视频/Klein_BFS加InstantID一键换脸，专注面部替换的人像写真级图生图方案_2106923033121345537.json、视频生成/图生视频/Qwen_2511_Edit搭配Klein_9B与InstantID，高相似度一键换脸换头图生图工作_2106924550947688450.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `ACE_TextTranslate`
- `AdaptiveLongestEdge_EditUtils`
- `ApplyInstantID`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `CropWithPadInfo_EditUtils`
- `DF_Get_image_size`
- `EditTextEncode_EditUtils`
- `EmptyLatentImage`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinOutputExtractor_EditUtils`
- `Flux2Scheduler`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImageScale`
- `ImageScaleToTotalPixels`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `InvertMask`
- `JoinImageWithAlpha`
- `KSampler`
- `KSamplerSelect`
- `LayerColor: ColorAdapter`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveInt`
- `RandomNoise`
- `SAM3_Detect`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy float`
- `easy imageConcat`
- `easy promptReplace`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ColorTransfer` —— 4/5 个有
- `GetImageSize` —— 3/5 个有
- `JjkText` —— 3/5 个有
- `KOOK_SaveJPGImage` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `solarL_SaveImagesToZip` —— 3/5 个有
- `ComfyMathExpression` —— 2/5 个有
- `CropWithPadInfo` —— 2/5 个有
- `EmptyImage` —— 2/5 个有
- `LayerUtility: ExtendCanvas` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `PrimitiveFloat` —— 2/5 个有
- `QwenEditConfigPreparer` —— 2/5 个有
- `QwenEditOutputExtractor` —— 2/5 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 2/5 个有
- `PreviewBridge` —— 1/5 个有
- `ReferenceLatent` —— 1/5 个有
- `VAEEncode` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.1 | 0.1 - 0.1 | 5 | 100% |
| 采样步数 | 4 | 4 - 8 | 5 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1.5 - 4.5 | 5 | 55% |
| 采样算法 | er_sde | - | 5 | 60% |
| 调度器 | beta | - | 5 | 60% |
| 重绘幅度 | 1 | 0.35 - 1 | 5 | 59% |
| 宽度 | 80 | 80 - 512 | 5 | 16% |
| 高度 | 80 | 80 - 512 | 5 | 16% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.1，观测区间 0.1 - 0.1，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1.5 - 4.5，5 个样本
- 采样算法 最常用 er_sde，5 个样本，一致性 60%
- 调度器 最常用 beta，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，5 个样本
- 宽度 中位数 80，观测区间 80 - 512，5 个样本，取值分散，一致性仅 16%
- 高度 中位数 80，观测区间 80 - 512，5 个样本，取值分散，一致性仅 16%
- 高发问题（15/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerMask: MaskGrow、LayerUtility: CropBoxResolve、LayerUtility: CropByMask、LayerUtility: CropByMask V2、LayerUtility: ImageRemoveAlpha

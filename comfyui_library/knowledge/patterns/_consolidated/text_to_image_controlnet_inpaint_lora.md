---
name: text_to_image_controlnet_inpaint_lora
type: Text To Image
frequency: 16
level: weak
coverage: 0.891313
common_nodes: [ACE_TextTranslate, AdaptiveLongestEdge_EditUtils, ApplyInstantID, CFGGuider, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, CropWithPadInfo_EditUtils, DF_Get_image_size, EditTextEncode_EditUtils, EmptyLatentImage, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinOutputExtractor_EditUtils, Flux2Scheduler, GetImageSize+, Image Comparer (rgthree), ImageCompositeMasked, ImageScale, ImageScaleToTotalPixels, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, InvertMask, JoinImageWithAlpha, KSampler, KSamplerSelect, LayerColor: ColorAdapter, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: CropByMask V2, LayerUtility: ImageRemoveAlpha, LayerUtility: PurgeVRAM V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveInt, RandomNoise, SAM3_Detect, SamplerCustomAdvanced, SaveImage, Text, UNETLoader, VAEDecode, VAELoader, easy float, easy imageConcat, easy promptReplace, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein BFS+InstantID一键究极换头头部迁移图生图工具_2101384693232005122.json, 图片生成/图生图/Klein BFS联合InstantID实现一键头部迁移与换头，角色一致性图生图效果出众_2102800572914167810.json, 图片生成/图生图/Qwen 2511 Edit+Klein 9B+InstantID一键换头相似度工具_2101386635115061249.json, 图片生成/图生图/Qwen 2511 Edit搭配Klein 9B与InstantID，高相似度一键换脸换头图生图工作_2102802141256699906.json, 图片生成/图生图/klein bfs instantid一键究极换头换脸脸部迁移角色一致性_2088223907684896769.json, 图片生成/图生图/klein bfs+instantid一键究极换头换脸｜头部脸部迁移人物角色一致性图生图_2088122187269103618.json, 图片生成/图生图/qwen 2511 edit+klein 9b+instant一键究极相似度换头换脸｜角色一致性人像_2088210046806216706.json, 图片生成/图生图/一键换脸2511+klein+instantid)_2105579990195724289.json, 图片生成/图生图/一键换脸2511+klein+instantid)_2108017806670385154.json, 图片生成/图生图/一键究极换头、头部迁移_klein_bfs_+_instantid_2103668076221919234.json, 图片生成/图生图/一键究极换头、头部迁移_klein_bfs_+_instantid_2104847804228259841.json, 图片生成/图生图/一键究极换头、头部迁移（ klein bfs + instantid）_2074806109537398786.json, 图片生成/图生图/一键究极相似度换头（qwen 2511 edit +klein 9b+instant id）_2085307613553709058.json, 视频生成/图生视频/Klein BFS加InstantID一键换脸专注面部替换人像写真级图生图方案_2107571369671221249.json, 视频生成/图生视频/Klein_BFS加InstantID一键换脸，专注面部替换的人像写真级图生图方案_2106923033121345537.json, 视频生成/图生视频/Qwen_2511_Edit搭配Klein_9B与InstantID，高相似度一键换脸换头图生图工作_2106924550947688450.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_lora

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Klein BFS+InstantID一键究极换头头部迁移图生图工具_2101384693232005122.json、图片生成/图生图/Klein BFS联合InstantID实现一键头部迁移与换头，角色一致性图生图效果出众_2102800572914167810.json、图片生成/图生图/Qwen 2511 Edit+Klein 9B+InstantID一键换头相似度工具_2101386635115061249.json、图片生成/图生图/Qwen 2511 Edit搭配Klein 9B与InstantID，高相似度一键换脸换头图生图工作_2102802141256699906.json、图片生成/图生图/klein bfs instantid一键究极换头换脸脸部迁移角色一致性_2088223907684896769.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 16 个 workflow 都包含：
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
- `GetImageSize` —— 14/16 个有
- `MathExpression|pysssss` —— 12/16 个有
- `JjkText` —— 10/16 个有
- `solarL_SaveImagesToZip` —— 10/16 个有
- `ColorTransfer` —— 9/16 个有
- `KOOK_SaveJPGImage` —— 9/16 个有
- `孤海注释` —— 8/16 个有
- `CropWithPadInfo` —— 7/16 个有
- `PreviewBridge` —— 7/16 个有
- `QwenEditConfigPreparer` —— 7/16 个有
- `QwenEditOutputExtractor` —— 7/16 个有
- `ReferenceLatent` —— 7/16 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 7/16 个有
- `VAEEncode` —— 7/16 个有
- `ComfyMathExpression` —— 4/16 个有
- `LayerUtility: ExtendCanvas` —— 4/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/16 个有
- `PrimitiveFloat` —— 4/16 个有
- `EmptyImage` —— 2/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.1 | 0.1 - 0.1 | 16 | 100% |
| 采样步数 | 4 | 4 - 8 | 16 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1.5 - 4.5 | 16 | 57% |
| 采样算法 | er_sde | - | 16 | 62% |
| 调度器 | beta | - | 16 | 62% |
| 重绘幅度 | 1 | 0.35 - 1 | 16 | 62% |
| 宽度 | 80 | 80 - 512 | 16 | 14% |
| 高度 | 80 | 80 - 512 | 16 | 14% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 40/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.1，观测区间 0.1 - 0.1，16 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 8，16 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1.5 - 4.5，16 个样本
- 采样算法 最常用 er_sde，16 个样本，一致性 62%
- 调度器 最常用 beta，16 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，16 个样本
- 宽度 中位数 80，观测区间 80 - 512，16 个样本，取值分散，一致性仅 14%
- 高度 中位数 80，观测区间 80 - 512，16 个样本，取值分散，一致性仅 14%
- 高发问题（40/16 个样本）：Steps较低可能导致细节不足

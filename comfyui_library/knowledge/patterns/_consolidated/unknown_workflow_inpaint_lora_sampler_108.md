---
name: unknown_workflow_inpaint_lora_sampler_108
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.642
common_nodes: [AddLabel, AddMask, BboxDetectorCombined_v2, BlockifyMask, Bookmark (rgthree), CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ConvertAny2Float, CreateVideo, DrawMaskOnImage, DualCLIPLoader, GetImageRangeFromBatch, GetImageSize, GetImageSizeAndCount, GetNode, GrowMask, ImageBatch, ImageConcatMulti, ImageFromBatch, ImageResizeKJv2, ImageToMask, ImpactImageBatchToImageList, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXVAddGuideMulti, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, MaskComposite, MaskListToMaskBatch, MaskPreview, PathchSageAttentionKJ, PlaySound|pysssss, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, RepeatImageBatch, SAM3_TrackToMask, SAM3_VideoTrack, SamplerCustomAdvanced, SaveVideo, SetNode, SimpleMath+, SolidMask, UNETLoader, UltralyticsDetectorProvider, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeForInpaint, VAELoaderKJ, VHS_DuplicateMasks, VHS_LoadVideo, easy anythingIndexSwitch, easy compare, easy ifElse, easy indexAnything, easy int]
problems: []
missing: []
members: [平台全量/2026 最强视频去字幕工具！15秒视频3分钟搞定_2060167107811303426.json, 视频生成/文生视频/2026 最强视频去字幕工具！15秒视频3分钟搞定_2095082256900648962.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_108

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/2026 最强视频去字幕工具！15秒视频3分钟搞定_2060167107811303426.json、视频生成/文生视频/2026 最强视频去字幕工具！15秒视频3分钟搞定_2095082256900648962.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `AddLabel`
- `AddMask`
- `BboxDetectorCombined_v2`
- `BlockifyMask`
- `Bookmark (rgthree)`
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConvertAny2Float`
- `CreateVideo`
- `DrawMaskOnImage`
- `DualCLIPLoader`
- `GetImageRangeFromBatch`
- `GetImageSize`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `ImageBatch`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImageToMask`
- `ImpactImageBatchToImageList`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXVAddGuideMulti`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MaskComposite`
- `MaskListToMaskBatch`
- `MaskPreview`
- `PathchSageAttentionKJ`
- `PlaySound|pysssss`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `RepeatImageBatch`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeForInpaint`
- `VAELoaderKJ`
- `VHS_DuplicateMasks`
- `VHS_LoadVideo`
- `easy anythingIndexSwitch`
- `easy compare`
- `easy ifElse`
- `easy indexAnything`
- `easy int`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

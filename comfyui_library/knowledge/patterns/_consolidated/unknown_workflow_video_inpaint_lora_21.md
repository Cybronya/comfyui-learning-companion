---
name: unknown_workflow_video_inpaint_lora_21
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.847
common_nodes: [AddMask, BboxDetectorCombined_v2, BlockifyMask, CFGGuider, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, ConvertAny2Float, CreateVideo, DrawMaskOnImage, DualCLIPLoader, GetImageRangeFromBatch, GrowMask, ImageComposite+, ImageCrop, ImpactImageBatchToImageList, ImpactSwitch, KSampler, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXVAddGuideMulti, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, ManualSigmas, MaskComposite, MaskListToMaskBatch, MathExpression|pysssss, ModelSamplingAuraFlow, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ReferenceLatent, SAM3_TrackToMask, SAM3_VideoTrack, SamplerCustomAdvanced, SaveVideo, SaveVideoRGBA, SimpleMath+, SimpleMathDual+, SolidMask, TextEncodeQwenImageEditPlus, UNETLoader, UltralyticsDetectorProvider, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeForInpaint, VAELoader, VAELoaderKJ, VHS_DuplicateMasks, VHS_LoadVideo, WanVideoAnimateEmbeds, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy anythingIndexSwitch, easy ifElse, easy indexAnything, easy int, easy isMaskEmpty, easy mathInt]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/LTX2.3_Wan2.2 视频去字幕2605 嘎嘎好用版_2004395523207561218.json, 平台全量/LTX2.3_Wan2.2 视频去字幕_2073585613860855810.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_21

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/LTX2.3_Wan2.2 视频去字幕2605 嘎嘎好用版_2004395523207561218.json、平台全量/LTX2.3_Wan2.2 视频去字幕_2073585613860855810.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `AddMask`
- `BboxDetectorCombined_v2`
- `BlockifyMask`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ConvertAny2Float`
- `CreateVideo`
- `DrawMaskOnImage`
- `DualCLIPLoader`
- `GetImageRangeFromBatch`
- `GrowMask`
- `ImageComposite+`
- `ImageCrop`
- `ImpactImageBatchToImageList`
- `ImpactSwitch`
- `KSampler`
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
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MaskComposite`
- `MaskListToMaskBatch`
- `MathExpression|pysssss`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ReferenceLatent`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SaveVideoRGBA`
- `SimpleMath+`
- `SimpleMathDual+`
- `SolidMask`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeForInpaint`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_DuplicateMasks`
- `VHS_LoadVideo`
- `WanVideoAnimateEmbeds`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy anythingIndexSwitch`
- `easy ifElse`
- `easy indexAnything`
- `easy int`
- `easy isMaskEmpty`
- `easy mathInt`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | sa_solver | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

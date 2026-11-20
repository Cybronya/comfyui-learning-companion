---
key: 平台全量/LTX2.3_Wan2.2 视频去字幕2605 嘎嘎好用版_2004395523207561218.json
name: LTX2.3_Wan2.2 视频去字幕2605 嘎嘎好用版_2004395523207561218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3_Wan2.2 视频去字幕2605 嘎嘎好用版_2004395523207561218.json
hash: 3cacfcec7d2aa222
coverage: 0.846847
learned_at: 2026-11-14 00:38:21
nodes: [UNETLoader, easy ifElse, LTXVConditioning, VAELoaderKJ, VAELoaderKJ, RandomNoise, CFGGuider, LTXVSeparateAVLatent, LTXVConcatAVLatent, ConvertAny2Float, easy anythingIndexSwitch, LoraLoaderModelOnly, easy anythingIndexSwitch, PathchSageAttentionKJ, LTXVEmptyLatentAudio, LTXVCropGuides, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, easy ifElse, VHS_DuplicateMasks, SolidMask, MathExpression|pysssss, ImageCrop, BboxDetectorCombined_v2, UltralyticsDetectorProvider, SimpleMath+, PrimitiveStringMultiline, PrimitiveStringMultiline, CLIPTextEncode, SAM3_VideoTrack, CLIPTextEncode, VHS_DuplicateMasks, AddMask, MaskComposite, SimpleMath+, SimpleMath+, ImpactImageBatchToImageList, LTXVAddGuideMulti, SamplerCustomAdvanced, SaveVideoRGBA, ManualSigmas, KSamplerSelect, LTXAddVideoICLoRAGuide, VAELoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXVCropGuides, PrimitiveStringMultiline, easy ifElse, CLIPTextEncode, SimpleMathDual+, PrimitiveInt, PrimitiveInt, VAEEncode, ConditioningZeroOut, ModelSamplingAuraFlow, PrimitiveInt, VAEDecodeTiled, VAEEncode, VAEEncodeForInpaint, LTXVImgToVideoConditionOnly, CheckpointLoaderSimple, PrimitiveBoolean, PrimitiveInt, easy mathInt, SAM3_TrackToMask, UNETLoader, easy ifElse, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, WanVideoSampler, WanVideoDecode, ReferenceLatent, PrimitiveStringMultiline, PrimitiveStringMultiline, GrowMask, MaskListToMaskBatch, easy indexAnything, easy indexAnything, TextEncodeQwenImageEditPlus, ImageComposite+, VAEDecode, DualCLIPLoader, Note, VHS_LoadVideo, easy int, LayerUtility: ImageScaleByAspectRatio V2, DrawMaskOnImage, easy isMaskEmpty, easy ifElse, KSampler, LTXVPreprocess, LTXVSeparateAVLatent, CFGGuider, SamplerCustomAdvanced, LTXVConcatAVLatent, easy anythingIndexSwitch, SolidMask, GetImageRangeFromBatch, BlockifyMask, WanVideoVAELoader, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoAnimateEmbeds, WanVideoTextEncode, PrimitiveFloat, ImpactSwitch, CreateVideo, SaveVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "sam3.1-multiplex-fp16.safetensors", "denoise": 1, "height": 25, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 42, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/LTX2.3_Wan2.2 视频去字幕2605 嘎嘎好用版_2004395523207561218.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3_Wan2.2 视频去字幕2605 嘎嘎好用版_2004395523207561218.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（111 个）：
- `UNETLoader` ★核心
- `easy ifElse`
- `LTXVConditioning`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `RandomNoise`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `ConvertAny2Float`
- `easy anythingIndexSwitch`
- `LoraLoaderModelOnly` ★核心
- `easy anythingIndexSwitch`
- `PathchSageAttentionKJ`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVCropGuides`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy ifElse`
- `VHS_DuplicateMasks`
- `SolidMask`
- `MathExpression|pysssss`
- `ImageCrop`
- `BboxDetectorCombined_v2`
- `UltralyticsDetectorProvider`
- `SimpleMath+`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `SAM3_VideoTrack`
- `CLIPTextEncode` ★核心
- `VHS_DuplicateMasks`
- `AddMask`
- `MaskComposite`
- `SimpleMath+`
- `SimpleMath+`
- `ImpactImageBatchToImageList`
- `LTXVAddGuideMulti`
- `SamplerCustomAdvanced` ★核心
- `SaveVideoRGBA`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXAddVideoICLoRAGuide`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVCropGuides`
- `PrimitiveStringMultiline`
- `easy ifElse`
- `CLIPTextEncode` ★核心
- `SimpleMathDual+`
- `PrimitiveInt`
- `PrimitiveInt`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `PrimitiveInt`
- `VAEDecodeTiled` ★核心
- `VAEEncode` ★核心
- `VAEEncodeForInpaint` ★核心
- `LTXVImgToVideoConditionOnly`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveBoolean`
- `PrimitiveInt`
- `easy mathInt`
- `SAM3_TrackToMask`
- `UNETLoader` ★核心
- `easy ifElse`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ReferenceLatent`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `GrowMask`
- `MaskListToMaskBatch`
- `easy indexAnything`
- `easy indexAnything`
- `TextEncodeQwenImageEditPlus`
- `ImageComposite+`
- `VAEDecode` ★核心
- `DualCLIPLoader`
- `Note`
- `VHS_LoadVideo`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DrawMaskOnImage`
- `easy isMaskEmpty`
- `easy ifElse`
- `KSampler` ★核心
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `easy anythingIndexSwitch`
- `SolidMask`
- `GetImageRangeFromBatch`
- `BlockifyMask`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoAnimateEmbeds`
- `WanVideoTextEncode`
- `PrimitiveFloat`
- `ImpactSwitch`
- `CreateVideo`
- `SaveVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`
- `seed` = `42`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **85%**（94/111）

**有卡**：`UNETLoader`、`LTXVConditioning`、`VAELoaderKJ`、`RandomNoise`、`CFGGuider`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`ConvertAny2Float`、`easy anythingIndexSwitch`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`VAEDecode`、`VHS_DuplicateMasks`、`SolidMask`、`MathExpression|pysssss`、`ImageCrop`、`BboxDetectorCombined_v2`、`UltralyticsDetectorProvider`、`SimpleMath+`、`CLIPTextEncode`、`SAM3_VideoTrack`、`AddMask`、`MaskComposite`、`ImpactImageBatchToImageList`、`LTXVAddGuideMulti`、`SamplerCustomAdvanced`、`SaveVideoRGBA`、`ManualSigmas`、`KSamplerSelect`、`LTXAddVideoICLoRAGuide`、`VAELoader`、`CLIPLoader`、`SimpleMathDual+`、`VAEEncode`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`VAEDecodeTiled`、`VAEEncodeForInpaint`、`LTXVImgToVideoConditionOnly`、`CheckpointLoaderSimple`、`PrimitiveBoolean`、`easy mathInt`、`SAM3_TrackToMask`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoDecode`、`ReferenceLatent`、`GrowMask`、`MaskListToMaskBatch`、`easy indexAnything`、`TextEncodeQwenImageEditPlus`、`ImageComposite+`、`DualCLIPLoader`、`VHS_LoadVideo`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`DrawMaskOnImage`、`easy isMaskEmpty`、`KSampler`、`LTXVPreprocess`、`GetImageRangeFromBatch`、`BlockifyMask`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoAnimateEmbeds`、`WanVideoTextEncode`、`CreateVideo`、`SaveVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

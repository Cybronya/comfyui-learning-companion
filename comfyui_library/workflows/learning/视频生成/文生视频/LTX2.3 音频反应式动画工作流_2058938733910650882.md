---
key: 视频生成/文生视频/LTX2.3 音频反应式动画工作流_2058938733910650882.json
name: LTX2.3 音频反应式动画工作流_2058938733910650882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 音频反应式动画工作流_2058938733910650882.json
hash: 375bc215420bb47b
coverage: 0.876106
learned_at: 2026-10-11 19:49:37
nodes: [LayerUtility: PurgeVRAM V2, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, LatentUpscaleModelLoader, CM_FloatToInt, JWImageResizeByLongerSide, SolidMask, SetLatentNoiseMask, CFGGuider, CFGGuider, CFGGuider, LTXVImgToVideoConditionOnly, SamplerCustomAdvanced, LTXVLatentUpsampler, GetLatentSizeAndCount, LTXVImgToVideoConditionOnly, SetLatentNoiseMask, LTXVConcatAVLatent, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, SolidMask, LTXVConcatAVLatent, SamplerCustomAdvanced, CreateVideo, SamplerCustomAdvanced, image_scale_pixel_v2, Audio Duration (mtb), SimpleMath+, easy showAnything, PrimitiveFloat, GetLatentSizeAndCount, LTXVConcatAVLatent, LTXVSeparateAVLatent, PathchSageAttentionKJ, LTXVConditioning, LTXVPreprocess, EmptyLTXVLatentVideo, PrimitiveInt, VAEDecodeTiled, CLIPTextEncode, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LTX2SamplingPreviewOverride, KSamplerSelect, ManualSigmas, LTXAddVideoICLoRAGuide, RandomNoise, Seed (rgthree), LTXVImgToVideoConditionOnly, CFGGuider, GetImageRangeFromBatch, easy imageSize, VAEEncodeForInpaint, RepeatImageBatch, Image To Mask, ManualSigmas, LayerUtility: ColorImage, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXICLoRALoaderModelOnly, PathchSageAttentionKJ, LTXICLoRALoaderModelOnly, LTXVPreprocess, easy imageCount, SamplerCustomAdvanced, VAEDecodeTiled, LTXVCropGuides, SetLatentNoiseMask, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVAudioVAEEncode, SimpleMath+, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, LoraLoaderModelOnly, CreateVideo, VAEDecodeTiled, PrimitiveFloat, Float, MelBandRoFormerModelLoader, TrimAudioDuration, MelBandRoFormerSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2_NAG, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXVEmptyLatentAudio, LTXVEmptyLatentAudio, PromptRelayEncode, Float, SaveVideo, SolidMask, LoadImage, PrimitiveBoolean, LoraLoaderModelOnly, LoraLoaderModelOnly, CheckpointLoaderSimple, LoraLoaderModelOnly, Text, LoadAudio, SaveVideo, JjkText]
patterns: []
missing: [Audio Duration (mtb), Image To Mask, LayerUtility: ColorImage, LayerUtility: PurgeVRAM V2, SimpleMath+, SimpleMath+, easy imageCount, Seed (rgthree), easy imageSize]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `Image To Mask` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ColorImage` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageCount` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTX2.3 音频反应式动画工作流_2058938733910650882.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 音频反应式动画工作流_2058938733910650882.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（113 个）：
- `LayerUtility: PurgeVRAM V2`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `LatentUpscaleModelLoader`
- `CM_FloatToInt`
- `JWImageResizeByLongerSide`
- `SolidMask`
- `SetLatentNoiseMask`
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `LTXVImgToVideoConditionOnly`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `GetLatentSizeAndCount`
- `LTXVImgToVideoConditionOnly`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoConditionOnly`
- `SolidMask`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `SamplerCustomAdvanced` ★核心
- `image_scale_pixel_v2`
- `Audio Duration (mtb)`
- `SimpleMath+`
- `easy showAnything`
- `PrimitiveFloat`
- `GetLatentSizeAndCount`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `PathchSageAttentionKJ`
- `LTXVConditioning`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `VAEDecodeTiled` ★核心
- `CLIPTextEncode` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LTX2SamplingPreviewOverride`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXAddVideoICLoRAGuide`
- `RandomNoise`
- `Seed (rgthree)`
- `LTXVImgToVideoConditionOnly`
- `CFGGuider`
- `GetImageRangeFromBatch`
- `easy imageSize`
- `VAEEncodeForInpaint` ★核心
- `RepeatImageBatch`
- `Image To Mask`
- `ManualSigmas`
- `LayerUtility: ColorImage`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXICLoRALoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVPreprocess`
- `easy imageCount`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVCropGuides`
- `SetLatentNoiseMask`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAEEncode` ★核心
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LoraLoaderModelOnly` ★核心
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `PrimitiveFloat`
- `Float`
- `MelBandRoFormerModelLoader`
- `TrimAudioDuration`
- `MelBandRoFormerSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `PromptRelayEncode`
- `Float`
- `SaveVideo`
- `SolidMask`
- `LoadImage`
- `PrimitiveBoolean`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `Text`
- `LoadAudio`
- `SaveVideo`
- `JjkText`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors`

## 知识

覆盖率 **88%**（99/113）

**有卡**：`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`LatentUpscaleModelLoader`、`CM_FloatToInt`、`JWImageResizeByLongerSide`、`SolidMask`、`SetLatentNoiseMask`、`CFGGuider`、`LTXVImgToVideoConditionOnly`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`GetLatentSizeAndCount`、`LTXVConcatAVLatent`、`CreateVideo`、`image_scale_pixel_v2`、`LTXVSeparateAVLatent`、`PathchSageAttentionKJ`、`LTXVConditioning`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`VAEDecodeTiled`、`CLIPTextEncode`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LTX2SamplingPreviewOverride`、`LTXAddVideoICLoRAGuide`、`GetImageRangeFromBatch`、`VAEEncodeForInpaint`、`RepeatImageBatch`、`LTXICLoRALoaderModelOnly`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`LTXVAudioVAEEncode`、`LoraLoaderModelOnly`、`Float`、`MelBandRoFormerModelLoader`、`TrimAudioDuration`、`MelBandRoFormerSampler`、`LTX2_NAG`、`LTXVEmptyLatentAudio`、`PromptRelayEncode`、`SaveVideo`、`LoadImage`、`PrimitiveBoolean`、`CheckpointLoaderSimple`、`Text`、`LoadAudio`

**缺卡**（9）：`Audio Duration (mtb)`、`Image To Mask`、`LayerUtility: ColorImage`、`LayerUtility: PurgeVRAM V2`、`SimpleMath+`、`SimpleMath+`、`easy imageCount`、`Seed (rgthree)`、`easy imageSize`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler

## 学习发现

- 次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `Image To Mask` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ColorImage` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageCount` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明

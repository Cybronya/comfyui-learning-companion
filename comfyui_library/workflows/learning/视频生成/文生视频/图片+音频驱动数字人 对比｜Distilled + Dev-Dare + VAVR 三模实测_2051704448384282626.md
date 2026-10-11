---
key: 视频生成/文生视频/图片+音频驱动数字人 对比｜Distilled + Dev-Dare + VAVR 三模实测_2051704448384282626.json
name: 图片+音频驱动数字人 对比｜Distilled + Dev-Dare + VAVR 三模实测_2051704448384282626
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/图片+音频驱动数字人 对比｜Distilled + Dev-Dare + VAVR 三模实测_2051704448384282626.json
hash: 63111d57ad19ed48
coverage: 0.917073
learned_at: 2026-10-11 19:49:48
nodes: [PrimitiveBoolean, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, CM_FloatToInt, JWImageResizeByLongerSide, LTXVConditioning, LTXVPreprocess, SolidMask, LTXVAudioVAEEncode, SetLatentNoiseMask, LoraLoaderModelOnly, PrimitiveInt, CFGGuider, CFGGuider, CFGGuider, LTXVImgToVideoConditionOnly, SamplerCustomAdvanced, LTXVLatentUpsampler, GetLatentSizeAndCount, LTXVImgToVideoConditionOnly, SolidMask, SetLatentNoiseMask, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, SolidMask, SetLatentNoiseMask, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SamplerCustomAdvanced, image_scale_pixel_v2, MelBandRoFormerSampler, MelBandRoFormerModelLoader, Audio Duration (mtb), SimpleMath+, easy showAnything, Float, GetLatentSizeAndCount, LTXVConcatAVLatent, LTXVSeparateAVLatent, VRAMReserver, TrimAudioDuration, LoraLoaderModelOnly, CheckpointLoaderSimple, LTXVAudioVAELoader, LoraLoaderModelOnly, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, PromptRelayEncode, CLIPTextEncode, LayerUtility: PurgeVRAM V2, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, Seed Everywhere, KepStringLiteral, LTX2_NAG, PrimitiveBoolean, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, CM_FloatToInt, JWImageResizeByLongerSide, LTXVConditioning, LTXVPreprocess, SolidMask, LTXVAudioVAEEncode, SetLatentNoiseMask, LoraLoaderModelOnly, PrimitiveInt, CFGGuider, CFGGuider, CFGGuider, LTXVImgToVideoConditionOnly, SamplerCustomAdvanced, LTXVLatentUpsampler, GetLatentSizeAndCount, LTXVImgToVideoConditionOnly, SolidMask, SetLatentNoiseMask, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, SolidMask, SetLatentNoiseMask, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, image_scale_pixel_v2, MelBandRoFormerSampler, MelBandRoFormerModelLoader, Audio Duration (mtb), SimpleMath+, easy showAnything, GetLatentSizeAndCount, LTXVConcatAVLatent, LTXVSeparateAVLatent, VRAMReserver, LoraLoaderModelOnly, LTXVAudioVAELoader, LoraLoaderModelOnly, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, PromptRelayEncode, CLIPTextEncode, LayerUtility: PurgeVRAM V2, LatentUpscaleModelLoader, LTX2_NAG, PrimitiveBoolean, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, CM_FloatToInt, JWImageResizeByLongerSide, LTXVConditioning, LTXVPreprocess, SolidMask, LTXVAudioVAEEncode, SetLatentNoiseMask, LoraLoaderModelOnly, PrimitiveInt, CFGGuider, CFGGuider, CFGGuider, LTXVImgToVideoConditionOnly, SamplerCustomAdvanced, LTXVLatentUpsampler, GetLatentSizeAndCount, LTXVImgToVideoConditionOnly, SolidMask, SetLatentNoiseMask, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, SolidMask, SetLatentNoiseMask, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, image_scale_pixel_v2, MelBandRoFormerSampler, MelBandRoFormerModelLoader, Audio Duration (mtb), SimpleMath+, easy showAnything, GetLatentSizeAndCount, LTXVConcatAVLatent, LTXVSeparateAVLatent, VRAMReserver, LoraLoaderModelOnly, LTXVAudioVAELoader, LoraLoaderModelOnly, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, PromptRelayEncode, CLIPTextEncode, LayerUtility: PurgeVRAM V2, LatentUpscaleModelLoader, LTX2_NAG, CheckpointLoaderSimple, LTXAVTextEncoderLoader, CheckpointLoaderSimple, LTXAVTextEncoderLoader, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVImgToVideoConditionOnly, KepStringLiteral, KepStringLiteral, LoadAudio, Float, SaveVideo, PrimitiveFloat, SaveVideo, LoadImage, SaveVideo]
patterns: []
missing: [Audio Duration (mtb), Audio Duration (mtb), Audio Duration (mtb), LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, SimpleMath+, SimpleMath+, SimpleMath+, Seed Everywhere]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-dare-merged-distilled-1.1.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/图片+音频驱动数字人 对比｜Distilled + Dev-Dare + VAVR 三模实测_2051704448384282626.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/图片+音频驱动数字人 对比｜Distilled + Dev-Dare + VAVR 三模实测_2051704448384282626.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（205 个）：
- `PrimitiveBoolean`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `CM_FloatToInt`
- `JWImageResizeByLongerSide`
- `LTXVConditioning`
- `LTXVPreprocess`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `LTXVImgToVideoConditionOnly`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `GetLatentSizeAndCount`
- `LTXVImgToVideoConditionOnly`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoConditionOnly`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SamplerCustomAdvanced` ★核心
- `image_scale_pixel_v2`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `Audio Duration (mtb)`
- `SimpleMath+`
- `easy showAnything`
- `Float`
- `GetLatentSizeAndCount`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `VRAMReserver`
- `TrimAudioDuration`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `PromptRelayEncode`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `Seed Everywhere`
- `KepStringLiteral`
- `LTX2_NAG`
- `PrimitiveBoolean`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `CM_FloatToInt`
- `JWImageResizeByLongerSide`
- `LTXVConditioning`
- `LTXVPreprocess`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `LTXVImgToVideoConditionOnly`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `GetLatentSizeAndCount`
- `LTXVImgToVideoConditionOnly`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoConditionOnly`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `image_scale_pixel_v2`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `Audio Duration (mtb)`
- `SimpleMath+`
- `easy showAnything`
- `GetLatentSizeAndCount`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `VRAMReserver`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `PromptRelayEncode`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LatentUpscaleModelLoader`
- `LTX2_NAG`
- `PrimitiveBoolean`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `CM_FloatToInt`
- `JWImageResizeByLongerSide`
- `LTXVConditioning`
- `LTXVPreprocess`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `LTXVImgToVideoConditionOnly`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `GetLatentSizeAndCount`
- `LTXVImgToVideoConditionOnly`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `image_scale_pixel_v2`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `Audio Duration (mtb)`
- `SimpleMath+`
- `easy showAnything`
- `GetLatentSizeAndCount`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `VRAMReserver`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `PromptRelayEncode`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LatentUpscaleModelLoader`
- `LTX2_NAG`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoConditionOnly`
- `KepStringLiteral`
- `KepStringLiteral`
- `LoadAudio`
- `Float`
- `SaveVideo`
- `PrimitiveFloat`
- `SaveVideo`
- `LoadImage`
- `SaveVideo`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-dare-merged-distilled-1.1.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（188/205）

**有卡**：`PrimitiveBoolean`、`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`CM_FloatToInt`、`JWImageResizeByLongerSide`、`LTXVConditioning`、`LTXVPreprocess`、`SolidMask`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LoraLoaderModelOnly`、`CFGGuider`、`LTXVImgToVideoConditionOnly`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`GetLatentSizeAndCount`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`image_scale_pixel_v2`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`Float`、`VRAMReserver`、`TrimAudioDuration`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`PromptRelayEncode`、`CLIPTextEncode`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`KepStringLiteral`、`LTX2_NAG`、`LoadAudio`、`SaveVideo`、`LoadImage`

**缺卡**（10）：`Audio Duration (mtb)`、`Audio Duration (mtb)`、`Audio Duration (mtb)`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`Seed Everywhere`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler

## 学习发现

- 次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明

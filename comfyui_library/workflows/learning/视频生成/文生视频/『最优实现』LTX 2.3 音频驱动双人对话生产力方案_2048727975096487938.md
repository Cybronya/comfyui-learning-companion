---
key: 视频生成/文生视频/『最优实现』LTX 2.3 音频驱动双人对话生产力方案_2048727975096487938.json
name: 『最优实现』LTX 2.3 音频驱动双人对话生产力方案_2048727975096487938
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/『最优实现』LTX 2.3 音频驱动双人对话生产力方案_2048727975096487938.json
hash: e0459f10007c45b2
coverage: 0.916667
learned_at: 2026-10-11 19:49:45
nodes: [LayerUtility: PurgeVRAM V2, SaveVideo, PrimitiveBoolean, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, LatentUpscaleModelLoader, CM_FloatToInt, JWImageResizeByLongerSide, SolidMask, SetLatentNoiseMask, CFGGuider, CFGGuider, CFGGuider, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, SamplerCustomAdvanced, LTXVLatentUpsampler, GetLatentSizeAndCount, LTXVImgToVideoConditionOnly, SolidMask, SetLatentNoiseMask, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, SolidMask, SetLatentNoiseMask, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CreateVideo, SamplerCustomAdvanced, image_scale_pixel_v2, Audio Duration (mtb), SimpleMath+, easy showAnything, TrimAudioDuration, PrimitiveFloat, GetLatentSizeAndCount, LTXVConcatAVLatent, LTXVSeparateAVLatent, MelBandRoFormerSampler, LTXVAudioVAEEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXVConditioning, LTXVPreprocess, EmptyLTXVLatentVideo, PrimitiveInt, LTXAVTextEncoderLoader, LTXVAudioVAELoader, VAEDecodeTiled, PromptRelayEncode, LTX2_NAG, CLIPTextEncode, LoraLoaderModelOnly, Float, LoadImage, Float, LoadAudio, MelBandRoFormerModelLoader]
patterns: []
missing: [Audio Duration (mtb), LayerUtility: PurgeVRAM V2, SimpleMath+]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/『最优实现』LTX 2.3 音频驱动双人对话生产力方案_2048727975096487938.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/『最优实现』LTX 2.3 音频驱动双人对话生产力方案_2048727975096487938.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `LayerUtility: PurgeVRAM V2`
- `SaveVideo`
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
- `LatentUpscaleModelLoader`
- `CM_FloatToInt`
- `JWImageResizeByLongerSide`
- `SolidMask`
- `SetLatentNoiseMask`
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
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
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SamplerCustomAdvanced` ★核心
- `image_scale_pixel_v2`
- `Audio Duration (mtb)`
- `SimpleMath+`
- `easy showAnything`
- `TrimAudioDuration`
- `PrimitiveFloat`
- `GetLatentSizeAndCount`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `VAEDecodeTiled` ★核心
- `PromptRelayEncode`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Float`
- `LoadImage`
- `Float`
- `LoadAudio`
- `MelBandRoFormerModelLoader`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **92%**（66/72）

**有卡**：`SaveVideo`、`PrimitiveBoolean`、`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`LatentUpscaleModelLoader`、`CM_FloatToInt`、`JWImageResizeByLongerSide`、`SolidMask`、`SetLatentNoiseMask`、`CFGGuider`、`LTXVEmptyLatentAudio`、`LTXVImgToVideoConditionOnly`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`GetLatentSizeAndCount`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`CreateVideo`、`image_scale_pixel_v2`、`TrimAudioDuration`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CheckpointLoaderSimple`、`LTXVConditioning`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`VAEDecodeTiled`、`PromptRelayEncode`、`LTX2_NAG`、`CLIPTextEncode`、`Float`、`LoadImage`、`LoadAudio`、`MelBandRoFormerModelLoader`

**缺卡**（3）：`Audio Duration (mtb)`、`LayerUtility: PurgeVRAM V2`、`SimpleMath+`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler

## 学习发现

- 次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识

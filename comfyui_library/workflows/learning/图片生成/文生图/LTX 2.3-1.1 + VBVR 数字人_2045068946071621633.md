---
key: 图片生成/文生图/LTX 2.3-1.1 + VBVR 数字人_2045068946071621633.json
name: LTX 2.3-1.1 + VBVR 数字人_2045068946071621633
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/LTX 2.3-1.1 + VBVR 数字人_2045068946071621633.json
hash: f6c1eb4f8e0b5406
coverage: 0.957746
learned_at: 2026-10-21 02:53:27
nodes: [LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, VRAMReserver, CLIPTextEncode, LoraLoaderModelOnly, CLIPTextEncode, SaveVideo, PrimitiveBoolean, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, LTXVAudioVAELoader, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, CM_FloatToInt, JWImageResizeByLongerSide, LTXVConditioning, LTXVPreprocess, SolidMask, LTXVAudioVAEEncode, LTX2_NAG, SetLatentNoiseMask, LoraLoaderModelOnly, PrimitiveInt, CFGGuider, CFGGuider, CFGGuider, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, GetLatentSizeAndCount, LTXVImgToVideoConditionOnly, SolidMask, SetLatentNoiseMask, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, GetLatentSizeAndCount, SolidMask, SetLatentNoiseMask, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SamplerCustomAdvanced, image_scale_pixel_v2, LoadImage, MelBandRoFormerSampler, MelBandRoFormerModelLoader, LoadAudio, Audio Duration (mtb), PrimitiveFloat, SimpleMath+, easy showAnything, TrimAudioDuration, Float, Float, CheckpointLoaderSimple]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 25, "width": 97}
---

# 图片生成/文生图/LTX 2.3-1.1 + VBVR 数字人_2045068946071621633.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/LTX 2.3-1.1 + VBVR 数字人_2045068946071621633.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly` ★核心
- `VRAMReserver`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
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
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `LTXAVTextEncoderLoader`
- `CM_FloatToInt`
- `JWImageResizeByLongerSide`
- `LTXVConditioning`
- `LTXVPreprocess`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `LTX2_NAG`
- `SetLatentNoiseMask`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `GetLatentSizeAndCount`
- `LTXVImgToVideoConditionOnly`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoConditionOnly`
- `GetLatentSizeAndCount`
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
- `LoadImage`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `LoadAudio`
- `Audio Duration (mtb)`
- `PrimitiveFloat`
- `SimpleMath+`
- `easy showAnything`
- `TrimAudioDuration`
- `Float`
- `Float`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **96%**（68/71）

**有卡**：`LayerUtility: PurgeVRAM V2`、`LoraLoaderModelOnly`、`VRAMReserver`、`CLIPTextEncode`、`SaveVideo`、`PrimitiveBoolean`、`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`CM_FloatToInt`、`JWImageResizeByLongerSide`、`LTXVConditioning`、`LTXVPreprocess`、`SolidMask`、`LTXVAudioVAEEncode`、`LTX2_NAG`、`SetLatentNoiseMask`、`CFGGuider`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoConditionOnly`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`GetLatentSizeAndCount`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`image_scale_pixel_v2`、`LoadImage`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`LoadAudio`、`Audio Duration (mtb)`、`SimpleMath+`、`TrimAudioDuration`、`Float`、`CheckpointLoaderSimple`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler

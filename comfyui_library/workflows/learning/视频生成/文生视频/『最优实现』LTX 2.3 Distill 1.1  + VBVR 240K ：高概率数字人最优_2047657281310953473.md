---
key: 视频生成/文生视频/『最优实现』LTX 2.3 Distill 1.1  + VBVR 240K ：高概率数字人最优_2047657281310953473.json
name: 『最优实现』LTX 2.3 Distill 1.1  + VBVR 240K ：高概率数字人最优_2047657281310953473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/『最优实现』LTX 2.3 Distill 1.1  + VBVR 240K ：高概率数字人最优_2047657281310953473.json
hash: 29c2dd7865e95629
coverage: 0.915493
learned_at: 2026-10-11 19:49:45
nodes: [LayerUtility: PurgeVRAM V2, VRAMReserver, LoraLoaderModelOnly, CLIPTextEncode, SaveVideo, PrimitiveBoolean, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, LTXVAudioVAELoader, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, CM_FloatToInt, JWImageResizeByLongerSide, LTXVConditioning, LTXVPreprocess, SolidMask, LTXVAudioVAEEncode, LTX2_NAG, SetLatentNoiseMask, LoraLoaderModelOnly, PrimitiveInt, CFGGuider, CFGGuider, CFGGuider, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVImgToVideoConditionOnly, SamplerCustomAdvanced, LTXVLatentUpsampler, GetLatentSizeAndCount, LTXVImgToVideoConditionOnly, SolidMask, SetLatentNoiseMask, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, SolidMask, SetLatentNoiseMask, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SamplerCustomAdvanced, image_scale_pixel_v2, MelBandRoFormerSampler, MelBandRoFormerModelLoader, Audio Duration (mtb), SimpleMath+, easy showAnything, TrimAudioDuration, Float, Float, LoraLoaderModelOnly, PrimitiveFloat, GetLatentSizeAndCount, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoadAudio, CLIPTextEncode, CheckpointLoaderSimple]
patterns: []
missing: [Audio Duration (mtb), LayerUtility: PurgeVRAM V2, SimpleMath+]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/『最优实现』LTX 2.3 Distill 1.1  + VBVR 240K ：高概率数字人最优_2047657281310953473.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/『最优实现』LTX 2.3 Distill 1.1  + VBVR 240K ：高概率数字人最优_2047657281310953473.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `LayerUtility: PurgeVRAM V2`
- `VRAMReserver`
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
- `TrimAudioDuration`
- `Float`
- `Float`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `GetLatentSizeAndCount`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoadAudio`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **92%**（65/71）

**有卡**：`VRAMReserver`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`SaveVideo`、`PrimitiveBoolean`、`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`CM_FloatToInt`、`JWImageResizeByLongerSide`、`LTXVConditioning`、`LTXVPreprocess`、`SolidMask`、`LTXVAudioVAEEncode`、`LTX2_NAG`、`SetLatentNoiseMask`、`CFGGuider`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoConditionOnly`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`GetLatentSizeAndCount`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`image_scale_pixel_v2`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`TrimAudioDuration`、`Float`、`LoadImage`、`LoadAudio`、`CheckpointLoaderSimple`

**缺卡**（3）：`Audio Duration (mtb)`、`LayerUtility: PurgeVRAM V2`、`SimpleMath+`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler

## 学习发现

- 次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识

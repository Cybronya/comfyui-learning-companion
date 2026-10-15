---
key: 视频生成/文生视频/LTX 2.3 图片+音频数字人 2.0｜Dev-Dare 音画驱动增强版_2051714450033524738.json
name: LTX 2.3 图片+音频数字人 2.0｜Dev-Dare 音画驱动增强版_2051714450033524738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3 图片+音频数字人 2.0｜Dev-Dare 音画驱动增强版_2051714450033524738.json
hash: 45ef1e03b04a07cd
coverage: 0.96
learned_at: 2026-10-15 22:44:32
nodes: [PrimitiveBoolean, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, CM_FloatToInt, JWImageResizeByLongerSide, LTXVConditioning, LTXVPreprocess, SolidMask, LTXVAudioVAEEncode, SetLatentNoiseMask, LoraLoaderModelOnly, PrimitiveInt, CFGGuider, CFGGuider, CFGGuider, LTXVImgToVideoConditionOnly, SamplerCustomAdvanced, LTXVLatentUpsampler, GetLatentSizeAndCount, LTXVImgToVideoConditionOnly, SolidMask, SetLatentNoiseMask, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, SolidMask, SetLatentNoiseMask, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SamplerCustomAdvanced, image_scale_pixel_v2, MelBandRoFormerSampler, MelBandRoFormerModelLoader, Audio Duration (mtb), SimpleMath+, easy showAnything, Float, Float, GetLatentSizeAndCount, LTXVConcatAVLatent, LTXVSeparateAVLatent, VRAMReserver, TrimAudioDuration, LoraLoaderModelOnly, LoadImage, SaveVideo, LoraLoaderModelOnly, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, PromptRelayEncode, LTX2_NAG, CLIPTextEncode, LayerUtility: PurgeVRAM V2, LatentUpscaleModelLoader, LoadAudio, PrimitiveFloat, Seed Everywhere, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, Text, Text, Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-dare-merged-distilled-1.1.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX 2.3 图片+音频数字人 2.0｜Dev-Dare 音画驱动增强版_2051714450033524738.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.3 图片+音频数字人 2.0｜Dev-Dare 音画驱动增强版_2051714450033524738.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
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
- `Float`
- `GetLatentSizeAndCount`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `VRAMReserver`
- `TrimAudioDuration`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `PromptRelayEncode`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `PrimitiveFloat`
- `Seed Everywhere`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `Text`
- `Text`
- `Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-dare-merged-distilled-1.1.safetensors`

## 知识

覆盖率 **96%**（72/75）

**有卡**：`PrimitiveBoolean`、`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`CM_FloatToInt`、`JWImageResizeByLongerSide`、`LTXVConditioning`、`LTXVPreprocess`、`SolidMask`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LoraLoaderModelOnly`、`CFGGuider`、`LTXVImgToVideoConditionOnly`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`GetLatentSizeAndCount`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`image_scale_pixel_v2`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`Audio Duration (mtb)`、`SimpleMath+`、`Float`、`VRAMReserver`、`TrimAudioDuration`、`LoadImage`、`SaveVideo`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`PromptRelayEncode`、`LTX2_NAG`、`CLIPTextEncode`、`LayerUtility: PurgeVRAM V2`、`LatentUpscaleModelLoader`、`LoadAudio`、`Seed Everywhere`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`Text`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler

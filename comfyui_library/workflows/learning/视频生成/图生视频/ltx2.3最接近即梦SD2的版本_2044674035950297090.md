---
key: 视频生成/图生视频/ltx2.3最接近即梦SD2的版本_2044674035950297090.json
name: ltx2.3最接近即梦SD2的版本_2044674035950297090.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2044674035950297090.json
hash: 2ece33b00deb91df
coverage: 0.935484
learned_at: 2026-10-15 22:36:40
nodes: [RandomNoise, KSamplerSelect, CFGGuider, CheckpointLoaderSimple, SamplerCustomAdvanced, LTXVSeparateAVLatent, Reroute, LTXVConcatAVLatent, LTXVCropGuides, VAEDecodeTiled, LTXVLatentUpsampler, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, KSamplerSelect, CFGGuider, PathchSageAttentionKJ, LTXVAudioVAEDecode, Reroute, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVAudioVAEDecode, PrimitiveBoolean, LTXVChunkFeedForward, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, CLIPTextEncode, SamplerCustomAdvanced, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, LatentUpscaleModelLoader, LTXVImgToVideoInplace, CR Text, Text Find and Replace, RandomNoise, TrimAudioDuration, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, SolidMask, SetLatentNoiseMask, LTXVAudioVAEEncode, LTXVAudioVAELoader, ManualSigmas, ManualSigmas, ManualSigmas, PrimitiveFloat, LTXVConcatAVLatent, Switch any [Crystools], LTXVConditioning, LTX2_NAG, QWEN_TextDisplay, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadAudio, RH_Captioner, LTXAVTextEncoderLoader, VHS_VideoCombine, VHS_VideoCombine, CR Text, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/ltx2.3最接近即梦SD2的版本_2044674035950297090.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044674035950297090.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（62 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `CheckpointLoaderSimple` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `Reroute`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `LTXVLatentUpsampler` ★核心
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `PathchSageAttentionKJ`
- `LTXVAudioVAEDecode` ★核心
- `Reroute`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveBoolean`
- `LTXVChunkFeedForward`
- `LTXVImgToVideoInplace`
- `LTXVEmptyLatentAudio` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `LatentUpscaleModelLoader`
- `LTXVImgToVideoInplace`
- `CR Text`
- `Text Find and Replace`
- `RandomNoise`
- `TrimAudioDuration`
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `LTXVAudioVAELoader`
- `ManualSigmas`
- `ManualSigmas`
- `ManualSigmas`
- `PrimitiveFloat`
- `LTXVConcatAVLatent`
- `Switch any [Crystools]`
- `LTXVConditioning`
- `LTX2_NAG`
- `QWEN_TextDisplay`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadAudio`
- `RH_Captioner`
- `LTXAVTextEncoderLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CR Text`
- `LoadImage`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（58/62）

**有卡**：`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`CheckpointLoaderSimple`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`VAEDecodeTiled`、`LTXVLatentUpsampler`、`ComfyMathExpression`、`PathchSageAttentionKJ`、`LTXVAudioVAEDecode`、`PrimitiveBoolean`、`LTXVChunkFeedForward`、`LTXVImgToVideoInplace`、`LTXVEmptyLatentAudio`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LatentUpscaleModelLoader`、`CR Text`、`Text Find and Replace`、`TrimAudioDuration`、`EmptyLTXVLatentVideo`、`SolidMask`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`LTXVAudioVAELoader`、`ManualSigmas`、`Switch any [Crystools]`、`LTXVConditioning`、`LTX2_NAG`、`QWEN_TextDisplay`、`LoraLoaderModelOnly`、`LoadAudio`、`RH_Captioner`、`LTXAVTextEncoderLoader`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

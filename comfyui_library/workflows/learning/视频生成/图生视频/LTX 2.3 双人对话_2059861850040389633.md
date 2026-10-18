---
key: 视频生成/图生视频/LTX 2.3 双人对话_2059861850040389633.json
name: LTX 2.3 双人对话_2059861850040389633.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX 2.3 双人对话_2059861850040389633.json
hash: b158634cd6935119
coverage: 0.936508
learned_at: 2026-10-15 22:38:43
nodes: [CLIPTextEncode, image_scale_pixel_v2, PrimitiveFloat, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, Seed Everywhere, KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, LTXVAudioVAELoader, LatentUpscaleModelLoader, PrimitiveBoolean, RandomNoise, RandomNoise, RandomNoise, LTXAVTextEncoderLoader, CM_FloatToInt, Image_Resize_longsize, LTXVEmptyLatentAudio, LTXVConditioning, LTX2_NAG, LTXVConcatAVLatent, CFGGuider, CFGGuider, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CreateVideo, DisTorchPurgeVRAMV2, LTXVPreprocess, LTXVImgToVideoConditionOnly, EmptyLTXVLatentVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, PromptRelayEncode, VRAMReserver, PathchSageAttentionKJ, VAEDecodeTiled, SaveVideo, CheckpointLoaderSimple, easy showAnything, RH_LLMAPI_Pro_Node, easy showAnything, ZML_SplitText, SimpleMath+, PrimitiveInt, easy int, LoadImage, Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX 2.3 双人对话_2059861850040389633.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2059861850040389633.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
- `CLIPTextEncode` ★核心
- `image_scale_pixel_v2`
- `PrimitiveFloat`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly` ★核心
- `Seed Everywhere`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `PrimitiveBoolean`
- `RandomNoise`
- `RandomNoise`
- `RandomNoise`
- `LTXAVTextEncoderLoader`
- `CM_FloatToInt`
- `Image_Resize_longsize`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `LTX2_NAG`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `DisTorchPurgeVRAMV2`
- `LTXVPreprocess`
- `LTXVImgToVideoConditionOnly`
- `EmptyLTXVLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PromptRelayEncode`
- `VRAMReserver`
- `PathchSageAttentionKJ`
- `VAEDecodeTiled` ★核心
- `SaveVideo`
- `CheckpointLoaderSimple` ★核心
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `easy showAnything`
- `ZML_SplitText`
- `SimpleMath+`
- `PrimitiveInt`
- `easy int`
- `LoadImage`
- `Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **94%**（59/63）

**有卡**：`CLIPTextEncode`、`image_scale_pixel_v2`、`LayerUtility: PurgeVRAM V2`、`LoraLoaderModelOnly`、`Seed Everywhere`、`KSamplerSelect`、`ManualSigmas`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`PrimitiveBoolean`、`RandomNoise`、`LTXAVTextEncoderLoader`、`CM_FloatToInt`、`Image_Resize_longsize`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`LTX2_NAG`、`LTXVConcatAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVImgToVideoConditionOnly`、`LTXVAudioVAEDecode`、`CreateVideo`、`DisTorchPurgeVRAMV2`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`PromptRelayEncode`、`VRAMReserver`、`PathchSageAttentionKJ`、`VAEDecodeTiled`、`SaveVideo`、`CheckpointLoaderSimple`、`RH_LLMAPI_Pro_Node`、`ZML_SplitText`、`SimpleMath+`、`easy int`、`LoadImage`、`Text`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

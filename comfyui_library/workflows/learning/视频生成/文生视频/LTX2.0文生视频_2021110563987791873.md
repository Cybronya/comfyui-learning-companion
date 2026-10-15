---
key: 视频生成/文生视频/LTX2.0文生视频_2021110563987791873.json
name: LTX2.0文生视频_2021110563987791873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.0文生视频_2021110563987791873.json
hash: 695653ca85a4c8a8
coverage: 0.933333
learned_at: 2026-10-15 22:44:54
nodes: [CFGGuider, LTXVSeparateAVLatent, ImageScaleBy, SamplerCustomAdvanced, LTXVConcatAVLatent, LTXVSeparateAVLatent, CFGGuider, SamplerCustomAdvanced, easy cleanGpuUsed, KSamplerSelect, KSamplerSelect, CR Text, CR Text, ImpactSwitch, PIP_IntegerCalculator, Int, PIP_IntegerCalculator, EmptyImage, PrimitiveInt, PrimitiveFloat, PrimitiveInt, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, easy cleanGpuUsed, CLIPTextEncode, easy cleanGpuUsed, LTXVConditioning, RandomNoise, easy cleanGpuUsed, CLIPTextEncode, easy cleanGpuUsed, ManualSigmas, LTXVConcatAVLatent, CheckpointLoaderSimple, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, LTXVAudioVAELoader, ManualSigmas, easy cleanGpuUsed, VHS_VideoCombine, VAEDecodeTiled, LTXVAudioVAEDecode, CR Text Concatenate, RandomNoise, LTXVLatentUpsampler, SaveAudio, GetImageSize, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, RH_LLMAPI_NODE, LTXVChunkFeedForward, ImpactSwitch, VRAMReserver, CR String To Combo, LoraLoaderModelOnly, LoraLoaderModelOnly, Display Any (rgthree), CR Text Concatenate, CR Text, CR Text Concatenate, CR Text, ManualSigmas, CR Text Concatenate, easy convertAnything, ttN concat, Int, Int, Int, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-distilled-fp8.safetensors", "height": 25, "width": 121}
---

# 视频生成/文生视频/LTX2.0文生视频_2021110563987791873.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.0文生视频_2021110563987791873.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `ImageScaleBy`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `CR Text`
- `CR Text`
- `ImpactSwitch`
- `PIP_IntegerCalculator`
- `Int`
- `PIP_IntegerCalculator`
- `EmptyImage`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `LTXVConditioning`
- `RandomNoise`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `CheckpointLoaderSimple` ★核心
- `LatentUpscaleModelLoader`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `ManualSigmas`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CR Text Concatenate`
- `RandomNoise`
- `LTXVLatentUpsampler` ★核心
- `SaveAudio`
- `GetImageSize`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `RH_LLMAPI_NODE`
- `LTXVChunkFeedForward`
- `ImpactSwitch`
- `VRAMReserver`
- `CR String To Combo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Display Any (rgthree)`
- `CR Text Concatenate`
- `CR Text`
- `CR Text Concatenate`
- `CR Text`
- `ManualSigmas`
- `CR Text Concatenate`
- `easy convertAnything`
- `ttN concat`
- `Int`
- `Int`
- `Int`
- `CR Text`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-distilled-fp8.safetensors`

## 知识

覆盖率 **93%**（70/75）

**有卡**：`CFGGuider`、`LTXVSeparateAVLatent`、`ImageScaleBy`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`easy cleanGpuUsed`、`KSamplerSelect`、`CR Text`、`PIP_IntegerCalculator`、`Int`、`EmptyImage`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`LTXVConditioning`、`RandomNoise`、`ManualSigmas`、`CheckpointLoaderSimple`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`VHS_VideoCombine`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CR Text Concatenate`、`LTXVLatentUpsampler`、`SaveAudio`、`GetImageSize`、`RH_LLMAPI_NODE`、`LTXVChunkFeedForward`、`VRAMReserver`、`CR String To Combo`、`LoraLoaderModelOnly`、`Display Any (rgthree)`、`easy convertAnything`、`ttN concat`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

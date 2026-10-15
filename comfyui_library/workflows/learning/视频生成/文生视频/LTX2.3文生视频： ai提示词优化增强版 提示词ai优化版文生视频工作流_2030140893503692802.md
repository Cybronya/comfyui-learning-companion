---
key: 视频生成/文生视频/LTX2.3文生视频： ai提示词优化增强版 提示词ai优化版文生视频工作流_2030140893503692802.json
name: LTX2.3文生视频： ai提示词优化增强版 提示词ai优化版文生视频工作流_2030140893503692802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频： ai提示词优化增强版 提示词ai优化版文生视频工作流_2030140893503692802.json
hash: 5bc574859e41c032
coverage: 0.934211
learned_at: 2026-10-15 22:45:13
nodes: [CFGGuider, LTXVSeparateAVLatent, ImageScaleBy, CFGGuider, easy cleanGpuUsed, KSamplerSelect, KSamplerSelect, PIP_IntegerCalculator, Int, PIP_IntegerCalculator, EmptyImage, PrimitiveInt, PrimitiveFloat, PrimitiveInt, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, easy cleanGpuUsed, CLIPTextEncode, easy cleanGpuUsed, LTXVConditioning, RandomNoise, easy cleanGpuUsed, CLIPTextEncode, easy cleanGpuUsed, LTXVConcatAVLatent, easy cleanGpuUsed, VHS_VideoCombine, VAEDecodeTiled, LTXVAudioVAEDecode, Int, Int, CR Text Concatenate, RandomNoise, GetImageSize, CR Text Concatenate, ttN concat, easy convertAnything, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, RH_LLMAPI_NODE, LTXVChunkFeedForward, VRAMReserver, CR String To Combo, LoraLoaderModelOnly, LoraLoaderModelOnly, Display Any (rgthree), CR Text Concatenate, CR Text Concatenate, CR Text, CheckpointLoaderSimple, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, LTXVAudioVAELoader, SamplerCustomAdvanced, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, SamplerCustomAdvanced, CR Text, ManualSigmas, LTXVScheduler, ManualSigmas, ManualSigmas, ImpactSwitch, ImpactSwitch, CR Text, CR Text, SaveAudio, Int, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled.safetensors", "height": 25, "width": 121}
---

# 视频生成/文生视频/LTX2.3文生视频： ai提示词优化增强版 提示词ai优化版文生视频工作流_2030140893503692802.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频： ai提示词优化增强版 提示词ai优化版文生视频工作流_2030140893503692802.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（76 个）：
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `ImageScaleBy`
- `CFGGuider`
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
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
- `LTXVConcatAVLatent`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `Int`
- `Int`
- `CR Text Concatenate`
- `RandomNoise`
- `GetImageSize`
- `CR Text Concatenate`
- `ttN concat`
- `easy convertAnything`
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
- `VRAMReserver`
- `CR String To Combo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Display Any (rgthree)`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text`
- `CheckpointLoaderSimple` ★核心
- `LatentUpscaleModelLoader`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `CR Text`
- `ManualSigmas`
- `LTXVScheduler`
- `ManualSigmas`
- `ManualSigmas`
- `ImpactSwitch`
- `ImpactSwitch`
- `CR Text`
- `CR Text`
- `SaveAudio`
- `Int`
- `CR Text`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled.safetensors`

## 知识

覆盖率 **93%**（71/76）

**有卡**：`CFGGuider`、`LTXVSeparateAVLatent`、`ImageScaleBy`、`easy cleanGpuUsed`、`KSamplerSelect`、`PIP_IntegerCalculator`、`Int`、`EmptyImage`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`LTXVConditioning`、`RandomNoise`、`LTXVConcatAVLatent`、`VHS_VideoCombine`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CR Text Concatenate`、`GetImageSize`、`ttN concat`、`easy convertAnything`、`CR Text`、`RH_LLMAPI_NODE`、`LTXVChunkFeedForward`、`VRAMReserver`、`CR String To Combo`、`LoraLoaderModelOnly`、`Display Any (rgthree)`、`CheckpointLoaderSimple`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`ManualSigmas`、`LTXVScheduler`、`SaveAudio`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

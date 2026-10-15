---
key: 视频生成/文生视频/LTX2.0 文生视频_2008733695988994049.json
name: LTX2.0 文生视频_2008733695988994049
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.0 文生视频_2008733695988994049.json
hash: 9a7872ea65244b92
coverage: 1
learned_at: 2026-10-15 22:44:49
nodes: [Int, Int, Int, Int, EmptyLTXVLatentVideo, LTXVConditioning, RandomNoise, CFGGuider, KSamplerSelect, intToFloat _O, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVAudioVAEDecode, CFGGuider, KSamplerSelect, ManualSigmas, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVAudioVAELoader, RandomNoise, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVConcatAVLatent, LTXVLatentUpsampler, LatentUpscaleModelLoader, CheckpointLoaderSimple, ManualSigmas, VHS_VideoCombine, VHS_VideoCombine, CLIPTextEncode, LoraLoaderModelOnly, Text, MathExpression|pysssss, LoadImage, LoadImage, LTXAVTextEncoderLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-distilled-fp8.safetensors", "height": 25, "width": 121}
---

# 视频生成/文生视频/LTX2.0 文生视频_2008733695988994049.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.0 文生视频_2008733695988994049.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（39 个）：
- `Int`
- `Int`
- `Int`
- `Int`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `intToFloat _O`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVAudioVAELoader`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `ManualSigmas`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Text`
- `MathExpression|pysssss`
- `LoadImage`
- `LoadImage`
- `LTXAVTextEncoderLoader`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-distilled-fp8.safetensors`

## 知识

覆盖率 **100%**（39/39）

**有卡**：`Int`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`intToFloat _O`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXVAudioVAELoader`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`VHS_VideoCombine`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`Text`、`MathExpression|pysssss`、`LoadImage`、`LTXAVTextEncoderLoader`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

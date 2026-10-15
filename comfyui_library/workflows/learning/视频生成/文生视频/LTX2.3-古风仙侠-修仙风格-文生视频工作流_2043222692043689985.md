---
key: 视频生成/文生视频/LTX2.3-古风仙侠-修仙风格-文生视频工作流_2043222692043689985.json
name: LTX2.3-古风仙侠-修仙风格-文生视频工作流_2043222692043689985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-古风仙侠-修仙风格-文生视频工作流_2043222692043689985.json
hash: 41a4e1f381ee204e
coverage: 0.954545
learned_at: 2026-10-15 22:45:03
nodes: [CLIPTextEncode, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, LTXVConcatAVLatent, PathchSageAttentionKJ, ManualSigmas, VHS_VideoCombine, LatentUpscaleModelLoader, CFGGuider, RandomNoise, CFGGuider, LTXVConditioning, KSamplerSelect, ManualSigmas, LTXVAudioVAELoader, ModelPatchTorchSettings, LTXVChunkFeedForward, CheckpointLoaderSimple, CheckpointLoaderSimple, PrimitiveInt, LTXVEmptyLatentAudio, easy int, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVScheduler, easy showAnything, VAEDecodeTiled, RandomNoise, LTXVLatentUpsampler, KSamplerSelect, LTXVConcatAVLatent, VAEDecodeTiled, VHS_VideoCombine, LoraLoaderModelOnly, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LTXVCropGuides, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVAudioVAEDecode, easy int, easy int, CLIPTextEncode, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 24, "width": 97}
---

# 视频生成/文生视频/LTX2.3-古风仙侠-修仙风格-文生视频工作流_2043222692043689985.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-古风仙侠-修仙风格-文生视频工作流_2043222692043689985.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（44 个）：
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConcatAVLatent`
- `PathchSageAttentionKJ`
- `ManualSigmas`
- `VHS_VideoCombine`
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `RandomNoise`
- `CFGGuider`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVAudioVAELoader`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `easy int`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVScheduler`
- `easy showAnything`
- `VAEDecodeTiled` ★核心
- `RandomNoise`
- `LTXVLatentUpsampler` ★核心
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `easy int`
- `easy int`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（42/44）

**有卡**：`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`PathchSageAttentionKJ`、`ManualSigmas`、`VHS_VideoCombine`、`LatentUpscaleModelLoader`、`CFGGuider`、`RandomNoise`、`LTXVConditioning`、`KSamplerSelect`、`LTXVAudioVAELoader`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`CheckpointLoaderSimple`、`LTXVEmptyLatentAudio`、`easy int`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVScheduler`、`VAEDecodeTiled`、`LTXVLatentUpsampler`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`LTXVCropGuides`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

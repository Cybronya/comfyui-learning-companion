---
key: 视频生成/文生视频/文生视频 加速版 LTX2.3 多角色对话 数字人说话唱歌_2043136851845844993.json
name: 文生视频 加速版 LTX2.3 多角色对话 数字人说话唱歌_2043136851845844993
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生视频 加速版 LTX2.3 多角色对话 数字人说话唱歌_2043136851845844993.json
hash: 5c8b2a118c8ffdc3
coverage: 0.88
learned_at: 2026-10-15 22:48:41
nodes: [CLIPTextEncode, CheckpointLoaderSimple, LTXVConditioning, LTXVAudioVAEDecode, Reroute, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVAudioVAELoader, LTXVAudioVAELoader, LTXAVTextEncoderLoader, PathchSageAttentionKJ, ModelPatchTorchSettings, LoraLoaderModelOnly, ManualSigmas, LTXVChunkFeedForward, RandomNoise, VAEDecodeTiled, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVAudioVAEDecode, SamplerCustomAdvanced, LTXVConcatAVLatent, RandomNoise, CFGGuider, LatentUpscaleModelLoader, LTXVCropGuides, LTXVLatentUpsampler, EmptyImage, KSamplerSelect, KSamplerSelect, VHS_VideoCombine, ManualSigmas, easy showAnything, LTXVScheduler, EmptyLTXVLatentVideo, easy showAnything, easy showAnything, easy showAnything, SimpleMath+, LayerUtility: ImageScaleByAspectRatio V2, easy int, easy int, easy float, Reroute, CheckpointLoaderSimple, VHS_VideoCombine, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 24, "width": 97}
---

# 视频生成/文生视频/文生视频 加速版 LTX2.3 多角色对话 数字人说话唱歌_2043136851845844993.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/文生视频 加速版 LTX2.3 多角色对话 数字人说话唱歌_2043136851845844993.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（50 个）：
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVConditioning`
- `LTXVAudioVAEDecode` ★核心
- `Reroute`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVAudioVAELoader`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LoraLoaderModelOnly` ★核心
- `ManualSigmas`
- `LTXVChunkFeedForward`
- `RandomNoise`
- `VAEDecodeTiled` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `RandomNoise`
- `CFGGuider`
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `EmptyImage`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `VHS_VideoCombine`
- `ManualSigmas`
- `easy showAnything`
- `LTXVScheduler`
- `EmptyLTXVLatentVideo`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `SimpleMath+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `easy int`
- `easy float`
- `Reroute`
- `CheckpointLoaderSimple` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（44/50）

**有卡**：`CLIPTextEncode`、`CheckpointLoaderSimple`、`LTXVConditioning`、`LTXVAudioVAEDecode`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LoraLoaderModelOnly`、`ManualSigmas`、`LTXVChunkFeedForward`、`RandomNoise`、`VAEDecodeTiled`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`EmptyImage`、`KSamplerSelect`、`VHS_VideoCombine`、`LTXVScheduler`、`EmptyLTXVLatentVideo`、`SimpleMath+`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`easy float`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

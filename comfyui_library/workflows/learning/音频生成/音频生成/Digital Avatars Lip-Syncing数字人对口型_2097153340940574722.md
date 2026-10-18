---
key: 音频生成/音频生成/Digital Avatars Lip-Syncing数字人对口型_2097153340940574722.json
name: Digital Avatars Lip-Syncing数字人对口型_2097153340940574722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Digital Avatars Lip-Syncing数字人对口型_2097153340940574722.json
hash: d7df88ceca35aa72
coverage: 0.757576
learned_at: 2026-10-18 17:45:29
nodes: [CLIPTextEncode, CLIPLoader, ConditioningZeroOut, AudioEncoderLoader, VAELoader, ModelPatchLoader, VAEDecode, easy cleanGpuUsed, KSamplerAdvanced, PathchSageAttentionKJ, LoraLoaderModelOnly, UNETLoader, ImageConcatMulti, AudioEncoderEncode, PainterAudioCut, easy showAnything, LoadAudio, PainterAV2V, VHS_VideoInfo, easy showAnything, MathExpression|pysssss, easy showAnything, easy showAnything, easy showAnything, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, VHS_LoadVideo, LoadImage, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, Note, Note]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": "normal", "sampler_name": 1, "scheduler": "dpmpp_sde", "seed": "enable", "steps": "randomize"}
---

# 音频生成/音频生成/Digital Avatars Lip-Syncing数字人对口型_2097153340940574722.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Digital Avatars Lip-Syncing数字人对口型_2097153340940574722.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（33 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ConditioningZeroOut`
- `AudioEncoderLoader`
- `VAELoader`
- `ModelPatchLoader`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ImageConcatMulti`
- `AudioEncoderEncode`
- `PainterAudioCut`
- `easy showAnything`
- `LoadAudio`
- `PainterAV2V`
- `VHS_VideoInfo`
- `easy showAnything`
- `MathExpression|pysssss`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `Note`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `3`
- `sampler_name` = `1`
- `scheduler` = `dpmpp_sde`
- `denoise` = `normal`

## 知识

覆盖率 **76%**（25/33）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`ConditioningZeroOut`、`AudioEncoderLoader`、`VAELoader`、`ModelPatchLoader`、`VAEDecode`、`easy cleanGpuUsed`、`KSamplerAdvanced`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`UNETLoader`、`ImageConcatMulti`、`AudioEncoderEncode`、`PainterAudioCut`、`LoadAudio`、`PainterAV2V`、`VHS_VideoInfo`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

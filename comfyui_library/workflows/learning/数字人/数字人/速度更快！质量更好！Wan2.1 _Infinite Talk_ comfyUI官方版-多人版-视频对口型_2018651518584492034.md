---
key: 数字人/数字人/速度更快！质量更好！Wan2.1 _Infinite Talk_ comfyUI官方版-多人版-视频对口型_2018651518584492034.json
name: 速度更快！质量更好！Wan2.1 _Infinite Talk_ comfyUI官方版-多人版-视频对口型_2018651518584492034
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/速度更快！质量更好！Wan2.1 _Infinite Talk_ comfyUI官方版-多人版-视频对口型_2018651518584492034.json
hash: e3c5e72725d69acc
coverage: 0.770492
learned_at: 2026-10-26 02:05:47
nodes: [PrimitiveInt, Reroute, Reroute, Reroute, PrimitiveInt, Reroute, Reroute, Reroute, Reroute, ConditioningZeroOut, Reroute, AudioEncoderEncode, AudioEncoderEncode, Reroute, MarkdownNote, KSamplerSelect, CFGGuider, BasicScheduler, RandomNoise, WanInfiniteTalkToVideo, WanInfiniteTalkToVideo, VAELoader, CLIPLoader, SamplerCustomAdvanced, UNETLoader, LoraLoaderModelOnly, AudioEncoderLoader, CLIPTextEncode, VAEDecode, CFGGuider, RandomNoise, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, CFGGuider, RandomNoise, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, VAEDecode, ImageFromBatch, AudioConcat, MarkdownNote, VAEDecode, ImageBatch, ImageFromBatch, ImageBatch, MarkdownNote, ModelPatchLoader, Label (rgthree), LoadAudio, LoadAudio, LoadImage, LoadImage, WanInfiniteTalkToVideo, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, CustomAddLabel, CustomAddLabel, CustomAddLabel]
patterns: []
missing: []
---

# 数字人/数字人/速度更快！质量更好！Wan2.1 _Infinite Talk_ comfyUI官方版-多人版-视频对口型_2018651518584492034.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/速度更快！质量更好！Wan2.1 _Infinite Talk_ comfyUI官方版-多人版-视频对口型_2018651518584492034.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（61 个）：
- `PrimitiveInt`
- `Reroute`
- `Reroute`
- `Reroute`
- `PrimitiveInt`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ConditioningZeroOut`
- `Reroute`
- `AudioEncoderEncode`
- `AudioEncoderEncode`
- `Reroute`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `BasicScheduler`
- `RandomNoise`
- `WanInfiniteTalkToVideo`
- `WanInfiniteTalkToVideo`
- `VAELoader`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `AudioEncoderLoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageFromBatch`
- `AudioConcat`
- `MarkdownNote`
- `VAEDecode` ★核心
- `ImageBatch`
- `ImageFromBatch`
- `ImageBatch`
- `MarkdownNote`
- `ModelPatchLoader`
- `Label (rgthree)`
- `LoadAudio`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `WanInfiniteTalkToVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CustomAddLabel`
- `CustomAddLabel`
- `CustomAddLabel`

## 知识

覆盖率 **77%**（47/61）

**有卡**：`ConditioningZeroOut`、`AudioEncoderEncode`、`KSamplerSelect`、`CFGGuider`、`BasicScheduler`、`RandomNoise`、`WanInfiniteTalkToVideo`、`VAELoader`、`CLIPLoader`、`SamplerCustomAdvanced`、`UNETLoader`、`LoraLoaderModelOnly`、`AudioEncoderLoader`、`CLIPTextEncode`、`VAEDecode`、`ImageFromBatch`、`AudioConcat`、`ImageBatch`、`ModelPatchLoader`、`Label (rgthree)`、`LoadAudio`、`LoadImage`、`VHS_VideoCombine`、`CustomAddLabel`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

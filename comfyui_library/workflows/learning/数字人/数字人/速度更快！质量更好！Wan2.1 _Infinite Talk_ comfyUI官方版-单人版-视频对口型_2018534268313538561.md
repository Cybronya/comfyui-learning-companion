---
key: 数字人/数字人/速度更快！质量更好！Wan2.1 _Infinite Talk_ comfyUI官方版-单人版-视频对口型_2018534268313538561.json
name: 速度更快！质量更好！Wan2.1 _Infinite Talk_ comfyUI官方版-单人版-视频对口型_2018534268313538561
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/速度更快！质量更好！Wan2.1 _Infinite Talk_ comfyUI官方版-单人版-视频对口型_2018534268313538561.json
hash: f743c10ac3e0e184
coverage: 0.786885
learned_at: 2026-10-26 02:05:47
nodes: [INTConstant, SetNode, INTConstant, SetNode, TrimAudioDuration, Reroute, Reroute, Reroute, Reroute, ConditioningZeroOut, Reroute, MarkdownNote, KSamplerSelect, BasicScheduler, RandomNoise, WanInfiniteTalkToVideo, VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, AudioEncoderLoader, WanInfiniteTalkToVideo, RandomNoise, KSamplerSelect, BasicScheduler, MarkdownNote, WanInfiniteTalkToVideo, CFGGuider, SamplerCustomAdvanced, VAEDecode, CFGGuider, RandomNoise, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, VAEDecode, ImageFromBatch, ImageBatch, CFGGuider, SamplerCustomAdvanced, VAEDecode, ImageFromBatch, ImageBatch, CLIPTextEncode, Reroute, AudioEncoderEncode, ModelPatchLoader, AudioCrop, MarkdownNote, Label (rgthree), GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, LoadAudio, VHS_LoadVideo, LoadImage, VHS_VideoCombine, CustomAddLabel, CustomAddLabel, CustomAddLabel]
patterns: []
missing: []
---

# 数字人/数字人/速度更快！质量更好！Wan2.1 _Infinite Talk_ comfyUI官方版-单人版-视频对口型_2018534268313538561.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/速度更快！质量更好！Wan2.1 _Infinite Talk_ comfyUI官方版-单人版-视频对口型_2018534268313538561.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（61 个）：
- `INTConstant`
- `SetNode`
- `INTConstant`
- `SetNode`
- `TrimAudioDuration`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ConditioningZeroOut`
- `Reroute`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `RandomNoise`
- `WanInfiniteTalkToVideo`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `AudioEncoderLoader`
- `WanInfiniteTalkToVideo`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `MarkdownNote`
- `WanInfiniteTalkToVideo`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageFromBatch`
- `ImageBatch`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageFromBatch`
- `ImageBatch`
- `CLIPTextEncode` ★核心
- `Reroute`
- `AudioEncoderEncode`
- `ModelPatchLoader`
- `AudioCrop`
- `MarkdownNote`
- `Label (rgthree)`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadAudio`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoCombine`
- `CustomAddLabel`
- `CustomAddLabel`
- `CustomAddLabel`

## 知识

覆盖率 **79%**（48/61）

**有卡**：`INTConstant`、`TrimAudioDuration`、`ConditioningZeroOut`、`KSamplerSelect`、`BasicScheduler`、`RandomNoise`、`WanInfiniteTalkToVideo`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`AudioEncoderLoader`、`CFGGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`ImageFromBatch`、`ImageBatch`、`CLIPTextEncode`、`AudioEncoderEncode`、`ModelPatchLoader`、`AudioCrop`、`Label (rgthree)`、`VHS_VideoCombine`、`LoadAudio`、`VHS_LoadVideo`、`LoadImage`、`CustomAddLabel`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

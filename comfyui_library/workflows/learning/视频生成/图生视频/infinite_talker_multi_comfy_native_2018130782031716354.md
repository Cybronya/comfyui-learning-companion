---
key: 视频生成/图生视频/infinite_talker_multi_comfy_native_2018130782031716354.json
name: infinite_talker_multi_comfy_native_2018130782031716354.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/infinite_talker_multi_comfy_native_2018130782031716354.json
hash: 593cf8ba46764708
coverage: 0.754386
learned_at: 2026-10-15 22:34:51
nodes: [PrimitiveInt, Reroute, Reroute, Reroute, PrimitiveInt, Reroute, Reroute, Reroute, Reroute, ConditioningZeroOut, Reroute, AudioEncoderEncode, AudioEncoderEncode, Reroute, MarkdownNote, KSamplerSelect, CFGGuider, BasicScheduler, RandomNoise, WanInfiniteTalkToVideo, WanInfiniteTalkToVideo, VAELoader, CLIPLoader, SamplerCustomAdvanced, UNETLoader, LoraLoaderModelOnly, AudioEncoderLoader, CLIPTextEncode, VAEDecode, CFGGuider, RandomNoise, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, VHS_VideoCombine, VHS_VideoCombine, WanInfiniteTalkToVideo, CFGGuider, RandomNoise, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, VAEDecode, ImageFromBatch, VHS_VideoCombine, AudioConcat, MarkdownNote, VAEDecode, ImageBatch, ImageFromBatch, ImageBatch, LoadAudio, LoadAudio, LoadImage, LoadImage, MarkdownNote, ModelPatchLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/infinite_talker_multi_comfy_native_2018130782031716354.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2018130782031716354.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（57 个）：
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
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageFromBatch`
- `VHS_VideoCombine`
- `AudioConcat`
- `MarkdownNote`
- `VAEDecode` ★核心
- `ImageBatch`
- `ImageFromBatch`
- `ImageBatch`
- `LoadAudio`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `ModelPatchLoader`

## 知识

覆盖率 **75%**（43/57）

**有卡**：`ConditioningZeroOut`、`AudioEncoderEncode`、`KSamplerSelect`、`CFGGuider`、`BasicScheduler`、`RandomNoise`、`WanInfiniteTalkToVideo`、`VAELoader`、`CLIPLoader`、`SamplerCustomAdvanced`、`UNETLoader`、`LoraLoaderModelOnly`、`AudioEncoderLoader`、`CLIPTextEncode`、`VAEDecode`、`VHS_VideoCombine`、`ImageFromBatch`、`AudioConcat`、`ImageBatch`、`LoadAudio`、`LoadImage`、`ModelPatchLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

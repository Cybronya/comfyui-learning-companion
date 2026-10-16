---
key: 视频生成/图生视频/Wan2.2+RCM+Infinite Talk官方对口型工作流高动态图生数字人_2018324382791245826.json
name: Wan2.2+RCM+Infinite Talk官方对口型工作流高动态图生数字人_2018324382791245826.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2018324382791245826.json
hash: d7c32b97438bf1f5
coverage: 0.97561
learned_at: 2026-10-15 22:34:56
nodes: [RH_GetAudioDuration, LoadImage, LoadImage, MarkdownNote, UNETLoader, UNETLoader, LoadAudio, CR Text, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, CLIPLoader, ModelPatchLoader, VAELoader, ImageResizeKJv2, RHHiddenNodes, SomethingToString, PainterAI2V, CLIPTextEncode, KSamplerAdvanced, CLIPTextEncode, KSamplerAdvanced, VAEDecode, WujiCleaner, ImageFromBatch, AudioSeparation, PainterAudioCut, Float to Int, SimpleMath+, AudioEncoderEncode, AudioEncoderLoader, SimpleMath+, ColorMatch, VHS_VideoCombine, INTConstant, INTConstant]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2+RCM+Infinite Talk官方对口型工作流高动态图生数字人_2018324382791245826.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2018324382791245826.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（41 个）：
- `RH_GetAudioDuration`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadAudio`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `ModelPatchLoader`
- `VAELoader`
- `ImageResizeKJv2`
- `RHHiddenNodes`
- `SomethingToString`
- `PainterAI2V`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `WujiCleaner`
- `ImageFromBatch`
- `AudioSeparation`
- `PainterAudioCut`
- `Float to Int`
- `SimpleMath+`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `SimpleMath+`
- `ColorMatch`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **98%**（40/41）

**有卡**：`RH_GetAudioDuration`、`LoadImage`、`UNETLoader`、`LoadAudio`、`CR Text`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPLoader`、`ModelPatchLoader`、`VAELoader`、`ImageResizeKJv2`、`RHHiddenNodes`、`SomethingToString`、`PainterAI2V`、`CLIPTextEncode`、`KSamplerAdvanced`、`VAEDecode`、`WujiCleaner`、`ImageFromBatch`、`AudioSeparation`、`PainterAudioCut`、`Float to Int`、`SimpleMath+`、`AudioEncoderEncode`、`AudioEncoderLoader`、`ColorMatch`、`VHS_VideoCombine`、`INTConstant`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

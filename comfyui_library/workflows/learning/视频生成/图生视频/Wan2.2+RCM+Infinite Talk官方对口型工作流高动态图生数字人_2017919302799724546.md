---
key: 视频生成/图生视频/Wan2.2+RCM+Infinite Talk官方对口型工作流高动态图生数字人_2017919302799724546.json
name: Wan2.2+RCM+Infinite Talk官方对口型工作流高动态图生数字人_2017919302799724546.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2+RCM+Infinite Talk官方对口型工作流高动态图生数字人_2017919302799724546.json
hash: eab41fb7192db571
coverage: 1
learned_at: 2026-10-15 22:34:51
nodes: [AudioSeparation, PainterAudioCut, AudioEncoderLoader, RH_GetAudioDuration, Float to Int, AudioEncoderEncode, PainterAI2V, VAEDecode, WujiCleaner, SimpleMath+, LoadImage, LoadAudio, ModelPatchLoader, VAELoader, ImageResizeKJv2, CLIPLoader, SimpleMath+, KSamplerAdvanced, KSamplerAdvanced, INTConstant, INTConstant, ImageFromBatch, ColorMatch, CR Text, VHS_VideoCombine, SomethingToString, RHHiddenNodes, CLIPTextEncode, CLIPTextEncode, UNETLoader, UNETLoader, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2+RCM+Infinite Talk官方对口型工作流高动态图生数字人_2017919302799724546.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2017919302799724546.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（39 个）：
- `AudioSeparation`
- `PainterAudioCut`
- `AudioEncoderLoader`
- `RH_GetAudioDuration`
- `Float to Int`
- `AudioEncoderEncode`
- `PainterAI2V`
- `VAEDecode` ★核心
- `WujiCleaner`
- `SimpleMath+`
- `LoadImage`
- `LoadAudio`
- `ModelPatchLoader`
- `VAELoader`
- `ImageResizeKJv2`
- `CLIPLoader`
- `SimpleMath+`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `INTConstant`
- `ImageFromBatch`
- `ColorMatch`
- `CR Text`
- `VHS_VideoCombine`
- `SomethingToString`
- `RHHiddenNodes`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（39/39）

**有卡**：`AudioSeparation`、`PainterAudioCut`、`AudioEncoderLoader`、`RH_GetAudioDuration`、`Float to Int`、`AudioEncoderEncode`、`PainterAI2V`、`VAEDecode`、`WujiCleaner`、`SimpleMath+`、`LoadImage`、`LoadAudio`、`ModelPatchLoader`、`VAELoader`、`ImageResizeKJv2`、`CLIPLoader`、`KSamplerAdvanced`、`INTConstant`、`ImageFromBatch`、`ColorMatch`、`CR Text`、`VHS_VideoCombine`、`SomethingToString`、`RHHiddenNodes`、`CLIPTextEncode`、`UNETLoader`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

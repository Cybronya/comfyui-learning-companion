---
key: 视频生成/图生视频/Wan2.2+RCM+Infinite Talk官方对口型工作流高动态图生数字人_2026965800891981825.json
name: Wan2.2+RCM+Infinite Talk官方对口型工作流高动态图生数字人_2026965800891981825.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2026965800891981825.json
hash: 62484ac47938ab3e
coverage: 1
learned_at: 2026-10-15 22:35:15
nodes: [LoadImage, INTConstant, INTConstant, LoadAudio, VAELoader, ModelPatchLoader, CLIPTextEncode, AudioSeparation, RH_GetAudioDuration, UNETLoader, LoraLoaderModelOnly, PainterAudioCut, LoraLoaderModelOnly, AudioEncoderLoader, PathchSageAttentionKJ, AudioEncoderEncode, ModelPatchTorchSettings, SimpleMath+, Float to Int, SimpleMath+, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, RHHiddenNodes, SomethingToString, ModelPatchTorchSettings, PathchSageAttentionKJ, CLIPLoader, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, PainterAI2V, VAEDecode, VHS_VideoCombine, ColorMatch, ImageFromBatch, WujiCleaner, ImageResizeKJv2, CR Text]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2+RCM+Infinite Talk官方对口型工作流高动态图生数字人_2026965800891981825.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2026965800891981825.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（39 个）：
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `LoadAudio`
- `VAELoader`
- `ModelPatchLoader`
- `CLIPTextEncode` ★核心
- `AudioSeparation`
- `RH_GetAudioDuration`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PainterAudioCut`
- `LoraLoaderModelOnly` ★核心
- `AudioEncoderLoader`
- `PathchSageAttentionKJ`
- `AudioEncoderEncode`
- `ModelPatchTorchSettings`
- `SimpleMath+`
- `Float to Int`
- `SimpleMath+`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RHHiddenNodes`
- `SomethingToString`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PainterAI2V`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `ColorMatch`
- `ImageFromBatch`
- `WujiCleaner`
- `ImageResizeKJv2`
- `CR Text`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（39/39）

**有卡**：`LoadImage`、`INTConstant`、`LoadAudio`、`VAELoader`、`ModelPatchLoader`、`CLIPTextEncode`、`AudioSeparation`、`RH_GetAudioDuration`、`UNETLoader`、`LoraLoaderModelOnly`、`PainterAudioCut`、`AudioEncoderLoader`、`PathchSageAttentionKJ`、`AudioEncoderEncode`、`ModelPatchTorchSettings`、`SimpleMath+`、`Float to Int`、`RHHiddenNodes`、`SomethingToString`、`CLIPLoader`、`KSamplerAdvanced`、`PainterAI2V`、`VAEDecode`、`VHS_VideoCombine`、`ColorMatch`、`ImageFromBatch`、`WujiCleaner`、`ImageResizeKJv2`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

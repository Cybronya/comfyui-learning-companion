---
key: 数字人/数字人/Wan2.2+RCM对口型工作流高动态_2021028256081780738.json
name: Wan2.2+RCM对口型工作流高动态_2021028256081780738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2+RCM对口型工作流高动态_2021028256081780738.json
hash: e3d066c64f02871e
coverage: 1
learned_at: 2026-10-26 01:57:54
nodes: [AudioSeparation, PainterAudioCut, AudioEncoderLoader, RH_GetAudioDuration, Float to Int, AudioEncoderEncode, PainterAI2V, VAEDecode, WujiCleaner, SimpleMath+, ModelPatchLoader, VAELoader, ImageResizeKJv2, CLIPLoader, SimpleMath+, KSamplerAdvanced, KSamplerAdvanced, INTConstant, INTConstant, ImageFromBatch, ColorMatch, VHS_VideoCombine, SomethingToString, RHHiddenNodes, CLIPTextEncode, CLIPTextEncode, UNETLoader, UNETLoader, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, CR Text, LoadAudio]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 数字人/数字人/Wan2.2+RCM对口型工作流高动态_2021028256081780738.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2+RCM对口型工作流高动态_2021028256081780738.json`

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
- `LoadImage`
- `CR Text`
- `LoadAudio`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（39/39）

**有卡**：`AudioSeparation`、`PainterAudioCut`、`AudioEncoderLoader`、`RH_GetAudioDuration`、`Float to Int`、`AudioEncoderEncode`、`PainterAI2V`、`VAEDecode`、`WujiCleaner`、`SimpleMath+`、`ModelPatchLoader`、`VAELoader`、`ImageResizeKJv2`、`CLIPLoader`、`KSamplerAdvanced`、`INTConstant`、`ImageFromBatch`、`ColorMatch`、`VHS_VideoCombine`、`SomethingToString`、`RHHiddenNodes`、`CLIPTextEncode`、`UNETLoader`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`LoadImage`、`CR Text`、`LoadAudio`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

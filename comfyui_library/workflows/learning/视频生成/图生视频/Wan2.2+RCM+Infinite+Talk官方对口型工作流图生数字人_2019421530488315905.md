---
key: 视频生成/图生视频/Wan2.2+RCM+Infinite+Talk官方对口型工作流图生数字人_2019421530488315905.json
name: Wan2.2+RCM+Infinite+Talk官方对口型工作流图生数字人_2019421530488315905.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2019421530488315905.json
hash: d99ad73d006da5f5
coverage: 1
learned_at: 2026-10-15 22:35:02
nodes: [AudioSeparation, PainterAudioCut, AudioEncoderLoader, RH_GetAudioDuration, Float to Int, AudioEncoderEncode, VAEDecode, WujiCleaner, SimpleMath+, VAELoader, CLIPLoader, SimpleMath+, KSamplerAdvanced, KSamplerAdvanced, INTConstant, INTConstant, ImageFromBatch, ColorMatch, SomethingToString, RHHiddenNodes, CLIPTextEncode, CLIPTextEncode, UNETLoader, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, ImageResizeKJv2, ModelPatchLoader, PainterAI2V, LoadImage, CR Text, LoadAudio, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2+RCM+Infinite+Talk官方对口型工作流图生数字人_2019421530488315905.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2019421530488315905.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（39 个）：
- `AudioSeparation`
- `PainterAudioCut`
- `AudioEncoderLoader`
- `RH_GetAudioDuration`
- `Float to Int`
- `AudioEncoderEncode`
- `VAEDecode` ★核心
- `WujiCleaner`
- `SimpleMath+`
- `VAELoader`
- `CLIPLoader`
- `SimpleMath+`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `INTConstant`
- `ImageFromBatch`
- `ColorMatch`
- `SomethingToString`
- `RHHiddenNodes`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ImageResizeKJv2`
- `ModelPatchLoader`
- `PainterAI2V`
- `LoadImage`
- `CR Text`
- `LoadAudio`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（39/39）

**有卡**：`AudioSeparation`、`PainterAudioCut`、`AudioEncoderLoader`、`RH_GetAudioDuration`、`Float to Int`、`AudioEncoderEncode`、`VAEDecode`、`WujiCleaner`、`SimpleMath+`、`VAELoader`、`CLIPLoader`、`KSamplerAdvanced`、`INTConstant`、`ImageFromBatch`、`ColorMatch`、`SomethingToString`、`RHHiddenNodes`、`CLIPTextEncode`、`UNETLoader`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`ModelPatchLoader`、`PainterAI2V`、`LoadImage`、`CR Text`、`LoadAudio`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

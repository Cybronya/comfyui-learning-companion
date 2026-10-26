---
key: 数字人/数字人/中间帧 Wan2.2 首尾帧+中间帧_1985539167335686145.json
name: 中间帧 Wan2.2 首尾帧+中间帧_1985539167335686145
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/中间帧 Wan2.2 首尾帧+中间帧_1985539167335686145.json
hash: 94bdde0e72036719
coverage: 1
learned_at: 2026-10-26 02:00:09
nodes: [INTConstant, ImageScaleBy, ImageScaleBy, ImageConcatMulti, CLIPLoader, VHS_VideoCombine, KSamplerAdvanced, INTConstant, ImageScaleBy, KSamplerAdvanced, ModelSamplingSD3, LoraLoaderModelOnly, CLIPTextEncode, ModelSamplingSD3, VAEDecode, VHS_VideoCombine, ImageConcanate, LoadImage, LoadImage, LoadImage, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, Int, Text, SimpleMath+, Int, UNETLoader, UNETLoader, LoraLoaderModelOnly, WanFirstMiddleLastFrameToVideo]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 数字人/数字人/中间帧 Wan2.2 首尾帧+中间帧_1985539167335686145.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/中间帧 Wan2.2 首尾帧+中间帧_1985539167335686145.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（33 个）：
- `INTConstant`
- `ImageScaleBy`
- `ImageScaleBy`
- `ImageConcatMulti`
- `CLIPLoader`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `ImageScaleBy`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `ImageConcanate`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `Text`
- `SimpleMath+`
- `Int`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanFirstMiddleLastFrameToVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `5`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（33/33）

**有卡**：`INTConstant`、`ImageScaleBy`、`ImageConcatMulti`、`CLIPLoader`、`VHS_VideoCombine`、`KSamplerAdvanced`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`VAEDecode`、`ImageConcanate`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`Int`、`Text`、`SimpleMath+`、`UNETLoader`、`WanFirstMiddleLastFrameToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

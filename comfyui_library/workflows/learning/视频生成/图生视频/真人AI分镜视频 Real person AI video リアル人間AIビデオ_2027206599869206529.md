---
key: 视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027206599869206529.json
name: 真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027206599869206529.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2027206599869206529.json
hash: e840cde0ecc4b976
coverage: 0.702128
learned_at: 2026-10-15 22:35:16
nodes: [GetNode, GetNode, KSamplerAdvanced, DiffusionModelLoaderKJ, LoraLoaderModelOnly, SetNode, DiffusionModelLoaderKJ, LoraLoaderModelOnly, VAELoader, CLIPLoader, SetNode, GetNode, GetNode, VAEDecode, LoraLoaderModelOnly, SetNode, SetNode, LayerUtility: PurgeVRAM V2, GetNode, KSamplerAdvanced, VAEEncode, GetNode, ImageFromBatch+, VAEEncode, PreviewImage, CLIPTextEncode, PrimitiveFloat, VHS_VideoCombine, JDCN_StringToList, Reroute, easy indexAnything, easy indexAnything, CLIPTextEncode, KSamplerAdvanced, WanImageToVideoSVIPro, CLIPTextEncode, WanImageToVideoSVIPro, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, VAEDecode, JWInteger, ImageBatchExtendWithOverlap, VHS_VideoCombine, VHS_VideoCombine, Text, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027206599869206529.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2027206599869206529.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `VAEEncode` ★核心
- `GetNode`
- `ImageFromBatch+`
- `VAEEncode` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `JDCN_StringToList`
- `Reroute`
- `easy indexAnything`
- `easy indexAnything`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideoSVIPro`
- `CLIPTextEncode` ★核心
- `WanImageToVideoSVIPro`
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `VAEDecode` ★核心
- `JWInteger`
- `ImageBatchExtendWithOverlap`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Text`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **70%**（33/47）

**有卡**：`KSamplerAdvanced`、`DiffusionModelLoaderKJ`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`VAEEncode`、`ImageFromBatch+`、`CLIPTextEncode`、`VHS_VideoCombine`、`JDCN_StringToList`、`easy indexAnything`、`WanImageToVideoSVIPro`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`ImageBatchExtendWithOverlap`、`Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode

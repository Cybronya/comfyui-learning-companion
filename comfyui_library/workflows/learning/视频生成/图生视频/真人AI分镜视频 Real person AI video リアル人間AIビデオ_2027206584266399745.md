---
key: 视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027206584266399745.json
name: 真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027206584266399745
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027206584266399745.json
hash: a3902cead9b827f4
coverage: 0.648148
learned_at: 2026-10-10 22:55:17
nodes: [GetNode, GetNode, KSamplerAdvanced, DiffusionModelLoaderKJ, LoraLoaderModelOnly, SetNode, DiffusionModelLoaderKJ, LoraLoaderModelOnly, SetNode, GetNode, GetNode, VAEDecode, LoraLoaderModelOnly, SetNode, SetNode, LayerUtility: PurgeVRAM V2, GetNode, KSamplerAdvanced, VAEEncode, GetNode, VAEEncode, PreviewImage, CLIPTextEncode, PrimitiveFloat, VHS_VideoCombine, JDCN_StringToList, Reroute, easy indexAnything, easy indexAnything, CLIPTextEncode, KSamplerAdvanced, WanImageToVideoSVIPro, CLIPTextEncode, WanImageToVideoSVIPro, KSamplerAdvanced, PreviewImage, VAEDecode, JWInteger, ImageBatchExtendWithOverlap, VHS_VideoCombine, VAELoader, CLIPLoader, LoadImage, Text, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, Loader, Loader, Loader, Loader, Loader, Loader, Loader, VHS_VideoCombine]
patterns: []
missing: [ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, easy indexAnything, easy indexAnything]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy indexAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy indexAnything` 知识库中没有该节点类型的任何知识]
---

# 视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027206584266399745.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027206584266399745.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
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
- `PreviewImage`
- `VAEDecode` ★核心
- `JWInteger`
- `ImageBatchExtendWithOverlap`
- `VHS_VideoCombine`
- `VAELoader`
- `CLIPLoader`
- `LoadImage`
- `Text`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Loader`
- `Loader`
- `Loader`
- `Loader`
- `Loader`
- `Loader`
- `Loader`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **65%**（35/54）

**有卡**：`KSamplerAdvanced`、`DiffusionModelLoaderKJ`、`LoraLoaderModelOnly`、`VAEDecode`、`VAEEncode`、`CLIPTextEncode`、`VHS_VideoCombine`、`JDCN_StringToList`、`WanImageToVideoSVIPro`、`JWInteger`、`ImageBatchExtendWithOverlap`、`VAELoader`、`CLIPLoader`、`LoadImage`、`Text`、`Loader`

**缺卡**（5）：`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`easy indexAnything`、`easy indexAnything`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy indexAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy indexAnything` 知识库中没有该节点类型的任何知识

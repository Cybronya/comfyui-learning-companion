---
key: 视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027227746778226690.json
name: 真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027227746778226690.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027227746778226690.json
hash: 6d82fe0ed958a859
coverage: 0.740741
learned_at: 2026-10-15 22:35:16
nodes: [GetNode, GetNode, KSamplerAdvanced, DiffusionModelLoaderKJ, LoraLoaderModelOnly, SetNode, DiffusionModelLoaderKJ, LoraLoaderModelOnly, SetNode, GetNode, GetNode, VAEDecode, LoraLoaderModelOnly, SetNode, SetNode, LayerUtility: PurgeVRAM V2, GetNode, KSamplerAdvanced, VAEEncode, GetNode, VAEEncode, PreviewImage, CLIPTextEncode, PrimitiveFloat, JDCN_StringToList, Reroute, easy indexAnything, easy indexAnything, CLIPTextEncode, KSamplerAdvanced, WanImageToVideoSVIPro, CLIPTextEncode, WanImageToVideoSVIPro, KSamplerAdvanced, PreviewImage, VAEDecode, JWInteger, ImageBatchExtendWithOverlap, VHS_VideoCombine, VAELoader, CLIPLoader, Text, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, Load3D, Load3D, Load3D, Load3D, Load3D, Load3D, Load3D, LoadImage, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027227746778226690.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2027227746778226690.json`

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
- `Text`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Load3D`
- `Load3D`
- `Load3D`
- `Load3D`
- `Load3D`
- `Load3D`
- `Load3D`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **74%**（40/54）

**有卡**：`KSamplerAdvanced`、`DiffusionModelLoaderKJ`、`LoraLoaderModelOnly`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`VAEEncode`、`CLIPTextEncode`、`JDCN_StringToList`、`easy indexAnything`、`WanImageToVideoSVIPro`、`JWInteger`、`ImageBatchExtendWithOverlap`、`VHS_VideoCombine`、`VAELoader`、`CLIPLoader`、`Text`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`Load3D`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode

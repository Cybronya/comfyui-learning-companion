---
key: 视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027266835749543937.json
name: 真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027266835749543937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027266835749543937.json
hash: ad8aa02b22838379
coverage: 0.745455
learned_at: 2026-10-15 22:43:06
nodes: [GetNode, GetNode, KSamplerAdvanced, DiffusionModelLoaderKJ, LoraLoaderModelOnly, SetNode, DiffusionModelLoaderKJ, LoraLoaderModelOnly, SetNode, GetNode, GetNode, VAEDecode, LoraLoaderModelOnly, SetNode, SetNode, LayerUtility: PurgeVRAM V2, GetNode, KSamplerAdvanced, VAEEncode, GetNode, VAEEncode, PreviewImage, PrimitiveFloat, VHS_VideoCombine, JDCN_StringToList, Reroute, easy indexAnything, easy indexAnything, CLIPTextEncode, KSamplerAdvanced, WanImageToVideoSVIPro, CLIPTextEncode, WanImageToVideoSVIPro, KSamplerAdvanced, PreviewImage, VAEDecode, JWInteger, ImageBatchExtendWithOverlap, VAELoader, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, load_GGUF, load_GGUF, load_GGUF, load_GGUF, load_GGUF, load_GGUF, load_GGUF, load_GGUF, VHS_VideoCombine, LoadImage, CLIPLoader, CLIPTextEncode, VHS_VideoCombine, Text]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027266835749543937.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027266835749543937.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
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
- `VAELoader`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `load_GGUF`
- `load_GGUF`
- `load_GGUF`
- `load_GGUF`
- `load_GGUF`
- `load_GGUF`
- `load_GGUF`
- `load_GGUF`
- `VHS_VideoCombine`
- `LoadImage`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `Text`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **75%**（41/55）

**有卡**：`KSamplerAdvanced`、`DiffusionModelLoaderKJ`、`LoraLoaderModelOnly`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`VAEEncode`、`VHS_VideoCombine`、`JDCN_StringToList`、`easy indexAnything`、`CLIPTextEncode`、`WanImageToVideoSVIPro`、`JWInteger`、`ImageBatchExtendWithOverlap`、`VAELoader`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`load_GGUF`、`LoadImage`、`CLIPLoader`、`Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、VAEEncode

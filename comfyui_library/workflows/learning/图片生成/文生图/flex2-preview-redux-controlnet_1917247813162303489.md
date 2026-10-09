---
key: 图片生成/文生图/flex2-preview-redux-controlnet_1917247813162303489.json
name: flex2-preview-redux-controlnet_1917247813162303489.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/flex2-preview-redux-controlnet_1917247813162303489.json
hash: 9b04bb4ae03c68a3
coverage: 0.78125
learned_at: 2026-10-07 22:07:56
nodes: [SetNode, EmptySD3LatentImage, VAEDecode, LayerUtility: PurgeVRAM, SetNode, SetNode, SetNode, DualCLIPLoader, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CFGZeroStar, UNETLoader, VAELoader, CLIPTextEncode, SetNode, GetImageSizeAndCount, CLIPVisionLoader, StyleModelApply, StyleModelLoader, Florence2Run, Florence2ModelLoader, CLIPVisionEncode, ImageScaleToTotalPixels, DepthAnythingPreprocessor, PreviewImage, ImageScaleToTotalPixels, ImageScaleToTotalPixels, Flex2Conditioner, SaveImage, LoadImage, LoadImage]
patterns: []
missing: [LayerUtility: PurgeVRAM]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "deis", "scheduler": "beta", "seed": 851662770584958, "steps": 25}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/flex2-preview-redux-controlnet_1917247813162303489.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1917247813162303489.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `SetNode`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `SetNode`
- `SetNode`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CFGZeroStar`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetImageSizeAndCount`
- `CLIPVisionLoader`
- `StyleModelApply`
- `StyleModelLoader`
- `Florence2Run`
- `Florence2ModelLoader`
- `CLIPVisionEncode`
- `ImageScaleToTotalPixels`
- `DepthAnythingPreprocessor`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `Flex2Conditioner`
- `SaveImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `851662770584958`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **78%**（25/32）

**有卡**：`EmptySD3LatentImage`、`VAEDecode`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`CFGZeroStar`、`UNETLoader`、`VAELoader`、`GetImageSizeAndCount`、`CLIPVisionLoader`、`StyleModelApply`、`StyleModelLoader`、`Florence2Run`、`Florence2ModelLoader`、`CLIPVisionEncode`、`ImageScaleToTotalPixels`、`DepthAnythingPreprocessor`、`Flex2Conditioner`、`SaveImage`、`LoadImage`

**缺卡**（1）：`LayerUtility: PurgeVRAM`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、DepthAnythingPreprocessor

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识

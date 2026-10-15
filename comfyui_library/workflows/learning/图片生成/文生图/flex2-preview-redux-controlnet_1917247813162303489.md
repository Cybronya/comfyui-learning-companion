---
key: 图片生成/文生图/flex2-preview-redux-controlnet_1917247813162303489.json
name: flex2-preview-redux-controlnet_1917247813162303489
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/flex2-preview-redux-controlnet_1917247813162303489.json
hash: 9b04bb4ae03c68a3
coverage: 0.78125
learned_at: 2026-10-10 20:59:18
nodes: [SetNode, EmptySD3LatentImage, VAEDecode, LayerUtility: PurgeVRAM, SetNode, SetNode, SetNode, DualCLIPLoader, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CFGZeroStar, UNETLoader, VAELoader, CLIPTextEncode, SetNode, GetImageSizeAndCount, CLIPVisionLoader, StyleModelApply, StyleModelLoader, Florence2Run, Florence2ModelLoader, CLIPVisionEncode, ImageScaleToTotalPixels, DepthAnythingPreprocessor, PreviewImage, ImageScaleToTotalPixels, ImageScaleToTotalPixels, Flex2Conditioner, SaveImage, LoadImage, LoadImage]
patterns: []
missing: [LayerUtility: PurgeVRAM]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "deis", "scheduler": "beta", "seed": 851662770584958, "steps": 25}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/flex2-preview-redux-controlnet_1917247813162303489.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/flex2-preview-redux-controlnet_1917247813162303489.json`

## 结构

**节点**（32 个）：
- `SetNode`
- `EmptySD3LatentImage`
- `VAEDecode`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `SetNode`
- `SetNode`
- `DualCLIPLoader`
- `LoraLoaderModelOnly`
- `KSampler`
- `CLIPTextEncode`
- `CFGZeroStar`
- `UNETLoader`
- `VAELoader`
- `CLIPTextEncode`
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

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `seed` = `851662770584958`
- `steps` = `25`

## 知识

覆盖率 **78%**（25/32）

**有卡**：`SetNode`、`EmptySD3LatentImage`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`CFGZeroStar`、`UNETLoader`、`VAELoader`、`GetImageSizeAndCount`、`CLIPVisionLoader`、`StyleModelApply`、`StyleModelLoader`、`Florence2Run`、`Florence2ModelLoader`、`CLIPVisionEncode`、`ImageScaleToTotalPixels`、`DepthAnythingPreprocessor`

**缺卡**（1）：`LayerUtility: PurgeVRAM`

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识

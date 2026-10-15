---
key: 图片生成/文生图/Flux最新Controlnet--Flex.2_1916356826265489409.json
name: Flux最新Controlnet--Flex.2_1916356826265489409
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux最新Controlnet--Flex.2_1916356826265489409.json
hash: 5645c3abd11d58eb
coverage: 0.636364
learned_at: 2026-10-10 20:58:38
nodes: [ShowText|pysssss, LayerUtility: TextJoin, DualCLIPLoader, VAELoader, SaveImage, VAEDecode, Note, GetNode, PreviewImage, PreviewImage, Image Comparer (rgthree), UNETLoader, SetNode, LoadImage, ImageScaleToTotalPixels, DWPreprocessor, RH_Captioner, Flex2Conditioner, KSampler, Flex2Conditioner, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, ImageScaleToTotalPixels, ImageScaleToTotalPixels, DownloadAndLoadDepthAnythingV2Model, PreviewImage, DepthAnything_V2, EmptyLatentImage, LoraLoaderModelOnly, CR Text, Note, Note]
patterns: [text_to_image]
missing: [CR Text, LayerUtility: TextJoin]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 982041649879483, "steps": 20, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Flux最新Controlnet--Flex.2_1916356826265489409.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux最新Controlnet--Flex.2_1916356826265489409.json`

## 结构

**节点**（33 个）：
- `ShowText|pysssss`
- `LayerUtility: TextJoin`
- `DualCLIPLoader`
- `VAELoader`
- `SaveImage`
- `VAEDecode`
- `Note`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `UNETLoader`
- `SetNode`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `DWPreprocessor`
- `RH_Captioner`
- `Flex2Conditioner`
- `KSampler`
- `Flex2Conditioner`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `LoraLoaderModelOnly`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `DownloadAndLoadDepthAnythingV2Model`
- `PreviewImage`
- `DepthAnything_V2`
- `EmptyLatentImage`
- `LoraLoaderModelOnly`
- `CR Text`
- `Note`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1536`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `982041649879483`
- `steps` = `20`
- `width` = `1024`

## 知识

覆盖率 **64%**（21/33）

**有卡**：`ShowText|pysssss`、`LayerUtility: TextJoin`、`DualCLIPLoader`、`VAELoader`、`SaveImage`、`VAEDecode`、`Note`、`GetNode`、`PreviewImage`、`Image Comparer (rgthree)`、`UNETLoader`、`SetNode`、`LoadImage`、`ImageScaleToTotalPixels`、`DWPreprocessor`、`RH_Captioner`、`Flex2Conditioner`、`KSampler`、`CLIPTextEncode`

**缺卡**（2）：`CR Text`、`LayerUtility: TextJoin`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识

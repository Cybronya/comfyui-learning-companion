---
key: 图片生成/文生图/Flux最新cn-Flex.2-depth+openpose_1916072736811323393.json
name: Flux最新cn-Flex.2-depth+openpose_1916072736811323393
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux最新cn-Flex.2-depth+openpose_1916072736811323393.json
hash: 035c3fa4da117d77
coverage: 0.625
learned_at: 2026-10-10 20:58:38
nodes: [ShowText|pysssss, LayerUtility: TextJoin, DualCLIPLoader, VAELoader, SaveImage, VAEDecode, Note, GetNode, PreviewImage, PreviewImage, PreviewImage, Image Comparer (rgthree), UNETLoader, SetNode, LoadImage, ImageScaleToTotalPixels, DWPreprocessor, RH_Captioner, Flex2Conditioner, KSampler, Flex2Conditioner, CR Text, Note, ImageScaleToTotalPixels, ImageScaleToTotalPixels, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, EmptyLatentImage, LoraLoaderModelOnly, DepthAnythingPreprocessor, Note]
patterns: [text_to_image]
missing: [CR Text, LayerUtility: TextJoin]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 664125298103807, "steps": 20, "width": 768}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Flux最新cn-Flex.2-depth+openpose_1916072736811323393.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux最新cn-Flex.2-depth+openpose_1916072736811323393.json`

## 结构

**节点**（32 个）：
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
- `CR Text`
- `Note`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `LoraLoaderModelOnly`
- `EmptyLatentImage`
- `LoraLoaderModelOnly`
- `DepthAnythingPreprocessor`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1280`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `664125298103807`
- `steps` = `20`
- `width` = `768`

## 知识

覆盖率 **62%**（20/32）

**有卡**：`ShowText|pysssss`、`LayerUtility: TextJoin`、`DualCLIPLoader`、`VAELoader`、`SaveImage`、`VAEDecode`、`Note`、`GetNode`、`PreviewImage`、`Image Comparer (rgthree)`、`UNETLoader`、`SetNode`、`LoadImage`、`ImageScaleToTotalPixels`、`DWPreprocessor`、`RH_Captioner`、`Flex2Conditioner`、`KSampler`

**缺卡**（2）：`CR Text`、`LayerUtility: TextJoin`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识

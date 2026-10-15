---
key: 图片生成/文生图/Flux最新cn-Flex.2-depth+openpose_1916072736811323393.json
name: Flux最新cn-Flex.2-depth+openpose_1916072736811323393
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux最新cn-Flex.2-depth+openpose_1916072736811323393.json
hash: 035c3fa4da117d77
coverage: 0.6875
learned_at: 2026-10-15 22:26:29
nodes: [ShowText|pysssss, LayerUtility: TextJoin, DualCLIPLoader, VAELoader, SaveImage, VAEDecode, Note, GetNode, PreviewImage, PreviewImage, PreviewImage, Image Comparer (rgthree), UNETLoader, SetNode, LoadImage, ImageScaleToTotalPixels, DWPreprocessor, RH_Captioner, Flex2Conditioner, KSampler, Flex2Conditioner, CR Text, Note, ImageScaleToTotalPixels, ImageScaleToTotalPixels, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, EmptyLatentImage, LoraLoaderModelOnly, DepthAnythingPreprocessor, Note]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 664125298103807, "steps": 20, "width": 768}
---

# 图片生成/文生图/Flux最新cn-Flex.2-depth+openpose_1916072736811323393.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux最新cn-Flex.2-depth+openpose_1916072736811323393.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `ShowText|pysssss`
- `LayerUtility: TextJoin`
- `DualCLIPLoader`
- `VAELoader`
- `SaveImage`
- `VAEDecode` ★核心
- `Note`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `SetNode`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `DWPreprocessor`
- `RH_Captioner`
- `Flex2Conditioner`
- `KSampler` ★核心
- `Flex2Conditioner`
- `CR Text`
- `Note`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `DepthAnythingPreprocessor`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `664125298103807`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `768`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **69%**（22/32）

**有卡**：`LayerUtility: TextJoin`、`DualCLIPLoader`、`VAELoader`、`SaveImage`、`VAEDecode`、`UNETLoader`、`LoadImage`、`ImageScaleToTotalPixels`、`DWPreprocessor`、`RH_Captioner`、`Flex2Conditioner`、`KSampler`、`CR Text`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`DepthAnythingPreprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、EmptyLatentImage、LoadImage、UNETLoader

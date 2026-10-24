---
key: 图片生成/图生图/​​Flex.2文生图+局部重绘+CN控制_1917180206874820610.json
name: ​​Flex.2文生图+局部重绘+CN控制_1917180206874820610
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/​​Flex.2文生图+局部重绘+CN控制_1917180206874820610.json
hash: fc26eb30072a1ef6
coverage: 0.913043
learned_at: 2026-10-23 11:47:15
nodes: [DeepTranslatorTextNode, UNETLoader, AIO_Preprocessor, ImageScaleToTotalPixels, PreviewImage, DualCLIPLoader, MaskToImage, GroundingDinoSAM2Segment (segment anything2), GroundingDinoModelLoader (segment anything2), ImageScaleToTotalPixels, SAM2ModelLoader (segment anything2), CLIPTextEncode, CLIPTextEncode, PreviewImage, LoraLoaderModelOnly, Flex2Conditioner, KSampler, VAEDecode, SaveImage, VAELoader, EmptyLatentImage, GrowMaskWithBlur, LoadImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": 1, "height": 1176, "sampler_name": "deis", "scheduler": "beta", "seed": 209552004960178, "steps": 28, "width": 768}
---

# 图片生成/图生图/​​Flex.2文生图+局部重绘+CN控制_1917180206874820610.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/​​Flex.2文生图+局部重绘+CN控制_1917180206874820610.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `DeepTranslatorTextNode`
- `UNETLoader` ★核心
- `AIO_Preprocessor`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `DualCLIPLoader`
- `MaskToImage`
- `GroundingDinoSAM2Segment (segment anything2)`
- `GroundingDinoModelLoader (segment anything2)`
- `ImageScaleToTotalPixels`
- `SAM2ModelLoader (segment anything2)`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `Flex2Conditioner`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `GrowMaskWithBlur`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `209552004960178`
- `steps` = `28`
- `cfg` = `8`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `768`
- `height` = `1176`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`DeepTranslatorTextNode`、`UNETLoader`、`AIO_Preprocessor`、`ImageScaleToTotalPixels`、`DualCLIPLoader`、`MaskToImage`、`GroundingDinoSAM2Segment (segment anything2)`、`GroundingDinoModelLoader (segment anything2)`、`SAM2ModelLoader (segment anything2)`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`Flex2Conditioner`、`KSampler`、`VAEDecode`、`SaveImage`、`VAELoader`、`EmptyLatentImage`、`GrowMaskWithBlur`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、EmptyLatentImage、LoadImage、UNETLoader

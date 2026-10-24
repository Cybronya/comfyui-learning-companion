---
key: 图片生成/图生图/Flex.2+Redux512_模仿生图_提示词重绘_1913045125293928450.json
name: Flex.2+Redux512_模仿生图_提示词重绘_1913045125293928450
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flex.2+Redux512_模仿生图_提示词重绘_1913045125293928450.json
hash: f5b7454d58629d32
coverage: 0.933333
learned_at: 2026-10-23 10:56:02
nodes: [CLIPVisionLoader, SaveImage, ConditioningZeroOut, StyleModelLoader, CLIPVisionEncode, VAELoader, DualCLIPLoader, EmptyLatentImage, Florence2ModelLoader, CLIPTextEncode, VAEDecode, KSampler, StyleModelApply, CFGZeroStarAndInit, UNETLoader, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, Florence2Run, SaveImage, LoraLoaderModelOnly, EmptyLatentImage, GetImageSize, Image Comparer (rgthree), PreviewImage, ImageScaleToTotalPixels, DepthAnythingPreprocessor, ImageScaleToTotalPixels, DualCLIPLoader, UNETLoader, KSampler, Flex2Conditioner, CFGZeroStarAndInit, CLIPTextEncode, ConditioningZeroOut, VAEDecode, VAELoader, VAEDecode, UNETLoader, LayerMask: MaskStroke, InpaintModelConditioning, KSampler, LoadImage, LoadImage, LoraLoaderModelOnly, Flex2Conditioner]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.30000000000000004, "height": 1120, "sampler_name": "euler", "scheduler": "normal", "seed": 412149478179797, "steps": 20, "width": 840}
---

# 图片生成/图生图/Flex.2+Redux512_模仿生图_提示词重绘_1913045125293928450.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flex.2+Redux512_模仿生图_提示词重绘_1913045125293928450.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `CLIPVisionLoader`
- `SaveImage`
- `ConditioningZeroOut`
- `StyleModelLoader`
- `CLIPVisionEncode`
- `VAELoader`
- `DualCLIPLoader`
- `EmptyLatentImage` ★核心
- `Florence2ModelLoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `StyleModelApply`
- `CFGZeroStarAndInit`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Florence2Run`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `GetImageSize`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `DepthAnythingPreprocessor`
- `ImageScaleToTotalPixels`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `Flex2Conditioner`
- `CFGZeroStarAndInit`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LayerMask: MaskStroke`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `Flex2Conditioner`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `840`
- `height` = `1120`
- `batch_size` = `1`
- `seed` = `412149478179797`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **93%**（42/45）

**有卡**：`CLIPVisionLoader`、`SaveImage`、`ConditioningZeroOut`、`StyleModelLoader`、`CLIPVisionEncode`、`VAELoader`、`DualCLIPLoader`、`EmptyLatentImage`、`Florence2ModelLoader`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`StyleModelApply`、`CFGZeroStarAndInit`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`Florence2Run`、`LoraLoaderModelOnly`、`GetImageSize`、`ImageScaleToTotalPixels`、`DepthAnythingPreprocessor`、`Flex2Conditioner`、`LayerMask: MaskStroke`、`InpaintModelConditioning`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage

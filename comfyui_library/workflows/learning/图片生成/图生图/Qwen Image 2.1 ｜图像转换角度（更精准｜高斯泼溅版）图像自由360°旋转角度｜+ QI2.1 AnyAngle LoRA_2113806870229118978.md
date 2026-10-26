---
key: 图片生成/图生图/Qwen Image 2.1 ｜图像转换角度（更精准｜高斯泼溅版）图像自由360°旋转角度｜+ QI2.1 AnyAngle LoRA_2113806870229118978.json
name: Qwen Image 2.1 ｜图像转换角度（更精准｜高斯泼溅版）图像自由360°旋转角度｜+ QI2.1 AnyAngle LoRA_2113806870229118978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 ｜图像转换角度（更精准｜高斯泼溅版）图像自由360°旋转角度｜+ QI2.1 AnyAngle LoRA_2113806870229118978.json
hash: 50732f6e608258a5
coverage: 0.628571
learned_at: 2026-10-26 22:02:59
nodes: [LoadSharpModel, SharpPredict, Note, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize, Note, Note, Note, ShowText|pysssss, LoadImage, Note, CLIPLoader, MarkdownNote, Note, UNETLoader, Note, Note, Note, LoadImage, INTConstant, LoadImage, LoraLoaderModelOnly, Image Comparer (rgthree), SaveImage, MarkdownNote, QwenImage21Cache, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, EmptyLatentImage, KSampler, TextEncodeQwenImage21, YCGaussianPreview, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 30, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 ｜图像转换角度（更精准｜高斯泼溅版）图像自由360°旋转角度｜+ QI2.1 AnyAngle LoRA_2113806870229118978.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 ｜图像转换角度（更精准｜高斯泼溅版）图像自由360°旋转角度｜+ QI2.1 AnyAngle LoRA_2113806870229118978.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `LoadSharpModel`
- `SharpPredict`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSize`
- `Note`
- `Note`
- `Note`
- `ShowText|pysssss`
- `LoadImage`
- `Note`
- `CLIPLoader`
- `MarkdownNote`
- `Note`
- `UNETLoader` ★核心
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `INTConstant`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `MarkdownNote`
- `QwenImage21Cache`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `YCGaussianPreview`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `42`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **63%**（22/35）

**有卡**：`LoadSharpModel`、`SharpPredict`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSize`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`INTConstant`、`LoraLoaderModelOnly`、`SaveImage`、`QwenImage21Cache`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImage21`、`YCGaussianPreview`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage

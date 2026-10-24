---
key: 图片生成/图生图/Z-Image Fun-ControlNet-Union 2.0 深度、姿态、条线，精准控制_1996476841798025217.json
name: Z-Image Fun-ControlNet-Union 2.0 深度、姿态、条线，精准控制_1996476841798025217
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-Image Fun-ControlNet-Union 2.0 深度、姿态、条线，精准控制_1996476841798025217.json
hash: 1b068543d80cf91c
coverage: 0.788462
learned_at: 2026-10-23 11:29:20
nodes: [CLIPTextEncode, SaveImage, AIO_Preprocessor, SaveImage, RH_Captioner, MaraScottIsEmptyOrNone_v1, easy showAnything, easy ifElse, ttN concat, CLIPLoader, VAELoader, ConditioningZeroOut, EmptyLatentImage, Text Multiline, AIO_Preprocessor, AIO_Preprocessor, PreviewImage, AIO_Preprocessor, ImageConcatMulti, AIO_Preprocessor, GetImageSizeAndCount, GetImageSizeAndCount, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, PreviewImage, SaveImage, ModelPatchLoader, VAEDecode, ImageConcatMulti, easy imageConcat, LayerUtility: ImageScaleByAspectRatio V2, ModelPatchLoader, PreviewImage, QwenImageDiffsynthControlnet, PreviewImage, KSampler, VAEDecode, SaveImage, ImageConcatMulti, UNETLoader, Reroute, KSampler, PreviewImage, easy imageConcat, easy imageConcat, easy imageConcat, PreviewImage, PreviewImage, ImpactSwitch, LoadImage, QwenImageDiffsynthControlnet]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 102757971275961, "steps": 10, "width": 1024}
---

# 图片生成/图生图/Z-Image Fun-ControlNet-Union 2.0 深度、姿态、条线，精准控制_1996476841798025217.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-Image Fun-ControlNet-Union 2.0 深度、姿态、条线，精准控制_1996476841798025217.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `CLIPTextEncode` ★核心
- `SaveImage`
- `AIO_Preprocessor`
- `SaveImage`
- `RH_Captioner`
- `MaraScottIsEmptyOrNone_v1`
- `easy showAnything`
- `easy ifElse`
- `ttN concat`
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `Text Multiline`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `PreviewImage`
- `AIO_Preprocessor`
- `ImageConcatMulti`
- `AIO_Preprocessor`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `SaveImage`
- `ModelPatchLoader`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `easy imageConcat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelPatchLoader`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `PreviewImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ImageConcatMulti`
- `UNETLoader` ★核心
- `Reroute`
- `KSampler` ★核心
- `PreviewImage`
- `easy imageConcat`
- `easy imageConcat`
- `easy imageConcat`
- `PreviewImage`
- `PreviewImage`
- `ImpactSwitch`
- `LoadImage`
- `QwenImageDiffsynthControlnet`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `102757971275961`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（41/52）

**有卡**：`CLIPTextEncode`、`SaveImage`、`AIO_Preprocessor`、`RH_Captioner`、`MaraScottIsEmptyOrNone_v1`、`ttN concat`、`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`EmptyLatentImage`、`Text Multiline`、`ImageConcatMulti`、`GetImageSizeAndCount`、`ModelPatchLoader`、`VAEDecode`、`easy imageConcat`、`LayerUtility: ImageScaleByAspectRatio V2`、`QwenImageDiffsynthControlnet`、`KSampler`、`UNETLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

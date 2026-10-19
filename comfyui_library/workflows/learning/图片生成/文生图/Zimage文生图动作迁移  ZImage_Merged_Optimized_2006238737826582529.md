---
key: 图片生成/文生图/Zimage文生图动作迁移  ZImage_Merged_Optimized_2006238737826582529.json
name: Zimage文生图动作迁移  ZImage_Merged_Optimized_2006238737826582529
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Zimage文生图动作迁移  ZImage_Merged_Optimized_2006238737826582529.json
hash: faaafbc9fe5123d5
coverage: 0.680851
learned_at: 2026-10-19 22:01:07
nodes: [GetNode, GoogleTranslateTextNode, SaveImage, LoadImage, Image Comparer (rgthree), SetNode, SetNode, RH_Captioner, CR Text, ShowText|pysssss, ShowText|pysssss, GetNode, Note, Note, easy showAnything, Note, PMRF, ConditioningZeroOut, QwenImageDiffsynthControlnet, KSampler, KSampler, CLIPLoader, VAELoader, EmptyLatentImage, ModelPatchLoader, ImageConcanate, UNETLoader, AIO_Preprocessor, ImageScaleToTotalPixels, LoraLoaderModelOnly, CLIPTextEncode, GetImageSize, PreviewImage, UpscaleModelLoader, Fast Groups Bypasser (rgthree), SaveImage, SaveImage, GetNode, SaveImage, Fast Groups Bypasser (rgthree), CR Text, PreviewBridge, easy imageSplitGrid, VAEDecode, ImageUpscaleWithModel, LoadImage, LoadImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.75, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 347947011947302, "steps": 10, "width": 1024}
---

# 图片生成/文生图/Zimage文生图动作迁移  ZImage_Merged_Optimized_2006238737826582529.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Zimage文生图动作迁移  ZImage_Merged_Optimized_2006238737826582529.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `GetNode`
- `GoogleTranslateTextNode`
- `SaveImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SetNode`
- `SetNode`
- `RH_Captioner`
- `CR Text`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `GetNode`
- `Note`
- `Note`
- `easy showAnything`
- `Note`
- `PMRF`
- `ConditioningZeroOut`
- `QwenImageDiffsynthControlnet`
- `KSampler` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ModelPatchLoader`
- `ImageConcanate`
- `UNETLoader` ★核心
- `AIO_Preprocessor`
- `ImageScaleToTotalPixels`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `PreviewImage`
- `UpscaleModelLoader`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `SaveImage`
- `GetNode`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`
- `PreviewBridge`
- `easy imageSplitGrid`
- `VAEDecode` ★核心
- `ImageUpscaleWithModel`
- `LoadImage`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `347947011947302`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.75`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **68%**（32/47）

**有卡**：`GoogleTranslateTextNode`、`SaveImage`、`LoadImage`、`RH_Captioner`、`CR Text`、`PMRF`、`ConditioningZeroOut`、`QwenImageDiffsynthControlnet`、`KSampler`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`ModelPatchLoader`、`ImageConcanate`、`UNETLoader`、`AIO_Preprocessor`、`ImageScaleToTotalPixels`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`GetImageSize`、`UpscaleModelLoader`、`PreviewBridge`、`easy imageSplitGrid`、`VAEDecode`、`ImageUpscaleWithModel`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

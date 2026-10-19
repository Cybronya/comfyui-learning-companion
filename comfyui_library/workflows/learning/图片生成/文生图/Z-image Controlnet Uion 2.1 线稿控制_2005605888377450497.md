---
key: 图片生成/文生图/Z-image Controlnet Uion 2.1 线稿控制_2005605888377450497.json
name: Z-image Controlnet Uion 2.1 线稿控制_2005605888377450497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image Controlnet Uion 2.1 线稿控制_2005605888377450497.json
hash: 6081073ff1521e0f
coverage: 0.875
learned_at: 2026-10-19 22:01:03
nodes: [KSampler (Efficient), LoadImage, AILab_QwenVL, UNETLoader, LoraLoaderModelOnly, CLIPLoader, ConditioningZeroOut, PreviewAny, QwenImageDiffsynthControlnet, ttN concat, CLIPTextEncode, ImageScaleToTotalPixels, GetImageSize, EmptyLatentImage, VAEDecode, UpscaleModelLoader, ImageUpscaleWithModel, Image Comparer (rgthree), SaveImage, LoadImage, PreviewImage, VAELoader, AIO_Preprocessor, ModelPatchLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 2, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 100, "steps": 8, "width": 1024}
---

# 图片生成/文生图/Z-image Controlnet Uion 2.1 线稿控制_2005605888377450497.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image Controlnet Uion 2.1 线稿控制_2005605888377450497.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `KSampler (Efficient)` ★核心
- `LoadImage`
- `AILab_QwenVL`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `ConditioningZeroOut`
- `PreviewAny`
- `QwenImageDiffsynthControlnet`
- `ttN concat`
- `CLIPTextEncode` ★核心
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`
- `PreviewImage`
- `VAELoader`
- `AIO_Preprocessor`
- `ModelPatchLoader`

## 关键参数

- `seed` = `100`
- `steps` = `8`
- `cfg` = `2`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`KSampler (Efficient)`、`LoadImage`、`AILab_QwenVL`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`ConditioningZeroOut`、`QwenImageDiffsynthControlnet`、`ttN concat`、`CLIPTextEncode`、`ImageScaleToTotalPixels`、`GetImageSize`、`EmptyLatentImage`、`VAEDecode`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`SaveImage`、`VAELoader`、`AIO_Preprocessor`、`ModelPatchLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

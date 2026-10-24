---
key: 图片生成/图生图/Z-image Controlnet Uion 2.1优化高级采样_2010904466274390017.json
name: Z-image Controlnet Uion 2.1优化高级采样_2010904466274390017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image Controlnet Uion 2.1优化高级采样_2010904466274390017.json
hash: 7f29dc775c381376
coverage: 0.9
learned_at: 2026-10-23 11:30:15
nodes: [CLIPLoader, VAELoader, AILab_QwenVL, GetImageSize, ConditioningZeroOut, CLIPTextEncode, ModelPatchLoader, EmptyLatentImage, PreviewImage, UpscaleModelLoader, ImageUpscaleWithModel, ImageScaleBy, SaveImage, Image Comparer (rgthree), AIO_Preprocessor, ImageScaleToTotalPixels, PreviewImage, VAEDecode, ttN concat, Display Any (rgthree), LoadImage, LoadImage, QwenImageDiffsynthControlnet, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, UNETLoader, Int, Int, ImageConcanate]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 10, "denoise": "simple", "height": 1536, "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "increment", "width": 1024}
---

# 图片生成/图生图/Z-image Controlnet Uion 2.1优化高级采样_2010904466274390017.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image Controlnet Uion 2.1优化高级采样_2010904466274390017.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CLIPLoader`
- `VAELoader`
- `AILab_QwenVL`
- `GetImageSize`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `ModelPatchLoader`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `SaveImage`
- `Image Comparer (rgthree)`
- `AIO_Preprocessor`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `VAEDecode` ★核心
- `ttN concat`
- `Display Any (rgthree)`
- `LoadImage`
- `LoadImage`
- `QwenImageDiffsynthControlnet`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Int`
- `Int`
- `ImageConcanate`

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `disable`
- `steps` = `increment`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（27/30）

**有卡**：`CLIPLoader`、`VAELoader`、`AILab_QwenVL`、`GetImageSize`、`ConditioningZeroOut`、`CLIPTextEncode`、`ModelPatchLoader`、`EmptyLatentImage`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScaleBy`、`SaveImage`、`AIO_Preprocessor`、`ImageScaleToTotalPixels`、`VAEDecode`、`ttN concat`、`Display Any (rgthree)`、`LoadImage`、`QwenImageDiffsynthControlnet`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`UNETLoader`、`Int`、`ImageConcanate`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

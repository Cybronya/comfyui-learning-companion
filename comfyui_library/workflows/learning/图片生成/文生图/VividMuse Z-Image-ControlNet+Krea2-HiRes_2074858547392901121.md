---
key: 图片生成/文生图/VividMuse Z-Image-ControlNet+Krea2-HiRes_2074858547392901121.json
name: VividMuse Z-Image-ControlNet+Krea2-HiRes_2074858547392901121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/VividMuse Z-Image-ControlNet+Krea2-HiRes_2074858547392901121.json
hash: e6b9e835c1904fee
coverage: 0.833333
learned_at: 2026-10-20 00:20:10
nodes: [ResolutionSelector, VAEDecode, KSamplerAdvanced, VAELoader, CLIPLoader, ConditioningZeroOut, CLIPTextEncode, ModelPatchLoader, QwenImageDiffsynthControlnet, KSamplerAdvanced, KSamplerAdvanced, SaveImage, ImageResize+, EmptyLatentImage, easy imageRemBg, VAEDecode, PreviewImage, AIO_Preprocessor, PreviewImage, VAEDecodeTiled, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UpscaleModelLoader, Fast Groups Bypasser (rgthree), ImageUpscaleWithModel, ImageUpscaleWithModel, ConditioningZeroOut, CLIPTextEncode, VAELoader, VAEEncodeTiled, CLIPLoader, PreviewImage, PreviewImage, ImageScaleToTotalPixels, LoraLoaderModelOnly, easy promptList, UpscaleModelLoader, KSamplerAdvanced, Seed (rgthree), UNETLoader, SaveImage, UNETLoader, LoadImage, VAEDecode, easy imageColorMatch, Image Comparer (rgthree), easy promptList, easy promptList, PrimitiveStringMultiline, easy promptList, PrimitiveStringMultiline, Image Comparer (rgthree), easy cleanGpuUsed]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": "kl_optimal", "height": 512, "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed", "width": 512}
---

# 图片生成/文生图/VividMuse Z-Image-ControlNet+Krea2-HiRes_2074858547392901121.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/VividMuse Z-Image-ControlNet+Krea2-HiRes_2074858547392901121.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `ResolutionSelector`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `CLIPLoader`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `ModelPatchLoader`
- `QwenImageDiffsynthControlnet`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SaveImage`
- `ImageResize+`
- `EmptyLatentImage` ★核心
- `easy imageRemBg`
- `VAEDecode` ★核心
- `PreviewImage`
- `AIO_Preprocessor`
- `PreviewImage`
- `VAEDecodeTiled` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UpscaleModelLoader`
- `Fast Groups Bypasser (rgthree)`
- `ImageUpscaleWithModel`
- `ImageUpscaleWithModel`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEEncodeTiled` ★核心
- `CLIPLoader`
- `PreviewImage`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `LoraLoaderModelOnly` ★核心
- `easy promptList`
- `UpscaleModelLoader`
- `KSamplerAdvanced` ★核心
- `Seed (rgthree)`
- `UNETLoader` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `easy imageColorMatch`
- `Image Comparer (rgthree)`
- `easy promptList`
- `easy promptList`
- `PrimitiveStringMultiline`
- `easy promptList`
- `PrimitiveStringMultiline`
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `kl_optimal`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（45/54）

**有卡**：`ResolutionSelector`、`VAEDecode`、`KSamplerAdvanced`、`VAELoader`、`CLIPLoader`、`ConditioningZeroOut`、`CLIPTextEncode`、`ModelPatchLoader`、`QwenImageDiffsynthControlnet`、`SaveImage`、`ImageResize+`、`EmptyLatentImage`、`easy imageRemBg`、`AIO_Preprocessor`、`VAEDecodeTiled`、`LoraLoaderModelOnly`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`VAEEncodeTiled`、`ImageScaleToTotalPixels`、`easy promptList`、`Seed (rgthree)`、`UNETLoader`、`LoadImage`、`easy imageColorMatch`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、ResolutionSelector

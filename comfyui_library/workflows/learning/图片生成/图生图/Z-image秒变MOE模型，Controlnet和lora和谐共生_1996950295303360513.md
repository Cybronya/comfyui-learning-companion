---
key: 图片生成/图生图/Z-image秒变MOE模型，Controlnet和lora和谐共生_1996950295303360513.json
name: Z-image秒变MOE模型，Controlnet和lora和谐共生_1996950295303360513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image秒变MOE模型，Controlnet和lora和谐共生_1996950295303360513.json
hash: c00df845191f0d75
coverage: 0.96
learned_at: 2026-10-23 11:31:51
nodes: [GetImageSize, VAEDecode, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, INTConstant, Seed (rgthree), QwenImageDiffsynthControlnet, ImageScaleToTotalPixels, PreviewImage, VAELoader, KSamplerAdvanced, INTConstant, KSamplerAdvanced, AIO_Preprocessor, ModelPatchLoader, UNETLoader, CLIPLoader, LoraLoaderModelOnly, ImageConcanate, SaveImage, SaveImage, UpscaleModelLoader, ImageUpscaleWithModel, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 10, "denoise": "simple", "height": 1536, "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize", "width": 1024}
---

# 图片生成/图生图/Z-image秒变MOE模型，Controlnet和lora和谐共生_1996950295303360513.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image秒变MOE模型，Controlnet和lora和谐共生_1996950295303360513.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `GetImageSize`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `INTConstant`
- `Seed (rgthree)`
- `QwenImageDiffsynthControlnet`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `KSamplerAdvanced` ★核心
- `AIO_Preprocessor`
- `ModelPatchLoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ImageConcanate`
- `SaveImage`
- `SaveImage`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`GetImageSize`、`VAEDecode`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyLatentImage`、`INTConstant`、`Seed (rgthree)`、`QwenImageDiffsynthControlnet`、`ImageScaleToTotalPixels`、`VAELoader`、`KSamplerAdvanced`、`AIO_Preprocessor`、`ModelPatchLoader`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`ImageConcanate`、`SaveImage`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

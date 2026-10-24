---
key: 图片生成/图生图/Z-IMAGE终极版自动洗图流+CN2.1+高清放大_2003476127446409218.json
name: Z-IMAGE终极版自动洗图流+CN2.1+高清放大_2003476127446409218
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-IMAGE终极版自动洗图流+CN2.1+高清放大_2003476127446409218.json
hash: 1f6b15d880937ed8
coverage: 0.896552
learned_at: 2026-10-23 11:29:12
nodes: [VAEDecode, PreviewImage, EmptyLatentImage, CLIPTextEncode, ConditioningZeroOut, ModelSamplingAuraFlow, Qwen3_VQA, ShowText|pysssss, AIO_Preprocessor, LayerUtility: ImageReel, PreviewImage, LayerUtility: ImageReelComposit, ImageScaleToTotalPixels, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, ImageResizeKJv2, HFEPostProcessor (lrzjason), QwenImageDiffsynthControlnet, ModelPatchLoader, LoadImage, UNETLoader, CLIPLoader, Int, Int, ImageResizeKJv2, KSampler, VAELoader, SaveImage, SeedVR2LoadVAEModel]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 736413688555592, "steps": 8, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-IMAGE终极版自动洗图流+CN2.1+高清放大_2003476127446409218.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-IMAGE终极版自动洗图流+CN2.1+高清放大_2003476127446409218.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `VAEDecode` ★核心
- `PreviewImage`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `Qwen3_VQA`
- `ShowText|pysssss`
- `AIO_Preprocessor`
- `LayerUtility: ImageReel`
- `PreviewImage`
- `LayerUtility: ImageReelComposit`
- `ImageScaleToTotalPixels`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `ImageResizeKJv2`
- `HFEPostProcessor (lrzjason)`
- `QwenImageDiffsynthControlnet`
- `ModelPatchLoader`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Int`
- `Int`
- `ImageResizeKJv2`
- `KSampler` ★核心
- `VAELoader`
- `SaveImage`
- `SeedVR2LoadVAEModel`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `736413688555592`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`VAEDecode`、`EmptyLatentImage`、`CLIPTextEncode`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`Qwen3_VQA`、`AIO_Preprocessor`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`ImageScaleToTotalPixels`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`ImageResizeKJv2`、`HFEPostProcessor (lrzjason)`、`QwenImageDiffsynthControlnet`、`ModelPatchLoader`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`Int`、`KSampler`、`VAELoader`、`SaveImage`、`SeedVR2LoadVAEModel`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

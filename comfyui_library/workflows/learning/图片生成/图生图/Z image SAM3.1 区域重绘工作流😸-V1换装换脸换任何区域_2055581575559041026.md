---
key: 图片生成/图生图/Z image SAM3.1 区域重绘工作流😸-V1换装换脸换任何区域_2055581575559041026.json
name: Z image SAM3.1 区域重绘工作流😸-V1换装换脸换任何区域_2055581575559041026
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z image SAM3.1 区域重绘工作流😸-V1换装换脸换任何区域_2055581575559041026.json
hash: c650f6f3288dce96
coverage: 0.827586
learned_at: 2026-10-23 11:28:59
nodes: [ModelSamplingAuraFlow, GenerateNoise, LGNoiseInjectionLatent, KSampler, ConditioningZeroOut, EmptyLatentImage, LoadImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, easy sam3ImageSegmentation, CR Seed, ZImageFunControlnet, LoraLoaderModelOnly, CLIPLoader, Image Comparer (rgthree), MarkdownNote, MarkdownNote, MaskPreview, Label (rgthree), Label (rgthree), ModelPatchLoader, VAELoader, UNETLoader, VAEDecode, SaveImage, easy sam3ModelLoader, PreviewImage, CLIPTextEncode, easy framesEditor]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "dpmpp_2s_ancestral", "scheduler": "bong_tangent", "seed": 398516390282088, "steps": 10, "width": 1024}
---

# 图片生成/图生图/Z image SAM3.1 区域重绘工作流😸-V1换装换脸换任何区域_2055581575559041026.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z image SAM3.1 区域重绘工作流😸-V1换装换脸换任何区域_2055581575559041026.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `ModelSamplingAuraFlow`
- `GenerateNoise`
- `LGNoiseInjectionLatent`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy sam3ImageSegmentation`
- `CR Seed`
- `ZImageFunControlnet`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `MarkdownNote`
- `MarkdownNote`
- `MaskPreview`
- `Label (rgthree)`
- `Label (rgthree)`
- `ModelPatchLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `easy sam3ModelLoader`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `easy framesEditor`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `398516390282088`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2s_ancestral`
- `scheduler` = `bong_tangent`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（24/29）

**有卡**：`ModelSamplingAuraFlow`、`GenerateNoise`、`LGNoiseInjectionLatent`、`KSampler`、`ConditioningZeroOut`、`EmptyLatentImage`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy sam3ImageSegmentation`、`CR Seed`、`ZImageFunControlnet`、`LoraLoaderModelOnly`、`CLIPLoader`、`MaskPreview`、`Label (rgthree)`、`ModelPatchLoader`、`VAELoader`、`UNETLoader`、`VAEDecode`、`SaveImage`、`easy sam3ModelLoader`、`CLIPTextEncode`、`easy framesEditor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

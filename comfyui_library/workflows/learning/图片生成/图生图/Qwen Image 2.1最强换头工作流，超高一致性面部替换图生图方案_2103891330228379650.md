---
key: 图片生成/图生图/Qwen Image 2.1最强换头工作流，超高一致性面部替换图生图方案_2103891330228379650.json
name: Qwen Image 2.1最强换头工作流，超高一致性面部替换图生图方案_2103891330228379650
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1最强换头工作流，超高一致性面部替换图生图方案_2103891330228379650.json
hash: 1a19c3a7aff3ba96
coverage: 0.684783
learned_at: 2026-10-21 00:42:41
nodes: [ModelAttentionBackend, ResizeImageMaskNode, ResizeImageMaskNode, QwenImage21Cache, KSamplerSelect, RandomNoise, CFGGuider, BasicScheduler, Seed (rgthree), FaceAnalysisModels, SamplerCustomAdvanced, easy cleanGpuUsed, VAEDecode, PreviewImage, VOSR2ModelLoader, VOSR2Upscale, Images to RGB, easy cleanGpuUsed, easy cleanGpuUsed, PreviewImage, easy cleanGpuUsed, Reroute, Reroute, ImageStitch, ResizeImageMaskNode, ResizeImageMaskNode, ImageStitch, Reroute, Reroute, Reroute, Reroute, Reroute, easy float, ImageScaleToMaxDimension, Reroute, SeedVR2LoadVAEModel, PreviewImage, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, Reroute, easy cleanGpuUsed, PreviewImage, Reroute, PreviewImage, Reroute, Reroute, TextEncodeQwenImage21, LoadImage, PreviewImage, PreviewImage, UNETLoader, CLIPLoader, VAELoader, Reroute, SaveImage, LoadImage, easy cleanGpuUsed, Image Comparer (rgthree), FaceEmbedDistance, Reroute, Reroute, Image Comparer (rgthree), Reroute, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1最强换头工作流，超高一致性面部替换图生图方案_2103891330228379650.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1最强换头工作流，超高一致性面部替换图生图方案_2103891330228379650.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（92 个）：
- `ModelAttentionBackend`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `QwenImage21Cache`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `BasicScheduler`
- `Seed (rgthree)`
- `FaceAnalysisModels`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `PreviewImage`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `Images to RGB`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `PreviewImage`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `ImageStitch`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `ImageStitch`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy float`
- `ImageScaleToMaxDimension`
- `Reroute`
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `Reroute`
- `easy cleanGpuUsed`
- `PreviewImage`
- `Reroute`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `TextEncodeQwenImage21`
- `LoadImage`
- `PreviewImage`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Reroute`
- `SaveImage`
- `LoadImage`
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `FaceEmbedDistance`
- `Reroute`
- `Reroute`
- `Image Comparer (rgthree)`
- `Reroute`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **68%**（63/92）

**有卡**：`ModelAttentionBackend`、`ResizeImageMaskNode`、`QwenImage21Cache`、`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`BasicScheduler`、`Seed (rgthree)`、`FaceAnalysisModels`、`SamplerCustomAdvanced`、`easy cleanGpuUsed`、`VAEDecode`、`VOSR2ModelLoader`、`VOSR2Upscale`、`Images to RGB`、`ImageStitch`、`easy float`、`ImageScaleToMaxDimension`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`TextEncodeQwenImage21`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`、`FaceEmbedDistance`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

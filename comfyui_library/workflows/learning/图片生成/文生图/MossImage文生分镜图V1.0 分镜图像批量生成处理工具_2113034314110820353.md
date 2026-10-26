---
key: 图片生成/文生图/MossImage文生分镜图V1.0 分镜图像批量生成处理工具_2113034314110820353.json
name: MossImage文生分镜图V1.0 分镜图像批量生成处理工具_2113034314110820353
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/MossImage文生分镜图V1.0 分镜图像批量生成处理工具_2113034314110820353.json
hash: a4b8e8473f40e8f8
coverage: 0.9
learned_at: 2026-10-26 22:08:29
nodes: [CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, ResolutionSelector, CR Prompt Text, KSampler, SaveImage, VAEDecode, VAELoader, UNETLoader, UNETLoader, MOSSImagePromptEnhancerT8, CLIPTextEncode, KSampler, SaveImage, VAEDecode, ImageStitch, PreviewImage, easy cleanGpuUsed, CLIPLoader, CR Prompt Text, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/MossImage文生分镜图V1.0 分镜图像批量生成处理工具_2113034314110820353.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/MossImage文生分镜图V1.0 分镜图像批量生成处理工具_2113034314110820353.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `CR Prompt Text`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `MOSSImagePromptEnhancerT8`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `ImageStitch`
- `PreviewImage`
- `easy cleanGpuUsed`
- `CLIPLoader`
- `CR Prompt Text`
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
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **90%**（45/50）

**有卡**：`CLIPTextEncode`、`EmptyLatentImage`、`ResolutionSelector`、`CR Prompt Text`、`KSampler`、`SaveImage`、`VAEDecode`、`VAELoader`、`UNETLoader`、`MOSSImagePromptEnhancerT8`、`ImageStitch`、`easy cleanGpuUsed`、`CLIPLoader`、`LoraLoaderModelOnly`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

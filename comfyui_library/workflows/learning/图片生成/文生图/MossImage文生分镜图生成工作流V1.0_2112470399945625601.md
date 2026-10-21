---
key: 图片生成/文生图/MossImage文生分镜图生成工作流V1.0_2112470399945625601.json
name: MossImage文生分镜图生成工作流V1.0_2112470399945625601
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/MossImage文生分镜图生成工作流V1.0_2112470399945625601.json
hash: 5cf76694a99b6819
coverage: 0.952381
learned_at: 2026-10-21 02:53:53
nodes: [CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, ResolutionSelector, CR Prompt Text, KSampler, SaveImage, VAEDecode, VAELoader, UNETLoader, UNETLoader, MOSSImagePromptEnhancerT8, CLIPTextEncode, KSampler, SaveImage, VAEDecode, ImageStitch, PreviewImage, easy cleanGpuUsed, CLIPLoader, CR Prompt Text]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 3.5, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 16, "width": 1024}
---

# 图片生成/文生图/MossImage文生分镜图生成工作流V1.0_2112470399945625601.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/MossImage文生分镜图生成工作流V1.0_2112470399945625601.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
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

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `19960422`
- `steps` = `16`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`CLIPTextEncode`、`EmptyLatentImage`、`ResolutionSelector`、`CR Prompt Text`、`KSampler`、`SaveImage`、`VAEDecode`、`VAELoader`、`UNETLoader`、`MOSSImagePromptEnhancerT8`、`ImageStitch`、`easy cleanGpuUsed`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

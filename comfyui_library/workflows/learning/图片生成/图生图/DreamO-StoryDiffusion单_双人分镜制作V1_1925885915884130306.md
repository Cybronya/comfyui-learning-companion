---
key: 图片生成/图生图/DreamO-StoryDiffusion单_双人分镜制作V1_1925885915884130306.json
name: DreamO-StoryDiffusion单_双人分镜制作V1_1925885915884130306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/DreamO-StoryDiffusion单_双人分镜制作V1_1925885915884130306.json
hash: aa9a0cb5d5d83ba7
coverage: 1
learned_at: 2026-10-23 10:52:24
nodes: [VAELoader, ImageBatch, StoryDiffusion_KSampler, EmptyLatentImage, VAEDecode, LoadImage, StoryDiffusion_Apply, SaveImage, EasyFunction_Lite, JWInteger, JWInteger, StoryDiffusion_CLIPTextEncode, CR Prompt Text, CR Prompt Text, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": 0.5, "height": 512, "sampler_name": "euler", "scheduler": "normal", "seed": 1656592934, "steps": 20, "width": 512}
---

# 图片生成/图生图/DreamO-StoryDiffusion单_双人分镜制作V1_1925885915884130306.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/DreamO-StoryDiffusion单_双人分镜制作V1_1925885915884130306.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `VAELoader`
- `ImageBatch`
- `StoryDiffusion_KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `StoryDiffusion_Apply`
- `SaveImage`
- `EasyFunction_Lite`
- `JWInteger`
- `JWInteger`
- `StoryDiffusion_CLIPTextEncode` ★核心
- `CR Prompt Text`
- `CR Prompt Text`
- `LoadImage`

## 关键参数

- `seed` = `1656592934`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `0.5`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`VAELoader`、`ImageBatch`、`StoryDiffusion_KSampler`、`EmptyLatentImage`、`VAEDecode`、`LoadImage`、`StoryDiffusion_Apply`、`SaveImage`、`EasyFunction_Lite`、`JWInteger`、`StoryDiffusion_CLIPTextEncode`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、EmptyLatentImage、LoadImage、StoryDiffusion_KSampler、StoryDiffusion_CLIPTextEncode、CR Prompt Text、SaveImage

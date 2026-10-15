---
key: 图片生成/文生图/StoryDiffusion+DreamO多人物一致性_1926146782307258370.json
name: StoryDiffusion+DreamO多人物一致性_1926146782307258370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/StoryDiffusion+DreamO多人物一致性_1926146782307258370.json
hash: d9834a969ded9826
coverage: 1
learned_at: 2026-10-15 22:27:33
nodes: [VAELoader, StoryDiffusion_CLIPTextEncode, EasyFunction_Lite, StoryDiffusion_KSampler, EmptyLatentImage, VAEDecode, LoadImage, ImageResize+, Image Batch, ImageResize+, LoadImage, StoryDiffusion_Apply, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": 0.5, "height": 512, "sampler_name": "euler", "scheduler": "normal", "seed": 1766578679, "steps": 20, "width": 456}
---

# 图片生成/文生图/StoryDiffusion+DreamO多人物一致性_1926146782307258370.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/StoryDiffusion+DreamO多人物一致性_1926146782307258370.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `VAELoader`
- `StoryDiffusion_CLIPTextEncode` ★核心
- `EasyFunction_Lite`
- `StoryDiffusion_KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `ImageResize+`
- `Image Batch`
- `ImageResize+`
- `LoadImage`
- `StoryDiffusion_Apply`
- `SaveImage`

## 关键参数

- `seed` = `1766578679`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `0.5`
- `width` = `456`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`VAELoader`、`StoryDiffusion_CLIPTextEncode`、`EasyFunction_Lite`、`StoryDiffusion_KSampler`、`EmptyLatentImage`、`VAEDecode`、`LoadImage`、`ImageResize+`、`Image Batch`、`StoryDiffusion_Apply`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、EmptyLatentImage、LoadImage、StoryDiffusion_KSampler、StoryDiffusion_CLIPTextEncode、ImageResize+、SaveImage

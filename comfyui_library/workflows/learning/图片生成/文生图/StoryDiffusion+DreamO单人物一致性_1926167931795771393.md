---
key: 图片生成/文生图/StoryDiffusion+DreamO单人物一致性_1926167931795771393.json
name: StoryDiffusion+DreamO单人物一致性_1926167931795771393
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/StoryDiffusion+DreamO单人物一致性_1926167931795771393.json
hash: e3287557508b1811
coverage: 1
learned_at: 2026-10-15 22:27:33
nodes: [VAELoader, StoryDiffusion_KSampler, EmptyLatentImage, VAEDecode, StoryDiffusion_Apply, SaveImage, ImageResize+, LoadImage, StoryDiffusion_CLIPTextEncode, EasyFunction_Lite]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": 0.5, "height": 512, "sampler_name": "euler", "scheduler": "normal", "seed": 218622350, "steps": 20, "width": 456}
---

# 图片生成/文生图/StoryDiffusion+DreamO单人物一致性_1926167931795771393.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/StoryDiffusion+DreamO单人物一致性_1926167931795771393.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（10 个）：
- `VAELoader`
- `StoryDiffusion_KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `StoryDiffusion_Apply`
- `SaveImage`
- `ImageResize+`
- `LoadImage`
- `StoryDiffusion_CLIPTextEncode` ★核心
- `EasyFunction_Lite`

## 关键参数

- `seed` = `218622350`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `0.5`
- `width` = `456`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`VAELoader`、`StoryDiffusion_KSampler`、`EmptyLatentImage`、`VAEDecode`、`StoryDiffusion_Apply`、`SaveImage`、`ImageResize+`、`LoadImage`、`StoryDiffusion_CLIPTextEncode`、`EasyFunction_Lite`

**用到的条目**：VAEDecode、VAELoader、EmptyLatentImage、LoadImage、StoryDiffusion_KSampler、StoryDiffusion_CLIPTextEncode、ImageResize+、SaveImage

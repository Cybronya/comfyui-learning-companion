---
key: 图片生成/文生图/StoryDiffusion+DreamO单人物一致性_1926167931795771393.json
name: StoryDiffusion+DreamO单人物一致性_1926167931795771393
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/StoryDiffusion+DreamO单人物一致性_1926167931795771393.json
hash: e3287557508b1811
coverage: 0.9
learned_at: 2026-10-10 20:59:12
nodes: [VAELoader, StoryDiffusion_KSampler, EmptyLatentImage, VAEDecode, StoryDiffusion_Apply, SaveImage, ImageResize+, LoadImage, StoryDiffusion_CLIPTextEncode, EasyFunction_Lite]
patterns: []
missing: [ImageResize+]
parameters: {"batch_size": 1, "cfg": 8, "denoise": 0.5, "height": 512, "sampler_name": "euler", "scheduler": "normal", "seed": 218622350, "steps": 20, "width": 456}
discoveries: [次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/StoryDiffusion+DreamO单人物一致性_1926167931795771393.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/StoryDiffusion+DreamO单人物一致性_1926167931795771393.json`

## 结构

**节点**（10 个）：
- `VAELoader`
- `StoryDiffusion_KSampler`
- `EmptyLatentImage`
- `VAEDecode`
- `StoryDiffusion_Apply`
- `SaveImage`
- `ImageResize+`
- `LoadImage`
- `StoryDiffusion_CLIPTextEncode`
- `EasyFunction_Lite`

## 关键参数

- `batch_size` = `1`
- `cfg` = `8`
- `denoise` = `0.5`
- `height` = `512`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `seed` = `218622350`
- `steps` = `20`
- `width` = `456`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`VAELoader`、`StoryDiffusion_KSampler`、`EmptyLatentImage`、`VAEDecode`、`StoryDiffusion_Apply`、`SaveImage`、`ImageResize+`、`LoadImage`、`StoryDiffusion_CLIPTextEncode`

**缺卡**（1）：`ImageResize+`

## 学习发现

- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明

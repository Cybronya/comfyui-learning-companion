---
key: 图片生成/文生图/StoryDiffusion+DreamO多人物一致性_1926146782307258370.json
name: StoryDiffusion+DreamO多人物一致性_1926146782307258370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/StoryDiffusion+DreamO多人物一致性_1926146782307258370.json
hash: d9834a969ded9826
coverage: 0.769231
learned_at: 2026-10-10 20:59:12
nodes: [VAELoader, StoryDiffusion_CLIPTextEncode, EasyFunction_Lite, StoryDiffusion_KSampler, EmptyLatentImage, VAEDecode, LoadImage, ImageResize+, Image Batch, ImageResize+, LoadImage, StoryDiffusion_Apply, SaveImage]
patterns: []
missing: [Image Batch, ImageResize+, ImageResize+]
parameters: {"batch_size": 1, "cfg": 8, "denoise": 0.5, "height": 512, "sampler_name": "euler", "scheduler": "normal", "seed": 1766578679, "steps": 20, "width": 456}
discoveries: [次要节点 `Image Batch` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/StoryDiffusion+DreamO多人物一致性_1926146782307258370.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/StoryDiffusion+DreamO多人物一致性_1926146782307258370.json`

## 结构

**节点**（13 个）：
- `VAELoader`
- `StoryDiffusion_CLIPTextEncode`
- `EasyFunction_Lite`
- `StoryDiffusion_KSampler`
- `EmptyLatentImage`
- `VAEDecode`
- `LoadImage`
- `ImageResize+`
- `Image Batch`
- `ImageResize+`
- `LoadImage`
- `StoryDiffusion_Apply`
- `SaveImage`

## 关键参数

- `batch_size` = `1`
- `cfg` = `8`
- `denoise` = `0.5`
- `height` = `512`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `seed` = `1766578679`
- `steps` = `20`
- `width` = `456`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`VAELoader`、`StoryDiffusion_CLIPTextEncode`、`EasyFunction_Lite`、`StoryDiffusion_KSampler`、`EmptyLatentImage`、`VAEDecode`、`LoadImage`、`ImageResize+`、`Image Batch`

**缺卡**（3）：`Image Batch`、`ImageResize+`、`ImageResize+`

## 学习发现

- 次要节点 `Image Batch` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明

---
key: 图片生成/文生图/全能图片G-Image-2.5文生图工作流_2098372445806878721.json
name: 全能图片G-Image-2.5文生图工作流_2098372445806878721
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/全能图片G-Image-2.5文生图工作流_2098372445806878721.json
hash: de2311c19dc259a6
coverage: 0.818182
learned_at: 2026-10-10 20:59:35
nodes: [SaveImage, Note, PrimitiveStringMultiline, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, TextEncodeQwenImageEditPlus, EmptySD3LatentImage, KSampler, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 24}
---

# 图片生成/文生图/全能图片G-Image-2.5文生图工作流_2098372445806878721.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/全能图片G-Image-2.5文生图工作流_2098372445806878721.json`

## 结构

**节点**（11 个）：
- `SaveImage`
- `Note`
- `PrimitiveStringMultiline`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode`
- `TextEncodeQwenImageEditPlus`
- `EmptySD3LatentImage`
- `KSampler`
- `VAEDecode`

## 关键参数

- `cfg` = `2.5`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `42`
- `steps` = `24`

## 知识

覆盖率 **82%**（9/11）

**有卡**：`SaveImage`、`Note`、`PrimitiveStringMultiline`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`TextEncodeQwenImageEditPlus`、`EmptySD3LatentImage`

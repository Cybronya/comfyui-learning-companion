---
key: 图片生成/文生图/qwen-image-2.1文生图｜高效创作，一键生图_2105572911326261250.json
name: qwen-image-2.1文生图｜高效创作，一键生图_2105572911326261250
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image-2.1文生图｜高效创作，一键生图_2105572911326261250.json
hash: 1753890444e56419
coverage: 1
learned_at: 2026-10-10 20:59:25
nodes: [UNETLoader, KSampler, VAELoader, EmptyLatentImage, VAEDecode, SaveImage, SaveImageAdvanced, CLIPLoader, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 60248155367650, "steps": 25, "width": 1080}
---

# 图片生成/文生图/qwen-image-2.1文生图｜高效创作，一键生图_2105572911326261250.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image-2.1文生图｜高效创作，一键生图_2105572911326261250.json`

## 结构

**节点**（9 个）：
- `UNETLoader`
- `KSampler`
- `VAELoader`
- `EmptyLatentImage`
- `VAEDecode`
- `SaveImage`
- `SaveImageAdvanced`
- `CLIPLoader`
- `TextEncodeQwenImage21`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1920`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `60248155367650`
- `steps` = `25`
- `width` = `1080`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`UNETLoader`、`KSampler`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`、`SaveImageAdvanced`、`CLIPLoader`、`TextEncodeQwenImage21`

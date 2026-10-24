---
key: 图片生成/图生图/Qwen image 2.1图片编辑-1_2112506837907099650.json
name: Qwen image 2.1图片编辑-1_2112506837907099650
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑-1_2112506837907099650.json
hash: a2103ff0b1655e8a
coverage: 0.857143
learned_at: 2026-10-23 11:14:01
nodes: [VAEDecode, ComfySwitchNode, QwenImage21Cache, KSampler, EmptyLatentImage, VAELoader, TextEncodeQwenImage21, CLIPLoader, SaveImage, PrimitiveStringMultiline, LoadImage, UNETLoader, easy int, easy int]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 16}
---

# 图片生成/图生图/Qwen image 2.1图片编辑-1_2112506837907099650.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图片编辑-1_2112506837907099650.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `SaveImage`
- `PrimitiveStringMultiline`
- `LoadImage`
- `UNETLoader` ★核心
- `easy int`
- `easy int`

## 关键参数

- `seed` = `999`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `16`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`VAEDecode`、`QwenImage21Cache`、`KSampler`、`EmptyLatentImage`、`VAELoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`SaveImage`、`LoadImage`、`UNETLoader`、`easy int`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache

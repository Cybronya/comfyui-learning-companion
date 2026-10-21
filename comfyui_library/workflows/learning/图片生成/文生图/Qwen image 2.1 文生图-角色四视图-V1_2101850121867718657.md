---
key: 图片生成/文生图/Qwen image 2.1 文生图-角色四视图-V1_2101850121867718657.json
name: Qwen image 2.1 文生图-角色四视图-V1_2101850121867718657
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图-角色四视图-V1_2101850121867718657.json
hash: 5de71c8694788208
coverage: 0.722222
learned_at: 2026-10-20 01:51:07
nodes: [TextEncodeQwenImage21, CLIPLoader, VAELoader, UNETLoader, KSampler, CLIPLoader, easy showAnything, EmptyLatentImage, TextGenerateLTX2Prompt, PrimitiveStringMultiline, VAEDecode, SaveImage, StringConcatenate, PrimitiveStringMultiline, ComfySwitchNode, PrimitiveStringMultiline, ResolutionSelector, PrimitiveBoolean]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 197422670593493, "steps": 50, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1 文生图-角色四视图-V1_2101850121867718657.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图-角色四视图-V1_2101850121867718657.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `TextGenerateLTX2Prompt`
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心
- `SaveImage`
- `StringConcatenate`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `PrimitiveBoolean`

## 关键参数

- `seed` = `197422670593493`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **72%**（13/18）

**有卡**：`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSampler`、`EmptyLatentImage`、`TextGenerateLTX2Prompt`、`VAEDecode`、`SaveImage`、`StringConcatenate`、`ResolutionSelector`、`PrimitiveBoolean`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

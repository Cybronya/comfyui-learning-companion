---
key: 图片生成/文生图/Qwen2.1文生图_2101145781234397185.json
name: Qwen2.1文生图_2101145781234397185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图_2101145781234397185.json
hash: 21815e0e4645c234
coverage: 0.833333
learned_at: 2026-10-20 01:51:22
nodes: [MarkdownNote, Note, EmptyLatentImage, KSampler, UNETLoader, ResolutionSelector, CLIPLoader, ConditioningZeroOut, TextEncodeQwenImageEditPlus, VAELoader, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen2.1文生图_2101145781234397185.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图_2101145781234397185.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（12 个）：
- `MarkdownNote`
- `Note`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `ResolutionSelector`
- `CLIPLoader`
- `ConditioningZeroOut`
- `TextEncodeQwenImageEditPlus`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`EmptyLatentImage`、`KSampler`、`UNETLoader`、`ResolutionSelector`、`CLIPLoader`、`ConditioningZeroOut`、`TextEncodeQwenImageEditPlus`、`VAELoader`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、ResolutionSelector、UNETLoader

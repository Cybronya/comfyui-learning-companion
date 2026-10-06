---
key: 图片生成/文生图/Qwen-image2.1 空间折叠流之太虚生成_2103043423883321346.json
name: Qwen-image2.1 空间折叠流之太虚生成_2103043423883321346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-image2.1 空间折叠流之太虚生成_2103043423883321346.json
hash: 467e55a908100e17
coverage: 0.6875
learned_at: 2026-10-07 02:25:59
nodes: [CLIPLoader, VAELoader, ImpactInt, ImpactInt, TextEncodeQwenImage21, GetNode, EmptyLatentImage, SetNode, GetNode, SetNode, VAEDecode, KSampler, SaveImage, UNETLoader, MarkdownNote, Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 257, "steps": 50, "width": 1024}
---

# 图片生成/文生图/Qwen-image2.1 空间折叠流之太虚生成_2103043423883321346.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-image2.1 空间折叠流之太虚生成_2103043423883321346.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `CLIPLoader`
- `VAELoader`
- `ImpactInt`
- `ImpactInt`
- `TextEncodeQwenImage21`
- `GetNode`
- `EmptyLatentImage` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `MarkdownNote`
- `Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `257`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **69%**（11/16）

**有卡**：`CLIPLoader`、`VAELoader`、`ImpactInt`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`SaveImage`、`UNETLoader`、`Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、UNETLoader、SaveImage

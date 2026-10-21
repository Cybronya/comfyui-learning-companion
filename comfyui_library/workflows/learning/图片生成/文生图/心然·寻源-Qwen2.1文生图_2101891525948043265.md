---
key: 图片生成/文生图/心然·寻源-Qwen2.1文生图_2101891525948043265.json
name: 心然·寻源-Qwen2.1文生图_2101891525948043265
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/心然·寻源-Qwen2.1文生图_2101891525948043265.json
hash: 3c06c2e96b2751ed
coverage: 0.464286
learned_at: 2026-10-20 01:52:31
nodes: [VAELoader, SetNode, SetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, ConditioningZeroOut, SetNode, SaveImage, SetNode, EmptyLatentImage, GetNode, SetNode, CLIPLoader, UNETLoader, GetNode, TextEncodeQwenImage21, GetNode, SetNode, TextGenerate, SetNode, KSampler, CLIPLoader, ResolutionSelector, MarkdownNote, StringConstantMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 567738645062791, "steps": 25, "width": 1024}
---

# 图片生成/文生图/心然·寻源-Qwen2.1文生图_2101891525948043265.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/心然·寻源-Qwen2.1文生图_2101891525948043265.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（28 个）：
- `VAELoader`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `SetNode`
- `SaveImage`
- `SetNode`
- `EmptyLatentImage` ★核心
- `GetNode`
- `SetNode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `GetNode`
- `TextEncodeQwenImage21`
- `GetNode`
- `SetNode`
- `TextGenerate`
- `SetNode`
- `KSampler` ★核心
- `CLIPLoader`
- `ResolutionSelector`
- `MarkdownNote`
- `StringConstantMultiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `567738645062791`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **46%**（13/28）

**有卡**：`VAELoader`、`VAEDecode`、`ConditioningZeroOut`、`SaveImage`、`EmptyLatentImage`、`CLIPLoader`、`UNETLoader`、`TextEncodeQwenImage21`、`TextGenerate`、`KSampler`、`ResolutionSelector`、`StringConstantMultiline`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、ResolutionSelector

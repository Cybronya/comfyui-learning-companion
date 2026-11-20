---
key: 平台全量/Qwen-2.1 抠图_2103378102855491586.json
name: Qwen-2.1 抠图_2103378102855491586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-2.1 抠图_2103378102855491586.json
hash: 6b14d18a88cd1329
coverage: 0.769231
learned_at: 2026-11-14 00:50:59
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, Label (rgthree), UNETLoader, VAELoader, CLIPLoader, QwenImage21Cache, KSampler, VAEDecode, SaveImage, LoadImage, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 65099404309120, "steps": 25}
---

# 平台全量/Qwen-2.1 抠图_2103378102855491586.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-2.1 抠图_2103378102855491586.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Label (rgthree)`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `65099404309120`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`Label (rgthree)`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`SaveImage`、`LoadImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader

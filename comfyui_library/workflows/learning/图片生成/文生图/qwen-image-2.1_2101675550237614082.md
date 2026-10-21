---
key: 图片生成/文生图/qwen-image-2.1_2101675550237614082.json
name: qwen-image-2.1_2101675550237614082
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image-2.1_2101675550237614082.json
hash: 92c0f9b1c2fef332
coverage: 0.866667
learned_at: 2026-10-20 01:51:55
nodes: [MarkdownNote, MarkdownNote, KSampler, QwenImage21Cache, UNETLoader, LoadImage, LoadImage, LoadImage, VAEDecode, SaveImage, TextEncodeQwenImage21, CLIPLoader, CR Text, CR Text, VAELoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 21923190535970, "steps": 25}
---

# 图片生成/文生图/qwen-image-2.1_2101675550237614082.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image-2.1_2101675550237614082.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `MarkdownNote`
- `MarkdownNote`
- `KSampler` ★核心
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `CR Text`
- `CR Text`
- `VAELoader`

## 关键参数

- `seed` = `21923190535970`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`KSampler`、`QwenImage21Cache`、`UNETLoader`、`LoadImage`、`VAEDecode`、`SaveImage`、`TextEncodeQwenImage21`、`CLIPLoader`、`CR Text`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader

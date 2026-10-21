---
key: 图片生成/文生图/qwen-image-2.1多图编辑_2101799458202804226.json
name: qwen-image-2.1多图编辑_2101799458202804226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image-2.1多图编辑_2101799458202804226.json
hash: f5252bd05cbb3102
coverage: 0.875
learned_at: 2026-10-20 01:51:56
nodes: [MarkdownNote, MarkdownNote, KSampler, QwenImage21Cache, UNETLoader, VAEDecode, LoadImage, LoadImage, CLIPLoader, LoadImage, TextEncodeQwenImage21, LoadImage, SaveImage, CR Text, CR Text, VAELoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 881558754900768, "steps": 25}
---

# 图片生成/文生图/qwen-image-2.1多图编辑_2101799458202804226.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image-2.1多图编辑_2101799458202804226.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `MarkdownNote`
- `MarkdownNote`
- `KSampler` ★核心
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `LoadImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `SaveImage`
- `CR Text`
- `CR Text`
- `VAELoader`

## 关键参数

- `seed` = `881558754900768`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`KSampler`、`QwenImage21Cache`、`UNETLoader`、`VAEDecode`、`LoadImage`、`CLIPLoader`、`TextEncodeQwenImage21`、`SaveImage`、`CR Text`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader

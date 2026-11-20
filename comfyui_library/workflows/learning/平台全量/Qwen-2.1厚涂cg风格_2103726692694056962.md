---
key: 平台全量/Qwen-2.1厚涂cg风格_2103726692694056962.json
name: Qwen-2.1厚涂cg风格_2103726692694056962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-2.1厚涂cg风格_2103726692694056962.json
hash: c1221dff7152970b
coverage: 0.733333
learned_at: 2026-11-14 00:51:00
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, VAELoader, JWInteger, easy imageConcat, PreviewImage, TextEncodeQwenImage21, QwenImage21Cache, KSampler, VAEDecode, CLIPLoader, SaveImage, UNETLoader, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1041383565880097, "steps": 25}
---

# 平台全量/Qwen-2.1厚涂cg风格_2103726692694056962.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-2.1厚涂cg风格_2103726692694056962.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `VAELoader`
- `JWInteger`
- `easy imageConcat`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `SaveImage`
- `UNETLoader` ★核心
- `LoadImage`

## 关键参数

- `seed` = `1041383565880097`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（11/15）

**有卡**：`VAELoader`、`JWInteger`、`easy imageConcat`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`CLIPLoader`、`SaveImage`、`UNETLoader`、`LoadImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader

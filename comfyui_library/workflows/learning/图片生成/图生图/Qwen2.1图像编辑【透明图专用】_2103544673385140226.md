---
key: 图片生成/图生图/Qwen2.1图像编辑【透明图专用】_2103544673385140226.json
name: Qwen2.1图像编辑【透明图专用】_2103544673385140226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1图像编辑【透明图专用】_2103544673385140226.json
hash: a992fe7f1164abb4
coverage: 0.882353
learned_at: 2026-10-21 00:43:38
nodes: [Note, CLIPLoader, VAELoader, QwenImage21Cache, KSampler, UNETLoader, VAEDecode, SaveImage, MarkdownNote, easy seed, TextEncodeQwenImage21, StringConcatenate, LoadImage, StringConstantMultiline, StringConstantMultiline, StringConcatenate, StringConstantMultiline]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 372980352069668, "steps": 40}
---

# 图片生成/图生图/Qwen2.1图像编辑【透明图专用】_2103544673385140226.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1图像编辑【透明图专用】_2103544673385140226.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `Note`
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `MarkdownNote`
- `easy seed`
- `TextEncodeQwenImage21`
- `StringConcatenate`
- `LoadImage`
- `StringConstantMultiline`
- `StringConstantMultiline`
- `StringConcatenate`
- `StringConstantMultiline`

## 关键参数

- `seed` = `372980352069668`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`KSampler`、`UNETLoader`、`VAEDecode`、`SaveImage`、`easy seed`、`TextEncodeQwenImage21`、`StringConcatenate`、`LoadImage`、`StringConstantMultiline`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader

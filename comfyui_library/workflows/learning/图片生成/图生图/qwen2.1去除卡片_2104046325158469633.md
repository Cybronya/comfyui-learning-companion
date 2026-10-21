---
key: 图片生成/图生图/qwen2.1去除卡片_2104046325158469633.json
name: qwen2.1去除卡片_2104046325158469633
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen2.1去除卡片_2104046325158469633.json
hash: 2fa77f7419d33783
coverage: 0.846154
learned_at: 2026-10-21 00:46:10
nodes: [Anything Everywhere3, VAELoader, UNETLoader, CLIPLoader, KSampler, SaveImage, PreviewImage, Text, TextEncodeQwenImage21, LoadImage, VAEDecode, Image Remove Alpha JK, ImageColorMatch+]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 328081650412903, "steps": 25}
---

# 图片生成/图生图/qwen2.1去除卡片_2104046325158469633.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen2.1去除卡片_2104046325158469633.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `Anything Everywhere3`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `SaveImage`
- `PreviewImage`
- `Text`
- `TextEncodeQwenImage21`
- `LoadImage`
- `VAEDecode` ★核心
- `Image Remove Alpha JK`
- `ImageColorMatch+`

## 关键参数

- `seed` = `328081650412903`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`VAELoader`、`UNETLoader`、`CLIPLoader`、`KSampler`、`SaveImage`、`Text`、`TextEncodeQwenImage21`、`LoadImage`、`VAEDecode`、`Image Remove Alpha JK`、`ImageColorMatch+`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、SaveImage

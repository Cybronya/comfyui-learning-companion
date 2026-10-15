---
key: 图片生成/文生图/Qwen Image2.1 图生图任意角度转换双图版_2105241162926878722.json
name: Qwen Image2.1 图生图任意角度转换双图版_2105241162926878722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image2.1 图生图任意角度转换双图版_2105241162926878722.json
hash: 2040524950a0b018
coverage: 0.846154
learned_at: 2026-10-10 20:58:55
nodes: [LoadImage, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, TextEncodeQwenImage21, QwenImage21Cache, KSampler, VAEDecode, SaveImage, MarkdownNote, MarkdownNote, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 20260930, "steps": 24}
---

# 图片生成/文生图/Qwen Image2.1 图生图任意角度转换双图版_2105241162926878722.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image2.1 图生图任意角度转换双图版_2105241162926878722.json`

## 结构

**节点**（13 个）：
- `LoadImage`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `KSampler`
- `VAEDecode`
- `SaveImage`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`

## 关键参数

- `cfg` = `3`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `20260930`
- `steps` = `24`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`SaveImage`、`MarkdownNote`

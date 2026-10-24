---
key: 图片生成/图生图/Qwein-image2.1分镜专用空镜（有人、无人）_2111716013799731201.json
name: Qwein-image2.1分镜专用空镜（有人、无人）_2111716013799731201
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwein-image2.1分镜专用空镜（有人、无人）_2111716013799731201.json
hash: 2abd573fd0ab5976
coverage: 0.823529
learned_at: 2026-10-23 11:11:30
nodes: [ManualSigmas, RH_Screenwriter, easy showAnything, ClownsharKSampler_Beta, WujiUpscaler2, UNETLoader, CLIPLoader, VAELoader, QwenImage21SageAttentionT8, SaveImage, VAEDecode, PreviewImage, TextEncodeQwenImage21, LoadImage, WujiImagePrompt, WujiPromptEditor, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": 1, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "bong_tangent"}
---

# 图片生成/图生图/Qwein-image2.1分镜专用空镜（有人、无人）_2111716013799731201.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwein-image2.1分镜专用空镜（有人、无人）_2111716013799731201.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `ManualSigmas`
- `RH_Screenwriter`
- `easy showAnything`
- `ClownsharKSampler_Beta` ★核心
- `WujiUpscaler2`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21SageAttentionT8`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `WujiImagePrompt`
- `WujiPromptEditor`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `0.5`
- `steps` = `bong_tangent`
- `cfg` = `8`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`ManualSigmas`、`RH_Screenwriter`、`ClownsharKSampler_Beta`、`WujiUpscaler2`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21SageAttentionT8`、`SaveImage`、`VAEDecode`、`TextEncodeQwenImage21`、`LoadImage`、`WujiImagePrompt`、`WujiPromptEditor`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、ClownsharKSampler_Beta、WujiUpscaler2

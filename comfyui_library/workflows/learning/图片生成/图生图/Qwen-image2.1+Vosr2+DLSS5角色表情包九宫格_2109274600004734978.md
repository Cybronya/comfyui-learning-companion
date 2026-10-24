---
key: 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色表情包九宫格_2109274600004734978.json
name: Qwen-image2.1+Vosr2+DLSS5角色表情包九宫格_2109274600004734978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色表情包九宫格_2109274600004734978.json
hash: debcb97aac3e543b
coverage: 0.882353
learned_at: 2026-10-23 11:18:23
nodes: [CLIPLoader, QwenImage21SageAttentionT8, ManualSigmas, VAELoader, ClownsharKSampler_Beta, UNETLoader, VAEDecode, SaveImage, easy showAnything, RH_Screenwriter, LoadImage, TextEncodeQwenImage21, PrimitiveStringMultiline, WujiCleaner, WujiUpscaler2, WujiImagePrompt, WujiPromptEditor]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": 1, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "bong_tangent"}
---

# 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色表情包九宫格_2109274600004734978.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色表情包九宫格_2109274600004734978.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `CLIPLoader`
- `QwenImage21SageAttentionT8`
- `ManualSigmas`
- `VAELoader`
- `ClownsharKSampler_Beta` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `easy showAnything`
- `RH_Screenwriter`
- `LoadImage`
- `TextEncodeQwenImage21`
- `PrimitiveStringMultiline`
- `WujiCleaner`
- `WujiUpscaler2`
- `WujiImagePrompt`
- `WujiPromptEditor`

## 关键参数

- `seed` = `0.5`
- `steps` = `bong_tangent`
- `cfg` = `8`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`CLIPLoader`、`QwenImage21SageAttentionT8`、`ManualSigmas`、`VAELoader`、`ClownsharKSampler_Beta`、`UNETLoader`、`VAEDecode`、`SaveImage`、`RH_Screenwriter`、`LoadImage`、`TextEncodeQwenImage21`、`WujiCleaner`、`WujiUpscaler2`、`WujiImagePrompt`、`WujiPromptEditor`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、ClownsharKSampler_Beta、WujiUpscaler2

---
key: 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆照（文生_图生）_2107810644580982786.json
name: Qwen-image2.1+Vosr2+DLSS5角色定妆照（文生_图生）_2107810644580982786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆照（文生_图生）_2107810644580982786.json
hash: 003cf6912fc046a9
coverage: 0.875
learned_at: 2026-10-21 00:43:23
nodes: [CLIPLoader, QwenImage21SageAttentionT8, ManualSigmas, LoadImage, TextEncodeQwenImage21, VAELoader, RH_Screenwriter, easy showAnything, SaveImage, VAEDecode, WujiImagePrompt, ClownsharKSampler_Beta, PrimitiveStringMultiline, WujiPromptEditor, UNETLoader, WujiUpscaler2]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": 1, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "bong_tangent"}
---

# 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆照（文生_图生）_2107810644580982786.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆照（文生_图生）_2107810644580982786.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `CLIPLoader`
- `QwenImage21SageAttentionT8`
- `ManualSigmas`
- `LoadImage`
- `TextEncodeQwenImage21`
- `VAELoader`
- `RH_Screenwriter`
- `easy showAnything`
- `SaveImage`
- `VAEDecode` ★核心
- `WujiImagePrompt`
- `ClownsharKSampler_Beta` ★核心
- `PrimitiveStringMultiline`
- `WujiPromptEditor`
- `UNETLoader` ★核心
- `WujiUpscaler2`

## 关键参数

- `seed` = `0.5`
- `steps` = `bong_tangent`
- `cfg` = `8`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`CLIPLoader`、`QwenImage21SageAttentionT8`、`ManualSigmas`、`LoadImage`、`TextEncodeQwenImage21`、`VAELoader`、`RH_Screenwriter`、`SaveImage`、`VAEDecode`、`WujiImagePrompt`、`ClownsharKSampler_Beta`、`WujiPromptEditor`、`UNETLoader`、`WujiUpscaler2`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、ClownsharKSampler_Beta、WujiUpscaler2

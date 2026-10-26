---
key: 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆照文生_图生_2114260663261552641.json
name: Qwen-image2.1+Vosr2+DLSS5角色定妆照文生_图生_2114260663261552641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆照文生_图生_2114260663261552641.json
hash: e1542e3c51869e2d
coverage: 0.833333
learned_at: 2026-10-26 22:03:26
nodes: [CLIPLoader, QwenImage21SageAttentionT8, ManualSigmas, LoadImage, TextEncodeQwenImage21, VAELoader, RH_Screenwriter, easy showAnything, SaveImage, VAEDecode, WujiImagePrompt, ClownsharKSampler_Beta, PrimitiveStringMultiline, WujiPromptEditor, UNETLoader, WujiUpscaler2, LoadImage, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": 1, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "bong_tangent"}
---

# 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆照文生_图生_2114260663261552641.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆照文生_图生_2114260663261552641.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
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
- `LoadImage`
- `PreviewImage`

## 关键参数

- `seed` = `0.5`
- `steps` = `bong_tangent`
- `cfg` = `8`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`CLIPLoader`、`QwenImage21SageAttentionT8`、`ManualSigmas`、`LoadImage`、`TextEncodeQwenImage21`、`VAELoader`、`RH_Screenwriter`、`SaveImage`、`VAEDecode`、`WujiImagePrompt`、`ClownsharKSampler_Beta`、`WujiPromptEditor`、`UNETLoader`、`WujiUpscaler2`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、ClownsharKSampler_Beta、WujiUpscaler2

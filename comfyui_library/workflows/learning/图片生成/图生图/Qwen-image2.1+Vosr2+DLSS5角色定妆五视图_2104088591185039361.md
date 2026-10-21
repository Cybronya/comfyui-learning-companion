---
key: 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆五视图_2104088591185039361.json
name: Qwen-image2.1+Vosr2+DLSS5角色定妆五视图_2104088591185039361
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆五视图_2104088591185039361.json
hash: 01ff7cd9f3b82994
coverage: 0.875
learned_at: 2026-10-21 00:43:23
nodes: [QwenImage21SageAttentionT8, ManualSigmas, easy showAnything, SaveImage, ClownsharKSampler_Beta, VAEDecode, UNETLoader, WujiUpscaler2, VAELoader, CLIPLoader, RH_Screenwriter, TextEncodeQwenImage21, LoadImage, WujiImagePrompt, PrimitiveStringMultiline, WujiPromptEditor]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": 1, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "bong_tangent"}
---

# 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆五视图_2104088591185039361.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆五视图_2104088591185039361.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `QwenImage21SageAttentionT8`
- `ManualSigmas`
- `easy showAnything`
- `SaveImage`
- `ClownsharKSampler_Beta` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `WujiUpscaler2`
- `VAELoader`
- `CLIPLoader`
- `RH_Screenwriter`
- `TextEncodeQwenImage21`
- `LoadImage`
- `WujiImagePrompt`
- `PrimitiveStringMultiline`
- `WujiPromptEditor`

## 关键参数

- `seed` = `0.5`
- `steps` = `bong_tangent`
- `cfg` = `8`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`QwenImage21SageAttentionT8`、`ManualSigmas`、`SaveImage`、`ClownsharKSampler_Beta`、`VAEDecode`、`UNETLoader`、`WujiUpscaler2`、`VAELoader`、`CLIPLoader`、`RH_Screenwriter`、`TextEncodeQwenImage21`、`LoadImage`、`WujiImagePrompt`、`WujiPromptEditor`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、ClownsharKSampler_Beta、WujiUpscaler2

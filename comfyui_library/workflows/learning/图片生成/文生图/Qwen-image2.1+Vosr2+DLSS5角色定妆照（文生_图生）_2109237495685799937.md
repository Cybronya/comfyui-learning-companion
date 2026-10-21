---
key: 图片生成/文生图/Qwen-image2.1+Vosr2+DLSS5角色定妆照（文生_图生）_2109237495685799937.json
name: Qwen-image2.1+Vosr2+DLSS5角色定妆照（文生_图生）_2109237495685799937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-image2.1+Vosr2+DLSS5角色定妆照（文生_图生）_2109237495685799937.json
hash: 998c8af8c5cd2e52
coverage: 0.882353
learned_at: 2026-10-21 02:54:38
nodes: [CLIPLoader, QwenImage21SageAttentionT8, ManualSigmas, LoadImage, WujiPromptEditor, TextEncodeQwenImage21, VAELoader, RH_Screenwriter, EmptyLatentImage, easy showAnything, SaveImage, VAEDecode, WujiUpscaler2, WujiImagePrompt, ClownsharKSampler_Beta, UNETLoader, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": 1, "height": 904, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "bong_tangent", "width": 1560}
---

# 图片生成/文生图/Qwen-image2.1+Vosr2+DLSS5角色定妆照（文生_图生）_2109237495685799937.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-image2.1+Vosr2+DLSS5角色定妆照（文生_图生）_2109237495685799937.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `CLIPLoader`
- `QwenImage21SageAttentionT8`
- `ManualSigmas`
- `LoadImage`
- `WujiPromptEditor`
- `TextEncodeQwenImage21`
- `VAELoader`
- `RH_Screenwriter`
- `EmptyLatentImage` ★核心
- `easy showAnything`
- `SaveImage`
- `VAEDecode` ★核心
- `WujiUpscaler2`
- `WujiImagePrompt`
- `ClownsharKSampler_Beta` ★核心
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1560`
- `height` = `904`
- `batch_size` = `1`
- `seed` = `0.5`
- `steps` = `bong_tangent`
- `cfg` = `8`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`CLIPLoader`、`QwenImage21SageAttentionT8`、`ManualSigmas`、`LoadImage`、`WujiPromptEditor`、`TextEncodeQwenImage21`、`VAELoader`、`RH_Screenwriter`、`EmptyLatentImage`、`SaveImage`、`VAEDecode`、`WujiUpscaler2`、`WujiImagePrompt`、`ClownsharKSampler_Beta`、`UNETLoader`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader、ClownsharKSampler_Beta

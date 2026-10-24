---
key: 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5影楼写真九宫格_2111712714950270978.json
name: Qwen-image2.1+Vosr2+DLSS5影楼写真九宫格_2111712714950270978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5影楼写真九宫格_2111712714950270978.json
hash: ba44d746476fc95f
coverage: 0.842105
learned_at: 2026-10-23 11:18:22
nodes: [ManualSigmas, RH_Screenwriter, easy showAnything, ClownsharKSampler_Beta, WujiUpscaler2, PrimitiveStringMultiline, LoadImage, UNETLoader, CLIPLoader, VAELoader, ImageScaleToTotalPixels, QwenImage21SageAttentionT8, TextEncodeQwenImage21, AutoCropFaces, WujiPromptEditor, SaveImage, VAEDecode, PreviewImage, WujiImagePrompt]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": 1, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "bong_tangent"}
---

# 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5影楼写真九宫格_2111712714950270978.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5影楼写真九宫格_2111712714950270978.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `ManualSigmas`
- `RH_Screenwriter`
- `easy showAnything`
- `ClownsharKSampler_Beta` ★核心
- `WujiUpscaler2`
- `PrimitiveStringMultiline`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `QwenImage21SageAttentionT8`
- `TextEncodeQwenImage21`
- `AutoCropFaces`
- `WujiPromptEditor`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `WujiImagePrompt`

## 关键参数

- `seed` = `0.5`
- `steps` = `bong_tangent`
- `cfg` = `8`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `1`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`ManualSigmas`、`RH_Screenwriter`、`ClownsharKSampler_Beta`、`WujiUpscaler2`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ImageScaleToTotalPixels`、`QwenImage21SageAttentionT8`、`TextEncodeQwenImage21`、`AutoCropFaces`、`WujiPromptEditor`、`SaveImage`、`VAEDecode`、`WujiImagePrompt`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、ClownsharKSampler_Beta、WujiUpscaler2

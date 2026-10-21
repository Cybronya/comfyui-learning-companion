---
key: 图片生成/图生图/Qwen-image2.1、image2.5二合一，多参海报生成器（文生、多图生均可）_2107839506576666626.json
name: Qwen-image2.1、image2.5二合一，多参海报生成器（文生、多图生均可）_2107839506576666626
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1、image2.5二合一，多参海报生成器（文生、多图生均可）_2107839506576666626.json
hash: 722022671650fdd4
coverage: 0.8
learned_at: 2026-10-21 00:43:28
nodes: [SaveImage, SaveImage, VAEDecode, PreviewAny, CLIPLoader, LoadImage, LoadImage, LoadImage, Fast Groups Muter (rgthree), ManualSigmas, QwenImage21SageAttentionT8, PrimitiveStringMultiline, RH_RhartImageG25SunburstImageToImage, ClownsharKSampler_Beta, QwenImage21EditTextEncode_EditUtils, VAELoader, ConditioningZeroOut, RH_Screenwriter, WujiImagePrompt, Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), UNETLoader, WujiUpscaler2, WujiCleaner, WujiPromptEditor]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": 1, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "bong_tangent"}
---

# 图片生成/图生图/Qwen-image2.1、image2.5二合一，多参海报生成器（文生、多图生均可）_2107839506576666626.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1、image2.5二合一，多参海报生成器（文生、多图生均可）_2107839506576666626.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewAny`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `ManualSigmas`
- `QwenImage21SageAttentionT8`
- `PrimitiveStringMultiline`
- `RH_RhartImageG25SunburstImageToImage`
- `ClownsharKSampler_Beta` ★核心
- `QwenImage21EditTextEncode_EditUtils`
- `VAELoader`
- `ConditioningZeroOut`
- `RH_Screenwriter`
- `WujiImagePrompt`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `UNETLoader` ★核心
- `WujiUpscaler2`
- `WujiCleaner`
- `WujiPromptEditor`

## 关键参数

- `seed` = `0.5`
- `steps` = `bong_tangent`
- `cfg` = `8`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `1`

## 知识

覆盖率 **80%**（20/25）

**有卡**：`SaveImage`、`VAEDecode`、`CLIPLoader`、`LoadImage`、`ManualSigmas`、`QwenImage21SageAttentionT8`、`RH_RhartImageG25SunburstImageToImage`、`ClownsharKSampler_Beta`、`QwenImage21EditTextEncode_EditUtils`、`VAELoader`、`ConditioningZeroOut`、`RH_Screenwriter`、`WujiImagePrompt`、`UNETLoader`、`WujiUpscaler2`、`WujiCleaner`、`WujiPromptEditor`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、ClownsharKSampler_Beta、QwenImage21EditTextEncode_EditUtils

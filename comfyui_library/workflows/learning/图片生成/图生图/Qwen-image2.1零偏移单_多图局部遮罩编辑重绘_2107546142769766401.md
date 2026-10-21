---
key: 图片生成/图生图/Qwen-image2.1零偏移单_多图局部遮罩编辑重绘_2107546142769766401.json
name: Qwen-image2.1零偏移单_多图局部遮罩编辑重绘_2107546142769766401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1零偏移单_多图局部遮罩编辑重绘_2107546142769766401.json
hash: d3f5c734cc511e3c
coverage: 0.842105
learned_at: 2026-10-21 00:43:31
nodes: [VAELoader, Image Comparer (rgthree), Note, SaveImage, VAEDecode, WujiCleaner, CLIPLoader, LoadImage, PrimitiveStringMultiline, UNETLoader, LoadImage, WujiUpscaler2, QwenImage21SageAttentionT8, QwenImage21EditTextEncode_EditUtils, ConditioningZeroOut, WujiImagePrompt, RH_Screenwriter, ManualSigmas, ClownsharKSampler_Beta]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": 1, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "bong_tangent"}
---

# 图片生成/图生图/Qwen-image2.1零偏移单_多图局部遮罩编辑重绘_2107546142769766401.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1零偏移单_多图局部遮罩编辑重绘_2107546142769766401.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `VAELoader`
- `Image Comparer (rgthree)`
- `Note`
- `SaveImage`
- `VAEDecode` ★核心
- `WujiCleaner`
- `CLIPLoader`
- `LoadImage`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `LoadImage`
- `WujiUpscaler2`
- `QwenImage21SageAttentionT8`
- `QwenImage21EditTextEncode_EditUtils`
- `ConditioningZeroOut`
- `WujiImagePrompt`
- `RH_Screenwriter`
- `ManualSigmas`
- `ClownsharKSampler_Beta` ★核心

## 关键参数

- `seed` = `0.5`
- `steps` = `bong_tangent`
- `cfg` = `8`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `1`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`VAELoader`、`SaveImage`、`VAEDecode`、`WujiCleaner`、`CLIPLoader`、`LoadImage`、`UNETLoader`、`WujiUpscaler2`、`QwenImage21SageAttentionT8`、`QwenImage21EditTextEncode_EditUtils`、`ConditioningZeroOut`、`WujiImagePrompt`、`RH_Screenwriter`、`ManualSigmas`、`ClownsharKSampler_Beta`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、ClownsharKSampler_Beta、QwenImage21EditTextEncode_EditUtils

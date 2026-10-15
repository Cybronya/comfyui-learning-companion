---
key: 图片生成/图生图/Qwen Image 2.1 文生、图像编辑一体化工作台_2105131610982141954.json
name: Qwen Image 2.1 文生、图像编辑一体化工作台_2105131610982141954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 文生、图像编辑一体化工作台_2105131610982141954.json
hash: c1d661ba79be1dd4
coverage: 0.657143
learned_at: 2026-10-15 22:25:11
nodes: [LoadImage, LoadImage, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, SetNode, VAEDecode, CLIPLoader, VAELoader, Reroute, LoadImage, LoadImage, UNETLoader, GoohaiRouteBlocker, 忽略多组孤海, QwenImage21SageAttentionT8, GetNode, KSampler, GoohaiRouteBlocker, 孤海注释, ShowText|pysssss, Image Comparer (rgthree), QwenImage21BlockCacheT8, QwenImage21SpectrumT8, RestoreQwenImage21GH, TextEncodeQwenImage21GH, LoadImageGoohai, SaveImage, GoohaiRatioAndResolution, DF_Text_Box, QwenImagePromptOptimizer, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 721893050101110, "steps": 30}
---

# 图片生成/图生图/Qwen Image 2.1 文生、图像编辑一体化工作台_2105131610982141954.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 文生、图像编辑一体化工作台_2105131610982141954.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `LoadImage`
- `LoadImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `SetNode`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Reroute`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `GoohaiRouteBlocker`
- `忽略多组孤海`
- `QwenImage21SageAttentionT8`
- `GetNode`
- `KSampler` ★核心
- `GoohaiRouteBlocker`
- `孤海注释`
- `ShowText|pysssss`
- `Image Comparer (rgthree)`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `RestoreQwenImage21GH`
- `TextEncodeQwenImage21GH`
- `LoadImageGoohai`
- `SaveImage`
- `GoohaiRatioAndResolution`
- `DF_Text_Box`
- `QwenImagePromptOptimizer`
- `LoadImage`

## 关键参数

- `seed` = `721893050101110`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **66%**（23/35）

**有卡**：`LoadImage`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`GoohaiRouteBlocker`、`忽略多组孤海`、`QwenImage21SageAttentionT8`、`KSampler`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`RestoreQwenImage21GH`、`TextEncodeQwenImage21GH`、`LoadImageGoohai`、`SaveImage`、`GoohaiRatioAndResolution`、`DF_Text_Box`、`QwenImagePromptOptimizer`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImage21GH、QwenImagePromptOptimizer

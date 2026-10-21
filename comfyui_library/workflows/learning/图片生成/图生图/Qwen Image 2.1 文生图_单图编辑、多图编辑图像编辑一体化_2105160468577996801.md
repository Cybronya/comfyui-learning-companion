---
key: 图片生成/图生图/Qwen Image 2.1 文生图_单图编辑、多图编辑图像编辑一体化_2105160468577996801.json
name: Qwen Image 2.1 文生图_单图编辑、多图编辑图像编辑一体化_2105160468577996801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 文生图_单图编辑、多图编辑图像编辑一体化_2105160468577996801.json
hash: 700198a970fc20fd
coverage: 0.657143
learned_at: 2026-10-21 00:42:15
nodes: [LoadImage, LoadImage, Reroute, LoadImage, Reroute, Reroute, Reroute, Reroute, Reroute, SetNode, VAEDecode, CLIPLoader, VAELoader, Reroute, LoadImage, LoadImage, UNETLoader, GoohaiRouteBlocker, 忽略多组孤海, QwenImage21SageAttentionT8, GetNode, KSampler, GoohaiRouteBlocker, ShowText|pysssss, Image Comparer (rgthree), QwenImage21BlockCacheT8, QwenImage21SpectrumT8, RestoreQwenImage21GH, TextEncodeQwenImage21GH, SaveImage, 孤海注释, QwenImagePromptOptimizer, LoadImageGoohai, GoohaiRatioAndResolution, DF_Text_Box]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 953816852336492, "steps": 30}
---

# 图片生成/图生图/Qwen Image 2.1 文生图_单图编辑、多图编辑图像编辑一体化_2105160468577996801.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 文生图_单图编辑、多图编辑图像编辑一体化_2105160468577996801.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `LoadImage`
- `LoadImage`
- `Reroute`
- `LoadImage`
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
- `ShowText|pysssss`
- `Image Comparer (rgthree)`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `RestoreQwenImage21GH`
- `TextEncodeQwenImage21GH`
- `SaveImage`
- `孤海注释`
- `QwenImagePromptOptimizer`
- `LoadImageGoohai`
- `GoohaiRatioAndResolution`
- `DF_Text_Box`

## 关键参数

- `seed` = `953816852336492`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **66%**（23/35）

**有卡**：`LoadImage`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`GoohaiRouteBlocker`、`忽略多组孤海`、`QwenImage21SageAttentionT8`、`KSampler`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`RestoreQwenImage21GH`、`TextEncodeQwenImage21GH`、`SaveImage`、`QwenImagePromptOptimizer`、`LoadImageGoohai`、`GoohaiRatioAndResolution`、`DF_Text_Box`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImage21GH、QwenImagePromptOptimizer

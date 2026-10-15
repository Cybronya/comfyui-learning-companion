---
key: 图片生成/文生图/Qwen Image 2.1 文生、图像编辑一体化_2103270694288183297.json
name: Qwen Image 2.1 文生、图像编辑一体化_2103270694288183297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生、图像编辑一体化_2103270694288183297.json
hash: fe204bc38bdd19ac
coverage: 0.628571
learned_at: 2026-10-10 21:27:39
nodes: [LoadImage, LoadImage, Reroute, LoadImage, Reroute, Reroute, Reroute, Reroute, Reroute, SetNode, VAEDecode, CLIPLoader, VAELoader, Reroute, LoadImage, LoadImage, UNETLoader, GoohaiRouteBlocker, GoohaiRatioAndResolution, 忽略多组孤海, QwenImage21SageAttentionT8, GetNode, KSampler, GoohaiRouteBlocker, 孤海注释, ShowText|pysssss, Image Comparer (rgthree), QwenImagePromptOptimizer, DF_Text_Box, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, RestoreQwenImage21GH, TextEncodeQwenImage21GH, LoadImageGoohai, SaveImage]
patterns: []
missing: [忽略多组孤海]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 746237649349839, "steps": 30}
discoveries: [次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen Image 2.1 文生、图像编辑一体化_2103270694288183297.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生、图像编辑一体化_2103270694288183297.json`

## 结构

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
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
- `Reroute`
- `LoadImage`
- `LoadImage`
- `UNETLoader`
- `GoohaiRouteBlocker`
- `GoohaiRatioAndResolution`
- `忽略多组孤海`
- `QwenImage21SageAttentionT8`
- `GetNode`
- `KSampler`
- `GoohaiRouteBlocker`
- `孤海注释`
- `ShowText|pysssss`
- `Image Comparer (rgthree)`
- `QwenImagePromptOptimizer`
- `DF_Text_Box`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `RestoreQwenImage21GH`
- `TextEncodeQwenImage21GH`
- `LoadImageGoohai`
- `SaveImage`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `746237649349839`
- `steps` = `30`

## 知识

覆盖率 **63%**（22/35）

**有卡**：`LoadImage`、`Reroute`、`SetNode`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`GoohaiRouteBlocker`、`GoohaiRatioAndResolution`、`忽略多组孤海`、`QwenImage21SageAttentionT8`、`GetNode`

**缺卡**（1）：`忽略多组孤海`

## 学习发现

- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识

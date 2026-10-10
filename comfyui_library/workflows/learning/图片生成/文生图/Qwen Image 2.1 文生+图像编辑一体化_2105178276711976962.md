---
key: Qwen Image 2.1 文生+图像编辑一体化_2105178276711976962.json
name: Qwen Image 2.1 文生+图像编辑一体化_2105178276711976962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生+图像编辑一体化_2105178276711976962.json
hash: f7d97a2a41864706
coverage: 0.785714
learned_at: 2026-10-10 20:58:51
nodes: [孤海注释, CLIPLoader, VAELoader, QwenImage21SpectrumT8, TextEncodeQwenImage21GH, KSampler, VAEDecode, RestoreQwenImage21GH, SaveImage, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, UNETLoader, GetNode, Image Comparer (rgthree), GoohaiRouteBlocker, GoohaiRatioAndResolution, ShowText|pysssss, QwenImagePromptOptimizer, 忽略多组孤海, DF_Text_Box, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SetNode, GoohaiRouteBlocker, LoadImage]
patterns: []
missing: [忽略多组孤海]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 58762643915688, "steps": 30}
discoveries: [次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识]
---

# Qwen Image 2.1 文生+图像编辑一体化_2105178276711976962.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生+图像编辑一体化_2105178276711976962.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `孤海注释`
- `CLIPLoader`
- `VAELoader`
- `QwenImage21SpectrumT8`
- `TextEncodeQwenImage21GH`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `RestoreQwenImage21GH`
- `SaveImage`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `UNETLoader` ★核心
- `GetNode`
- `Image Comparer (rgthree)`
- `GoohaiRouteBlocker`
- `GoohaiRatioAndResolution`
- `ShowText|pysssss`
- `QwenImagePromptOptimizer`
- `忽略多组孤海`
- `DF_Text_Box`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `GoohaiRouteBlocker`
- `LoadImage`

## 关键参数

- `seed` = `58762643915688`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（22/28）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21SpectrumT8`、`TextEncodeQwenImage21GH`、`KSampler`、`VAEDecode`、`RestoreQwenImage21GH`、`SaveImage`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`UNETLoader`、`GoohaiRouteBlocker`、`GoohaiRatioAndResolution`、`QwenImagePromptOptimizer`、`DF_Text_Box`、`LoadImage`

**缺卡**（1）：`忽略多组孤海`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImage21GH、QwenImagePromptOptimizer

## 学习发现

- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识

---
key: 图片生成/图生图/AI图像创作丨Qwen Image 2.1丨文生图 _ 图像编辑_2112739173701607425.json
name: AI图像创作丨Qwen Image 2.1丨文生图 _ 图像编辑_2112739173701607425
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/AI图像创作丨Qwen Image 2.1丨文生图 _ 图像编辑_2112739173701607425.json
hash: 0010797a87e216d0
coverage: 0.702703
learned_at: 2026-10-23 10:50:31
nodes: [LoadImage, LoadImage, Reroute, LoadImage, Reroute, Reroute, Reroute, Reroute, Reroute, SetNode, VAEDecode, CLIPLoader, Reroute, LoadImage, LoadImage, GoohaiRatioAndResolution, 忽略多组孤海, QwenImage21SageAttentionT8, GetNode, KSampler, Image Comparer (rgthree), DF_Text_Box, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, RestoreQwenImage21GH, LoadImageGoohai, VAELoader, GoohaiRouteBlocker, UNETLoader, easy ifElse, GoohaiAnyExists, LoraLoaderModelOnly, GoohaiRouteBlocker, TextEncodeQwenImage21GH, QwenImagePromptOptimizer, GoohaiDisplayAny, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1005966062794466, "steps": 30}
---

# 图片生成/图生图/AI图像创作丨Qwen Image 2.1丨文生图 _ 图像编辑_2112739173701607425.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/AI图像创作丨Qwen Image 2.1丨文生图 _ 图像编辑_2112739173701607425.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
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
- `Reroute`
- `LoadImage`
- `LoadImage`
- `GoohaiRatioAndResolution`
- `忽略多组孤海`
- `QwenImage21SageAttentionT8`
- `GetNode`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `DF_Text_Box`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `RestoreQwenImage21GH`
- `LoadImageGoohai`
- `VAELoader`
- `GoohaiRouteBlocker`
- `UNETLoader` ★核心
- `easy ifElse`
- `GoohaiAnyExists`
- `LoraLoaderModelOnly` ★核心
- `GoohaiRouteBlocker`
- `TextEncodeQwenImage21GH`
- `QwenImagePromptOptimizer`
- `GoohaiDisplayAny`
- `SaveImage`

## 关键参数

- `seed` = `1005966062794466`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **70%**（26/37）

**有卡**：`LoadImage`、`VAEDecode`、`CLIPLoader`、`GoohaiRatioAndResolution`、`忽略多组孤海`、`QwenImage21SageAttentionT8`、`KSampler`、`DF_Text_Box`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`RestoreQwenImage21GH`、`LoadImageGoohai`、`VAELoader`、`GoohaiRouteBlocker`、`UNETLoader`、`GoohaiAnyExists`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21GH`、`QwenImagePromptOptimizer`、`GoohaiDisplayAny`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImage21GH

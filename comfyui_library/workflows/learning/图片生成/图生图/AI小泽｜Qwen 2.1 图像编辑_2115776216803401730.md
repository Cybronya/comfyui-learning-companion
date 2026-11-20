---
key: 图片生成/图生图/AI小泽｜Qwen 2.1 图像编辑_2115776216803401730.json
name: AI小泽｜Qwen 2.1 图像编辑_2115776216803401730
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/AI小泽｜Qwen 2.1 图像编辑_2115776216803401730.json
hash: e3fcb9027faeeebb
coverage: 0.684211
learned_at: 2026-10-30 17:49:23
nodes: [LoadImage, LoadImage, Reroute, LoadImage, Reroute, Reroute, Reroute, Reroute, Reroute, SetNode, VAEDecode, CLIPLoader, Reroute, LoadImage, LoadImage, GoohaiRatioAndResolution, 忽略多组孤海, QwenImage21SageAttentionT8, GetNode, KSampler, 孤海注释, Image Comparer (rgthree), DF_Text_Box, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, RestoreQwenImage21GH, VAELoader, GoohaiRouteBlocker, UNETLoader, easy ifElse, GoohaiAnyExists, LoraLoaderModelOnly, GoohaiRouteBlocker, TextEncodeQwenImage21GH, QwenImagePromptOptimizer, GoohaiDisplayAny, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 176136635118004, "steps": 30}
---

# 图片生成/图生图/AI小泽｜Qwen 2.1 图像编辑_2115776216803401730.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/AI小泽｜Qwen 2.1 图像编辑_2115776216803401730.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
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
- `孤海注释`
- `Image Comparer (rgthree)`
- `DF_Text_Box`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `RestoreQwenImage21GH`
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
- `LoadImage`

## 关键参数

- `seed` = `176136635118004`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **68%**（26/38）

**有卡**：`LoadImage`、`VAEDecode`、`CLIPLoader`、`GoohaiRatioAndResolution`、`忽略多组孤海`、`QwenImage21SageAttentionT8`、`KSampler`、`DF_Text_Box`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`RestoreQwenImage21GH`、`VAELoader`、`GoohaiRouteBlocker`、`UNETLoader`、`GoohaiAnyExists`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21GH`、`QwenImagePromptOptimizer`、`GoohaiDisplayAny`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImage21GH

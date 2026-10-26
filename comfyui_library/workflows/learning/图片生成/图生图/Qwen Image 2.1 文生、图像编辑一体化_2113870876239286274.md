---
key: 图片生成/图生图/Qwen Image 2.1 文生、图像编辑一体化_2113870876239286274.json
name: Qwen Image 2.1 文生、图像编辑一体化_2113870876239286274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 文生、图像编辑一体化_2113870876239286274.json
hash: d70de245b507739d
coverage: 0.684211
learned_at: 2026-10-26 22:02:59
nodes: [LoadImage, LoadImage, LoadImage, Reroute, Reroute, Reroute, Reroute, Reroute, SetNode, VAEDecode, CLIPLoader, LoadImage, LoadImage, 忽略多组孤海, QwenImage21SageAttentionT8, GetNode, KSampler, 孤海注释, Image Comparer (rgthree), RestoreQwenImage21GH, VAELoader, GoohaiRouteBlocker, UNETLoader, easy ifElse, GoohaiAnyExists, GoohaiRouteBlocker, TextEncodeQwenImage21GH, QwenImagePromptOptimizer, GoohaiDisplayAny, SaveImage, DF_Text_Box, Reroute, Reroute, LoraLoaderModelOnly, GoohaiRatioAndResolution, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, LoadImageGoohai]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 660805466069410, "steps": 30}
---

# 图片生成/图生图/Qwen Image 2.1 文生、图像编辑一体化_2113870876239286274.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 文生、图像编辑一体化_2113870876239286274.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `SetNode`
- `VAEDecode` ★核心
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `忽略多组孤海`
- `QwenImage21SageAttentionT8`
- `GetNode`
- `KSampler` ★核心
- `孤海注释`
- `Image Comparer (rgthree)`
- `RestoreQwenImage21GH`
- `VAELoader`
- `GoohaiRouteBlocker`
- `UNETLoader` ★核心
- `easy ifElse`
- `GoohaiAnyExists`
- `GoohaiRouteBlocker`
- `TextEncodeQwenImage21GH`
- `QwenImagePromptOptimizer`
- `GoohaiDisplayAny`
- `SaveImage`
- `DF_Text_Box`
- `Reroute`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `GoohaiRatioAndResolution`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `LoadImageGoohai`

## 关键参数

- `seed` = `660805466069410`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **68%**（26/38）

**有卡**：`LoadImage`、`VAEDecode`、`CLIPLoader`、`忽略多组孤海`、`QwenImage21SageAttentionT8`、`KSampler`、`RestoreQwenImage21GH`、`VAELoader`、`GoohaiRouteBlocker`、`UNETLoader`、`GoohaiAnyExists`、`TextEncodeQwenImage21GH`、`QwenImagePromptOptimizer`、`GoohaiDisplayAny`、`SaveImage`、`DF_Text_Box`、`LoraLoaderModelOnly`、`GoohaiRatioAndResolution`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`LoadImageGoohai`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImage21GH

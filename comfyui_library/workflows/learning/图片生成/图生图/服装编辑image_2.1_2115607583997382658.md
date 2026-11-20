---
key: 图片生成/图生图/服装编辑image_2.1_2115607583997382658.json
name: 服装编辑image_2.1_2115607583997382658
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/服装编辑image_2.1_2115607583997382658.json
hash: 9c32e893899a3ede
coverage: 0.684211
learned_at: 2026-10-30 17:53:26
nodes: [LoadImage, LoadImage, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, SetNode, VAEDecode, CLIPLoader, VAELoader, Reroute, LoadImage, LoadImage, GoohaiRouteBlocker, TextEncodeQwenImage21GH, GoohaiRatioAndResolution, 忽略多组孤海, QwenImage21SageAttentionT8, GetNode, RestoreQwenImage21GH, KSampler, GoohaiRouteBlocker, 孤海注释, Image Comparer (rgthree), QwenImage21BlockCacheT8, QwenImage21SpectrumT8, LoadImage, DF_Text_Box, QwenImagePromptOptimizer, LoadImageGoohai, UNETLoader, SaveImage, LoraLoaderModelOnly, GoohaiDisplayAny, easy ifElse, GoohaiAnyExists]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 975699917493812, "steps": 30}
---

# 图片生成/图生图/服装编辑image_2.1_2115607583997382658.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/服装编辑image_2.1_2115607583997382658.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
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
- `GoohaiRouteBlocker`
- `TextEncodeQwenImage21GH`
- `GoohaiRatioAndResolution`
- `忽略多组孤海`
- `QwenImage21SageAttentionT8`
- `GetNode`
- `RestoreQwenImage21GH`
- `KSampler` ★核心
- `GoohaiRouteBlocker`
- `孤海注释`
- `Image Comparer (rgthree)`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `LoadImage`
- `DF_Text_Box`
- `QwenImagePromptOptimizer`
- `LoadImageGoohai`
- `UNETLoader` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `GoohaiDisplayAny`
- `easy ifElse`
- `GoohaiAnyExists`

## 关键参数

- `seed` = `975699917493812`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **68%**（26/38）

**有卡**：`LoadImage`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`GoohaiRouteBlocker`、`TextEncodeQwenImage21GH`、`GoohaiRatioAndResolution`、`忽略多组孤海`、`QwenImage21SageAttentionT8`、`RestoreQwenImage21GH`、`KSampler`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`DF_Text_Box`、`QwenImagePromptOptimizer`、`LoadImageGoohai`、`UNETLoader`、`SaveImage`、`LoraLoaderModelOnly`、`GoohaiDisplayAny`、`GoohaiAnyExists`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImage21GH

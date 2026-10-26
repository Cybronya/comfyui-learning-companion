---
key: 图片生成/图生图/Qwen Image 2.1 图像编辑API测试_2113833350678011906.json
name: Qwen Image 2.1 图像编辑API测试_2113833350678011906
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 图像编辑API测试_2113833350678011906.json
hash: 185e83a1994b38e5
coverage: 0.692308
learned_at: 2026-10-26 22:02:58
nodes: [LoadImage, LoadImage, Reroute, LoadImage, Reroute, Reroute, Reroute, Reroute, Reroute, SetNode, VAEDecode, CLIPLoader, Reroute, LoadImage, LoadImage, 忽略多组孤海, QwenImage21SageAttentionT8, GetNode, 孤海注释, Image Comparer (rgthree), LoadImageGoohai, VAELoader, UNETLoader, GoohaiRouteBlocker, GoohaiDisplayAny, SaveImage, RestoreQwenImage21GH, QwenImage21SpectrumT8, QwenImage21BlockCacheT8, TextEncodeQwenImage21GH, LoraLoaderModelOnly, QwenImagePromptOptimizer, GoohaiRouteBlocker, GoohaiAnyExists, easy ifElse, KSampler, LoraLoaderModelOnly, DF_Text_Box, GoohaiRatioAndResolution]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 909209092588123, "steps": 30}
---

# 图片生成/图生图/Qwen Image 2.1 图像编辑API测试_2113833350678011906.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 图像编辑API测试_2113833350678011906.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
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
- `忽略多组孤海`
- `QwenImage21SageAttentionT8`
- `GetNode`
- `孤海注释`
- `Image Comparer (rgthree)`
- `LoadImageGoohai`
- `VAELoader`
- `UNETLoader` ★核心
- `GoohaiRouteBlocker`
- `GoohaiDisplayAny`
- `SaveImage`
- `RestoreQwenImage21GH`
- `QwenImage21SpectrumT8`
- `QwenImage21BlockCacheT8`
- `TextEncodeQwenImage21GH`
- `LoraLoaderModelOnly` ★核心
- `QwenImagePromptOptimizer`
- `GoohaiRouteBlocker`
- `GoohaiAnyExists`
- `easy ifElse`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `DF_Text_Box`
- `GoohaiRatioAndResolution`

## 关键参数

- `seed` = `909209092588123`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **69%**（27/39）

**有卡**：`LoadImage`、`VAEDecode`、`CLIPLoader`、`忽略多组孤海`、`QwenImage21SageAttentionT8`、`LoadImageGoohai`、`VAELoader`、`UNETLoader`、`GoohaiRouteBlocker`、`GoohaiDisplayAny`、`SaveImage`、`RestoreQwenImage21GH`、`QwenImage21SpectrumT8`、`QwenImage21BlockCacheT8`、`TextEncodeQwenImage21GH`、`LoraLoaderModelOnly`、`QwenImagePromptOptimizer`、`GoohaiAnyExists`、`KSampler`、`DF_Text_Box`、`GoohaiRatioAndResolution`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImage21GH

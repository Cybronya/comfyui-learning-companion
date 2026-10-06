---
key: 图片生成/反推提示词/Qwen Image 2.1 文生、图像编辑一体化_2103270694288183297.json
name: Qwen Image 2.1 文生、图像编辑一体化_2103270694288183297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen Image 2.1 文生、图像编辑一体化_2103270694288183297.json
hash: fe204bc38bdd19ac
coverage: 0.314286
learned_at: 2026-10-06 21:36:19
nodes: [LoadImage, LoadImage, Reroute, LoadImage, Reroute, Reroute, Reroute, Reroute, Reroute, SetNode, VAEDecode, CLIPLoader, VAELoader, Reroute, LoadImage, LoadImage, UNETLoader, GoohaiRouteBlocker, GoohaiRatioAndResolution, 忽略多组孤海, QwenImage21SageAttentionT8, GetNode, KSampler, GoohaiRouteBlocker, 孤海注释, ShowText|pysssss, Image Comparer (rgthree), QwenImagePromptOptimizer, DF_Text_Box, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, RestoreQwenImage21GH, TextEncodeQwenImage21GH, LoadImageGoohai, SaveImage]
patterns: []
missing: [DF_Text_Box, GoohaiRouteBlocker, GoohaiRouteBlocker, LoadImageGoohai, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, RestoreQwenImage21GH, 忽略多组孤海, GoohaiRatioAndResolution, QwenImagePromptOptimizer, TextEncodeQwenImage21GH]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 746237649349839, "steps": 30}
discoveries: [次要节点 `DF_Text_Box` 知识库中没有该节点类型的任何知识, 次要节点 `GoohaiRouteBlocker` 知识库中没有该节点类型的任何知识, 次要节点 `GoohaiRouteBlocker` 知识库中没有该节点类型的任何知识, 次要节点 `LoadImageGoohai` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21BlockCacheT8` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21SageAttentionT8` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21SpectrumT8` 知识库中没有该节点类型的任何知识, 次要节点 `RestoreQwenImage21GH` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `GoohaiRatioAndResolution` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `QwenImagePromptOptimizer` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `TextEncodeQwenImage21GH` 仅有 VAE 的通用知识，没有该节点自己的说明]
---

# 图片生成/反推提示词/Qwen Image 2.1 文生、图像编辑一体化_2103270694288183297.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen Image 2.1 文生、图像编辑一体化_2103270694288183297.json`

## 结构

**生成流程**：Model → Sampling → Decode → Output → Other

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
- `GoohaiRatioAndResolution`
- `忽略多组孤海`
- `QwenImage21SageAttentionT8`
- `GetNode`
- `KSampler` ★核心
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

- `seed` = `746237649349839`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **31%**（11/35）

**有卡**：`LoadImage`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSampler`、`SaveImage`

**缺卡**（12）：`DF_Text_Box`、`GoohaiRouteBlocker`、`GoohaiRouteBlocker`、`LoadImageGoohai`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`QwenImage21SpectrumT8`、`RestoreQwenImage21GH`、`忽略多组孤海`、`GoohaiRatioAndResolution`、`QwenImagePromptOptimizer`、`TextEncodeQwenImage21GH`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、SaveImage、sd15-t2i-basic

## 学习发现

- 次要节点 `DF_Text_Box` 知识库中没有该节点类型的任何知识
- 次要节点 `GoohaiRouteBlocker` 知识库中没有该节点类型的任何知识
- 次要节点 `GoohaiRouteBlocker` 知识库中没有该节点类型的任何知识
- 次要节点 `LoadImageGoohai` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21BlockCacheT8` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21SageAttentionT8` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21SpectrumT8` 知识库中没有该节点类型的任何知识
- 次要节点 `RestoreQwenImage21GH` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `GoohaiRatioAndResolution` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `QwenImagePromptOptimizer` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `TextEncodeQwenImage21GH` 仅有 VAE 的通用知识，没有该节点自己的说明

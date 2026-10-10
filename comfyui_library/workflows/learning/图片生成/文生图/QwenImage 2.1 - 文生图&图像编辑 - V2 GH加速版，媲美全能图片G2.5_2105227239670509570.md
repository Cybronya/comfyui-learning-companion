---
key: QwenImage 2.1 - 文生图&图像编辑 - V2 GH加速版，媲美全能图片G2.5_2105227239670509570.json
name: QwenImage 2.1 - 文生图&图像编辑 - V2 GH加速版，媲美全能图片G2.5_2105227239670509570
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QwenImage 2.1 - 文生图&图像编辑 - V2 GH加速版，媲美全能图片G2.5_2105227239670509570.json
hash: d37df278db7dd051
coverage: 0.5
learned_at: 2026-10-10 20:59:07
nodes: [LoadImage, CLIPLoader, VAELoader, CLIPTextEncode, VAEDecode, CLIPTextEncode, LatentSwitch, VAEEncode, VAELoader, CLIPLoader, ReferenceLatent, ReferenceLatent, KSamplerAdvanced, UNETLoader, ImageScaleToTotalPixels, PDIMAGE_LongerSize, SetNode, JWFloat, LoadImage, LoadImage, SetNode, SetNode, LoadImage, SetNode, SetNode, LoadImage, SetNode, GetNode, SetNode, VAEDecode, KSampler, GetNode, GetNode, GetNode, GetNode, GetNode, UNETLoader, GetNode, SetNode, GetNode, QwenImage21BlockCacheT8, GetNode, QwenImage21SpectrumT8, GoohaiRouteBlocker, TextEncodeQwenImage21GH, SetNode, GetNode, 忽略多组孤海, SaveImage, RestoreQwenImage21GH, SetNode, GetNode, GoohaiRouteBlocker, Fast Groups Bypasser (rgthree), SaveImage, QwenImagePromptOptimizer, GetNode, SetNode, GetNode, QwenImage21SageAttentionT8, GetNode, LoadImage, SetNode, FastGroupsBypassSwitch, GetNode, SetNode, CS_Preview_Any, easy showAnything, SetNode, GetNode, ShowText|pysssss, DF_Text_Box, Image Comparer (rgthree), GetNode, GetNode, PreviewImage, PreviewImage, GoohaiRatioAndResolution]
patterns: [image_to_image]
missing: [忽略多组孤海]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 735756756078566, "steps": 30}
discoveries: [次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识]
---

# QwenImage 2.1 - 文生图&图像编辑 - V2 GH加速版，媲美全能图片G2.5_2105227239670509570.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QwenImage 2.1 - 文生图&图像编辑 - V2 GH加速版，媲美全能图片G2.5_2105227239670509570.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（78 个）：
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LatentSwitch`
- `VAEEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `ReferenceLatent`
- `ReferenceLatent`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `ImageScaleToTotalPixels`
- `PDIMAGE_LongerSize`
- `SetNode`
- `JWFloat`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `QwenImage21BlockCacheT8`
- `GetNode`
- `QwenImage21SpectrumT8`
- `GoohaiRouteBlocker`
- `TextEncodeQwenImage21GH`
- `SetNode`
- `GetNode`
- `忽略多组孤海`
- `SaveImage`
- `RestoreQwenImage21GH`
- `SetNode`
- `GetNode`
- `GoohaiRouteBlocker`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `QwenImagePromptOptimizer`
- `GetNode`
- `SetNode`
- `GetNode`
- `QwenImage21SageAttentionT8`
- `GetNode`
- `LoadImage`
- `SetNode`
- `FastGroupsBypassSwitch`
- `GetNode`
- `SetNode`
- `CS_Preview_Any`
- `easy showAnything`
- `SetNode`
- `GetNode`
- `ShowText|pysssss`
- `DF_Text_Box`
- `Image Comparer (rgthree)`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `GoohaiRatioAndResolution`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `735756756078566`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **50%**（39/78）

**有卡**：`LoadImage`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`LatentSwitch`、`VAEEncode`、`ReferenceLatent`、`KSamplerAdvanced`、`UNETLoader`、`ImageScaleToTotalPixels`、`PDIMAGE_LongerSize`、`JWFloat`、`KSampler`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`GoohaiRouteBlocker`、`TextEncodeQwenImage21GH`、`SaveImage`、`RestoreQwenImage21GH`、`QwenImagePromptOptimizer`、`QwenImage21SageAttentionT8`、`FastGroupsBypassSwitch`、`CS_Preview_Any`、`DF_Text_Box`、`GoohaiRatioAndResolution`

**缺卡**（1）：`忽略多组孤海`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识

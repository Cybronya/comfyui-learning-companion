---
key: 图片生成/图生图/Qwen Image 2.1 局部编辑修改_2103026012618584066.json
name: Qwen Image 2.1 局部编辑修改_2103026012618584066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 局部编辑修改_2103026012618584066.json
hash: 5617a354ae6386f6
coverage: 0.653846
learned_at: 2026-10-10 20:48:05
nodes: [VAELoader, QwenImage21Cache, CLIPLoader, easy showAnything, Reroute, GrowMaskWithBlur, LayerUtility: CropByMask V2, GrowMaskWithBlur, LayerUtility: RestoreCropBox, ColorMatch, LayerUtility: ImageScaleRestore V2, VAEDecode, LoadImage, Image Comparer (rgthree), SaveImage, QwenPERewriteT8, LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text, TextEncodeQwenImage21, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, UNETLoader, QwenImage21SpectrumT8, KSampler, EmptyLatentImage, ComfySwitchNode]
patterns: []
missing: [LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LayerUtility: RestoreCropBox, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
discoveries: [次要节点 `LayerUtility: CropByMask V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleRestore V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: RestoreCropBox` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Qwen Image 2.1 局部编辑修改_2103026012618584066.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 局部编辑修改_2103026012618584066.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `VAELoader`
- `QwenImage21Cache`
- `CLIPLoader`
- `easy showAnything`
- `Reroute`
- `GrowMaskWithBlur`
- `LayerUtility: CropByMask V2`
- `GrowMaskWithBlur`
- `LayerUtility: RestoreCropBox`
- `ColorMatch`
- `LayerUtility: ImageScaleRestore V2`
- `VAEDecode` ★核心
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `QwenPERewriteT8`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Prompt Text`
- `TextEncodeQwenImage21`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `UNETLoader` ★核心
- `QwenImage21SpectrumT8`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`

## 关键参数

- `seed` = `19960422`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **65%**（17/26）

**有卡**：`VAELoader`、`QwenImage21Cache`、`CLIPLoader`、`GrowMaskWithBlur`、`ColorMatch`、`VAEDecode`、`LoadImage`、`SaveImage`、`QwenPERewriteT8`、`TextEncodeQwenImage21`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`UNETLoader`、`QwenImage21SpectrumT8`、`KSampler`、`EmptyLatentImage`

**缺卡**（5）：`LayerUtility: CropByMask V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleRestore V2`、`LayerUtility: RestoreCropBox`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache

## 学习发现

- 次要节点 `LayerUtility: CropByMask V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleRestore V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: RestoreCropBox` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明

---
key: Flux.1-Krea-Dev文生图&图生图_1951120800927653890.json
name: Flux.1-Krea-Dev文生图&图生图_1951120800927653890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图&图生图_1951120800927653890.json
hash: 8a631ded1921f75d
coverage: 0.516129
learned_at: 2026-10-10 20:58:36
nodes: [RepeatLatentBatch, UNETLoader, VAEEncode, BasicGuider, SamplerCustomAdvanced, RandomNoise, VAEDecode, DualCLIPLoader, VAELoader, CLIPTextEncode, EmptyLatentImage, CR SDXL Aspect Ratio, Text Concatenate, ImageScaleDownToSize, SaveImage, LoadImage, Text Multiline, Text Concatenate, WD14Tagger|pysssss, ImpactSwitch, ImpactSwitch, Note, Note, BasicScheduler, KSamplerSelect, easy showAnything, PreviewImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, Note, CR Text]
patterns: []
missing: [CR Text, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, Text Concatenate, Text Concatenate, Text Multiline, WD14Tagger|pysssss, CR SDXL Aspect Ratio]
parameters: {"batch_size": 4, "height": 1280, "width": 768}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `WD14Tagger|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明]
---

# Flux.1-Krea-Dev文生图&图生图_1951120800927653890.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图&图生图_1951120800927653890.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `RepeatLatentBatch`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `VAEDecode` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CR SDXL Aspect Ratio`
- `Text Concatenate`
- `ImageScaleDownToSize`
- `SaveImage`
- `LoadImage`
- `Text Multiline`
- `Text Concatenate`
- `WD14Tagger|pysssss`
- `ImpactSwitch`
- `ImpactSwitch`
- `Note`
- `Note`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `easy showAnything`
- `PreviewImage`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `Note`
- `CR Text`

## 关键参数

- `width` = `768`
- `height` = `1280`
- `batch_size` = `4`

## 知识

覆盖率 **52%**（16/31）

**有卡**：`RepeatLatentBatch`、`UNETLoader`、`VAEEncode`、`BasicGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`VAEDecode`、`DualCLIPLoader`、`VAELoader`、`CLIPTextEncode`、`EmptyLatentImage`、`ImageScaleDownToSize`、`SaveImage`、`LoadImage`、`BasicScheduler`、`KSamplerSelect`

**缺卡**（8）：`CR Text`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`Text Concatenate`、`Text Concatenate`、`Text Multiline`、`WD14Tagger|pysssss`、`CR SDXL Aspect Ratio`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `WD14Tagger|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明

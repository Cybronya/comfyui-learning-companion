---
key: 图片生成/文生图/Flux.1-Krea-Dev文生图&图生图_1951120800927653890.json
name: Flux.1-Krea-Dev文生图&图生图_1951120800927653890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev文生图&图生图_1951120800927653890.json
hash: 8a631ded1921f75d
coverage: 0.774194
learned_at: 2026-10-15 22:26:25
nodes: [RepeatLatentBatch, UNETLoader, VAEEncode, BasicGuider, SamplerCustomAdvanced, RandomNoise, VAEDecode, DualCLIPLoader, VAELoader, CLIPTextEncode, EmptyLatentImage, CR SDXL Aspect Ratio, Text Concatenate, ImageScaleDownToSize, SaveImage, LoadImage, Text Multiline, Text Concatenate, WD14Tagger|pysssss, ImpactSwitch, ImpactSwitch, Note, Note, BasicScheduler, KSamplerSelect, easy showAnything, PreviewImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, Note, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 4, "height": 1280, "width": 768}
---

# 图片生成/文生图/Flux.1-Krea-Dev文生图&图生图_1951120800927653890.json

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

覆盖率 **77%**（24/31）

**有卡**：`RepeatLatentBatch`、`UNETLoader`、`VAEEncode`、`BasicGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`VAEDecode`、`DualCLIPLoader`、`VAELoader`、`CLIPTextEncode`、`EmptyLatentImage`、`CR SDXL Aspect Ratio`、`Text Concatenate`、`ImageScaleDownToSize`、`SaveImage`、`LoadImage`、`Text Multiline`、`WD14Tagger|pysssss`、`BasicScheduler`、`KSamplerSelect`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、KSamplerSelect、SamplerCustomAdvanced

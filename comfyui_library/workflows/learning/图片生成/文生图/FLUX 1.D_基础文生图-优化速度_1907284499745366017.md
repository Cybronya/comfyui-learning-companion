---
key: 图片生成/文生图/FLUX 1.D_基础文生图-优化速度_1907284499745366017.json
name: FLUX 1.D_基础文生图-优化速度_1907284499745366017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX 1.D_基础文生图-优化速度_1907284499745366017.json
hash: 3a716a60c503e213
coverage: 0.638889
learned_at: 2026-10-10 20:58:31
nodes: [BasicGuider, FluxGuidance, SamplerCustomAdvanced, RandomNoise, VAELoader, EmptyLatentImage, Text Multiline, SiliconflowLLM, easy showAnything, ArtGallery_Zho, easy seed, easy promptConcat, KSamplerSelect, BasicScheduler, SaveImage, Node Collector (rgthree), Node Combiner (rgthree), easy showAnything, Text Multiline, DifferentialDiffusion, Fast Bypasser (rgthree), easy seed, ChinesePrompt_Mix, Int, Int, LoraLoader, CFGZeroStarAndInit, VAEDecode, easy cleanGpuUsed, CLIPTextEncode, DualCLIPLoader, UNETLoader, CFGZeroStarAndInit, ApplyFBCacheOnModel, Text Multiline, Text Multiline]
patterns: [lora]
missing: [Fast Bypasser (rgthree), Node Collector (rgthree), Node Combiner (rgthree), Text Multiline, Text Multiline, Text Multiline, Text Multiline, easy cleanGpuUsed, easy promptConcat, easy seed, easy seed]
parameters: {"batch_size": 3, "height": 512, "lora_name": "F.1-Ghibli Characters-吉卜力动漫人物_F.1-吉卜力人物-V1.0.safetensors", "strength_clip": 1, "strength_model": 1.0000000000000002, "width": 512}
discoveries: [次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Node Collector (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Node Combiner (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/FLUX 1.D_基础文生图-优化速度_1907284499745366017.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX 1.D_基础文生图-优化速度_1907284499745366017.json`

## 结构

**节点**（36 个）：
- `BasicGuider`
- `FluxGuidance`
- `SamplerCustomAdvanced`
- `RandomNoise`
- `VAELoader`
- `EmptyLatentImage`
- `Text Multiline`
- `SiliconflowLLM`
- `easy showAnything`
- `ArtGallery_Zho`
- `easy seed`
- `easy promptConcat`
- `KSamplerSelect`
- `BasicScheduler`
- `SaveImage`
- `Node Collector (rgthree)`
- `Node Combiner (rgthree)`
- `easy showAnything`
- `Text Multiline`
- `DifferentialDiffusion`
- `Fast Bypasser (rgthree)`
- `easy seed`
- `ChinesePrompt_Mix`
- `Int`
- `Int`
- `LoraLoader`
- `CFGZeroStarAndInit`
- `VAEDecode`
- `easy cleanGpuUsed`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `UNETLoader`
- `CFGZeroStarAndInit`
- `ApplyFBCacheOnModel`
- `Text Multiline`
- `Text Multiline`

**识别到的模式**：lora

## 关键参数

- `batch_size` = `3`
- `height` = `512`
- `lora_name` = `F.1-Ghibli Characters-吉卜力动漫人物_F.1-吉卜力人物-V1.0.safetensors`
- `strength_clip` = `1`
- `strength_model` = `1.0000000000000002`
- `width` = `512`

## 知识

覆盖率 **64%**（23/36）

**有卡**：`BasicGuider`、`FluxGuidance`、`SamplerCustomAdvanced`、`RandomNoise`、`VAELoader`、`EmptyLatentImage`、`Text Multiline`、`SiliconflowLLM`、`easy showAnything`、`ArtGallery_Zho`、`easy seed`、`easy promptConcat`、`KSamplerSelect`、`BasicScheduler`、`SaveImage`、`Node Collector (rgthree)`、`Node Combiner (rgthree)`、`DifferentialDiffusion`、`Fast Bypasser (rgthree)`、`ChinesePrompt_Mix`

**缺卡**（11）：`Fast Bypasser (rgthree)`、`Node Collector (rgthree)`、`Node Combiner (rgthree)`、`Text Multiline`、`Text Multiline`、`Text Multiline`、`Text Multiline`、`easy cleanGpuUsed`、`easy promptConcat`、`easy seed`、`easy seed`

## 学习发现

- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Node Collector (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Node Combiner (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明

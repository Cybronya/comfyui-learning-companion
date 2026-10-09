---
key: 图片生成/文生图/Upscaler-F.1专属高清放大CN模型_1925152412171235330.json
name: Upscaler-F.1专属高清放大CN模型_1925152412171235330.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Upscaler-F.1专属高清放大CN模型_1925152412171235330.json
hash: 3dc1f7095960a419
coverage: 0.724138
learned_at: 2026-10-07 22:22:57
nodes: [Reroute, Note, Fast Groups Bypasser (rgthree), Reroute, SamplerCustomAdvanced, BasicGuider, RandomNoise, KSamplerSelect, BasicScheduler, VAEEncode, Reroute, VAEDecode, CLIPTextEncodeFlux, CLIPTextEncodeFlux, RepeatLatentBatch, Display Any (rgthree), SaveImage, Miaoshouai_Tagger, LoraLoader, DualCLIPLoader, UNETLoader, VAELoader, StringFunction|pysssss, GetImageSizeAndCount, ControlNetLoader, ControlNetApplyAdvanced, LoadImage, LatentUpscaleBy, Image Comparer (rgthree)]
patterns: [lora]
missing: [Display Any (rgthree), StringFunction|pysssss]
parameters: {"controlnet_strength": 0.7000000000000002, "lora_name": null, "strength_clip": 1, "strength_model": 0.8}
discoveries: [次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Upscaler-F.1专属高清放大CN模型_1925152412171235330.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1925152412171235330.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `Reroute`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEEncode` ★核心
- `Reroute`
- `VAEDecode` ★核心
- `CLIPTextEncodeFlux` ★核心
- `CLIPTextEncodeFlux` ★核心
- `RepeatLatentBatch`
- `Display Any (rgthree)`
- `SaveImage`
- `Miaoshouai_Tagger`
- `LoraLoader` ★核心
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `StringFunction|pysssss`
- `GetImageSizeAndCount`
- `ControlNetLoader`
- `ControlNetApplyAdvanced` ★核心
- `LoadImage`
- `LatentUpscaleBy`
- `Image Comparer (rgthree)`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `None`
- `strength_model` = `0.8`
- `strength_clip` = `1`
- `controlnet_strength` = `0.7000000000000002`

## 知识

覆盖率 **72%**（21/29）

**有卡**：`SamplerCustomAdvanced`、`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`BasicScheduler`、`VAEEncode`、`VAEDecode`、`CLIPTextEncodeFlux`、`RepeatLatentBatch`、`SaveImage`、`Miaoshouai_Tagger`、`LoraLoader`、`DualCLIPLoader`、`UNETLoader`、`VAELoader`、`GetImageSizeAndCount`、`ControlNetLoader`、`ControlNetApplyAdvanced`、`LoadImage`、`LatentUpscaleBy`

**缺卡**（2）：`Display Any (rgthree)`、`StringFunction|pysssss`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识

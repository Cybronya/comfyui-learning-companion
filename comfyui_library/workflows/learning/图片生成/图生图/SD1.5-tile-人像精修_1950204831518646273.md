---
key: 图片生成/图生图/SD1.5-tile-人像精修_1950204831518646273.json
name: SD1.5-tile-人像精修_1950204831518646273
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5-tile-人像精修_1950204831518646273.json
hash: cc7233574fbe7680
coverage: 0.487805
learned_at: 2026-10-23 11:23:35
nodes: [SetNode, GetNode, GetNode, VAEEncode, Reroute (rgthree), Reroute (rgthree), SetNode, GetNode, Reroute (rgthree), SetNode, GetNode, CheckpointLoaderSimple, CLIPTextEncode, CLIPTextEncode, PreviewImage, ChinesePrompt_Mix, ControlNetApply, ChinesePrompt_Mix, UltralyticsDetectorProvider, ConstrainImage|pysssss, Reroute (rgthree), CannyEdgePreprocessor, LoraLoader, ControlNetApply, ControlNetLoader, Reroute (rgthree), ControlNetLoader, Reroute (rgthree), KSampler, FaceDetailer, SaveImage, Reroute, Reroute, LoraLoader, GetNode, Image Comparer (rgthree), Image Comparer (rgthree), LoadImage, VAEDecode, Reroute, Reroute]
patterns: [image_to_image, controlnet, lora]
missing: []
parameters: {"cfg": 8, "checkpoint": "majicMIX realistic 麦橘写实_v7.safetensors", "controlnet_strength": 0.7000000000000002, "denoise": 0.2, "lora_name": "林鹤-妆容，美颜，磨皮，滤镜，四合一差异炼丹功能性lora。_v1.safetensors", "sampler_name": "euler", "scheduler": "normal", "seed": 293840785063917, "steps": 15, "strength_clip": 1, "strength_model": 0.2700000000000001}
---

# 图片生成/图生图/SD1.5-tile-人像精修_1950204831518646273.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5-tile-人像精修_1950204831518646273.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `Reroute (rgthree)`
- `Reroute (rgthree)`
- `SetNode`
- `GetNode`
- `Reroute (rgthree)`
- `SetNode`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ChinesePrompt_Mix`
- `ControlNetApply` ★核心
- `ChinesePrompt_Mix`
- `UltralyticsDetectorProvider`
- `ConstrainImage|pysssss`
- `Reroute (rgthree)`
- `CannyEdgePreprocessor`
- `LoraLoader` ★核心
- `ControlNetApply` ★核心
- `ControlNetLoader`
- `Reroute (rgthree)`
- `ControlNetLoader`
- `Reroute (rgthree)`
- `KSampler` ★核心
- `FaceDetailer`
- `SaveImage`
- `Reroute`
- `Reroute`
- `LoraLoader` ★核心
- `GetNode`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `LoadImage`
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`

**识别到的模式**：image_to_image、controlnet、lora

## 关键参数

- `checkpoint` = `majicMIX realistic 麦橘写实_v7.safetensors`
- `controlnet_strength` = `0.7000000000000002`
- `lora_name` = `林鹤-妆容，美颜，磨皮，滤镜，四合一差异炼丹功能性lora。_v1.safetensors`
- `strength_model` = `0.2700000000000001`
- `strength_clip` = `1`
- `seed` = `293840785063917`
- `steps` = `15`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `0.2`

## 知识

覆盖率 **49%**（20/41）

**有卡**：`VAEEncode`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`ChinesePrompt_Mix`、`ControlNetApply`、`UltralyticsDetectorProvider`、`ConstrainImage|pysssss`、`CannyEdgePreprocessor`、`LoraLoader`、`ControlNetLoader`、`KSampler`、`FaceDetailer`、`SaveImage`、`LoadImage`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetLoader、CannyEdgePreprocessor、ControlNetApply

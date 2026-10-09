---
key: 图片生成/文生图/Wan2.2文生图_极简版_1950891831544455170.json
name: Wan2.2文生图_极简版_1950891831544455170.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2文生图_极简版_1950891831544455170.json
hash: 48fdb653046e0161
coverage: 0.612245
learned_at: 2026-10-07 22:58:43
nodes: [LayerUtility: If , TextCombinerTwo, TextCombinerTwo, easy int, LoadImage, UNETLoader, CLIPTextEncode, easy cleanGpuUsed, JjkText, RH_Captioner, RH_Prompter, easy int, UNETLoader, ModelSamplingSD3, CLIPLoader, CLIPTextEncode, VAELoader, VAEEncode, VAEDecode, ModelSamplingSD3, ModelSamplingSD3, VAEDecode, JWStringConcat, JjkText, CLIPTextEncode, KSampler, LatentUpscaleBy, easy int, KSamplerAdvanced, KSamplerAdvanced, easy int, EmptyHunyuanLatentVideo, PreviewBridge, easy int, easy float, JjkText, easy int, PreviewBridge, SaveImage, easy float, easy float, JjkText, easy boolean, ImpactSwitch, Wan22PromptSelector, easy showAnything, JWStringConcat, JjkText, Seed_]
patterns: [image_to_image]
missing: [LayerUtility: If , easy boolean, easy cleanGpuUsed, easy float, easy float, easy float, easy int, easy int, easy int, easy int, easy int, easy int]
parameters: {"cfg": 20, "denoise": "normal", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `LayerUtility: If ` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Wan2.2文生图_极简版_1950891831544455170.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1950891831544455170.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `LayerUtility: If `
- `TextCombinerTwo`
- `TextCombinerTwo`
- `easy int`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `JjkText`
- `RH_Captioner`
- `RH_Prompter`
- `easy int`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `JWStringConcat`
- `JjkText`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LatentUpscaleBy`
- `easy int`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy int`
- `EmptyHunyuanLatentVideo`
- `PreviewBridge`
- `easy int`
- `easy float`
- `JjkText`
- `easy int`
- `PreviewBridge`
- `SaveImage`
- `easy float`
- `easy float`
- `JjkText`
- `easy boolean`
- `ImpactSwitch`
- `Wan22PromptSelector`
- `easy showAnything`
- `JWStringConcat`
- `JjkText`
- `Seed_`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **61%**（30/49）

**有卡**：`TextCombinerTwo`、`LoadImage`、`UNETLoader`、`CLIPTextEncode`、`RH_Captioner`、`RH_Prompter`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`VAEDecode`、`JWStringConcat`、`KSampler`、`LatentUpscaleBy`、`KSamplerAdvanced`、`EmptyHunyuanLatentVideo`、`PreviewBridge`、`SaveImage`、`Wan22PromptSelector`、`Seed_`

**缺卡**（12）：`LayerUtility: If `、`easy boolean`、`easy cleanGpuUsed`、`easy float`、`easy float`、`easy float`、`easy int`、`easy int`、`easy int`、`easy int`、`easy int`、`easy int`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `LayerUtility: If ` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识

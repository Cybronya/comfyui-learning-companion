---
key: 图片生成/图生图/Qwen Image 2.1漫转真工作流2609_2105932118147817473.json
name: Qwen Image 2.1漫转真工作流2609_2105932118147817473.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1漫转真工作流2609_2105932118147817473.json
hash: 790c647ea95280e9
coverage: 0.73913
learned_at: 2026-10-09 22:09:17
nodes: [孤海注释, JoinStrings, PrimitiveBoolean, ComfySwitchNode, CLIPLoader, VAELoader, LoraLoaderModelOnly, UNETLoader, CLIPLoader, TextEncodeQwenImage21, QwenImage21Cache, VAEDecode, EmptyLatentImage, BatchImagesNode, easy positive, TextGenerate, ShowText|pysssss, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, easy positive, KSampler, LoadImage, ResolutionSelector]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, easy positive, easy positive]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 535254766028910, "steps": 25, "width": 1024}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/Qwen Image 2.1漫转真工作流2609_2105932118147817473.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2105932118147817473.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `孤海注释`
- `JoinStrings`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `BatchImagesNode`
- `easy positive`
- `TextGenerate`
- `ShowText|pysssss`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy positive`
- `KSampler` ★核心
- `LoadImage`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `535254766028910`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **74%**（17/23）

**有卡**：`JoinStrings`、`PrimitiveBoolean`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`VAEDecode`、`EmptyLatentImage`、`BatchImagesNode`、`TextGenerate`、`SaveImage`、`KSampler`、`LoadImage`、`ResolutionSelector`

**缺卡**（3）：`LayerUtility: ImageScaleByAspectRatio V2`、`easy positive`、`easy positive`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识

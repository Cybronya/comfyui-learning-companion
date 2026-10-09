---
key: 图片生成/文生图/QwenImage-RebalanceV1现实增强 VS 原版_1984151149953646593.json
name: QwenImage-RebalanceV1现实增强 VS 原版_1984151149953646593.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QwenImage-RebalanceV1现实增强 VS 原版_1984151149953646593.json
hash: 1a1c73d1dc9a51ba
coverage: 0.7
learned_at: 2026-10-09 20:05:46
nodes: [LayerUtility: PurgeVRAM V2, ModelSamplingAuraFlow, CLIPTextEncode, CLIPTextEncode, LayerUtility: PurgeVRAM V2, ModelSamplingAuraFlow, CLIPTextEncode, LoraLoaderModelOnly, CLIPTextEncode, KSampler, KSampler, PrimitiveInt, EmptySD3LatentImage, Image Comparer (rgthree), Text Concatenate, Text Multiline, Fast Groups Bypasser (rgthree), UNETLoader, CLIPLoader, VAELoader, LoadImage, AILab_QwenVL, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, SaveImage, VAEDecode, SaveImage, Note, ShowText|pysssss]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, Text Concatenate, Text Multiline]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 496328613975437, "steps": 10}
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/QwenImage-RebalanceV1现实增强 VS 原版_1984151149953646593.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1984151149953646593.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `PrimitiveInt`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `Text Concatenate`
- `Text Multiline`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `AILab_QwenVL`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `Note`
- `ShowText|pysssss`

## 关键参数

- `seed` = `496328613975437`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **70%**（21/30）

**有卡**：`ModelSamplingAuraFlow`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`KSampler`、`EmptySD3LatentImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`AILab_QwenVL`、`VAEDecode`、`SaveImage`

**缺卡**（4）：`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`Text Concatenate`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识

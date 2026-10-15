---
key: 图片生成/文生图/Flux+ControlNet_UnionPro2_v2_1927179095069851650.json
name: Flux+ControlNet_UnionPro2_v2_1927179095069851650
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux+ControlNet_UnionPro2_v2_1927179095069851650.json
hash: 30c029a0824851c5
coverage: 0.740741
learned_at: 2026-10-10 20:58:35
nodes: [DualCLIPLoader, RandomNoise, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, PreviewImage, VAEDecode, SaveImage, ImpactCombineConditionings, VAELoader, PreviewImage, ConditioningZeroOut, ControlNetLoader, ControlNetApplyAdvanced, BasicScheduler, Note, EmptySD3LatentImage, CLIPTextEncodeFlux, LoadImage, ModelSamplingFlux, UNETLoader, Note, PrimitiveNode, PrimitiveNode, Text Multiline, AIO_Preprocessor, LoraLoaderModelOnly]
patterns: []
missing: [Text Multiline]
parameters: {"controlnet_strength": 0.7000000000000002}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Flux+ControlNet_UnionPro2_v2_1927179095069851650.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux+ControlNet_UnionPro2_v2_1927179095069851650.json`

## 结构

**节点**（27 个）：
- `DualCLIPLoader`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect`
- `SamplerCustomAdvanced`
- `PreviewImage`
- `VAEDecode`
- `SaveImage`
- `ImpactCombineConditionings`
- `VAELoader`
- `PreviewImage`
- `ConditioningZeroOut`
- `ControlNetLoader`
- `ControlNetApplyAdvanced`
- `BasicScheduler`
- `Note`
- `EmptySD3LatentImage`
- `CLIPTextEncodeFlux`
- `LoadImage`
- `ModelSamplingFlux`
- `UNETLoader`
- `Note`
- `PrimitiveNode`
- `PrimitiveNode`
- `Text Multiline`
- `AIO_Preprocessor`
- `LoraLoaderModelOnly`

## 关键参数

- `controlnet_strength` = `0.7000000000000002`

## 知识

覆盖率 **74%**（20/27）

**有卡**：`DualCLIPLoader`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`PreviewImage`、`VAEDecode`、`SaveImage`、`ImpactCombineConditionings`、`VAELoader`、`ConditioningZeroOut`、`ControlNetLoader`、`ControlNetApplyAdvanced`、`BasicScheduler`、`Note`、`EmptySD3LatentImage`、`CLIPTextEncodeFlux`、`LoadImage`、`ModelSamplingFlux`

**缺卡**（1）：`Text Multiline`

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识

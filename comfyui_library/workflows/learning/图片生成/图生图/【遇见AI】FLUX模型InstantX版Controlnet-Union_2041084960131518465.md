---
key: 图片生成/图生图/【遇见AI】FLUX模型InstantX版Controlnet-Union_2041084960131518465.json
name: 【遇见AI】FLUX模型InstantX版Controlnet-Union_2041084960131518465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】FLUX模型InstantX版Controlnet-Union_2041084960131518465.json
hash: dd538e60cc49aae7
coverage: 0.875
learned_at: 2026-10-23 11:51:58
nodes: [BasicGuider, VAEDecode, KSamplerSelect, SaveImage, BasicScheduler, ModelSamplingFlux, EmptyLatentImage, PrimitiveNode, PrimitiveNode, CLIPTextEncodeFlux, RandomNoise, ControlNetApplySD3, ConditioningZeroOut, SamplerCustomAdvanced, CannyEdgePreprocessor, Note, LoadImage, LoadImage, LoadImage, ControlNetLoader, SetUnionControlNetType, UnetLoaderGGUF, DualCLIPLoader, VAELoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "controlnet_strength": 1, "height": 1024, "width": 1024}
---

# 图片生成/图生图/【遇见AI】FLUX模型InstantX版Controlnet-Union_2041084960131518465.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】FLUX模型InstantX版Controlnet-Union_2041084960131518465.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（24 个）：
- `BasicGuider`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `SaveImage`
- `BasicScheduler`
- `ModelSamplingFlux`
- `EmptyLatentImage` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `CLIPTextEncodeFlux` ★核心
- `RandomNoise`
- `ControlNetApplySD3` ★核心
- `ConditioningZeroOut`
- `SamplerCustomAdvanced` ★核心
- `CannyEdgePreprocessor`
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ControlNetLoader`
- `SetUnionControlNetType`
- `UnetLoaderGGUF` ★核心
- `DualCLIPLoader`
- `VAELoader`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `controlnet_strength` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`BasicGuider`、`VAEDecode`、`KSamplerSelect`、`SaveImage`、`BasicScheduler`、`ModelSamplingFlux`、`EmptyLatentImage`、`CLIPTextEncodeFlux`、`RandomNoise`、`ControlNetApplySD3`、`ConditioningZeroOut`、`SamplerCustomAdvanced`、`CannyEdgePreprocessor`、`LoadImage`、`ControlNetLoader`、`SetUnionControlNetType`、`UnetLoaderGGUF`、`DualCLIPLoader`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、ConditioningZeroOut、EmptyLatentImage、LoadImage、ControlNetLoader、SetUnionControlNetType、CannyEdgePreprocessor

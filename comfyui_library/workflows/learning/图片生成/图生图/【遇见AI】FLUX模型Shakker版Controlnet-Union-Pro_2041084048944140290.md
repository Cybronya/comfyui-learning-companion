---
key: 图片生成/图生图/【遇见AI】FLUX模型Shakker版Controlnet-Union-Pro_2041084048944140290.json
name: 【遇见AI】FLUX模型Shakker版Controlnet-Union-Pro_2041084048944140290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】FLUX模型Shakker版Controlnet-Union-Pro_2041084048944140290.json
hash: fca4f1d403428d7e
coverage: 0.807692
learned_at: 2026-10-23 11:52:01
nodes: [OpenposePreprocessor, PreviewImage, Note, SetUnionControlNetType, VAEDecode, KSamplerSelect, SaveImage, BasicScheduler, ModelSamplingFlux, EmptyLatentImage, PrimitiveNode, SamplerCustomAdvanced, BasicGuider, RandomNoise, ConditioningZeroOut, ControlNetApplySD3, Note, LoadImage, LoadImage, ControlNetLoader, LoadImage, CLIPTextEncodeFlux, UnetLoaderGGUF, DualCLIPLoader, VAELoader, PrimitiveNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "controlnet_strength": 0.8, "height": 1024, "width": 1024}
---

# 图片生成/图生图/【遇见AI】FLUX模型Shakker版Controlnet-Union-Pro_2041084048944140290.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】FLUX模型Shakker版Controlnet-Union-Pro_2041084048944140290.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（26 个）：
- `OpenposePreprocessor`
- `PreviewImage`
- `Note`
- `SetUnionControlNetType`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `SaveImage`
- `BasicScheduler`
- `ModelSamplingFlux`
- `EmptyLatentImage` ★核心
- `PrimitiveNode`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `RandomNoise`
- `ConditioningZeroOut`
- `ControlNetApplySD3` ★核心
- `Note`
- `LoadImage`
- `LoadImage`
- `ControlNetLoader`
- `LoadImage`
- `CLIPTextEncodeFlux` ★核心
- `UnetLoaderGGUF` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `PrimitiveNode`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `controlnet_strength` = `0.8`

## 知识

覆盖率 **81%**（21/26）

**有卡**：`OpenposePreprocessor`、`SetUnionControlNetType`、`VAEDecode`、`KSamplerSelect`、`SaveImage`、`BasicScheduler`、`ModelSamplingFlux`、`EmptyLatentImage`、`SamplerCustomAdvanced`、`BasicGuider`、`RandomNoise`、`ConditioningZeroOut`、`ControlNetApplySD3`、`LoadImage`、`ControlNetLoader`、`CLIPTextEncodeFlux`、`UnetLoaderGGUF`、`DualCLIPLoader`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、ConditioningZeroOut、EmptyLatentImage、LoadImage、ControlNetLoader、OpenposePreprocessor、SetUnionControlNetType

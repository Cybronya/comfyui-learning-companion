---
key: 图片生成/图生图/SRPO-image-fix-workflow_1967519002291474434.json
name: SRPO-image-fix-workflow_1967519002291474434
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SRPO-image-fix-workflow_1967519002291474434.json
hash: 2d51bc77cfdfc6c7
coverage: 0.904762
learned_at: 2026-10-23 11:24:07
nodes: [FluxGuidance, ModelSamplingFlux, BasicGuider, SamplerCustomAdvanced, SeedVR2, LayerUtility: PurgeVRAM V2, VAEDecode, SaveImage, UNETLoader, DualCLIPLoader, VAELoader, PrimitiveNode, PrimitiveNode, RandomNoise, CLIPTextEncode, LoadImage, KSamplerSelect, BasicScheduler, VAEEncode, EmptySD3LatentImage, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/SRPO-image-fix-workflow_1967519002291474434.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SRPO-image-fix-workflow_1967519002291474434.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `FluxGuidance`
- `ModelSamplingFlux`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `SeedVR2`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `PrimitiveNode`
- `PrimitiveNode`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEEncode` ★核心
- `EmptySD3LatentImage`
- `SaveImage`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`FluxGuidance`、`ModelSamplingFlux`、`BasicGuider`、`SamplerCustomAdvanced`、`SeedVR2`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`SaveImage`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`RandomNoise`、`CLIPTextEncode`、`LoadImage`、`KSamplerSelect`、`BasicScheduler`、`VAEEncode`、`EmptySD3LatentImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced

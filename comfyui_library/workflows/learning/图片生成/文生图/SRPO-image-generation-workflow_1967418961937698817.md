---
key: 图片生成/文生图/SRPO-image-generation-workflow_1967418961937698817.json
name: SRPO-image-generation-workflow_1967418961937698817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SRPO-image-generation-workflow_1967418961937698817.json
hash: cb3ad7d830ae66e7
coverage: 0.894737
learned_at: 2026-10-15 22:27:32
nodes: [PrimitiveNode, PrimitiveNode, SeedVR2, VAEDecode, SaveImage, BasicGuider, UNETLoader, DualCLIPLoader, VAELoader, FluxGuidance, SamplerCustomAdvanced, EmptySD3LatentImage, RandomNoise, KSamplerSelect, BasicScheduler, ModelSamplingFlux, SaveImage, LayerUtility: PurgeVRAM V2, CLIPTextEncode]
patterns: []
missing: []
---

# 图片生成/文生图/SRPO-image-generation-workflow_1967418961937698817.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SRPO-image-generation-workflow_1967418961937698817.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `PrimitiveNode`
- `PrimitiveNode`
- `SeedVR2`
- `VAEDecode` ★核心
- `SaveImage`
- `BasicGuider`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `FluxGuidance`
- `SamplerCustomAdvanced` ★核心
- `EmptySD3LatentImage`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ModelSamplingFlux`
- `SaveImage`
- `LayerUtility: PurgeVRAM V2`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **89%**（17/19）

**有卡**：`SeedVR2`、`VAEDecode`、`SaveImage`、`BasicGuider`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`FluxGuidance`、`SamplerCustomAdvanced`、`EmptySD3LatentImage`、`RandomNoise`、`KSamplerSelect`、`BasicScheduler`、`ModelSamplingFlux`、`LayerUtility: PurgeVRAM V2`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、SeedVR2

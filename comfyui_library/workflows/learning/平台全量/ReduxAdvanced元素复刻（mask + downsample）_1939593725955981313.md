---
key: 平台全量/ReduxAdvanced元素复刻（mask + downsample）_1939593725955981313.json
name: ReduxAdvanced元素复刻（mask + downsample）_1939593725955981313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ReduxAdvanced元素复刻（mask + downsample）_1939593725955981313.json
hash: db54171829e8b63b
coverage: 0.833333
learned_at: 2026-11-14 00:54:45
nodes: [SamplerCustomAdvanced, PrimitiveNode, BasicGuider, ModelSamplingFlux, BasicScheduler, KSamplerSelect, RandomNoise, VAEDecode, EmptySD3LatentImage, Note, UNETLoader, DualCLIPLoader, VAELoader, StyleModelLoader, PreviewImage, CLIPVisionLoader, ReduxAdvanced, LoadImage, FluxGuidance, CLIPTextEncode, PrimitiveNode, Note Plus (mtb), LoadImageFromUrl, SaveImage]
patterns: []
missing: []
---

# 平台全量/ReduxAdvanced元素复刻（mask + downsample）_1939593725955981313.json

> 来源文件 `comfyui_library/workflows/平台全量/ReduxAdvanced元素复刻（mask + downsample）_1939593725955981313.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `SamplerCustomAdvanced` ★核心
- `PrimitiveNode`
- `BasicGuider`
- `ModelSamplingFlux`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `VAEDecode` ★核心
- `EmptySD3LatentImage`
- `Note`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `StyleModelLoader`
- `PreviewImage`
- `CLIPVisionLoader`
- `ReduxAdvanced`
- `LoadImage`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `Note Plus (mtb)`
- `LoadImageFromUrl`
- `SaveImage`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`SamplerCustomAdvanced`、`BasicGuider`、`ModelSamplingFlux`、`BasicScheduler`、`KSamplerSelect`、`RandomNoise`、`VAEDecode`、`EmptySD3LatentImage`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`StyleModelLoader`、`CLIPVisionLoader`、`ReduxAdvanced`、`LoadImage`、`FluxGuidance`、`CLIPTextEncode`、`Note Plus (mtb)`、`LoadImageFromUrl`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced

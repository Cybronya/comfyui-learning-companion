---
key: 图片生成/文生图/In Context Photo Manipulation_1939209223630725122.json
name: In Context Photo Manipulation_1939209223630725122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/In Context Photo Manipulation_1939209223630725122.json
hash: e37066f76ad47e96
coverage: 0.944444
learned_at: 2026-10-15 22:26:34
nodes: [BasicGuider, BasicScheduler, UNETLoader, RandomNoise, CLIPTextEncode, DualCLIPLoader, VAELoader, LoraLoaderModelOnly, Note Plus (mtb), LoadImageFromUrl, CR SDXL Aspect Ratio, SamplerCustomAdvanced, VAEDecode, Reroute, SaveImage, ModelSamplingFlux, KSamplerSelect, FluxGuidance]
patterns: []
missing: []
---

# 图片生成/文生图/In Context Photo Manipulation_1939209223630725122.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/In Context Photo Manipulation_1939209223630725122.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `BasicGuider`
- `BasicScheduler`
- `UNETLoader` ★核心
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `Note Plus (mtb)`
- `LoadImageFromUrl`
- `CR SDXL Aspect Ratio`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `Reroute`
- `SaveImage`
- `ModelSamplingFlux`
- `KSamplerSelect` ★核心
- `FluxGuidance`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`BasicGuider`、`BasicScheduler`、`UNETLoader`、`RandomNoise`、`CLIPTextEncode`、`DualCLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`Note Plus (mtb)`、`LoadImageFromUrl`、`CR SDXL Aspect Ratio`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`ModelSamplingFlux`、`KSamplerSelect`、`FluxGuidance`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced

---
key: In Context Photo Manipulation_1939209223630725122.json
name: In Context Photo Manipulation_1939209223630725122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/In Context Photo Manipulation_1939209223630725122.json
hash: e37066f76ad47e96
coverage: 0.833333
learned_at: 2026-10-10 20:58:40
nodes: [BasicGuider, BasicScheduler, UNETLoader, RandomNoise, CLIPTextEncode, DualCLIPLoader, VAELoader, LoraLoaderModelOnly, Note Plus (mtb), LoadImageFromUrl, CR SDXL Aspect Ratio, SamplerCustomAdvanced, VAEDecode, Reroute, SaveImage, ModelSamplingFlux, KSamplerSelect, FluxGuidance]
patterns: []
missing: [Note Plus (mtb), CR SDXL Aspect Ratio]
discoveries: [次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明]
---

# In Context Photo Manipulation_1939209223630725122.json

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

覆盖率 **83%**（15/18）

**有卡**：`BasicGuider`、`BasicScheduler`、`UNETLoader`、`RandomNoise`、`CLIPTextEncode`、`DualCLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`LoadImageFromUrl`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`ModelSamplingFlux`、`KSamplerSelect`、`FluxGuidance`

**缺卡**（2）：`Note Plus (mtb)`、`CR SDXL Aspect Ratio`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明

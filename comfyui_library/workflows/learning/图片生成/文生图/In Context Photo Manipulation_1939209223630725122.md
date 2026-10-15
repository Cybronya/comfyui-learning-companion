---
key: 图片生成/文生图/In Context Photo Manipulation_1939209223630725122.json
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

# 图片生成/文生图/In Context Photo Manipulation_1939209223630725122.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/In Context Photo Manipulation_1939209223630725122.json`

## 结构

**节点**（18 个）：
- `BasicGuider`
- `BasicScheduler`
- `UNETLoader`
- `RandomNoise`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly`
- `Note Plus (mtb)`
- `LoadImageFromUrl`
- `CR SDXL Aspect Ratio`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `Reroute`
- `SaveImage`
- `ModelSamplingFlux`
- `KSamplerSelect`
- `FluxGuidance`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`BasicGuider`、`BasicScheduler`、`UNETLoader`、`RandomNoise`、`CLIPTextEncode`、`DualCLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`Note Plus (mtb)`、`LoadImageFromUrl`、`CR SDXL Aspect Ratio`、`SamplerCustomAdvanced`、`VAEDecode`、`Reroute`、`SaveImage`

**缺卡**（2）：`Note Plus (mtb)`、`CR SDXL Aspect Ratio`

## 学习发现

- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明

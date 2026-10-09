---
key: 图片生成/文生图/Flux.2-klein-9b_1927021794954268673.json
name: Flux.2-klein-9b_1927021794954268673.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2-klein-9b_1927021794954268673.json
hash: d9377c57e7e55b79
coverage: 0.782609
learned_at: 2026-10-07 19:12:50
nodes: [KSamplerSelect, EmptyFlux2LatentImage, RandomNoise, ConditioningZeroOut, SamplerCustomAdvanced, VAELoader, Flux2Scheduler, LayerUtility: PurgeVRAM V2, CFGGuider, VAEDecode, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, PrimitiveInt, PrimitiveInt, ttN seed, SaveImage, CLIPTextEncode, UNETLoader, CLIPLoader, easy promptList, SaveImage, Text]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, easy promptList, ttN seed]
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `ttN seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Flux.2-klein-9b_1927021794954268673.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1927021794954268673.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `KSamplerSelect` ★核心
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `ConditioningZeroOut`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `Flux2Scheduler`
- `LayerUtility: PurgeVRAM V2`
- `CFGGuider`
- `VAEDecode` ★核心
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `PrimitiveInt`
- `PrimitiveInt`
- `ttN seed`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `easy promptList`
- `SaveImage`
- `Text`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`KSamplerSelect`、`EmptyFlux2LatentImage`、`RandomNoise`、`ConditioningZeroOut`、`SamplerCustomAdvanced`、`VAELoader`、`Flux2Scheduler`、`CFGGuider`、`VAEDecode`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SaveImage`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`Text`

**缺卡**（3）：`LayerUtility: PurgeVRAM V2`、`easy promptList`、`ttN seed`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、CFGGuider、KSamplerSelect

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy promptList` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `ttN seed` 仅有 KSampler 的通用知识，没有该节点自己的说明

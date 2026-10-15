---
key: 图片生成/文生图/Flux.2-klein-9b_1927021794954268673.json
name: Flux.2-klein-9b_1927021794954268673
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2-klein-9b_1927021794954268673.json
hash: d9377c57e7e55b79
coverage: 0.913043
learned_at: 2026-10-15 22:26:26
nodes: [KSamplerSelect, EmptyFlux2LatentImage, RandomNoise, ConditioningZeroOut, SamplerCustomAdvanced, VAELoader, Flux2Scheduler, LayerUtility: PurgeVRAM V2, CFGGuider, VAEDecode, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, PrimitiveInt, PrimitiveInt, ttN seed, SaveImage, CLIPTextEncode, UNETLoader, CLIPLoader, easy promptList, SaveImage, Text]
patterns: []
missing: []
---

# 图片生成/文生图/Flux.2-klein-9b_1927021794954268673.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2-klein-9b_1927021794954268673.json`

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

覆盖率 **91%**（21/23）

**有卡**：`KSamplerSelect`、`EmptyFlux2LatentImage`、`RandomNoise`、`ConditioningZeroOut`、`SamplerCustomAdvanced`、`VAELoader`、`Flux2Scheduler`、`LayerUtility: PurgeVRAM V2`、`CFGGuider`、`VAEDecode`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`ttN seed`、`SaveImage`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`easy promptList`、`Text`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、CFGGuider、KSamplerSelect

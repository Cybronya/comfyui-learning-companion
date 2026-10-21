---
key: 图片生成/文生图/Flux.2-klein-4b + SeedVR2_2012787694857883649.json
name: Flux.2-klein-4b + SeedVR2_2012787694857883649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2-klein-4b + SeedVR2_2012787694857883649.json
hash: a847ad403294b72f
coverage: 0.913043
learned_at: 2026-10-19 22:15:01
nodes: [KSamplerSelect, EmptyFlux2LatentImage, RandomNoise, ConditioningZeroOut, SamplerCustomAdvanced, VAELoader, Flux2Scheduler, LayerUtility: PurgeVRAM V2, CFGGuider, VAEDecode, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, PrimitiveInt, PrimitiveInt, ttN seed, SaveImage, SaveImage, CLIPTextEncode, easy promptList, Text, UNETLoader, CLIPLoader]
patterns: []
missing: []
---

# 图片生成/文生图/Flux.2-klein-4b + SeedVR2_2012787694857883649.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2-klein-4b + SeedVR2_2012787694857883649.json`

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
- `SaveImage`
- `CLIPTextEncode` ★核心
- `easy promptList`
- `Text`
- `UNETLoader` ★核心
- `CLIPLoader`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`KSamplerSelect`、`EmptyFlux2LatentImage`、`RandomNoise`、`ConditioningZeroOut`、`SamplerCustomAdvanced`、`VAELoader`、`Flux2Scheduler`、`LayerUtility: PurgeVRAM V2`、`CFGGuider`、`VAEDecode`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`ttN seed`、`SaveImage`、`CLIPTextEncode`、`easy promptList`、`Text`、`UNETLoader`、`CLIPLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、CFGGuider、KSamplerSelect

---
key: 图片生成/文生图/文生图（解禁模型）：Flux.2 Klein 9B_2051283326727663617.json
name: 文生图（解禁模型）：Flux.2 Klein 9B_2051283326727663617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图（解禁模型）：Flux.2 Klein 9B_2051283326727663617.json
hash: def8e46ba5a45518
coverage: 0.944444
learned_at: 2026-10-21 03:01:08
nodes: [VAELoader, RandomNoise, SamplerCustomAdvanced, CLIPLoader, ConditioningZeroOut, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, VAEDecode, SaveImage, Image Comparer (rgthree), UNETLoader, CLIPTextEncode, SaveImage]
patterns: []
missing: []
---

# 图片生成/文生图/文生图（解禁模型）：Flux.2 Klein 9B_2051283326727663617.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图（解禁模型）：Flux.2 Klein 9B_2051283326727663617.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `VAELoader`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `CLIPLoader`
- `ConditioningZeroOut`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`VAELoader`、`RandomNoise`、`SamplerCustomAdvanced`、`CLIPLoader`、`ConditioningZeroOut`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`VAEDecode`、`SaveImage`、`UNETLoader`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、CFGGuider、KSamplerSelect

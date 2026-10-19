---
key: 图片生成/文生图/👾怪獸-FLUX.2文生图+提示词扩写👾_1993647811195584514.json
name: 👾怪獸-FLUX.2文生图+提示词扩写👾_1993647811195584514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/👾怪獸-FLUX.2文生图+提示词扩写👾_1993647811195584514.json
hash: 9ba1e737f39dfa56
coverage: 0.823529
learned_at: 2026-10-19 21:33:48
nodes: [UNETLoader, Int, RH_LLMAPI_NODE, CLIPLoader, VAELoader, LayerUtility: PurgeVRAM V2, ConditioningZeroOut, FluxGuidance, CLIPTextEncode, VAEDecode, KSampler, SaveImage, Int, PrimitiveStringMultiline, PreviewAny, EmptyFlux2LatentImage, ImpactSwitch]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 633670228214707, "steps": 20}
---

# 图片生成/文生图/👾怪獸-FLUX.2文生图+提示词扩写👾_1993647811195584514.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/👾怪獸-FLUX.2文生图+提示词扩写👾_1993647811195584514.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `UNETLoader` ★核心
- `Int`
- `RH_LLMAPI_NODE`
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: PurgeVRAM V2`
- `ConditioningZeroOut`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `Int`
- `PrimitiveStringMultiline`
- `PreviewAny`
- `EmptyFlux2LatentImage`
- `ImpactSwitch`

## 关键参数

- `seed` = `633670228214707`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`UNETLoader`、`Int`、`RH_LLMAPI_NODE`、`CLIPLoader`、`VAELoader`、`LayerUtility: PurgeVRAM V2`、`ConditioningZeroOut`、`FluxGuidance`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`SaveImage`、`EmptyFlux2LatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、FluxGuidance

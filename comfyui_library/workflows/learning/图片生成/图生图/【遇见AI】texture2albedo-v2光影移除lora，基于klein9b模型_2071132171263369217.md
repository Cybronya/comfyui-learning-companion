---
key: 图片生成/图生图/【遇见AI】texture2albedo-v2光影移除lora，基于klein9b模型_2071132171263369217.json
name: 【遇见AI】texture2albedo-v2光影移除lora，基于klein9b模型_2071132171263369217
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】texture2albedo-v2光影移除lora，基于klein9b模型_2071132171263369217.json
hash: d742988802d43c71
coverage: 0.918919
learned_at: 2026-10-23 11:52:22
nodes: [RandomNoise, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, VAEDecode, Flux2Scheduler, VAEEncode, FluxGuidance, ReferenceLatent, SaveImage, CLIPTextEncode, ImpactImageInfo, RandomNoise, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, Flux2Scheduler, CLIPTextEncode, ImpactImageInfo, FluxGuidance, SaveImage, VAEDecode, ReferenceLatent, Image Comparer (rgthree), Image Comparer (rgthree), MarkdownNote, VAEEncode, LoadImage, LoadImage, UNETLoader, CLIPLoader, VAELoader, UNETLoader, CLIPLoader, VAELoader, LoadImage, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 图片生成/图生图/【遇见AI】texture2albedo-v2光影移除lora，基于klein9b模型_2071132171263369217.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】texture2albedo-v2光影移除lora，基于klein9b模型_2071132171263369217.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `Flux2Scheduler`
- `VAEEncode` ★核心
- `FluxGuidance`
- `ReferenceLatent`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `ImpactImageInfo`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `Flux2Scheduler`
- `CLIPTextEncode` ★核心
- `ImpactImageInfo`
- `FluxGuidance`
- `SaveImage`
- `VAEDecode` ★核心
- `ReferenceLatent`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `MarkdownNote`
- `VAEEncode` ★核心
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **92%**（34/37）

**有卡**：`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEDecode`、`Flux2Scheduler`、`VAEEncode`、`FluxGuidance`、`ReferenceLatent`、`SaveImage`、`CLIPTextEncode`、`ImpactImageInfo`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance

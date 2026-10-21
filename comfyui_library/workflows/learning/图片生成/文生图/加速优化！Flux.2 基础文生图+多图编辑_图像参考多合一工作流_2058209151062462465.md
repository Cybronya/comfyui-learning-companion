---
key: 图片生成/文生图/加速优化！Flux.2 基础文生图+多图编辑_图像参考多合一工作流_2058209151062462465.json
name: 加速优化！Flux.2 基础文生图+多图编辑_图像参考多合一工作流_2058209151062462465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/加速优化！Flux.2 基础文生图+多图编辑_图像参考多合一工作流_2058209151062462465.json
hash: 25985ebdf44e18a2
coverage: 0.660714
learned_at: 2026-10-19 22:46:31
nodes: [BasicGuider, KSamplerSelect, RandomNoise, EmptyFlux2LatentImage, SamplerCustomAdvanced, Flux2Scheduler, VAEDecode, CLIPTextEncode, 1hew_AnySwitchSelect, ImageScaleToTotalPixels, ReferenceLatent, VAEEncode, ImageScaleToTotalPixels, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, easy imageRemBg, easy imageRemBg, VAEEncode, LoadImage, ReferenceLatent, LoadImage, easy imageRemBg, LoadImage, SetNode, SetNode, FluxGuidance, SetNode, PrimitiveInt, easy seed, PrimitiveInt, GetNode, SaveImage, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, PrimitiveInt, Int, Note, PrimitiveNode, Note, Anything Everywhere, Text, UNETLoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, EasyCache, PathchSageAttentionKJ, ModelPatchTorchSettings, Anything Everywhere, Anything Everywhere, VAELoader]
patterns: []
missing: []
---

# 图片生成/文生图/加速优化！Flux.2 基础文生图+多图编辑_图像参考多合一工作流_2058209151062462465.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/加速优化！Flux.2 基础文生图+多图编辑_图像参考多合一工作流_2058209151062462465.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `BasicGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `Flux2Scheduler`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `1hew_AnySwitchSelect`
- `ImageScaleToTotalPixels`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `easy imageRemBg`
- `easy imageRemBg`
- `VAEEncode` ★核心
- `LoadImage`
- `ReferenceLatent`
- `LoadImage`
- `easy imageRemBg`
- `LoadImage`
- `SetNode`
- `SetNode`
- `FluxGuidance`
- `SetNode`
- `PrimitiveInt`
- `easy seed`
- `PrimitiveInt`
- `GetNode`
- `SaveImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `Int`
- `Note`
- `PrimitiveNode`
- `Note`
- `Anything Everywhere`
- `Text`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EasyCache`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Anything Everywhere`
- `Anything Everywhere`
- `VAELoader`

## 知识

覆盖率 **66%**（37/56）

**有卡**：`BasicGuider`、`KSamplerSelect`、`RandomNoise`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`Flux2Scheduler`、`VAEDecode`、`CLIPTextEncode`、`1hew_AnySwitchSelect`、`ImageScaleToTotalPixels`、`ReferenceLatent`、`VAEEncode`、`easy imageRemBg`、`LoadImage`、`FluxGuidance`、`easy seed`、`SaveImage`、`Int`、`Text`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`EasyCache`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance

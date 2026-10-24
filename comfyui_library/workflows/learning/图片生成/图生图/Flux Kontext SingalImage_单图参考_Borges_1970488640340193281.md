---
key: 图片生成/图生图/Flux Kontext SingalImage_单图参考_Borges_1970488640340193281.json
name: Flux Kontext SingalImage_单图参考_Borges_1970488640340193281
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext SingalImage_单图参考_Borges_1970488640340193281.json
hash: d06a8ad53e2f356c
coverage: 0.826087
learned_at: 2026-10-23 10:57:25
nodes: [KSamplerSelect, BasicGuider, SetNode, SetNode, SetNode, BasicScheduler, VAEDecode, UNETLoader, VAELoader, SamplerCustomAdvanced, PreviewImage, LoadImage, RandomNoise, EmptyLatentImage, FluxGuidance, ReferenceLatent, VAEEncode, DualCLIPLoader, CLIPTextEncode, FluxKontextImageScale, SaveImage, Note Plus (mtb), LoadImageFromUrl]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1536, "width": 1024}
---

# 图片生成/图生图/Flux Kontext SingalImage_单图参考_Borges_1970488640340193281.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext SingalImage_单图参考_Borges_1970488640340193281.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `SetNode`
- `SetNode`
- `SetNode`
- `BasicScheduler`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `LoadImage`
- `RandomNoise`
- `EmptyLatentImage` ★核心
- `FluxGuidance`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `FluxKontextImageScale`
- `SaveImage`
- `Note Plus (mtb)`
- `LoadImageFromUrl`

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`KSamplerSelect`、`BasicGuider`、`BasicScheduler`、`VAEDecode`、`UNETLoader`、`VAELoader`、`SamplerCustomAdvanced`、`LoadImage`、`RandomNoise`、`EmptyLatentImage`、`FluxGuidance`、`ReferenceLatent`、`VAEEncode`、`DualCLIPLoader`、`CLIPTextEncode`、`FluxKontextImageScale`、`SaveImage`、`Note Plus (mtb)`、`LoadImageFromUrl`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、FluxGuidance、KSamplerSelect

---
key: 图片生成/图生图/Flux Kontext Inpaint_Borges_1970488705611952129.json
name: Flux Kontext Inpaint_Borges_1970488705611952129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Inpaint_Borges_1970488705611952129.json
hash: ba03c744a8be3e65
coverage: 0.846154
learned_at: 2026-10-23 10:57:23
nodes: [KSamplerSelect, BasicGuider, SetNode, SetNode, SetNode, BasicScheduler, UNETLoader, VAELoader, FluxGuidance, ReferenceLatent, DualCLIPLoader, RandomNoise, ImageScale, LoadImage, ResizeMask, Kontext Inpainting Conditioning, LoadImage, VAEEncode, FluxKontextImageScale, PreviewImage, SamplerCustomAdvanced, VAEDecode, SaveImage, CLIPTextEncode, Note Plus (mtb), LoadImageFromUrl]
patterns: []
missing: []
---

# 图片生成/图生图/Flux Kontext Inpaint_Borges_1970488705611952129.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Inpaint_Borges_1970488705611952129.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `SetNode`
- `SetNode`
- `SetNode`
- `BasicScheduler`
- `UNETLoader` ★核心
- `VAELoader`
- `FluxGuidance`
- `ReferenceLatent`
- `DualCLIPLoader`
- `RandomNoise`
- `ImageScale`
- `LoadImage`
- `ResizeMask`
- `Kontext Inpainting Conditioning`
- `LoadImage`
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `PreviewImage`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `Note Plus (mtb)`
- `LoadImageFromUrl`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`KSamplerSelect`、`BasicGuider`、`BasicScheduler`、`UNETLoader`、`VAELoader`、`FluxGuidance`、`ReferenceLatent`、`DualCLIPLoader`、`RandomNoise`、`ImageScale`、`LoadImage`、`ResizeMask`、`Kontext Inpainting Conditioning`、`VAEEncode`、`FluxKontextImageScale`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`Note Plus (mtb)`、`LoadImageFromUrl`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced

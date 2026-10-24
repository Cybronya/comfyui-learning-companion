---
key: 图片生成/图生图/Flux Kontext 2imagePlus_双图参考改进版_Borges_1970488674284675073.json
name: Flux Kontext 2imagePlus_双图参考改进版_Borges_1970488674284675073
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext 2imagePlus_双图参考改进版_Borges_1970488674284675073.json
hash: 98c2664eaeb006ed
coverage: 0.518519
learned_at: 2026-10-23 10:56:22
nodes: [KSamplerSelect, SamplerCustomAdvanced, VAEDecode, RMBG, RMBG, RMBG, SetNode, GetNode, GoogleTranslateTextNode, GetNode, SetNode, LoadImage, SetNode, RMBG, GetNode, GetNode, Any Switch (rgthree), Any Switch (rgthree), SetNode, SetNode, easy showAnything, Any Switch (rgthree), SetNode, Note, BasicScheduler, SetNode, SetNode, GetNode, CLIPTextEncode, FluxGuidance, ReferenceLatent, BasicGuider, GetNode, GetNode, ModelSamplingFlux, DualCLIPLoader, VAELoader, UNETLoader, VAEEncode, GetNode, GetNode, ImageStitch, EmptyLatentImage, PreviewImage, Fast Groups Muter (rgthree), FluxResolutionNode, Fast Groups Muter (rgthree), ResizeImageMixlab, LoadImage, JjkText, SaveImage, RandomNoise, Note Plus (mtb), LoadImageFromUrl]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1280, "width": 1024}
---

# 图片生成/图生图/Flux Kontext 2imagePlus_双图参考改进版_Borges_1970488674284675073.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext 2imagePlus_双图参考改进版_Borges_1970488674284675073.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `RMBG`
- `RMBG`
- `RMBG`
- `SetNode`
- `GetNode`
- `GoogleTranslateTextNode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `RMBG`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `Any Switch (rgthree)`
- `SetNode`
- `Note`
- `BasicScheduler`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ReferenceLatent`
- `BasicGuider`
- `GetNode`
- `GetNode`
- `ModelSamplingFlux`
- `DualCLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `ImageStitch`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `Fast Groups Muter (rgthree)`
- `FluxResolutionNode`
- `Fast Groups Muter (rgthree)`
- `ResizeImageMixlab`
- `LoadImage`
- `JjkText`
- `SaveImage`
- `RandomNoise`
- `Note Plus (mtb)`
- `LoadImageFromUrl`

## 关键参数

- `width` = `1024`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **52%**（28/54）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEDecode`、`RMBG`、`GoogleTranslateTextNode`、`LoadImage`、`BasicScheduler`、`CLIPTextEncode`、`FluxGuidance`、`ReferenceLatent`、`BasicGuider`、`ModelSamplingFlux`、`DualCLIPLoader`、`VAELoader`、`UNETLoader`、`VAEEncode`、`ImageStitch`、`EmptyLatentImage`、`FluxResolutionNode`、`ResizeImageMixlab`、`SaveImage`、`RandomNoise`、`Note Plus (mtb)`、`LoadImageFromUrl`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、FluxGuidance、KSamplerSelect

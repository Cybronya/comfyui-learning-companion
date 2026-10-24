---
key: 图片生成/图生图/Flux Kontext 2imagePlus_双图参考改进版_Borges_1951581485935570946.json
name: Flux Kontext 2imagePlus_双图参考改进版_Borges_1951581485935570946
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext 2imagePlus_双图参考改进版_Borges_1951581485935570946.json
hash: 4cd39b7fecc0cedc
coverage: 0.5
learned_at: 2026-10-23 10:56:22
nodes: [KSamplerSelect, SamplerCustomAdvanced, VAEDecode, RMBG, RMBG, RMBG, SetNode, GetNode, GoogleTranslateTextNode, GetNode, LoadImage, SetNode, LoadImage, SetNode, RMBG, GetNode, GetNode, Any Switch (rgthree), Any Switch (rgthree), SetNode, SetNode, easy showAnything, Any Switch (rgthree), SetNode, Note, BasicScheduler, SetNode, SetNode, GetNode, CLIPTextEncode, FluxGuidance, ReferenceLatent, BasicGuider, GetNode, GetNode, ModelSamplingFlux, DualCLIPLoader, VAELoader, UNETLoader, VAEEncode, GetNode, GetNode, ImageStitch, EmptyLatentImage, SaveImage, FluxResolutionNode, RandomNoise, PreviewImage, JjkText, Note Plus (mtb), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1280, "width": 1024}
---

# 图片生成/图生图/Flux Kontext 2imagePlus_双图参考改进版_Borges_1951581485935570946.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext 2imagePlus_双图参考改进版_Borges_1951581485935570946.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
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
- `LoadImage`
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
- `SaveImage`
- `FluxResolutionNode`
- `RandomNoise`
- `PreviewImage`
- `JjkText`
- `Note Plus (mtb)`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **50%**（26/52）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEDecode`、`RMBG`、`GoogleTranslateTextNode`、`LoadImage`、`BasicScheduler`、`CLIPTextEncode`、`FluxGuidance`、`ReferenceLatent`、`BasicGuider`、`ModelSamplingFlux`、`DualCLIPLoader`、`VAELoader`、`UNETLoader`、`VAEEncode`、`ImageStitch`、`EmptyLatentImage`、`SaveImage`、`FluxResolutionNode`、`RandomNoise`、`Note Plus (mtb)`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、FluxGuidance、KSamplerSelect

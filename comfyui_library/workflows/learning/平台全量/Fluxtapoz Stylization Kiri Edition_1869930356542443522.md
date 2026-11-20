---
key: 平台全量/Fluxtapoz Stylization Kiri Edition_1869930356542443522.json
name: Fluxtapoz Stylization Kiri Edition_1869930356542443522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Fluxtapoz Stylization Kiri Edition_1869930356542443522.json
hash: 2b920b0ef24f8b1a
coverage: 0.576271
learned_at: 2026-11-14 00:30:15
nodes: [BasicGuider, FluxDeGuidance, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, easy imageSize, INTConstant, INTConstant, FluxReverseODESampler, SamplerCustomAdvanced, CLIPTextEncode, GetNode, VAEEncode, GetNode, GetNode, BasicGuider, SamplerCustomAdvanced, DisableNoise, FluxForwardODESampler, FlipSigmas, InFluxModelSamplingPred, BasicScheduler, GetNode, GetNode, GetNode, FluxDeGuidance, GetNode, GetNode, GetNode, GetNode, VAEDecode, DisableNoise, GetNode, BasicScheduler, OutFluxModelSamplingPred, CLIPTextEncode, LatentUpscaleBy, GetNode, ViewText, Fast Groups Bypasser (rgthree), UNETLoader, DualCLIPLoader, VAELoader, CLIPTextEncode, RH_Captioner, LoraLoaderModelOnly, Note, Image Comparer (rgthree), PreviewImage, VAEDecode, SaveImage, PreviewImage, LoadImage, KSampler (Efficient), Note]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 711884786501255, "steps": 33}
---

# 平台全量/Fluxtapoz Stylization Kiri Edition_1869930356542443522.json

> 来源文件 `comfyui_library/workflows/平台全量/Fluxtapoz Stylization Kiri Edition_1869930356542443522.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `BasicGuider`
- `FluxDeGuidance`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy imageSize`
- `INTConstant`
- `INTConstant`
- `FluxReverseODESampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `DisableNoise`
- `FluxForwardODESampler` ★核心
- `FlipSigmas`
- `InFluxModelSamplingPred`
- `BasicScheduler`
- `GetNode`
- `GetNode`
- `GetNode`
- `FluxDeGuidance`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `DisableNoise`
- `GetNode`
- `BasicScheduler`
- `OutFluxModelSamplingPred`
- `CLIPTextEncode` ★核心
- `LatentUpscaleBy`
- `GetNode`
- `ViewText`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `RH_Captioner`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `LoadImage`
- `KSampler (Efficient)` ★核心
- `Note`

## 关键参数

- `seed` = `711884786501255`
- `steps` = `33`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **58%**（34/59）

**有卡**：`BasicGuider`、`FluxDeGuidance`、`easy imageSize`、`INTConstant`、`FluxReverseODESampler`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`VAEEncode`、`DisableNoise`、`FluxForwardODESampler`、`FlipSigmas`、`InFluxModelSamplingPred`、`BasicScheduler`、`VAEDecode`、`OutFluxModelSamplingPred`、`LatentUpscaleBy`、`ViewText`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`RH_Captioner`、`LoraLoaderModelOnly`、`SaveImage`、`LoadImage`、`KSampler (Efficient)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxDeGuidance、FluxForwardODESampler

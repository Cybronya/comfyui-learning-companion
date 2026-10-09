---
key: 图片生成/文生图/fluxtopaz RF inverse + controlnet_1958569814094725122.json
name: fluxtopaz RF inverse + controlnet_1958569814094725122.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/fluxtopaz RF inverse + controlnet_1958569814094725122.json
hash: 04a54e3ef026d7c2
coverage: 0.596491
learned_at: 2026-10-07 23:31:33
nodes: [SetNode, ImageScale, DisableNoise, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, VAEDecode, GetNode, FluxDeGuidance, FlipSigmas, InFluxModelSamplingPred, GetNode, SamplerCustomAdvanced, GetNode, GetNode, INTConstant, INTConstant, ImageConcatMulti, DualCLIPLoader, UNETLoader, GetNode, LoraLoaderModelOnly, GetNode, GetNode, OutFluxModelSamplingPred, GetNode, GetNode, VAELoader, GetNode, GetNode, BasicGuider, FluxDeGuidance, ControlNetLoader, LoadImage, VAEDecode, PreviewImage, Note, DisableNoise, BasicScheduler, VAEEncode, BasicGuider, FluxForwardODESampler, BasicScheduler, Note, SamplerCustomAdvanced, PreviewImage, SaveImage, LoadImage, CLIPTextEncode, CLIPTextEncode, AIO_Preprocessor, FluxUnionControlNetApply, FluxReverseODESampler]
patterns: []
missing: []
parameters: {"controlnet_strength": "canny"}
---

# 图片生成/文生图/fluxtopaz RF inverse + controlnet_1958569814094725122.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1958569814094725122.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `SetNode`
- `ImageScale`
- `DisableNoise`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `FluxDeGuidance`
- `FlipSigmas`
- `InFluxModelSamplingPred`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `ImageConcatMulti`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `OutFluxModelSamplingPred`
- `GetNode`
- `GetNode`
- `VAELoader`
- `GetNode`
- `GetNode`
- `BasicGuider`
- `FluxDeGuidance`
- `ControlNetLoader`
- `LoadImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `Note`
- `DisableNoise`
- `BasicScheduler`
- `VAEEncode` ★核心
- `BasicGuider`
- `FluxForwardODESampler` ★核心
- `BasicScheduler`
- `Note`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `SaveImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `AIO_Preprocessor`
- `FluxUnionControlNetApply` ★核心
- `FluxReverseODESampler` ★核心

## 关键参数

- `controlnet_strength` = `canny`

## 知识

覆盖率 **60%**（34/57）

**有卡**：`ImageScale`、`DisableNoise`、`VAEDecode`、`FluxDeGuidance`、`FlipSigmas`、`InFluxModelSamplingPred`、`SamplerCustomAdvanced`、`INTConstant`、`ImageConcatMulti`、`DualCLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`OutFluxModelSamplingPred`、`VAELoader`、`BasicGuider`、`ControlNetLoader`、`LoadImage`、`BasicScheduler`、`VAEEncode`、`FluxForwardODESampler`、`SaveImage`、`CLIPTextEncode`、`AIO_Preprocessor`、`FluxUnionControlNetApply`、`FluxReverseODESampler`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、ControlNetLoader、FluxUnionControlNetApply

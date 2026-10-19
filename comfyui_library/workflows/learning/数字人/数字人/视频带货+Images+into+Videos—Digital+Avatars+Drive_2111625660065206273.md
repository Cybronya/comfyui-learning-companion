---
key: 数字人/数字人/视频带货+Images+into+Videos—Digital+Avatars+Drive_2111625660065206273.json
name: 视频带货+Images+into+Videos—Digital+Avatars+Drive_2111625660065206273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/视频带货+Images+into+Videos—Digital+Avatars+Drive_2111625660065206273.json
hash: a75542dde9602d2e
coverage: 0.757576
learned_at: 2026-10-19 00:41:12
nodes: [VAELoader, VAELoader, LoraLoaderModelOnly, UNETLoader, VAEDecodeAudio, VAEDecode, SetNode, SamplerCustomAdvanced, SetNode, ComfyMathExpression, LTXVSeparateAVLatent, LTXVConcatAVLatent, ManualSigmas, BasicScheduler, GetNode, KSamplerSelect, BasicGuider, CLIPLoader, RandomNoise, BasicGuider, GetNode, GetNode, SamplerCustomAdvanced, MiniMaxH3ReferenceToVideo, SetNode, MinimaxH3LatentUpscaler3D, LoadImage, LoadImage, VHS_VideoCombine, PrimitiveFloat, ResolutionSelector, JjkText, LoadImage]
patterns: []
missing: []
---

# 数字人/数字人/视频带货+Images+into+Videos—Digital+Avatars+Drive_2111625660065206273.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/视频带货+Images+into+Videos—Digital+Avatars+Drive_2111625660065206273.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（33 个）：
- `VAELoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `ComfyMathExpression`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `BasicScheduler`
- `GetNode`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `CLIPLoader`
- `RandomNoise`
- `BasicGuider`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3ReferenceToVideo`
- `SetNode`
- `MinimaxH3LatentUpscaler3D`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `PrimitiveFloat`
- `ResolutionSelector`
- `JjkText`
- `LoadImage`

## 知识

覆盖率 **76%**（25/33）

**有卡**：`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`ManualSigmas`、`BasicScheduler`、`KSamplerSelect`、`BasicGuider`、`CLIPLoader`、`RandomNoise`、`MiniMaxH3ReferenceToVideo`、`MinimaxH3LatentUpscaler3D`、`LoadImage`、`VHS_VideoCombine`、`ResolutionSelector`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

---
key: 视频生成/图生视频/视频带货+Images+into+Videos—Digital+Avatars+Drive_2101558136091013122.json
name: 视频带货+Images+into+Videos—Digital+Avatars+Drive_2101558136091013122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/视频带货+Images+into+Videos—Digital+Avatars+Drive_2101558136091013122.json
hash: e32021be502861e3
coverage: 0.742857
learned_at: 2026-10-17 02:15:12
nodes: [VAELoader, VAELoader, LoraLoaderModelOnly, UNETLoader, VAEDecodeAudio, VAEDecode, SetNode, SamplerCustomAdvanced, SetNode, ComfyMathExpression, LTXVSeparateAVLatent, LTXVConcatAVLatent, ManualSigmas, BasicScheduler, GetNode, KSamplerSelect, BasicGuider, CLIPLoader, RandomNoise, BasicGuider, GetNode, GetNode, SamplerCustomAdvanced, MiniMaxH3ReferenceToVideo, SetNode, MinimaxH3LatentUpscaler3D, LoadImage, LoadImage, VHS_VideoCombine, PrimitiveFloat, ResolutionSelector, LoadImage, JjkText, EmptyImage, PreviewImage]
patterns: []
missing: []
---

# 视频生成/图生视频/视频带货+Images+into+Videos—Digital+Avatars+Drive_2101558136091013122.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/视频带货+Images+into+Videos—Digital+Avatars+Drive_2101558136091013122.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
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
- `LoadImage`
- `JjkText`
- `EmptyImage`
- `PreviewImage`

## 知识

覆盖率 **74%**（26/35）

**有卡**：`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`ManualSigmas`、`BasicScheduler`、`KSamplerSelect`、`BasicGuider`、`CLIPLoader`、`RandomNoise`、`MiniMaxH3ReferenceToVideo`、`MinimaxH3LatentUpscaler3D`、`LoadImage`、`VHS_VideoCombine`、`ResolutionSelector`、`EmptyImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

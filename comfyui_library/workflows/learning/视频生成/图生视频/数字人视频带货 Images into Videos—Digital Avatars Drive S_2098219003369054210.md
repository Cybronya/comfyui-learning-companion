---
key: 视频生成/图生视频/数字人视频带货 Images into Videos—Digital Avatars Drive S_2098219003369054210.json
name: 数字人视频带货 Images into Videos—Digital Avatars Drive S_2098219003369054210
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/数字人视频带货 Images into Videos—Digital Avatars Drive S_2098219003369054210.json
hash: 4665c4eced9a74c3
coverage: 0.757576
learned_at: 2026-10-17 01:45:13
nodes: [VAELoader, VAELoader, LoraLoaderModelOnly, UNETLoader, VAEDecodeAudio, VAEDecode, SetNode, SamplerCustomAdvanced, SetNode, ComfyMathExpression, LTXVSeparateAVLatent, LTXVConcatAVLatent, ManualSigmas, BasicScheduler, GetNode, KSamplerSelect, BasicGuider, CLIPLoader, RandomNoise, BasicGuider, GetNode, GetNode, SamplerCustomAdvanced, MiniMaxH3ReferenceToVideo, SetNode, MinimaxH3LatentUpscaler3D, LoadImage, LoadImage, LoadImage, JjkText, VHS_VideoCombine, PrimitiveFloat, ResolutionSelector]
patterns: []
missing: []
---

# 视频生成/图生视频/数字人视频带货 Images into Videos—Digital Avatars Drive S_2098219003369054210.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/数字人视频带货 Images into Videos—Digital Avatars Drive S_2098219003369054210.json`

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
- `LoadImage`
- `JjkText`
- `VHS_VideoCombine`
- `PrimitiveFloat`
- `ResolutionSelector`

## 知识

覆盖率 **76%**（25/33）

**有卡**：`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`ManualSigmas`、`BasicScheduler`、`KSamplerSelect`、`BasicGuider`、`CLIPLoader`、`RandomNoise`、`MiniMaxH3ReferenceToVideo`、`MinimaxH3LatentUpscaler3D`、`LoadImage`、`VHS_VideoCombine`、`ResolutionSelector`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

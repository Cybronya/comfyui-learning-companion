---
key: 视频生成/图生视频/MiniMax-H3_ Digital Avatars for Video E-co数字人视频带货！_2095315877355937794.json
name: MiniMax-H3_ Digital Avatars for Video E-co数字人视频带货！_2095315877355937794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3_ Digital Avatars for Video E-co数字人视频带货！_2095315877355937794.json
hash: 574d764907228839
coverage: 0.735294
learned_at: 2026-10-17 00:02:27
nodes: [VAELoader, VAELoader, LoraLoaderModelOnly, UNETLoader, VAEDecodeAudio, VAEDecode, SetNode, SamplerCustomAdvanced, SetNode, ComfyMathExpression, LTXVSeparateAVLatent, LTXVConcatAVLatent, ManualSigmas, BasicScheduler, MarkdownNote, GetNode, KSamplerSelect, BasicGuider, CLIPLoader, RandomNoise, BasicGuider, GetNode, GetNode, SamplerCustomAdvanced, MiniMaxH3ReferenceToVideo, SetNode, MinimaxH3LatentUpscaler3D, LoadImage, LoadImage, LoadImage, JjkText, ResolutionSelector, PrimitiveFloat, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax-H3_ Digital Avatars for Video E-co数字人视频带货！_2095315877355937794.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3_ Digital Avatars for Video E-co数字人视频带货！_2095315877355937794.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（34 个）：
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
- `MarkdownNote`
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
- `ResolutionSelector`
- `PrimitiveFloat`
- `VHS_VideoCombine`

## 知识

覆盖率 **74%**（25/34）

**有卡**：`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`ManualSigmas`、`BasicScheduler`、`KSamplerSelect`、`BasicGuider`、`CLIPLoader`、`RandomNoise`、`MiniMaxH3ReferenceToVideo`、`MinimaxH3LatentUpscaler3D`、`LoadImage`、`ResolutionSelector`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

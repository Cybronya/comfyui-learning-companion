---
key: 视频生成/图生视频/MiniMax-H3_ Digital Avatars for Video E-co数字人视频带货_2108165309235548162.json
name: MiniMax-H3_ Digital Avatars for Video E-co数字人视频带货_2108165309235548162
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3_ Digital Avatars for Video E-co数字人视频带货_2108165309235548162.json
hash: ce1cbe1759b102e2
coverage: 0.735294
learned_at: 2026-10-17 22:18:21
nodes: [VAELoader, VAELoader, LoraLoaderModelOnly, UNETLoader, VAEDecodeAudio, VAEDecode, SetNode, SamplerCustomAdvanced, SetNode, ComfyMathExpression, LTXVSeparateAVLatent, LTXVConcatAVLatent, ManualSigmas, BasicScheduler, MarkdownNote, GetNode, KSamplerSelect, BasicGuider, CLIPLoader, RandomNoise, BasicGuider, GetNode, GetNode, SamplerCustomAdvanced, MiniMaxH3ReferenceToVideo, SetNode, MinimaxH3LatentUpscaler3D, ResolutionSelector, PrimitiveFloat, VHS_VideoCombine, LoadImage, JjkText, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax-H3_ Digital Avatars for Video E-co数字人视频带货_2108165309235548162.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3_ Digital Avatars for Video E-co数字人视频带货_2108165309235548162.json`

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
- `ResolutionSelector`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `LoadImage`
- `JjkText`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **74%**（25/34）

**有卡**：`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`ManualSigmas`、`BasicScheduler`、`KSamplerSelect`、`BasicGuider`、`CLIPLoader`、`RandomNoise`、`MiniMaxH3ReferenceToVideo`、`MinimaxH3LatentUpscaler3D`、`ResolutionSelector`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

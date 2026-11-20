---
key: 数字人/数字人/MiniMax-H3_Digital_Avatars_for_Video_E-co数字人视频带货！_2115216078598135809.json
name: MiniMax-H3_Digital_Avatars_for_Video_E-co数字人视频带货！_2115216078598135809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/MiniMax-H3_Digital_Avatars_for_Video_E-co数字人视频带货！_2115216078598135809.json
hash: 4adccc2db89bf336
coverage: 0.735294
learned_at: 2026-10-30 17:56:36
nodes: [VAELoader, VAELoader, LoraLoaderModelOnly, UNETLoader, VAEDecodeAudio, VAEDecode, SetNode, SamplerCustomAdvanced, SetNode, ComfyMathExpression, LTXVSeparateAVLatent, LTXVConcatAVLatent, ManualSigmas, BasicScheduler, MarkdownNote, GetNode, KSamplerSelect, BasicGuider, CLIPLoader, RandomNoise, BasicGuider, GetNode, GetNode, SamplerCustomAdvanced, MiniMaxH3ReferenceToVideo, SetNode, MinimaxH3LatentUpscaler3D, LoadImage, LoadImage, LoadImage, JjkText, ResolutionSelector, PrimitiveFloat, VHS_VideoCombine]
patterns: []
missing: []
---

# 数字人/数字人/MiniMax-H3_Digital_Avatars_for_Video_E-co数字人视频带货！_2115216078598135809.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/MiniMax-H3_Digital_Avatars_for_Video_E-co数字人视频带货！_2115216078598135809.json`

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

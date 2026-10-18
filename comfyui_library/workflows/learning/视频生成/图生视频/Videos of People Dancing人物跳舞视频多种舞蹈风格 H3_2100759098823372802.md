---
key: 视频生成/图生视频/Videos of People Dancing人物跳舞视频多种舞蹈风格 H3_2100759098823372802.json
name: Videos of People Dancing人物跳舞视频多种舞蹈风格 H3_2100759098823372802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Videos of People Dancing人物跳舞视频多种舞蹈风格 H3_2100759098823372802.json
hash: 67673909b86b68ad
coverage: 0.868421
learned_at: 2026-10-17 02:14:37
nodes: [VAELoader, VAELoader, ManualSigmas, VAEDecode, VAEDecodeAudio, SplitSigmas, CLIPLoader, SamplerCustomAdvanced, KSamplerSelect, SamplerCustomAdvanced, ManualSigmas, BasicScheduler, BasicGuider, BasicGuider, ManualSigmas, LTXVSeparateAVLatent, VAEDecode, VAEDecodeAudio, ModelAttentionBackend, MiniMaxH3SigmaShift, RandomNoise, MarkdownNote, VHS_VideoCombine, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, UNETLoader, ModelPreviewOverrideKJ, MinimaxH3LatentUpscaler3D, LTXVConcatAVLatent, ResolutionSelector, RHHiddenNodes, easy showAnything, ComfyMathExpression, PrimitiveFloat, MarkdownNote, CR Prompt Text, Note, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Videos of People Dancing人物跳舞视频多种舞蹈风格 H3_2100759098823372802.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Videos of People Dancing人物跳舞视频多种舞蹈风格 H3_2100759098823372802.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（38 个）：
- `VAELoader`
- `VAELoader`
- `ManualSigmas`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SplitSigmas`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `BasicScheduler`
- `BasicGuider`
- `BasicGuider`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `ModelAttentionBackend`
- `MiniMaxH3SigmaShift`
- `RandomNoise`
- `MarkdownNote`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3ReferenceToVideo`
- `UNETLoader` ★核心
- `ModelPreviewOverrideKJ`
- `MinimaxH3LatentUpscaler3D`
- `LTXVConcatAVLatent`
- `ResolutionSelector`
- `RHHiddenNodes`
- `easy showAnything`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `MarkdownNote`
- `CR Prompt Text`
- `Note`
- `LoadImage`

## 知识

覆盖率 **87%**（33/38）

**有卡**：`VAELoader`、`ManualSigmas`、`VAEDecode`、`VAEDecodeAudio`、`SplitSigmas`、`CLIPLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`LTXVSeparateAVLatent`、`ModelAttentionBackend`、`MiniMaxH3SigmaShift`、`RandomNoise`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`MiniMaxH3ReferenceToVideo`、`UNETLoader`、`ModelPreviewOverrideKJ`、`MinimaxH3LatentUpscaler3D`、`LTXVConcatAVLatent`、`ResolutionSelector`、`RHHiddenNodes`、`ComfyMathExpression`、`CR Prompt Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

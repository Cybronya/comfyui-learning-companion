---
key: 视频生成/图生视频/H3_People_Dancing人物跳舞多种舞蹈风格+跳舞自动机-Minimax+_2107443341985148930.json
name: H3_People_Dancing人物跳舞多种舞蹈风格+跳舞自动机-Minimax+_2107443341985148930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/H3_People_Dancing人物跳舞多种舞蹈风格+跳舞自动机-Minimax+_2107443341985148930.json
hash: 2548c959ec196b56
coverage: 0.85
learned_at: 2026-10-17 22:17:21
nodes: [VAELoader, VAELoader, ManualSigmas, VAEDecode, VAEDecodeAudio, SplitSigmas, CLIPLoader, SamplerCustomAdvanced, KSamplerSelect, SamplerCustomAdvanced, ManualSigmas, BasicScheduler, BasicGuider, BasicGuider, ManualSigmas, LTXVSeparateAVLatent, VAEDecode, VAEDecodeAudio, ModelAttentionBackend, MiniMaxH3SigmaShift, RandomNoise, MarkdownNote, VHS_VideoCombine, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, UNETLoader, ModelPreviewOverrideKJ, MinimaxH3LatentUpscaler3D, LTXVConcatAVLatent, ResolutionSelector, RHHiddenNodes, easy showAnything, ComfyMathExpression, PrimitiveFloat, MarkdownNote, CR Prompt Text, Note, LoadImage, EmptyImage, PreviewImage]
patterns: []
missing: []
---

# 视频生成/图生视频/H3_People_Dancing人物跳舞多种舞蹈风格+跳舞自动机-Minimax+_2107443341985148930.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/H3_People_Dancing人物跳舞多种舞蹈风格+跳舞自动机-Minimax+_2107443341985148930.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
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
- `EmptyImage`
- `PreviewImage`

## 知识

覆盖率 **85%**（34/40）

**有卡**：`VAELoader`、`ManualSigmas`、`VAEDecode`、`VAEDecodeAudio`、`SplitSigmas`、`CLIPLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`LTXVSeparateAVLatent`、`ModelAttentionBackend`、`MiniMaxH3SigmaShift`、`RandomNoise`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`MiniMaxH3ReferenceToVideo`、`UNETLoader`、`ModelPreviewOverrideKJ`、`MinimaxH3LatentUpscaler3D`、`LTXVConcatAVLatent`、`ResolutionSelector`、`RHHiddenNodes`、`ComfyMathExpression`、`CR Prompt Text`、`LoadImage`、`EmptyImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

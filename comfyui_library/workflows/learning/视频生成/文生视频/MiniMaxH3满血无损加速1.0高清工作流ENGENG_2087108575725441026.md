---
key: 视频生成/文生视频/MiniMaxH3满血无损加速1.0高清工作流ENGENG_2087108575725441026.json
name: MiniMaxH3满血无损加速1.0高清工作流ENGENG_2087108575725441026
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMaxH3满血无损加速1.0高清工作流ENGENG_2087108575725441026.json
hash: 3b563211c3132691
coverage: 0.688172
learned_at: 2026-10-15 22:46:28
nodes: [ResolutionSelector, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, CreateVideo, BasicScheduler, MarkdownNote, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicGuider, RandomNoise, CreateVideo, BasicScheduler, SamplerCustomAdvanced, SaveVideo, MarkdownNote, ComfyMathExpression, ComfyMathExpression, CLIPLoader, KSamplerSelect, BasicGuider, RandomNoise, MiniMaxH3ReferenceToVideo, LoadImage, PrimitiveFloat, ResolutionSelector, PrimitiveFloat, MarkdownNote, MarkdownNote, MarkdownNote, SaveVideo, MiniMaxH3ReferenceToVideo, CLIPLoader, BasicGuider, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, BasicScheduler, ComfyMathExpression, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Groups Bypasser (rgthree), Note, UniBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Groups Bypasser (rgthree), Note, UNETLoader, UniBlockSwap, EasyCache, PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Groups Bypasser (rgthree), Note, LoadImage, LoadImage, LoadImage, UNETLoader, Fast Groups Bypasser (rgthree), UNETLoader, MarkdownNote, SamplerCustomAdvanced, VAEDecodeAudio, VAEDecode, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, CLIPLoader, VAELoader, VAELoader, LoadImage, MarkdownNote, UniBlockSwap, EasyCache, EasyCache, PrimitiveStringMultiline, PrimitiveStringMultiline, VHS_VideoCombine, MarkdownNote, Note, Note, Note, Note, Note, Note, Note, Note]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMaxH3满血无损加速1.0高清工作流ENGENG_2087108575725441026.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMaxH3满血无损加速1.0高清工作流ENGENG_2087108575725441026.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（93 个）：
- `ResolutionSelector`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `BasicScheduler`
- `MarkdownNote`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `CreateVideo`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `SaveVideo`
- `MarkdownNote`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `PrimitiveFloat`
- `ResolutionSelector`
- `PrimitiveFloat`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `SaveVideo`
- `MiniMaxH3ReferenceToVideo`
- `CLIPLoader`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `ComfyMathExpression`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `UniBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `UNETLoader` ★核心
- `UniBlockSwap`
- `EasyCache`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoadImage`
- `MarkdownNote`
- `UniBlockSwap`
- `EasyCache`
- `EasyCache`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `MarkdownNote`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`

## 知识

覆盖率 **69%**（64/93）

**有卡**：`ResolutionSelector`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`CreateVideo`、`BasicScheduler`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`SaveVideo`、`ComfyMathExpression`、`CLIPLoader`、`MiniMaxH3ReferenceToVideo`、`LoadImage`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`UniBlockSwap`、`UNETLoader`、`EasyCache`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

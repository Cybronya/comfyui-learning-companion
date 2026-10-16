---
key: 视频生成/图生视频/MiniMaxH3-ref2va超级加速版-仅支持1.0分辨率_2089629306782834690.json
name: MiniMaxH3-ref2va超级加速版-仅支持1.0分辨率_2089629306782834690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMaxH3-ref2va超级加速版-仅支持1.0分辨率_2089629306782834690.json
hash: 2b13b671651934e1
coverage: 0.506849
learned_at: 2026-10-16 22:02:07
nodes: [SetNode, GetNode, GetNode, BasicGuider, GetNode, GetNode, VAEDecode, VAEDecodeAudio, SetNode, SetNode, SetNode, MarkdownNote, ImageScale, ImageScale, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, MarkdownNote, ImageScale, MarkdownNote, SetNode, GetNode, GetNode, VHS_VideoCombine, ImageScale, ImageScale, LoadImage, ImageScale, MiniMaxH3TurboSampler, SetNode, SetNode, Note, SetNode, Text Multiline, LoadImage, easy compare, ComfyMathExpression, SetNode, SetNode, GetNode, Note, Label (rgthree), Label (rgthree), SetNode, ModelPatchTorchSettings, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveInt, LoadImage, LoadImage, LoadImage, LoadImage, UNETLoader, CLIPLoader, VAELoader, VAELoader, MiniMaxH3TurboLoRA, PrimitiveFloat, BasicScheduler, RandomNoise, SamplerCustomAdvanced, SetNode, GetNode, SetNode, MiniMaxH3ReferenceToVideo, MarkdownNote, LoadAudio, LoadAudio, LoadAudio, ResolutionSelector]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMaxH3-ref2va超级加速版-仅支持1.0分辨率_2089629306782834690.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMaxH3-ref2va超级加速版-仅支持1.0分辨率_2089629306782834690.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（73 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `BasicGuider`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `ImageScale`
- `ImageScale`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `ImageScale`
- `MarkdownNote`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `ImageScale`
- `ImageScale`
- `LoadImage`
- `ImageScale`
- `MiniMaxH3TurboSampler` ★核心
- `SetNode`
- `SetNode`
- `Note`
- `SetNode`
- `Text Multiline`
- `LoadImage`
- `easy compare`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `GetNode`
- `Note`
- `Label (rgthree)`
- `Label (rgthree)`
- `SetNode`
- `ModelPatchTorchSettings`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `MiniMaxH3TurboLoRA`
- `PrimitiveFloat`
- `BasicScheduler`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `MiniMaxH3ReferenceToVideo`
- `MarkdownNote`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `ResolutionSelector`

## 知识

覆盖率 **51%**（37/73）

**有卡**：`BasicGuider`、`VAEDecode`、`VAEDecodeAudio`、`ImageScale`、`VHS_VideoCombine`、`LoadImage`、`MiniMaxH3TurboSampler`、`Text Multiline`、`easy compare`、`ComfyMathExpression`、`Label (rgthree)`、`ModelPatchTorchSettings`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`MiniMaxH3TurboLoRA`、`BasicScheduler`、`RandomNoise`、`SamplerCustomAdvanced`、`MiniMaxH3ReferenceToVideo`、`LoadAudio`、`ResolutionSelector`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3TurboSampler

---
key: 平台全量/MinimaxH3_Char_Swap 视频角色替换 支持表情跟踪 ComfyUI 工作流_2110617485354561538.json
name: MinimaxH3_Char_Swap 视频角色替换 支持表情跟踪 ComfyUI 工作流_2110617485354561538
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/MinimaxH3_Char_Swap 视频角色替换 支持表情跟踪 ComfyUI 工作流_2110617485354561538.json
hash: d641dccc0f776dd4
coverage: 0.581818
learned_at: 2026-11-14 00:45:59
nodes: [SetNode, SetNode, SetNode, MiniMaxChunkFeedForward, ModelPatchTorchSettings, GetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, VAEDecodeAudio, MarkdownNote, VAEDecode, SeedNode, StringConcatenate, SetNode, PrimitiveFloat, GetNode, KSamplerSelect, BasicScheduler, GetNode, RandomNoise, SamplerCustomAdvanced, BasicGuider, GetNode, Note, SetNode, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, XB_CanvasLabel, UNETLoader, CLIPLoader, VAELoader, VAELoader, ComfyMathExpression, SetNode, floatToInt _O, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageResizeKJv2, ResolutionSelector, PrimitiveFloat, VHS_LoadVideo, VedaSparseAttention, SetNode, MiniMaxH3SigmaShift, LoadImage, Note, VHS_VideoCombine, ImageResizeKJv2]
patterns: []
missing: []
---

# 平台全量/MinimaxH3_Char_Swap 视频角色替换 支持表情跟踪 ComfyUI 工作流_2110617485354561538.json

> 来源文件 `comfyui_library/workflows/平台全量/MinimaxH3_Char_Swap 视频角色替换 支持表情跟踪 ComfyUI 工作流_2110617485354561538.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（55 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `MiniMaxChunkFeedForward`
- `ModelPatchTorchSettings`
- `GetNode`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PathchSageAttentionKJ`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `MarkdownNote`
- `VAEDecode` ★核心
- `SeedNode`
- `StringConcatenate`
- `SetNode`
- `PrimitiveFloat`
- `GetNode`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `GetNode`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `GetNode`
- `Note`
- `SetNode`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `XB_CanvasLabel`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `ComfyMathExpression`
- `SetNode`
- `floatToInt _O`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `ResolutionSelector`
- `PrimitiveFloat`
- `VHS_LoadVideo`
- `VedaSparseAttention`
- `SetNode`
- `MiniMaxH3SigmaShift`
- `LoadImage`
- `Note`
- `VHS_VideoCombine`
- `ImageResizeKJv2`

## 知识

覆盖率 **58%**（32/55）

**有卡**：`MiniMaxChunkFeedForward`、`ModelPatchTorchSettings`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`PathchSageAttentionKJ`、`VAEDecodeAudio`、`VAEDecode`、`SeedNode`、`StringConcatenate`、`KSamplerSelect`、`BasicScheduler`、`RandomNoise`、`SamplerCustomAdvanced`、`BasicGuider`、`MiniMaxH3ReferenceToVideo`、`XB_CanvasLabel`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ComfyMathExpression`、`floatToInt _O`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`ResolutionSelector`、`VHS_LoadVideo`、`VedaSparseAttention`、`MiniMaxH3SigmaShift`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

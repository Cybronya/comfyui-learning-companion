---
key: 视频生成/图生视频/MinimaxH3_Char_Swap_视频角色替换_支持表情跟踪_ComfyUI_工作流_2114187327802273794.json
name: MinimaxH3_Char_Swap_视频角色替换_支持表情跟踪_ComfyUI_工作流_2114187327802273794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MinimaxH3_Char_Swap_视频角色替换_支持表情跟踪_ComfyUI_工作流_2114187327802273794.json
hash: d03eeb3f547f73ef
coverage: 0.578947
learned_at: 2026-10-26 22:13:48
nodes: [SetNode, SetNode, SetNode, MiniMaxChunkFeedForward, ModelPatchTorchSettings, GetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, VAEDecodeAudio, MarkdownNote, VAEDecode, SeedNode, StringConcatenate, SetNode, PrimitiveFloat, GetNode, KSamplerSelect, BasicScheduler, GetNode, RandomNoise, SamplerCustomAdvanced, BasicGuider, GetNode, Note, SetNode, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, XB_CanvasLabel, UNETLoader, CLIPLoader, VAELoader, VAELoader, ComfyMathExpression, SetNode, floatToInt _O, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageResizeKJv2, ResolutionSelector, PrimitiveFloat, VHS_LoadVideo, VedaSparseAttention, SetNode, MiniMaxH3SigmaShift, LoadImage, Note, VHS_VideoCombine, ImageResizeKJv2, EmptyImage, PreviewImage]
patterns: []
missing: []
---

# 视频生成/图生视频/MinimaxH3_Char_Swap_视频角色替换_支持表情跟踪_ComfyUI_工作流_2114187327802273794.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MinimaxH3_Char_Swap_视频角色替换_支持表情跟踪_ComfyUI_工作流_2114187327802273794.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
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
- `EmptyImage`
- `PreviewImage`

## 知识

覆盖率 **58%**（33/57）

**有卡**：`MiniMaxChunkFeedForward`、`ModelPatchTorchSettings`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`PathchSageAttentionKJ`、`VAEDecodeAudio`、`VAEDecode`、`SeedNode`、`StringConcatenate`、`KSamplerSelect`、`BasicScheduler`、`RandomNoise`、`SamplerCustomAdvanced`、`BasicGuider`、`MiniMaxH3ReferenceToVideo`、`XB_CanvasLabel`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ComfyMathExpression`、`floatToInt _O`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`ResolutionSelector`、`VHS_LoadVideo`、`VedaSparseAttention`、`MiniMaxH3SigmaShift`、`LoadImage`、`VHS_VideoCombine`、`EmptyImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

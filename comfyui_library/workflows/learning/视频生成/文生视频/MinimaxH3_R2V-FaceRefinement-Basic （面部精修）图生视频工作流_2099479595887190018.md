---
key: 视频生成/文生视频/MinimaxH3_R2V-FaceRefinement-Basic （面部精修）图生视频工作流_2099479595887190018.json
name: MinimaxH3_R2V-FaceRefinement-Basic （面部精修）图生视频工作流_2099479595887190018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MinimaxH3_R2V-FaceRefinement-Basic （面部精修）图生视频工作流_2099479595887190018.json
hash: 492dc0dc5fdbdf11
coverage: 0.557143
learned_at: 2026-10-15 22:46:44
nodes: [MarkdownNote, PrimitiveFloat, SetNode, SetNode, SetNode, SetNode, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, MiniMaxH3SigmaShift, SetNode, SeedNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, BasicGuider, GetNode, BasicScheduler, GetNode, RandomNoise, KSamplerSelect, GetNode, VAEDecodeAudio, SamplerCustomAdvanced, SetNode, GetNode, GetNode, GetNode, H3PerFrameDenoise, GetNode, RandomNoise, GetNode, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, GetNode, GetNode, GetNode, VAEDecode, ResolutionSelector, VAEDecode, MiniMaxH3ReferenceToVideo, H3InjectVideoLatent, BasicScheduler, H3FaceStitch, VHS_VideoCombine, VHS_VideoCombine, PrimitiveFloat, ComfyMathExpression, PrimitiveFloat, VHS_VideoCombine, StringConcatenate, MiniMaxH3ReferenceToVideo, LoadAudio, UNETLoader, CLIPLoader, SetNode, VAELoader, SetNode, VAELoader, LoraLoaderModelOnly, ModelPatchTorchSettings, H3FaceTrackCrop, ImageResizeKJv2, PrimitiveStringMultiline, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/MinimaxH3_R2V-FaceRefinement-Basic （面部精修）图生视频工作流_2099479595887190018.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MinimaxH3_R2V-FaceRefinement-Basic （面部精修）图生视频工作流_2099479595887190018.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（70 个）：
- `MarkdownNote`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PathchSageAttentionKJ`
- `MiniMaxH3SigmaShift`
- `SetNode`
- `SeedNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `BasicGuider`
- `GetNode`
- `BasicScheduler`
- `GetNode`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `GetNode`
- `VAEDecodeAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `H3PerFrameDenoise`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `ResolutionSelector`
- `VAEDecode` ★核心
- `MiniMaxH3ReferenceToVideo`
- `H3InjectVideoLatent`
- `BasicScheduler`
- `H3FaceStitch`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `StringConcatenate`
- `MiniMaxH3ReferenceToVideo`
- `LoadAudio`
- `UNETLoader` ★核心
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `H3FaceTrackCrop`
- `ImageResizeKJv2`
- `PrimitiveStringMultiline`
- `LoadImage`

## 知识

覆盖率 **56%**（39/70）

**有卡**：`MiniMaxChunkFeedForward`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`PathchSageAttentionKJ`、`MiniMaxH3SigmaShift`、`SeedNode`、`BasicGuider`、`BasicScheduler`、`RandomNoise`、`KSamplerSelect`、`VAEDecodeAudio`、`SamplerCustomAdvanced`、`H3PerFrameDenoise`、`VAEDecode`、`ResolutionSelector`、`MiniMaxH3ReferenceToVideo`、`H3InjectVideoLatent`、`H3FaceStitch`、`VHS_VideoCombine`、`ComfyMathExpression`、`StringConcatenate`、`LoadAudio`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`ModelPatchTorchSettings`、`H3FaceTrackCrop`、`ImageResizeKJv2`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

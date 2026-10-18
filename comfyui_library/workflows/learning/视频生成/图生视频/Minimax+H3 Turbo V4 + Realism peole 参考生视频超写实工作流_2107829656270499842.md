---
key: 视频生成/图生视频/Minimax+H3 Turbo V4 + Realism peole 参考生视频超写实工作流_2107829656270499842.json
name: Minimax+H3 Turbo V4 + Realism peole 参考生视频超写实工作流_2107829656270499842
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax+H3 Turbo V4 + Realism peole 参考生视频超写实工作流_2107829656270499842.json
hash: 3e4614a179ba19f1
coverage: 0.386555
learned_at: 2026-10-17 22:18:45
nodes: [SetNode, LoadImage, LoadImage, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_LoadVideo, SetNode, SetNode, SetNode, VHS_LoadVideo, SetNode, SetNode, LoadImage, LoadImage, LoadImage, SetNode, SetNode, SetNode, GetNode, SetNode, Reroute, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecodeAudio, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, MiniMaxH3ReferenceToVideo, ComfyMathExpression, SetNode, SamplerCustomAdvanced, SetNode, BasicGuider, SetNode, SetNode, SetNode, VAEDecode, VAEDecodeAudio, GetNode, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, SetNode, LoadAudio, SetNode, LoadAudio, SetNode, RandomNoise, KSamplerSelect, SplitSigmas, LoadImage, VHS_LoadVideo, Note, VHS_VideoCombine, SamplerCustomAdvanced, SetNode, Note, MinimaxH3LatentUpscaler3D, BasicScheduler, MarkdownNote, Note, VHS_VideoCombine, LoadAudio, LoadImage, LoadImage, LoadImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, VAELoader, Note, MiniMaxH3MemoryEfficientSageAttentionPatch, SetNode, LoraLoaderModelOnly, Note, LoraLoaderModelOnly, Note, PrimitiveFloat, ResolutionSelector, Text, easy float, SetNode, SetNode, GetNode, Note, MiniMaxH3DualClockSamplerT8]
patterns: []
missing: []
---

# 视频生成/图生视频/Minimax+H3 Turbo V4 + Realism peole 参考生视频超写实工作流_2107829656270499842.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax+H3 Turbo V4 + Realism peole 参考生视频超写实工作流_2107829656270499842.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（119 个）：
- `SetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `Reroute`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
- `ComfyMathExpression`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `BasicGuider`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SetNode`
- `LoadAudio`
- `SetNode`
- `LoadAudio`
- `SetNode`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `SplitSigmas`
- `LoadImage`
- `VHS_LoadVideo`
- `Note`
- `VHS_VideoCombine`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `Note`
- `MinimaxH3LatentUpscaler3D`
- `BasicScheduler`
- `MarkdownNote`
- `Note`
- `VHS_VideoCombine`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `Note`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `PrimitiveFloat`
- `ResolutionSelector`
- `Text`
- `easy float`
- `SetNode`
- `SetNode`
- `GetNode`
- `Note`
- `MiniMaxH3DualClockSamplerT8` ★核心

## 知识

覆盖率 **39%**（46/119）

**有卡**：`LoadImage`、`VHS_LoadVideo`、`VAEDecodeAudio`、`VAEDecode`、`MiniMaxH3ReferenceToVideo`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`BasicGuider`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LoadAudio`、`RandomNoise`、`KSamplerSelect`、`SplitSigmas`、`VHS_VideoCombine`、`MinimaxH3LatentUpscaler3D`、`BasicScheduler`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ResolutionSelector`、`Text`、`easy float`、`MiniMaxH3DualClockSamplerT8`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

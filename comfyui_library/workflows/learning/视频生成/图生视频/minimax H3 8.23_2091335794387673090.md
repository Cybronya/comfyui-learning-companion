---
key: 视频生成/图生视频/minimax H3 8.23_2091335794387673090.json
name: minimax H3 8.23_2091335794387673090
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/minimax H3 8.23_2091335794387673090.json
hash: f2406c8e9d984535
coverage: 0.942857
learned_at: 2026-10-16 22:30:50
nodes: [CLIPLoader, VAELoader, BasicGuider, RandomNoise, MiniMaxH3AVDecodeT8, SamplerCustomAdvanced, ComfyMathExpression, MiniMaxH3DualClockSamplerT8, VHS_VideoCombine, MiniMaxH3MemoryEfficientSageAttentionPatch, VAELoader, MiniMaxH3AudioConditioningT8, ModelAttentionBackend, SolAttnMiniMax, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, UNETLoader, LoraLoaderBypassModelOnly, LoadAudio, LoadAudio, LoadAudio, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, PrimitiveFloat, MarkdownNote, CR Prompt Text, ResolutionSelector, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/minimax H3 8.23_2091335794387673090.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/minimax H3 8.23_2091335794387673090.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Other

**节点**（35 个）：
- `CLIPLoader`
- `VAELoader`
- `BasicGuider`
- `RandomNoise`
- `MiniMaxH3AVDecodeT8`
- `SamplerCustomAdvanced` ★核心
- `ComfyMathExpression`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `VHS_VideoCombine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `VAELoader`
- `MiniMaxH3AudioConditioningT8`
- `ModelAttentionBackend`
- `SolAttnMiniMax`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `PrimitiveFloat`
- `MarkdownNote`
- `CR Prompt Text`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **94%**（33/35）

**有卡**：`CLIPLoader`、`VAELoader`、`BasicGuider`、`RandomNoise`、`MiniMaxH3AVDecodeT8`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`MiniMaxH3DualClockSamplerT8`、`VHS_VideoCombine`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3AudioConditioningT8`、`ModelAttentionBackend`、`SolAttnMiniMax`、`LoadImage`、`UNETLoader`、`LoraLoaderBypassModelOnly`、`LoadAudio`、`easy cleanGpuUsed`、`CR Prompt Text`、`ResolutionSelector`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8

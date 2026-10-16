---
key: 视频生成/图生视频/(双时钟-8步高质量极速)Minimax参考生视频V2（Lightx2v1.1）_2090388161544417282.json
name: (双时钟-8步高质量极速)Minimax参考生视频V2（Lightx2v1.1）_2090388161544417282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(双时钟-8步高质量极速)Minimax参考生视频V2（Lightx2v1.1）_2090388161544417282.json
hash: 47ccb5de25a61bd6
coverage: 0.931034
learned_at: 2026-10-16 22:01:50
nodes: [CLIPLoader, VAELoader, BasicGuider, RandomNoise, MiniMaxH3AVDecodeT8, MarkdownNote, SamplerCustomAdvanced, ComfyMathExpression, MiniMaxH3DualClockSamplerT8, CR Prompt Text, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, VAELoader, ModelAttentionBackend, SolAttnMiniMax, ResolutionSelector, PrimitiveFloat, UNETLoader, LoraLoaderBypassModelOnly, MiniMaxH3AudioConditioningT8]
patterns: []
missing: []
---

# 视频生成/图生视频/(双时钟-8步高质量极速)Minimax参考生视频V2（Lightx2v1.1）_2090388161544417282.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/(双时钟-8步高质量极速)Minimax参考生视频V2（Lightx2v1.1）_2090388161544417282.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Other

**节点**（29 个）：
- `CLIPLoader`
- `VAELoader`
- `BasicGuider`
- `RandomNoise`
- `MiniMaxH3AVDecodeT8`
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `ComfyMathExpression`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `CR Prompt Text`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `VAELoader`
- `ModelAttentionBackend`
- `SolAttnMiniMax`
- `ResolutionSelector`
- `PrimitiveFloat`
- `UNETLoader` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3AudioConditioningT8`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`CLIPLoader`、`VAELoader`、`BasicGuider`、`RandomNoise`、`MiniMaxH3AVDecodeT8`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`MiniMaxH3DualClockSamplerT8`、`CR Prompt Text`、`VHS_VideoCombine`、`LoadImage`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`SolAttnMiniMax`、`ResolutionSelector`、`UNETLoader`、`LoraLoaderBypassModelOnly`、`MiniMaxH3AudioConditioningT8`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8

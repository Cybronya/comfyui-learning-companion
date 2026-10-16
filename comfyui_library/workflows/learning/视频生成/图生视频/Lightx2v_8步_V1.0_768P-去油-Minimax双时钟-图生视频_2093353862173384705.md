---
key: 视频生成/图生视频/Lightx2v_8步_V1.0_768P-去油-Minimax双时钟-图生视频_2093353862173384705.json
name: Lightx2v_8步_V1.0_768P-去油-Minimax双时钟-图生视频_2093353862173384705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Lightx2v_8步_V1.0_768P-去油-Minimax双时钟-图生视频_2093353862173384705.json
hash: 326e918327478b57
coverage: 0.76
learned_at: 2026-10-16 23:42:09
nodes: [RandomNoise, MiniMaxH3AVDecodeT8, BasicGuider, SamplerCustomAdvanced, MiniMaxH3DualClockSamplerT8, MarkdownNote, MarkdownNote, MarkdownNote, ComfyMathExpression, VAELoader, VAELoader, CLIPLoader, ModelAttentionBackend, MiniMaxH3MemoryEfficientSageAttentionPatch, MarkdownNote, 孤海注释, PrimitiveFloat, UNETLoader, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, CR Prompt Text, MiniMaxH3AudioConditioningT8, ResolutionSelector, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Lightx2v_8步_V1.0_768P-去油-Minimax双时钟-图生视频_2093353862173384705.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Lightx2v_8步_V1.0_768P-去油-Minimax双时钟-图生视频_2093353862173384705.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Other

**节点**（25 个）：
- `RandomNoise`
- `MiniMaxH3AVDecodeT8`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ComfyMathExpression`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `ModelAttentionBackend`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MarkdownNote`
- `孤海注释`
- `PrimitiveFloat`
- `UNETLoader` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `CR Prompt Text`
- `MiniMaxH3AudioConditioningT8`
- `ResolutionSelector`
- `LoadImage`

## 知识

覆盖率 **76%**（19/25）

**有卡**：`RandomNoise`、`MiniMaxH3AVDecodeT8`、`BasicGuider`、`SamplerCustomAdvanced`、`MiniMaxH3DualClockSamplerT8`、`ComfyMathExpression`、`VAELoader`、`CLIPLoader`、`ModelAttentionBackend`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`UNETLoader`、`LoraLoaderBypassModelOnly`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`CR Prompt Text`、`MiniMaxH3AudioConditioningT8`、`ResolutionSelector`、`LoadImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8

---
key: 视频生成/视频生视频/MiniMax-H3-视频复刻-数字人-视频换人、视频换产品、视频换文案（替换原视频语音）.json
name: MiniMax-H3-视频复刻-数字人-视频换人、视频换产品、视频换文案（替换原视频语音）
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/视频生视频/MiniMax-H3-视频复刻-数字人-视频换人、视频换产品、视频换文案（替换原视频语音）.json
hash: 2752fca9a891d581
coverage: 0.6875
learned_at: 2026-10-15 22:49:16
nodes: [CLIPLoader, VAELoader, VAELoader, ComfyMathExpression, UNETLoader, SolAttnMiniMax, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, MiniMaxH3DualClockSamplerT8, BasicGuider, RandomNoise, MarkdownNote, SamplerCustomAdvanced, LoraLoaderBypassModelOnly, PrimitiveFloat, MarkdownNote, MarkdownNote, LoadImage, CR Prompt Text, LoadImage, MiniMaxH3AudioConditioningT8, ResolutionSelector, VHS_VideoCombine, MiniMaxH3AVDecodeT8, VHS_LoadVideo, MarkdownNote, 孤海注释, MarkdownNote, MarkdownNote, 孤海注释, VHS_LoadVideo, 孤海注释]
patterns: []
missing: []
---

# 视频生成/视频生视频/MiniMax-H3-视频复刻-数字人-视频换人、视频换产品、视频换文案（替换原视频语音）.json

> 来源文件 `comfyui_library/workflows/视频生成/视频生视频/MiniMax-H3-视频复刻-数字人-视频换人、视频换产品、视频换文案（替换原视频语音）.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Other

**节点**（32 个）：
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `ComfyMathExpression`
- `UNETLoader` ★核心
- `SolAttnMiniMax`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `BasicGuider`
- `RandomNoise`
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `PrimitiveFloat`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `CR Prompt Text`
- `LoadImage`
- `MiniMaxH3AudioConditioningT8`
- `ResolutionSelector`
- `VHS_VideoCombine`
- `MiniMaxH3AVDecodeT8`
- `VHS_LoadVideo`
- `MarkdownNote`
- `孤海注释`
- `MarkdownNote`
- `MarkdownNote`
- `孤海注释`
- `VHS_LoadVideo`
- `孤海注释`

## 知识

覆盖率 **69%**（22/32）

**有卡**：`CLIPLoader`、`VAELoader`、`ComfyMathExpression`、`UNETLoader`、`SolAttnMiniMax`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`MiniMaxH3DualClockSamplerT8`、`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`LoraLoaderBypassModelOnly`、`LoadImage`、`CR Prompt Text`、`MiniMaxH3AudioConditioningT8`、`ResolutionSelector`、`VHS_VideoCombine`、`MiniMaxH3AVDecodeT8`、`VHS_LoadVideo`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8

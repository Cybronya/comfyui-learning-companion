---
key: 视频生成/视频生视频/MiniMax-H3-视频复刻-数字人-视频换人、视频换产品、文案不换（保持原视频语音）.json
name: MiniMax-H3-视频复刻-数字人-视频换人、视频换产品、文案不换（保持原视频语音）
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/视频生视频/MiniMax-H3-视频复刻-数字人-视频换人、视频换产品、文案不换（保持原视频语音）.json
hash: 22cd60c727a7912d
coverage: 0.65625
learned_at: 2026-10-07 00:37:45
nodes: [CLIPLoader, VAELoader, VAELoader, ComfyMathExpression, UNETLoader, SolAttnMiniMax, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, MiniMaxH3DualClockSamplerT8, BasicGuider, RandomNoise, MarkdownNote, SamplerCustomAdvanced, LoraLoaderBypassModelOnly, PrimitiveFloat, MarkdownNote, MarkdownNote, LoadImage, CR Prompt Text, LoadImage, ResolutionSelector, VHS_LoadVideo, VHS_LoadVideo, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MarkdownNote, MarkdownNote, MarkdownNote, VHS_VideoCombine, 孤海注释, 孤海注释, 孤海注释]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/视频生视频/MiniMax-H3-视频复刻-数字人-视频换人、视频换产品、文案不换（保持原视频语音）.json

> 来源文件 `comfyui_library/workflows/视频生成/视频生视频/MiniMax-H3-视频复刻-数字人-视频换人、视频换产品、文案不换（保持原视频语音）.json`

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
- `ResolutionSelector`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `VHS_VideoCombine`
- `孤海注释`
- `孤海注释`
- `孤海注释`

## 知识

覆盖率 **66%**（21/32）

**有卡**：`CLIPLoader`、`VAELoader`、`ComfyMathExpression`、`UNETLoader`、`SolAttnMiniMax`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`MiniMaxH3DualClockSamplerT8`、`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`LoraLoaderBypassModelOnly`、`LoadImage`、`ResolutionSelector`、`VHS_LoadVideo`、`MiniMaxH3AVDecodeT8`、`MiniMaxH3AudioConditioningT8`、`VHS_VideoCombine`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明

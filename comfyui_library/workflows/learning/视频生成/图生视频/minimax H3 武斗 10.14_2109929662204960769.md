---
key: 视频生成/图生视频/minimax H3 武斗 10.14_2109929662204960769.json
name: minimax H3 武斗 10.14_2109929662204960769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/minimax H3 武斗 10.14_2109929662204960769.json
hash: 36f6cb83c7eed2b5
coverage: 0.944444
learned_at: 2026-10-18 00:24:03
nodes: [ResolutionSelector, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, SamplerCustomAdvanced, BasicGuider, UNETLoader, CLIPLoader, RandomNoise, ComfyMathExpression, PrimitiveFloat, MiniMaxH3ReferenceToVideo, LoraLoaderModelOnly, ManualSigmas, VHS_VideoCombine, ModelAttentionBackend, BlockSparseAttention, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, LoadAudio, LoadAudio, LoadAudio, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Text]
patterns: []
missing: []
---

# 视频生成/图生视频/minimax H3 武斗 10.14_2109929662204960769.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/minimax H3 武斗 10.14_2109929662204960769.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（36 个）：
- `ResolutionSelector`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `UNETLoader` ★核心
- `CLIPLoader`
- `RandomNoise`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `MiniMaxH3ReferenceToVideo`
- `LoraLoaderModelOnly` ★核心
- `ManualSigmas`
- `VHS_VideoCombine`
- `ModelAttentionBackend`
- `BlockSparseAttention`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Text`

## 知识

覆盖率 **94%**（34/36）

**有卡**：`ResolutionSelector`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`SamplerCustomAdvanced`、`BasicGuider`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`LoraLoaderModelOnly`、`ManualSigmas`、`VHS_VideoCombine`、`ModelAttentionBackend`、`BlockSparseAttention`、`LoadAudio`、`LoadImage`、`Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

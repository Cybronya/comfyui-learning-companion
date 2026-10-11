---
key: 视频生成/文生视频/【遇见AI】Minimax H3 的lightx2v正式版1.0加速lora，4步8步_2087808921359699970.json
name: 【遇见AI】Minimax H3 的lightx2v正式版1.0加速lora，4步8步_2087808921359699970
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【遇见AI】Minimax H3 的lightx2v正式版1.0加速lora，4步8步_2087808921359699970.json
hash: a4f0dae8e9309eca
coverage: 0.84
learned_at: 2026-10-11 20:53:51
nodes: [ResolutionSelector, KSamplerSelect, BasicGuider, SamplerCustomAdvanced, ComfyMathExpression, VAEDecodeAudio, VAEDecode, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, ModelAttentionBackend, BasicScheduler, MiniMaxH3ImageToVideo, MarkdownNote, MarkdownNote, SaveVideo, CreateVideo, LoadImage, MarkdownNote, LoadImage, UNETLoader, CLIPLoader, VAELoader, VAELoader, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 视频生成/文生视频/【遇见AI】Minimax H3 的lightx2v正式版1.0加速lora，4步8步_2087808921359699970.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【遇见AI】Minimax H3 的lightx2v正式版1.0加速lora，4步8步_2087808921359699970.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（25 个）：
- `ResolutionSelector`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `ComfyMathExpression`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ModelAttentionBackend`
- `BasicScheduler`
- `MiniMaxH3ImageToVideo`
- `MarkdownNote`
- `MarkdownNote`
- `SaveVideo`
- `CreateVideo`
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **84%**（21/25）

**有卡**：`ResolutionSelector`、`KSamplerSelect`、`BasicGuider`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`VAEDecodeAudio`、`VAEDecode`、`PathchSageAttentionKJ`、`RandomNoise`、`ModelAttentionBackend`、`BasicScheduler`、`MiniMaxH3ImageToVideo`、`SaveVideo`、`CreateVideo`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

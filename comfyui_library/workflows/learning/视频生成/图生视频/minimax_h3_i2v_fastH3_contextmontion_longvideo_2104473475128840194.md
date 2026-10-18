---
key: 视频生成/图生视频/minimax_h3_i2v_fastH3_contextmontion_longvideo_2104473475128840194.json
name: minimax_h3_i2v_fastH3_contextmontion_longvideo_2104473475128840194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/minimax_h3_i2v_fastH3_contextmontion_longvideo_2104473475128840194.json
hash: eb3d949fd8d19e55
coverage: 0.657895
learned_at: 2026-10-17 22:19:16
nodes: [VAEDecode, VAEDecodeAudio, VAELoader, MiniMaxH3ImageToVideo, PrimitiveFloat, CLIPLoader, ComfyMathExpression, SamplerCustomAdvanced, KSamplerSelect, MarkdownNote, MarkdownNote, BasicGuider, RandomNoise, VAELoader, UNETLoader, MiniMaxH3SigmaShift, ModelAttentionBackend, BlockSparseAttention, BasicScheduler, ResolutionSelector, VHS_VideoCombine, PrimitiveNode, SetNode, SetNode, SetNode, SetNode, SetNode, MiniMaxH3MotionContext, GetNode, GetNode, MiniMaxH3MotionContextChain, MiniMaxH3MotionContextTrim, SetNode, PrimitiveStringMultiline, LoadImage, LoadImage, MiniMaxH3MotionContextLoadLatent, MiniMaxH3MotionContextSaveLatent]
patterns: []
missing: []
---

# 视频生成/图生视频/minimax_h3_i2v_fastH3_contextmontion_longvideo_2104473475128840194.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/minimax_h3_i2v_fastH3_contextmontion_longvideo_2104473475128840194.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（38 个）：
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VAELoader`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `CLIPLoader`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `BasicGuider`
- `RandomNoise`
- `VAELoader`
- `UNETLoader` ★核心
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `BlockSparseAttention`
- `BasicScheduler`
- `ResolutionSelector`
- `VHS_VideoCombine`
- `PrimitiveNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MiniMaxH3MotionContext`
- `GetNode`
- `GetNode`
- `MiniMaxH3MotionContextChain`
- `MiniMaxH3MotionContextTrim`
- `SetNode`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3MotionContextLoadLatent`
- `MiniMaxH3MotionContextSaveLatent`

## 知识

覆盖率 **66%**（25/38）

**有卡**：`VAEDecode`、`VAEDecodeAudio`、`VAELoader`、`MiniMaxH3ImageToVideo`、`CLIPLoader`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`UNETLoader`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`BlockSparseAttention`、`BasicScheduler`、`ResolutionSelector`、`VHS_VideoCombine`、`MiniMaxH3MotionContext`、`MiniMaxH3MotionContextChain`、`MiniMaxH3MotionContextTrim`、`LoadImage`、`MiniMaxH3MotionContextLoadLatent`、`MiniMaxH3MotionContextSaveLatent`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

---
key: 视频生成/图生视频/【遇见AI】Minimax H3 长视频连续衔接插件 H3 Motion Context REF2V_2090326053301612546.json
name: 【遇见AI】Minimax H3 长视频连续衔接插件 H3 Motion Context REF2V_2090326053301612546
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【遇见AI】Minimax H3 长视频连续衔接插件 H3 Motion Context REF2V_2090326053301612546.json
hash: 4bf73b68fd0c7bfd
coverage: 0.933333
learned_at: 2026-10-16 22:02:23
nodes: [MiniMaxH3MemoryEfficientSageAttentionPatch, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, PrimitiveFloat, LoadAudio, VHS_LoadVideo, RandomNoise, BasicGuider, KSamplerSelect, BasicScheduler, MiniMaxH3MotionContextLoadLatent, MiniMaxH3MotionContext, MiniMaxH3MotionContextTrim, CreateVideo, SaveVideo, ResolutionSelector, ComfyMathExpression, MarkdownNote, LoadImage, LoadImage, UNETLoader, CLIPLoader, VAELoader, VAELoader, LoraLoaderModelOnly, LoadImage, LoadImage, MiniMaxH3ReferenceToVideo, MiniMaxH3MotionContextSaveLatent]
patterns: []
missing: []
---

# 视频生成/图生视频/【遇见AI】Minimax H3 长视频连续衔接插件 H3 Motion Context REF2V_2090326053301612546.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/【遇见AI】Minimax H3 长视频连续衔接插件 H3 Motion Context REF2V_2090326053301612546.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（30 个）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `PrimitiveFloat`
- `LoadAudio`
- `VHS_LoadVideo`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `MiniMaxH3MotionContextLoadLatent`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContextTrim`
- `CreateVideo`
- `SaveVideo`
- `ResolutionSelector`
- `ComfyMathExpression`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3MotionContextSaveLatent`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`MiniMaxH3MemoryEfficientSageAttentionPatch`、`SamplerCustomAdvanced`、`VAEDecode`、`VAEDecodeAudio`、`LoadAudio`、`VHS_LoadVideo`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`MiniMaxH3MotionContextLoadLatent`、`MiniMaxH3MotionContext`、`MiniMaxH3MotionContextTrim`、`CreateVideo`、`SaveVideo`、`ResolutionSelector`、`ComfyMathExpression`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`MiniMaxH3ReferenceToVideo`、`MiniMaxH3MotionContextSaveLatent`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

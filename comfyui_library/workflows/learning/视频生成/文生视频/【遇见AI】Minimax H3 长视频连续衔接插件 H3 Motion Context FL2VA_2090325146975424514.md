---
key: 视频生成/文生视频/【遇见AI】Minimax H3 长视频连续衔接插件 H3 Motion Context FL2VA_2090325146975424514.json
name: 【遇见AI】Minimax H3 长视频连续衔接插件 H3 Motion Context FL2VA_2090325146975424514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【遇见AI】Minimax H3 长视频连续衔接插件 H3 Motion Context FL2VA_2090325146975424514.json
hash: c92a81b43334a12b
coverage: 0.888889
learned_at: 2026-10-11 21:19:52
nodes: [BasicGuider, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, MiniMaxH3MemoryEfficientSageAttentionPatch, BasicScheduler, ResolutionSelector, PrimitiveFloat, MarkdownNote, VAEDecode, CreateVideo, SaveVideo, ComfyMathExpression, MiniMaxH3MotionContext, MiniMaxH3MotionContextTrim, MiniMaxH3MotionContextLoadLatent, MarkdownNote, LoadImage, LoadImage, UNETLoader, CLIPLoader, LoraLoaderModelOnly, MiniMaxH3MotionContextSaveLatent, VAEDecodeAudio, MiniMaxH3ImageToVideo, VAELoader, VAELoader]
patterns: []
missing: []
---

# 视频生成/文生视频/【遇见AI】Minimax H3 长视频连续衔接插件 H3 Motion Context FL2VA_2090325146975424514.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【遇见AI】Minimax H3 长视频连续衔接插件 H3 Motion Context FL2VA_2090325146975424514.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（27 个）：
- `BasicGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `BasicScheduler`
- `ResolutionSelector`
- `PrimitiveFloat`
- `MarkdownNote`
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `ComfyMathExpression`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContextTrim`
- `MiniMaxH3MotionContextLoadLatent`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3MotionContextSaveLatent`
- `VAEDecodeAudio` ★核心
- `MiniMaxH3ImageToVideo`
- `VAELoader`
- `VAELoader`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`BasicGuider`、`KSamplerSelect`、`RandomNoise`、`SamplerCustomAdvanced`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BasicScheduler`、`ResolutionSelector`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`ComfyMathExpression`、`MiniMaxH3MotionContext`、`MiniMaxH3MotionContextTrim`、`MiniMaxH3MotionContextLoadLatent`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`MiniMaxH3MotionContextSaveLatent`、`VAEDecodeAudio`、`MiniMaxH3ImageToVideo`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

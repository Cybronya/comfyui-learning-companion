---
key: 视频生成/图生视频/8步加速-Minimax参考生视频Sage Attention Patch+4步lora_2085390372628422658.json
name: 8步加速-Minimax参考生视频Sage Attention Patch+4步lora_2085390372628422658
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/8步加速-Minimax参考生视频Sage Attention Patch+4步lora_2085390372628422658.json
hash: 56443e26490c1d11
coverage: 0.846154
learned_at: 2026-10-16 20:50:18
nodes: [VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, BasicGuider, CLIPLoader, CreateVideo, MiniMaxH3ReferenceToVideo, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, RandomNoise, UNETLoader, MarkdownNote, LoraLoaderModelOnly, ComfyMathExpression, LoadImage, LoadImage, LoadImage, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, SaveVideo, PrimitiveFloat, ResolutionSelector, 孤海注释, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/图生视频/8步加速-Minimax参考生视频Sage Attention Patch+4步lora_2085390372628422658.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/8步加速-Minimax参考生视频Sage Attention Patch+4步lora_2085390372628422658.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（26 个）：
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `BasicGuider`
- `CLIPLoader`
- `CreateVideo`
- `MiniMaxH3ReferenceToVideo`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `RandomNoise`
- `UNETLoader` ★核心
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `ComfyMathExpression`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SaveVideo`
- `PrimitiveFloat`
- `ResolutionSelector`
- `孤海注释`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`BasicGuider`、`CLIPLoader`、`CreateVideo`、`MiniMaxH3ReferenceToVideo`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`RandomNoise`、`UNETLoader`、`LoraLoaderModelOnly`、`ComfyMathExpression`、`LoadImage`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`SaveVideo`、`ResolutionSelector`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

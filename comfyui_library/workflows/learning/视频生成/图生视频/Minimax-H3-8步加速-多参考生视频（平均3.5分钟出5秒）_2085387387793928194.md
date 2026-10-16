---
key: 视频生成/图生视频/Minimax-H3-8步加速-多参考生视频（平均3.5分钟出5秒）_2085387387793928194.json
name: Minimax-H3-8步加速-多参考生视频（平均3.5分钟出5秒）_2085387387793928194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax-H3-8步加速-多参考生视频（平均3.5分钟出5秒）_2085387387793928194.json
hash: d5b77dce2787918e
coverage: 0.851852
learned_at: 2026-10-16 20:50:33
nodes: [VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, BasicGuider, CLIPLoader, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, RandomNoise, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, PathchSageAttentionKJ, ResolutionSelector, PrimitiveFloat, PrimitiveFloat, CreateVideo, Note, UNETLoader, SaveVideo, ComfyMathExpression, LoadImage, MiniMaxH3ReferenceToVideo, LoadImage, ImageScaleToTotalPixels, ImageScaleToTotalPixels, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/图生视频/Minimax-H3-8步加速-多参考生视频（平均3.5分钟出5秒）_2085387387793928194.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax-H3-8步加速-多参考生视频（平均3.5分钟出5秒）_2085387387793928194.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `BasicGuider`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `RandomNoise`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ResolutionSelector`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `CreateVideo`
- `Note`
- `UNETLoader` ★核心
- `SaveVideo`
- `ComfyMathExpression`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`BasicGuider`、`CLIPLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`RandomNoise`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ResolutionSelector`、`CreateVideo`、`UNETLoader`、`SaveVideo`、`ComfyMathExpression`、`LoadImage`、`MiniMaxH3ReferenceToVideo`、`ImageScaleToTotalPixels`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

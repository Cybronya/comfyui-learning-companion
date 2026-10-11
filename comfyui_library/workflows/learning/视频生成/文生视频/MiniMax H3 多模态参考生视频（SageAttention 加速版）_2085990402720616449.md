---
key: 视频生成/文生视频/MiniMax H3 多模态参考生视频（SageAttention 加速版）_2085990402720616449.json
name: MiniMax H3 多模态参考生视频（SageAttention 加速版）_2085990402720616449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 多模态参考生视频（SageAttention 加速版）_2085990402720616449.json
hash: e72a9f8d86deff34
coverage: 0.875
learned_at: 2026-10-11 20:53:40
nodes: [SaveVideo, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, BasicGuider, CLIPLoader, RandomNoise, CreateVideo, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MiniMaxH3ReferenceToVideo, GetVideoComponents, LoadVideo, LoadVideo, LoadVideo, LoadAudio, LoadAudio, LoadAudio, ComfyMathExpression, GetVideoComponents, MarkdownNote, GetVideoComponents, MarkdownNote, ResolutionSelector, MarkdownNote, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, LoadImage, PrimitiveStringMultiline, PrimitiveFloat]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3 多模态参考生视频（SageAttention 加速版）_2085990402720616449.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 多模态参考生视频（SageAttention 加速版）_2085990402720616449.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（40 个）：
- `SaveVideo`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `CLIPLoader`
- `RandomNoise`
- `CreateVideo`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `GetVideoComponents`
- `LoadVideo`
- `LoadVideo`
- `LoadVideo`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `ComfyMathExpression`
- `GetVideoComponents`
- `MarkdownNote`
- `GetVideoComponents`
- `MarkdownNote`
- `ResolutionSelector`
- `MarkdownNote`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader` ★核心
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`SaveVideo`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`BasicGuider`、`CLIPLoader`、`RandomNoise`、`CreateVideo`、`LoadImage`、`MiniMaxH3ReferenceToVideo`、`GetVideoComponents`、`LoadVideo`、`LoadAudio`、`ComfyMathExpression`、`ResolutionSelector`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

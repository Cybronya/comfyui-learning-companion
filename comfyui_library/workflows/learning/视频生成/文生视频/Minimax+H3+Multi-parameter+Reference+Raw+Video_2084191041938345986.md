---
key: 视频生成/文生视频/Minimax+H3+Multi-parameter+Reference+Raw+Video_2084191041938345986.json
name: Minimax+H3+Multi-parameter+Reference+Raw+Video_2084191041938345986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Minimax+H3+Multi-parameter+Reference+Raw+Video_2084191041938345986.json
hash: f6ec81b724fc061b
coverage: 0.8
learned_at: 2026-10-15 22:46:40
nodes: [MarkdownNote, MarkdownNote, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, BasicGuider, UNETLoader, CLIPLoader, RandomNoise, CreateVideo, ComfyMathExpression, VAELoader, SaveVideo, MarkdownNote, ResolutionSelector, LoadVideo, MiniMaxH3ReferenceToVideo, VHS_LoadVideo, LoadImage, LoadImage, PrimitiveStringMultiline, PrimitiveFloat]
patterns: []
missing: []
---

# 视频生成/文生视频/Minimax+H3+Multi-parameter+Reference+Raw+Video_2084191041938345986.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Minimax+H3+Multi-parameter+Reference+Raw+Video_2084191041938345986.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（25 个）：
- `MarkdownNote`
- `MarkdownNote`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `UNETLoader` ★核心
- `CLIPLoader`
- `RandomNoise`
- `CreateVideo`
- `ComfyMathExpression`
- `VAELoader`
- `SaveVideo`
- `MarkdownNote`
- `ResolutionSelector`
- `LoadVideo`
- `MiniMaxH3ReferenceToVideo`
- `VHS_LoadVideo`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`

## 知识

覆盖率 **80%**（20/25）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`BasicGuider`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`CreateVideo`、`ComfyMathExpression`、`SaveVideo`、`ResolutionSelector`、`LoadVideo`、`MiniMaxH3ReferenceToVideo`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

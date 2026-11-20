---
key: 平台全量/video_minimax_h3_r2v_soundtrack_2119441622462193666.json
name: video_minimax_h3_r2v_soundtrack_2119441622462193666
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/video_minimax_h3_r2v_soundtrack_2119441622462193666.json
hash: 82ef0b452650125d
coverage: 0.807692
learned_at: 2026-11-14 01:18:41
nodes: [SaveVideo, ResolutionSelector, MarkdownNote, MarkdownNote, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, BasicGuider, UNETLoader, CLIPLoader, RandomNoise, CreateVideo, ComfyMathExpression, PrimitiveFloat, MiniMaxH3ReferenceToVideo, LoadImage, PrimitiveStringMultiline, LoadImage, MarkdownNote, LoadAudio, LoadAudio, LoadAudio]
patterns: []
missing: []
---

# 平台全量/video_minimax_h3_r2v_soundtrack_2119441622462193666.json

> 来源文件 `comfyui_library/workflows/平台全量/video_minimax_h3_r2v_soundtrack_2119441622462193666.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（26 个）：
- `SaveVideo`
- `ResolutionSelector`
- `MarkdownNote`
- `MarkdownNote`
- `VAELoader`
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
- `PrimitiveFloat`
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LoadImage`
- `MarkdownNote`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`

## 知识

覆盖率 **81%**（21/26）

**有卡**：`SaveVideo`、`ResolutionSelector`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`BasicGuider`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`CreateVideo`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`LoadImage`、`LoadAudio`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

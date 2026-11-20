---
key: 视频生成/图生视频/video_minimax_h3_r2v_spectrum_2116576147646533634.json
name: video_minimax_h3_r2v_spectrum_2116576147646533634
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/video_minimax_h3_r2v_spectrum_2116576147646533634.json
hash: 7c7769f0a66cdcae
coverage: 0.791667
learned_at: 2026-11-02 19:19:05
nodes: [SaveVideo, ResolutionSelector, MarkdownNote, MarkdownNote, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, BasicGuider, UNETLoader, CLIPLoader, RandomNoise, CreateVideo, ComfyMathExpression, PrimitiveFloat, MiniMaxH3ReferenceToVideo, LoadImage, PrimitiveStringMultiline, LoadImage, MarkdownNote, SpectrumApplyMiniMaxH3]
patterns: []
missing: []
---

# 视频生成/图生视频/video_minimax_h3_r2v_spectrum_2116576147646533634.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/video_minimax_h3_r2v_spectrum_2116576147646533634.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（24 个）：
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
- `SpectrumApplyMiniMaxH3`

## 知识

覆盖率 **79%**（19/24）

**有卡**：`SaveVideo`、`ResolutionSelector`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`BasicGuider`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`CreateVideo`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`LoadImage`、`SpectrumApplyMiniMaxH3`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

---
key: 视频生成/图生视频/MiniMax_ref2v_imgvideoaudio_2092306138221072386.json
name: MiniMax_ref2v_imgvideoaudio_2092306138221072386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax_ref2v_imgvideoaudio_2092306138221072386.json
hash: 235f6b76bbe4e286
coverage: 0.878788
learned_at: 2026-10-16 22:59:13
nodes: [KSamplerSelect, SamplerCustomAdvanced, BasicGuider, RandomNoise, ComfyMathExpression, BasicScheduler, VAEDecode, VAEDecodeAudio, MarkdownNote, VAELoader, VAELoader, PathchSageAttentionKJ, PainterVRAM, LoadAudio, VHS_LoadVideo, MarkdownNote, Label (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, MiniMaxH3ReferenceToVideo, UNETLoader, CLIPLoader, ResolutionSelector, PrimitiveFloat, LoadImage, LoadImage, LoadImage, LoadImage, VHS_VideoCombine, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax_ref2v_imgvideoaudio_2092306138221072386.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax_ref2v_imgvideoaudio_2092306138221072386.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（33 个）：
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `RandomNoise`
- `ComfyMathExpression`
- `BasicScheduler`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `MarkdownNote`
- `VAELoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `PainterVRAM`
- `LoadAudio`
- `VHS_LoadVideo`
- `MarkdownNote`
- `Label (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ResolutionSelector`
- `PrimitiveFloat`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `LoadImage`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **88%**（29/33）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`BasicGuider`、`RandomNoise`、`ComfyMathExpression`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`VAELoader`、`PathchSageAttentionKJ`、`PainterVRAM`、`LoadAudio`、`VHS_LoadVideo`、`Label (rgthree)`、`LoadImage`、`MiniMaxH3ReferenceToVideo`、`UNETLoader`、`CLIPLoader`、`ResolutionSelector`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

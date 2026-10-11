---
key: 视频生成/文生视频/MiniMax H3多合一｜Turbo4 + Sage + T8 Stable 组合加速版｜B站UP主@好奇漫步_2086728037277720578.json
name: MiniMax H3多合一｜Turbo4 + Sage + T8 Stable 组合加速版｜B站UP主@好奇漫步_2086728037277720578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3多合一｜Turbo4 + Sage + T8 Stable 组合加速版｜B站UP主@好奇漫步_2086728037277720578.json
hash: 3762b731b7544e9b
coverage: 0.847059
learned_at: 2026-10-11 20:53:42
nodes: [SaveVideo, MiniMaxH3ImageToVideo, SaveVideo, SaveVideo, UNETLoader, UNETLoader, KSamplerSelect, BasicScheduler, BasicScheduler, SamplerCustomAdvanced, VAEDecodeAudio, RandomNoise, BasicGuider, VAEDecode, CreateVideo, MiniMaxH3ImageToVideo, RandomNoise, BasicGuider, BasicGuider, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, CreateVideo, SamplerCustomAdvanced, VAELoader, VAELoader, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, MarkdownNote, ResolutionSelector, MarkdownNote, MarkdownNote, PrimitiveFloat, SaveVideo, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadVideo, LoadVideo, LoadImage, LoadVideo, LoadImage, CLIPLoader, GetVideoComponents, GetVideoComponents, GetVideoComponents, LoadAudio, LoadAudio, LoadAudio, BasicGuider, RandomNoise, VAEDecode, VAEDecodeAudio, SamplerCustomAdvanced, CreateVideo, VAEDecode, VAEDecodeAudio, CreateVideo, MiniMaxH3ReferenceToVideo, LoadImage, MarkdownNote, MarkdownNote, MarkdownNote, LoraLoaderBypassModelOnly, MiniMaxH3DualClockSamplerT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MarkdownNote, MiniMaxH3ImageToVideo, LoadImage, LoadImage, PrimitiveInt, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3多合一｜Turbo4 + Sage + T8 Stable 组合加速版｜B站UP主@好奇漫步_2086728037277720578.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3多合一｜Turbo4 + Sage + T8 Stable 组合加速版｜B站UP主@好奇漫步_2086728037277720578.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（85 个）：
- `SaveVideo`
- `MiniMaxH3ImageToVideo`
- `SaveVideo`
- `SaveVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeAudio` ★核心
- `RandomNoise`
- `BasicGuider`
- `VAEDecode` ★核心
- `CreateVideo`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `BasicGuider`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `VAELoader`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `MarkdownNote`
- `ResolutionSelector`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveFloat`
- `SaveVideo`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadVideo`
- `LoadVideo`
- `LoadImage`
- `LoadVideo`
- `LoadImage`
- `CLIPLoader`
- `GetVideoComponents`
- `GetVideoComponents`
- `GetVideoComponents`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `BasicGuider`
- `RandomNoise`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MarkdownNote`
- `MiniMaxH3ImageToVideo`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **85%**（72/85）

**有卡**：`SaveVideo`、`MiniMaxH3ImageToVideo`、`UNETLoader`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`RandomNoise`、`BasicGuider`、`VAEDecode`、`CreateVideo`、`VAELoader`、`ComfyMathExpression`、`ResolutionSelector`、`LoadImage`、`LoadVideo`、`CLIPLoader`、`GetVideoComponents`、`LoadAudio`、`MiniMaxH3ReferenceToVideo`、`LoraLoaderBypassModelOnly`、`MiniMaxH3DualClockSamplerT8`、`MiniMaxH3MemoryEfficientSageAttentionPatch`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

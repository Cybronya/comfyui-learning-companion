---
key: 视频生成/文生视频/MiniMax H3多合一｜V6_LightX2V官方Turbo4加速版｜B站UP主@好奇漫步_2086676399020142594.json
name: MiniMax H3多合一｜V6_LightX2V官方Turbo4加速版｜B站UP主@好奇漫步_2086676399020142594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3多合一｜V6_LightX2V官方Turbo4加速版｜B站UP主@好奇漫步_2086676399020142594.json
hash: 159fd0a6535c2ec2
coverage: 0.841463
learned_at: 2026-10-15 22:45:55
nodes: [SaveVideo, MiniMaxH3ImageToVideo, SaveVideo, SaveVideo, LoadImage, UNETLoader, UNETLoader, BasicGuider, VAEDecode, RandomNoise, BasicGuider, MiniMaxH3ImageToVideo, BasicGuider, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, CreateVideo, SamplerCustomAdvanced, VAELoader, VAELoader, ComfyMathExpression, MarkdownNote, ResolutionSelector, MarkdownNote, MarkdownNote, SaveVideo, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadVideo, LoadVideo, LoadImage, LoadVideo, LoadImage, CLIPLoader, GetVideoComponents, GetVideoComponents, GetVideoComponents, LoadAudio, LoadAudio, LoadAudio, BasicGuider, RandomNoise, VAEDecode, VAEDecodeAudio, SamplerCustomAdvanced, CreateVideo, VAEDecode, VAEDecodeAudio, CreateVideo, LoadImage, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, LoadImage, MiniMaxH3ReferenceToVideo, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, KSamplerSelect, MiniMaxH3ImageToVideo, LoraLoaderBypassModelOnly, RandomNoise, VAEDecodeAudio, CreateVideo, BasicScheduler, SamplerCustomAdvanced, MiniMaxH3DualClockSamplerT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3DualClockSamplerT8, PrimitiveInt, PrimitiveStringMultiline, PrimitiveFloat]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3多合一｜V6_LightX2V官方Turbo4加速版｜B站UP主@好奇漫步_2086676399020142594.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3多合一｜V6_LightX2V官方Turbo4加速版｜B站UP主@好奇漫步_2086676399020142594.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（82 个）：
- `SaveVideo`
- `MiniMaxH3ImageToVideo`
- `SaveVideo`
- `SaveVideo`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `BasicGuider`
- `VAEDecode` ★核心
- `RandomNoise`
- `BasicGuider`
- `MiniMaxH3ImageToVideo`
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
- `MarkdownNote`
- `ResolutionSelector`
- `MarkdownNote`
- `MarkdownNote`
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
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `KSamplerSelect` ★核心
- `MiniMaxH3ImageToVideo`
- `LoraLoaderBypassModelOnly` ★核心
- `RandomNoise`
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`

## 知识

覆盖率 **84%**（69/82）

**有卡**：`SaveVideo`、`MiniMaxH3ImageToVideo`、`LoadImage`、`UNETLoader`、`BasicGuider`、`VAEDecode`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`CreateVideo`、`VAELoader`、`ComfyMathExpression`、`ResolutionSelector`、`LoadVideo`、`CLIPLoader`、`GetVideoComponents`、`LoadAudio`、`MiniMaxH3ReferenceToVideo`、`KSamplerSelect`、`LoraLoaderBypassModelOnly`、`BasicScheduler`、`MiniMaxH3DualClockSamplerT8`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

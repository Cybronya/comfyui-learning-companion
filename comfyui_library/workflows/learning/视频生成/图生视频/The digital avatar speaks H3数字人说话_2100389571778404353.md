---
key: 视频生成/图生视频/The digital avatar speaks H3数字人说话_2100389571778404353.json
name: The digital avatar speaks H3数字人说话_2100389571778404353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/The digital avatar speaks H3数字人说话_2100389571778404353.json
hash: aef3f4ecb6331243
coverage: 0.827586
learned_at: 2026-10-17 01:59:21
nodes: [VAELoader, VAELoader, CLIPLoader, BasicGuider, JoinStrings, JoinStrings, VAEDecode, VAEDecodeAudio, AILab_QwenVL, MiniMaxH3ReferenceToVideo, JoinStrings, RandomNoise, SamplerCustomAdvanced, CreateVideo, PathchSageAttentionKJ, PrimitiveStringMultiline, ComfyMathExpression, PrimitiveStringMultiline, KSamplerSelect, UNETLoader, BasicScheduler, AudioCrop, LoadImage, PrimitiveStringMultiline, SaveVideo, LoadAudio, MarkdownNote, PrimitiveFloat, ResolutionSelector]
patterns: []
missing: []
---

# 视频生成/图生视频/The digital avatar speaks H3数字人说话_2100389571778404353.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/The digital avatar speaks H3数字人说话_2100389571778404353.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（29 个）：
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `BasicGuider`
- `JoinStrings`
- `JoinStrings`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `AILab_QwenVL`
- `MiniMaxH3ReferenceToVideo`
- `JoinStrings`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `ComfyMathExpression`
- `PrimitiveStringMultiline`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `BasicScheduler`
- `AudioCrop`
- `LoadImage`
- `PrimitiveStringMultiline`
- `SaveVideo`
- `LoadAudio`
- `MarkdownNote`
- `PrimitiveFloat`
- `ResolutionSelector`

## 知识

覆盖率 **83%**（24/29）

**有卡**：`VAELoader`、`CLIPLoader`、`BasicGuider`、`JoinStrings`、`VAEDecode`、`VAEDecodeAudio`、`AILab_QwenVL`、`MiniMaxH3ReferenceToVideo`、`RandomNoise`、`SamplerCustomAdvanced`、`CreateVideo`、`PathchSageAttentionKJ`、`ComfyMathExpression`、`KSamplerSelect`、`UNETLoader`、`BasicScheduler`、`AudioCrop`、`LoadImage`、`SaveVideo`、`LoadAudio`、`ResolutionSelector`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

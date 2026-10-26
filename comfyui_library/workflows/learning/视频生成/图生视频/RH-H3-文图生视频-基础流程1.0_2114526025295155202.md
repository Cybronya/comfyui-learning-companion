---
key: 视频生成/图生视频/RH-H3-文图生视频-基础流程1.0_2114526025295155202.json
name: RH-H3-文图生视频-基础流程1.0_2114526025295155202
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/RH-H3-文图生视频-基础流程1.0_2114526025295155202.json
hash: dd74496819ba09da
coverage: 0.869565
learned_at: 2026-10-26 22:13:57
nodes: [PrimitiveFloat, PrimitiveStringMultiline, MarkdownNote, LoadImage, LoadImage, LoadImage, PathchSageAttentionKJ, CLIPLoader, VAELoader, RandomNoise, UNETLoader, LoraLoaderModelOnly, ResolutionSelector, BasicGuider, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, VAEDecodeAudio, VAEDecode, ComfyMathExpression, MiniMaxH3ImageToVideo, VAELoader, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/RH-H3-文图生视频-基础流程1.0_2114526025295155202.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/RH-H3-文图生视频-基础流程1.0_2114526025295155202.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（23 个）：
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `VAELoader`
- `RandomNoise`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ResolutionSelector`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `ComfyMathExpression`
- `MiniMaxH3ImageToVideo`
- `VAELoader`
- `VHS_VideoCombine`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`LoadImage`、`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoader`、`RandomNoise`、`UNETLoader`、`LoraLoaderModelOnly`、`ResolutionSelector`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`VAEDecode`、`ComfyMathExpression`、`MiniMaxH3ImageToVideo`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

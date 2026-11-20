---
key: 视频生成/图生视频/RH-H3-文图生视频-基础流程1.0_2115600681053806594.json
name: RH-H3-文图生视频-基础流程1.0_2115600681053806594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/RH-H3-文图生视频-基础流程1.0_2115600681053806594.json
hash: 4bcdd3e946476a88
coverage: 0.869565
learned_at: 2026-10-30 17:58:36
nodes: [PrimitiveFloat, PrimitiveStringMultiline, MarkdownNote, LoadImage, LoadImage, LoadImage, PathchSageAttentionKJ, CLIPLoader, VAELoader, RandomNoise, UNETLoader, LoraLoaderModelOnly, ResolutionSelector, BasicGuider, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, VAEDecodeAudio, VAEDecode, ComfyMathExpression, MiniMaxH3ImageToVideo, VAELoader, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/RH-H3-文图生视频-基础流程1.0_2115600681053806594.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/RH-H3-文图生视频-基础流程1.0_2115600681053806594.json`

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

---
key: 视频生成/图生视频/RH-H3-参考生视频-基础流程1.0_2115597164633214977.json
name: RH-H3-参考生视频-基础流程1.0_2115597164633214977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/RH-H3-参考生视频-基础流程1.0_2115597164633214977.json
hash: ac0f4e16f99397d8
coverage: 0.869565
learned_at: 2026-10-30 17:58:35
nodes: [VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, BasicGuider, KSamplerSelect, BasicScheduler, ResolutionSelector, PrimitiveFloat, ComfyMathExpression, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, MarkdownNote, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, CLIPLoader, VAELoader, VAELoader, RandomNoise, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/RH-H3-参考生视频-基础流程1.0_2115597164633214977.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/RH-H3-参考生视频-基础流程1.0_2115597164633214977.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（23 个）：
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ResolutionSelector`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `RandomNoise`
- `VHS_VideoCombine`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`ResolutionSelector`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`LoadImage`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`RandomNoise`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

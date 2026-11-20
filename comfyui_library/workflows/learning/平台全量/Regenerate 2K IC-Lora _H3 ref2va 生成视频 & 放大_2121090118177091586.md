---
key: 平台全量/Regenerate 2K IC-Lora _H3 ref2va 生成视频 & 放大_2121090118177091586.json
name: Regenerate 2K IC-Lora _H3 ref2va 生成视频 & 放大_2121090118177091586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Regenerate 2K IC-Lora _H3 ref2va 生成视频 & 放大_2121090118177091586.json
hash: 394defa809b2716e
coverage: 0.942857
learned_at: 2026-11-14 00:54:49
nodes: [CLIPLoader, OpenH3ICPrompt, UNETLoader, BlockSparseAttention, ModelAttentionBackend, ConditioningZeroOut, ResolutionSelector, LoraLoaderModelOnly, PrimitiveFloat, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecodeAudio, VAEDecode, ComfyMathExpression, OpenH3ICDraft, VAELoader, MiniMaxH3ReferenceToVideo, LatentUpscaleModelLoader, MiniMaxH3LatentUpscaleWithModel, OpenH3ICComposeLatent, OpenH3ICSigmas, RandomNoise, BasicGuider, KSamplerSelect, VAELoader, VAEDecode, VHS_VideoCombine, VHS_VideoCombine, MiniMaxH3ReferenceToVideo, LoadImage, SamplerCustomAdvanced, SelfLiftH3Sampler, KSamplerSelect, BasicScheduler, MarkdownNote]
patterns: []
missing: []
---

# 平台全量/Regenerate 2K IC-Lora _H3 ref2va 生成视频 & 放大_2121090118177091586.json

> 来源文件 `comfyui_library/workflows/平台全量/Regenerate 2K IC-Lora _H3 ref2va 生成视频 & 放大_2121090118177091586.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（35 个）：
- `CLIPLoader`
- `OpenH3ICPrompt`
- `UNETLoader` ★核心
- `BlockSparseAttention`
- `ModelAttentionBackend`
- `ConditioningZeroOut`
- `ResolutionSelector`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `ComfyMathExpression`
- `OpenH3ICDraft`
- `VAELoader`
- `MiniMaxH3ReferenceToVideo`
- `LatentUpscaleModelLoader`
- `MiniMaxH3LatentUpscaleWithModel`
- `OpenH3ICComposeLatent`
- `OpenH3ICSigmas`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `SelfLiftH3Sampler` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `MarkdownNote`

## 知识

覆盖率 **94%**（33/35）

**有卡**：`CLIPLoader`、`OpenH3ICPrompt`、`UNETLoader`、`BlockSparseAttention`、`ModelAttentionBackend`、`ConditioningZeroOut`、`ResolutionSelector`、`LoraLoaderModelOnly`、`VAEDecodeAudio`、`VAEDecode`、`ComfyMathExpression`、`OpenH3ICDraft`、`VAELoader`、`MiniMaxH3ReferenceToVideo`、`LatentUpscaleModelLoader`、`MiniMaxH3LatentUpscaleWithModel`、`OpenH3ICComposeLatent`、`OpenH3ICSigmas`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`VHS_VideoCombine`、`LoadImage`、`SamplerCustomAdvanced`、`SelfLiftH3Sampler`、`BasicScheduler`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
